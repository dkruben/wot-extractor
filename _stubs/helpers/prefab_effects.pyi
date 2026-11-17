# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/prefab_effects.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from PrefabEffectsAvailability import getDebugForceHitType as getDebugForceHitType, getPrefabEffectsAvailable as getPrefabEffectsAvailable, setPrefabEffectsEnabledForBattle as setPrefabEffectsEnabledForBattle
from constants import VEHICLE_HIT_EFFECT as VEHICLE_HIT_EFFECT, IS_DEVELOPMENT as IS_DEVELOPMENT
from items import vehicles as vehicles
from items.components.component_constants import INVALID_EFFECT_INDEX as INVALID_EFFECT_INDEX
_DEFAULT_ENABLED_FOR_BATTLE = False
_cachedPrefabEffectsAvailable = _DEFAULT_ENABLED_FOR_BATTLE

def _checkHitTypeOverride(hitType):
    ...
def _resolveShotEffectItem(prefabEffIndex, hitType):
    ...
def setCachePrefabEffectsEnabledForBattle(enabledForBattle):
    ...
def resetCachePrefabEffectsEnabledForBattle():
    ...
def resolvePrefabStickerID(prefabEffIndex, hitType):
    ...
def resolveGunPrefabEffects(gunPrefabEffects):
    ...
def resolveShotPrefabEffect(prefabEffIndex, hitType):
    ...
def resolveDamageStickerPrefab(prefabEffIndex, hitType):
    ...
