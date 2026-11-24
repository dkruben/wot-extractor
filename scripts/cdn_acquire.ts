// Run inside the separately checked-out pinned archive engine.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync, spawnSync } from 'node:child_process';
import { SparseArchive, type Block } from './lib/archive.js';
import { applyDelta, deltaTarget } from './lib/delta.js';
import { installCdnFetch } from './cdn_fetch.mjs';
import { fingerprint, recipeKey, legacyRecipeKey } from './cdn_package_cache.mjs';

const flag = (name: string) => {
  const index = process.argv.indexOf(name), value = process.argv[index + 1];
  if (index < 0 || !value || value.startsWith('--')) throw new Error(`Missing ${name}`);
  return path.resolve(value);
};
const discoveryPath = flag('--discovery');
const cache = flag('--cache');
const evidence = flag('--evidence');
const discovery = JSON.parse(fs.readFileSync(discoveryPath, 'utf8'));
const catalogPath = process.argv.includes('--regions-file') ? flag('--regions-file') :
  execFileSync('python', ['-c', 'from wot_extractor.cdn_regions import CATALOG_PATH; print(CATALOG_PATH)'], { encoding: 'utf8' }).trim();
const regions = JSON.parse(fs.readFileSync(catalogPath, 'utf8'));
if (!Object.hasOwn(regions, discovery.realm) || regions[discovery.realm].guid !== discovery.guid ||
    regions[discovery.realm].host !== discovery.host || !discovery.release_ready) {
  throw new Error('Catalogued WG active-install plan required; RU/LESTA and ambiguous chains are excluded');
}
const metrics = installCdnFetch();
// Keep the archive library's disk writes bounded as well as its HTTP reads.
// A source-bearing package can be several GB even when we retain few members.
const fill = SparseArchive.prototype.fill;
SparseArchive.prototype.fill = async function(start: number, length: number) {
  const chunk = 32 * 1024 * 1024;
  for (let offset = 0; offset < length; offset += chunk) {
    await fill.call(this, start + offset, Math.min(chunk, length - offset));
  }
};
const work = path.join(cache, 'acquisition-work');
fs.mkdirSync(work, { recursive: true });
fs.mkdirSync(evidence, { recursive: true });
const log = (message: string) => console.log(`[cdn-acquire] ${message}`);
type Source = { archive: SparseArchive; block: Block; identity: unknown };
type Recipe = { base: Source; deltas: Source[] };
const packages = new Map<string, Recipe>();
const loose = new Map<string, Source>();
const archives: SparseArchive[] = [];
const pkgName = (name: string) => /^res\/packages\/[^/]+\.pkg$/.test(name);
const looseName = (name: string) => !/^(?:_service|win64|res\/cef)\//.test(name) && !name.startsWith('res/packages/') && /\.(xml|txt|def|mo|py|json|js|css|html|ts|unbound)$/i.test(name);
let cacheHits = 0, rebuilt = 0;

async function read(source: Source, folder: string) {
  fs.mkdirSync(folder, { recursive: true });
  const result = await source.archive.extract(source.block, folder);
  if (source.block.packed > 64 * 1024 * 1024) await source.archive.reset();
  return result;
}

async function main() {
  for (const part of ['client', 'sdcontent', 'locale']) {
    for (const [index, patch] of discovery.chains[part].entries()) {
      const directory = path.join(work, `${part}-${index}`);
      fs.mkdirSync(directory, { recursive: true });
      const archive = await SparseArchive.open(directory, patch.volumes);
      archives.push(archive);
      let entries = 0;
      for (const block of archive.index().values()) {
        const identity = { part, from: patch.from, to: patch.to, files: patch.files, torrent: patch.torrent,
          name: block.name, crc: block.crc, packed: block.packed };
        const source = { archive, block, identity };
        const target = deltaTarget(block.name);
        if (target) {
          const recipe = packages.get(target);
          if (!recipe) throw new Error(`Delta has no earlier base: ${target}`);
          recipe.deltas.push(source);
          entries++;
        } else if (pkgName(block.name)) {
          packages.set(block.name, { base: source, deltas: [] });
          entries++;
        } else if (looseName(block.name) && block.packed > 0) {
          loose.set(block.name, source);
        }
        if (/delete|remove/i.test(block.name) && !block.name.startsWith('res/packages/') && /\.(list|lst|txt)$/i.test(block.name)) {
          throw new Error(`Unreviewed patch deletion instructions: ${block.name}`);
        }
      }
      log(`${part} ${patch.from} -> ${patch.to}: ${entries} package entries indexed`);
    }
  }
  const paths = loose.get('paths.xml');
  if (!paths) throw new Error('No current paths.xml');
  const pathsFile = await read(paths, path.join(work, 'paths'));
  const active: string[] = JSON.parse(execFileSync('python', ['-m', 'wot_extractor.cdn_acquire', 'active', pathsFile], { encoding: 'utf8' }));
  if (active.length < 80) throw new Error('Unexpectedly small active source-package inventory');
  const selected = [];
  fs.mkdirSync(path.join(cache, 'packages'), { recursive: true });
  for (const name of active) {
    const recipe = packages.get(name);
    if (!recipe) throw new Error(`Active package is missing from locked chains: ${name}`);
    // A republished install may have new URLs/versions while most package blocks
    // are byte-identical. Reuse the archive's package CRC and packed size, not
    // the release-wide torrent identity. Missing CRCs retain conservative keys.
    const signature = recipeKey(recipe);
    const destination = path.join(cache, 'packages', signature);
    const legacySignature = legacyRecipeKey(recipe);
    const legacy = path.join(cache, 'packages', legacySignature);
    if (!fs.existsSync(destination) && fs.existsSync(legacy) &&
        spawnSync('python', ['-m', 'wot_extractor.cdn_acquire', 'validate', legacy, '--fingerprint', legacySignature], { stdio: 'ignore' }).status === 0) {
      const marker = path.join(legacy, 'package.json');
      const manifest = JSON.parse(fs.readFileSync(marker, 'utf8'));
      manifest.fingerprint = signature;
      fs.writeFileSync(marker, JSON.stringify(manifest));
      fs.renameSync(legacy, destination);
    }
    const valid = spawnSync('python', ['-m', 'wot_extractor.cdn_acquire', 'validate', destination, '--fingerprint', signature], { stdio: 'ignore' }).status === 0;
    if (valid) {
      cacheHits++;
      log(`cache hit ${name}`);
    } else {
      // This directory belongs only to this content-addressed cache entry.
      if (fs.existsSync(destination)) fs.rmSync(destination, { recursive: true, force: true });
      const folder = path.join(work, 'package');
      fs.mkdirSync(folder, { recursive: true });
      log(`rebuild ${name}: base ${(recipe.base.block.packed / 1e6).toFixed(1)} MB, ${recipe.deltas.length} deltas`);
      let file = await read(recipe.base, folder);
      for (const [index, delta] of recipe.deltas.entries()) {
        const input = await read(delta, path.join(folder, `delta-${index}`));
        const next = path.join(folder, `patched-${index}.pkg`);
        applyDelta(file, input, next);
        fs.rmSync(file);
        file = next;
      }
      const pending = destination + '.pending';
      if (fs.existsSync(pending)) fs.rmSync(pending, { recursive: true, force: true });
      execFileSync('python', ['-m', 'wot_extractor.cdn_acquire', 'import', file, pending,
        '--container', name, '--fingerprint', signature], { stdio: 'inherit' });
      fs.renameSync(pending, destination);
      fs.rmSync(folder, { recursive: true, force: true });
      rebuilt++;
    }
    selected.push({ name, fingerprint: signature });
  }
  const looseFiles = [];
  for (const [name, source] of loose) {
    const signature = fingerprint(source.identity);
    const directory = path.join(cache, 'loose', signature);
    const filename = path.join(directory, name);
    const marker = path.join(directory, 'sha256');
    let valid = fs.existsSync(filename) && fs.existsSync(marker);
    if (valid) valid = fingerprint(fs.readFileSync(filename).toString('base64')) === fs.readFileSync(marker, 'utf8');
    if (!valid) {
      await read(source, directory);
      fs.writeFileSync(marker, fingerprint(fs.readFileSync(filename).toString('base64')));
    }
    looseFiles.push({ name, path: filename });
  }
  const plan = { realm: discovery.realm, version: discovery.version, fingerprint: discovery.fingerprint,
    release_ready: discovery.release_ready, scope: 'active SD source packages; audio excluded',
    packages: selected, loose: looseFiles, package_cache_hits: cacheHits, packages_rebuilt: rebuilt,
    package_count: selected.length };
  fs.writeFileSync(path.join(cache, 'plan.json'), JSON.stringify(plan, null, 2));
  fs.writeFileSync(path.join(evidence, 'acquisition.json'), JSON.stringify(plan, null, 2));
  log(`complete: ${cacheHits} packages reused, ${rebuilt} rebuilt`);
}

main().catch(error => { console.error(error); process.exitCode = 1; }).finally(() => {
  fs.writeFileSync(path.join(evidence, 'cdn-transfer.json'), JSON.stringify(metrics, null, 2));
  // Only our explicitly named scratch tree; cached inputs and processing state stay.
  fs.rmSync(work, { recursive: true, force: true });
});
