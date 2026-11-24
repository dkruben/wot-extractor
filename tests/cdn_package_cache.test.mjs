import assert from 'node:assert/strict';
import test from 'node:test';
import { recipeKey, legacyRecipeKey } from '../scripts/cdn_package_cache.mjs';

const source = (release, crc = 'ABC123') => ({
  block: { name: 'res/packages/scripts.pkg', crc, packed: 100 },
  identity: { release, url: `https://cdn.example/${release}`, crc },
});

test('unchanged package blocks survive a republished release and mirror change', () => {
  const first = { base: source('first'), deltas: [] };
  const next = { base: source('next'), deltas: [] };
  assert.equal(recipeKey(first), recipeKey(next));
  assert.notEqual(legacyRecipeKey(first), legacyRecipeKey(next));
});

test('changed base or delta invalidates its package cache', () => {
  const recipe = { base: source('release'), deltas: [] };
  assert.notEqual(recipeKey(recipe), recipeKey({ base: source('release', 'changed'), deltas: [] }));
  assert.notEqual(recipeKey(recipe), recipeKey({ ...recipe, deltas: [source('patch')] }));
});

test('missing archive CRC keeps conservative release-specific identity', () => {
  assert.notEqual(recipeKey({ base: source('first', ''), deltas: [] }),
    recipeKey({ base: source('next', ''), deltas: [] }));
});
