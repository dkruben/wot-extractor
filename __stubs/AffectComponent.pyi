# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AffectComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import CGF as CGF
import GenericComponents as GenericComponents
from helpers import dependency as dependency
from shared_utils import nextTick as nextTick
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache as IBattleDynamicObjectsCache
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from battle_royale.gui.battle_control.controllers.br_battle_sounds import BREvents as BREvents
_logger: Any
_HEAL_OVER_TIME_ZONE_ = 0
_DAMAGE_OVER_TIME_ZONE_ = 1
_FIRE_CIRCLE_ZONE_ = 2
_ZONE_ACTIVATE_EVENT_: dict
_ZONE_DEACTIVATE_EVENT_: dict

class AffectComponent(object):
    __guiSessionProvider: Any
    hasDebuff: Any
    __gameObject: Any
    __spaceID: Any
    __particle: Any
    __influenceZoneType: Any
    __isPlayerVehicle: Any
    __soundPlaying: Any
    __vehicleEffectConfig: Any
    __ownVehicleID: Any
    def __init__(self, gameObject, zoneType, isPlayerVehicle, spaceID, hasDebuff, vehicleID=None):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def _createParticles(self):
        ...
    def _removeParticles(self):
        ...
    def _activateSoundEvent(self):
        ...
    def _deactivateSoundEvent(self):
        ...
    def getVehicleConfig(self):
        ...
    def _onUpdateObservedVehicleData(self, vehicleID, *args):
        ...
    def _onVehicleKilled(self, targetID, *_):
        ...

class TrapAffectComponent(AffectComponent):
    __guiSessionProvider: Any
    def __init__(self, gameObject, isPlayerVehicle, spaceID, vehicleID):
        ...

class FireCircleAffectComponent(AffectComponent):
    def __init__(self, gameObject, isPlayerVehicle, spaceID, vehicleID):
        ...

class RepairAffectComponent(AffectComponent):
    __guiSessionProvider: Any
    def __init__(self, gameObject, isPlayerVehicle, spaceID, vehicleID):
        ...

class AffectComponentsSystem(CGF.System):
    TrapActivated: Any
    TrapDeactivated: Any
    FireCircleActivated: Any
    FireCircleDeactivated: Any
    RepairActivated: Any
    RepairDeactivated: Any
    Reactions: Any
    def update(self):
        ...

def getInfluenceZoneType(pointDescr):
    ...
def getEffectConfig(influenceZoneType, config):
    ...
