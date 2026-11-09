# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/comp7_dyn_objects_cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import ArenaType as ArenaType
import BigWorld as BigWorld
import CGF as CGF
from points_of_interest_shared import PoiType as PoiType
from dyn_objects_cache import DynObjectsBase as DynObjectsBase, _SpawnPointsConfig as _SpawnPointsConfig, _PointsOfInterestConfig as _PointsOfInterestConfig
_CONFIG_PATH = 'scripts/dynamic_objects.xml'
_logger: Any

class Comp7DynObjects(DynObjectsBase):
    _AOE_HEAL_KEY = 'aoeHeal'
    _ILLUMINATION_FLARE_KEY = 'illuminationFlare'
    __ALL_KEYS: tuple
    _SPAWNPOINT_VISUAL_PATH_KEY = 'spawnPointVisualPath'
    __prefabPaths: Any
    __cachedPrefabs: Any
    __spawnPointConfig: Any
    __pointsOfInterestConfig: Any
    _initialized: Any
    def __init__(self):
        ...
    def init(self, dataSection):
        ...
    def clear(self):
        ...
    def destroy(self):
        ...
    def getAoeHealPrefab(self):
        ...
    def getSpawnPointsConfig(self):
        ...
    def getPointOfInterestConfig(self):
        ...
    def __collectPrefabsToCache(self):
        ...
    @staticmethod
    def __isPoiTypePresentOnArena(poiType):
        ...
    @staticmethod
    def __readPrefab(dataSection, key):
        ...
