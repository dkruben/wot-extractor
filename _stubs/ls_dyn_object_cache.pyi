# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/ls_dyn_object_cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import CGF as CGF
import ResMgr as ResMgr
from dyn_objects_cache import DynObjectsBase as DynObjectsBase
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache as IBattleDynamicObjectsCache

class LSPrefabs(object):
    BEAM_IDLE = 'lsBeamIdle'
    BEAM_DAMAGE = 'lsBeamDamage'
    ALL: tuple

class LSEffects(object):
    PHASE_SWITCH = 'lsPhaseSwitch'
    ALL: tuple

class _LSDynObjects(DynObjectsBase):
    __prefabPaths: Any
    __effectSections: Any
    _initialized: Any
    def __init__(self):
        ...
    def init(self, dataSection):
        ...
    def clear(self):
        ...
    def destroy(self):
        ...
    def getPrefab(self, key):
        ...
    def getEffectSection(self, key):
        ...
    @staticmethod
    def __readPrefab(dataSection, key):
        ...
    @staticmethod
    def __readEffect(dataSection, key):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def getPrefabPath(objID, dynamicObjectsCache=None, battleSession=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getEffectSection(objID, dynamicObjectsCache=None, battleSession=None):
    ...
