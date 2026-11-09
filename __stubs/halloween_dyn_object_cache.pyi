# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween_dyn_object_cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import ResMgr as ResMgr
from dyn_objects_cache import DynObjectsBase as DynObjectsBase
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache as IBattleDynamicObjectsCache
from collections import namedtuple as namedtuple

class HWPrefabs(object):
    SOULS_COLLECTOR = 'hwSoulsCollector'
    ALL: tuple

class HWEffects(object):
    PHASE_SWITCH = 'hwPhaseSwitch'
    ALL: tuple

class HWModels(object):
    DEATHZONE_BORDER_RECT = 'hwDeathZoneBorderRect'
    DEATHZONE_BORDER_CIRCLE = 'hwDeathZoneBorderCircle'
    ALL: tuple

class HWHexapodTerrainEffects(object):
    SECTION = 'hwHexapodTerrainEffects'
    DEFAULT_GROUP = 'defaultGroup'
    Effect: Any
    DEFAULT_DURATION = 3.0
    DEFAULT_RATE = 1.0
    DEFAULT_SOUND = ''

class _HalloweenDynObjects(DynObjectsBase):
    __prefabPaths: Any
    __effectSections: Any
    __models: Any
    __hexapodTerrainEffects: Any
    def __init__(self):
        ...
    def init(self, dataSection):
        ...
    def destroy(self):
        ...
    def getPrefab(self, key):
        ...
    def getEffectSection(self, key):
        ...
    def getModel(self, key):
        ...
    def getHexapodTerrainEffects(self, group=None):
        ...
    @staticmethod
    def __readPrefab(dataSection, key):
        ...
    @staticmethod
    def __readEffect(dataSection, key):
        ...
    @staticmethod
    def __readModel(dataSection, key):
        ...
    def __readHexapodTerrainEffects(self, dataSection):
        ...
    def __readHexapodTerrainGroup(self, dataSection):
        ...
    def __readHexapodTerrainEffect(self, dataSection):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def getPrefabPath(objID, dynamicObjectsCache=None, battleSession=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getEffectSection(objID, dynamicObjectsCache=None, battleSession=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getModel(objID, dynamicObjectsCache=None, battleSession=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getHexapodTerrainEffects(group=..., dynamicObjectsCache=None, battleSession=None):
    ...
