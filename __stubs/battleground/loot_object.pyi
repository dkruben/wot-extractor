# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/battleground/loot_object.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import CGF as CGF
from helpers import dependency as dependency
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache as IBattleDynamicObjectsCache
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any

class SteelHunterDynamicObjectsCachingManager(CGF.System):
    __dynamicObjectsCache: Any
    __cachedPrefabs: Any
    __cachedConfig: Any
    def __init__(self):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def __cachePrefabs(self, lootDescr):
        ...
    def __getConfig(self):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def loadLootById(typeID, dynamicObjectsCache=None, battleSession=None):
    ...
