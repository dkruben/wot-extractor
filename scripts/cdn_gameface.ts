// Adapter for the separately checked-out, pinned wot.build archive API.
// Copy this file into that checkout before execution; no engine code is vendored.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { SparseArchive } from './lib/archive.js';
import { drainPatches, recipes, rebuildPackage } from './lib/patched.js';
import { resolveClient } from './lib/wgus.js';
import { installCdnFetch } from './cdn_fetch.mjs';

const value = (name: string) => {
  const index = process.argv.indexOf(name);
  const result = process.argv[index + 1];
  if (index < 0 || !result || result.startsWith('--')) throw new Error(`Missing ${name}`);
  return result;
};
const realm = value('--realm');
const host = value('--host');
const out = path.resolve(value('--out'));
const evidence = path.resolve(value('--evidence'));
const catalog = JSON.parse(fs.readFileSync(value('--regions-file'), 'utf8'));
const target = catalog[realm];
if (!target || target.host !== host || !/^WOT\.[A-Z]+\.PRODUCTION$/.test(target.guid)) {
  throw new Error('Region/host is not in the WG-only catalog; RU/LESTA are excluded');
}
const wanted = (name: string) => /^res\/packages\/(gui-part\d+|scripts)\.pkg$/.test(name);

const metrics = installCdnFetch();

async function main() {
  if (fs.existsSync(out)) throw new Error('Output must be a new isolated directory');
  const client = await resolveClient(host, target.guid);
  if (!client) throw new Error('No client build available');
  const [full, ...patches] = client.getChain('client');
  if (!full) throw new Error('No client package chain');
  const scratch = fs.mkdtempSync(path.join(os.tmpdir(), 'gameface-cdn-'));
  fs.mkdirSync(out, { recursive: true });
  fs.mkdirSync(evidence, { recursive: true });
  const log = (message: string) => console.log(`[cdn-gameface] ${message}`);
  const packages: string[] = [];
  try {
    const drained = await drainPatches(patches, scratch, wanted, log);
    const base = path.join(scratch, 'base');
    fs.mkdirSync(base);
    const archive = await SparseArchive.open(base, full.volumes);
    const plan = recipes(archive, [...archive.index().values()], wanted, drained);
    if (![...plan.keys()].some(name => /gui-part\d+\.pkg$/.test(name))) throw new Error('No GUI packages');
    for (const [name, recipe] of plan) {
      const work = path.join(scratch, 'package');
      fs.mkdirSync(work, { recursive: true });
      log(`Rebuilding ${name}: ${recipe.base.block.packed} base bytes, ${recipe.deltas.length} deltas`);
      const pkg = await rebuildPackage(recipe, work);
      execFileSync('python', ['-m', 'wot_extractor.cdn_gameface', 'import', pkg, out,
        '--realm', realm, '--container', name], { stdio: 'inherit' });
      packages.push(name);
      fs.rmSync(work, { recursive: true });
      await recipe.base.archive.reset();
    }
    fs.writeFileSync(path.join(out, '.version_name'), client.versionName + '\n');
    fs.writeFileSync(path.join(out, 'cdn-gameface.json'), JSON.stringify({
      realm, version: client.versionName, scope: 'base-gui-and-scripts; game modes excluded',
      host: client.host, packages,
    }, null, 2));
  } finally {
    fs.writeFileSync(path.join(evidence, 'cdn-transfer.json'), JSON.stringify(metrics, null, 2));
    fs.rmSync(scratch, { recursive: true, force: true });
    log(`HTTP response body bytes: ${metrics.bodyBytes}, range requests: ${metrics.rangeRequests}`);
  }
}

main().catch(error => { console.error(error); process.exitCode = 1; });
