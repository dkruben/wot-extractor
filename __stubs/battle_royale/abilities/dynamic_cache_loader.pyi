# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/abilities/dynamic_cache_loader.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import NetworkComponents as NetworkComponents
import Math as Math
import CGF as CGF
import ResMgr as ResMgr
from constants import IS_CLIENT as IS_CLIENT
from helpers import dependency as dependency
from helpers.EffectsList import effectsFromSection as effectsFromSection
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache as IBattleDynamicObjectsCache
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak
from items import vehicles as vehicles
_logger: Any

class Vehicle(object):
    ...

class DynamicObjectsCacheLoader(object):
    guiSessionProvider: Any
    spaceID: Any
    equipmentID: Any
    zonesPosition: Any
    team: Any
    __influenceZoneType: Any
    __visual: Any
    fireIDs: Any
    gameObject: Any
    def __init__(self, spaceID, equipmentID, zonesPosition, team):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def __onResourceLoaded(self, effectP, position, scaleRatio, pointDescr, resourceRefs):
        ...
    def __getEffectConfig(self, config):
        ...
    def _onUpdateObservedVehicleData(self, vehicleID, *args):
        ...

class DynamicObjectsCacheLoaderSystem(CGF.System):
    DynamicObjectsCacheActivated: Any
    DynamicObjectsCacheDeactivated: Any
    Reactions: Any
    def update(self):
        ...

def _getTrapOrRepairPointDescr(equipmentID):
    ...
def _getPlayerVehicleImpl(who):
    ...
