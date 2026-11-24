import crypto from 'node:crypto';

export const fingerprint = value => crypto.createHash('sha256').update(JSON.stringify(value)).digest('hex');

export function recipeKey(recipe) {
  const identity = source => source.block.crc
    ? { name: source.block.name, crc: source.block.crc, packed: source.block.packed }
    : source.identity;
  return fingerprint({ schema: 2, base: identity(recipe.base), deltas: recipe.deltas.map(identity) });
}

export function legacyRecipeKey(recipe) {
  return fingerprint({ schema: 1, base: recipe.base.identity, deltas: recipe.deltas.map(d => d.identity) });
}
