# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/DestructibleEntityState.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import typing as typing
import BigWorld as BigWorld
import CGF as CGF
import GenericComponents as GenericComponents
import Math as Math
import destructible_entities as destructible_entities
import helpers as helpers
from DestructibleStickers import DestructibleStickers as DestructibleStickers
from cgf_client_common.game_object_holder import GameObjectHolder as GameObjectHolder
from helpers.EffectsList import effectsFromSection as effectsFromSection, EffectsListPlayer as EffectsListPlayer
from vehicle_systems.tankStructure import ColliderTypes as ColliderTypes
COLLISION_SEGMENT_LENGTH = 2

class ASSEMBLER_NAME_SUFFIXES(object):
    VISUAL = '_vis'
    PHYSICS = '_phys'

class PART_PROPERTIES(object):
    HIGHLIGHTABLE = 0
    HIGHLIGHTBYVISUAL = 2

class DestructibleEntityState(GameObjectHolder):
    guiNode: Any
    damageStickers: Any
    name: Any
    __entityId: Any
    __stateName: Any
    __stateProperties: Any
    __guiNode: Any
    __active: Any
    __visualModel: Any
    __damageStickers: Any
    __gameObjects: Any
    __effectsPlayer: Any
    __trigger: Any
    collisionComponent: Any
    state: Any
    class DestructibleEntityStateComponent(object):
        state: Any
        def __init__(self, state):
            ...
    def __init__(self, stateName, stateProperties, entityId, trigger, spaceID):
        ...
    def isTriggered(self):
        ...
    def reduceSegmentLength(self, hitCompIndx, segStart, segEnd):
        ...
    def prereqs(self, spaceId):
        ...
    def onResourcesLoaded(self, prereqs):
        ...
    def setParent(self, parent):
        ...
    def activate(self, matrix):
        ...
    def onActivate(self, collisionComponent):
        ...
    def deactivate(self):
        ...
    def destroy(self):
        ...
    def collideAllWorld(self, startPoint, endPoint):
        ...
    def isDestructibleComponent(self, componentID):
        ...
    def __playEffect(self, effectName, model):
        ...
    def __stopEffect(self):
        ...

class DestructibleEntityStatesSystem(CGF.System):
    Activate: Any
    Reactions: Any
    def update(self):
        ...
