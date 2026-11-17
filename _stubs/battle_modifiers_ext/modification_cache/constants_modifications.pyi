# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_modifiers/scripts/common/battle_modifiers_ext/modification_cache/constants_modifications.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import AOI as AOI
from battle_modifiers_common.battle_modifiers import BattleParams as BattleParams, ConstantsSet as ConstantsSet, CONSTANTS_ORIGINAL as CONSTANTS_ORIGINAL
from battle_modifiers_ext.constants_ext import USE_CONSTANTS_CACHE as USE_CONSTANTS_CACHE, MAX_CONSTANTS_CACHE_LAYER_COUNT as MAX_CONSTANTS_CACHE_LAYER_COUNT, ModifierDomain as ModifierDomain
from battle_modifiers_ext.modification_cache.modification_cache import ModificationCache as ModificationCache
from typing import TYPE_CHECKING as TYPE_CHECKING, Optional as Optional, Union as Union
from battle_modifiers_common import BATTLE_MODIFIERS_TYPE as BATTLE_MODIFIERS_TYPE
g_cache = None

class ConstantsModification(ConstantsSet):
    VEHICLE_CIRCULAR_AOI_RADIUS: Any
    VEHICLE_CIRCULAR_AOI_RADIUS_HYSTERESIS_MARGIN: Any
    PIERCING_POWER_INTERPOLATION_DIST_FIRST: Any
    PIERCING_POWER_INTERPOLATION_DIST_LAST: Any
    DAMAGE_INTERPOLATION_DIST_FIRST: Any
    DAMAGE_INTERPOLATION_DIST_LAST: Any
    def __init__(self, modifiers):
        ...
    def __modifyConstants(self, modifiers):
        ...

class ConstantsModificationCache(ModificationCache):
    DEFAULT_LAYER_COUNT = MAX_CONSTANTS_CACHE_LAYER_COUNT
    __slots__: tuple
    def get(self, battleModifiers=None):
        ...

def init():
    ...
