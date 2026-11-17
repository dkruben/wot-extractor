# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/destructible_entities.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import ResMgr as ResMgr
from items import _xml as _xml
from constants import IS_CLIENT as IS_CLIENT, IS_BASEAPP as IS_BASEAPP, IS_BOT as IS_BOT, IS_CELLAPP as IS_CELLAPP, IS_WEB as IS_WEB
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV
from collections import namedtuple as namedtuple, OrderedDict as OrderedDict
import material_kinds as material_kinds
from material_kinds import EFFECT_MATERIAL_INDEXES_BY_NAMES as EFFECT_MATERIAL_INDEXES_BY_NAMES
g_destructibleEntitiesCache = None
DestructibleMaterialInfo: Any

class DESTRUCTIBLE_ENTITY_TYPES:
    EPIC_HEADQUARTER = 2
    EPIC_HEADQUARTER89 = 3
    EPIC_HEADQUARTERS: tuple

class DestructibleEntitiesCache(object):
    destructibleEntityTypes: Any
    mapActivityLists: Any
    destroyEffectLists: Any
    materials: Any
    def __init__(self):
        ...
    def getDestructibleEntityType(self, typeID):
        ...
    def getMapActivityList(self, name):
        ...
    def getDestroyEffectList(self, name):
        ...
    def addDestructibleEntityType(self, destructibleEntityType):
        ...

class DestructibleEntityType(object):
    maxNumStateComponents: Any
    id: Any
    displayName: Any
    health: Any
    destroyedNotificationRadius: Any
    materials: Any
    states: Any
    observationPoints: Any
    observedPoints: Any
    directVisionRadius: Any
    normalRadioDistance: Any
    def __init__(self, id, displayName, health, destroyedNotificationRadius, materials, observationPoints=..., observedPoints=..., directVisionRadius=None, normalRadioDistance=None):
        ...
    def addState(self, name, state):
        ...

class DestructibleEntityState(object):
    components: Any
    effect: Any
    def __init__(self):
        ...
    def addComponent(self, id, stateComponent):
        ...
    def setClientProperties(self, effect):
        ...

class DestructibleEntityStateComponent(object):
    destructible: Any
    physicsModel: Any
    guiNode: Any
    visualModel: Any
    def __init__(self, destructible, physicsModel):
        ...
    def setClientProperties(self, guiNode, visualModel):
        ...

def init():
    ...
def determineDestructibleEntityTypeID(validVehicleLevels, defaultTypeID):
    ...
def _readType(xmlCtx, section):
    ...
def _readPointList(xmlCtx, section):
    ...
def _readState(xmlCtx, section):
    ...
def _readStateComponent(xmlCtx, section):
    ...
def _readDestructibleEntitiesEffects(filename):
    ...
def _readMaterials(parentXmlCtx, section):
    ...
