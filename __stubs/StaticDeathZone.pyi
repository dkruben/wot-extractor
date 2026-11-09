# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/StaticDeathZone.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import random as random
import BigWorld as BigWorld
import Math as Math
import Event as Event
from LimitedVisibilityEntity import LimitedVisibilityEntity as LimitedVisibilityEntity
from items import vehicles as vehicles
from helpers import dependency as dependency
from PlayerEvents import g_playerEvents as g_playerEvents
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV
from shared_utils import nextTick as nextTick
from constants import DEATH_ZONE_MASK_PATTERN as DEATH_ZONE_MASK_PATTERN
_TIME_TO_STOP_FIRE_ON_LEAVE_ZONE = 5.0

class StaticDeathZone(LimitedVisibilityEntity):
    onVehicleEntered: Any
    onVehicleLeft: Any
    onDamage: Any
    sessionProvider: Any
    _warningIsVisible: Any
    __callbackOnLeaveDeathZone: Any
    __functionOnLeaveDeathZone: Any
    _marker: Any
    _onActiveChanged: Any
    onMaskAdded: Any
    def __init__(self):
        ...
    @property
    def visual(self):
        ...
    @property
    def masks(self):
        ...
    @property
    def onActiveChanged(self):
        ...
    @property
    def isAvatarReady(self):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onDynamicComponentCreated(self, component):
        ...
    def onLeaveWorld(self):
        ...
    def getClosestPoint(self, pos, searchRadius):
        ...
    def onEntityEnteredInZone(self, entityID):
        ...
    def onEntityLeftZone(self, entityID):
        ...
    def onDeathZoneNotification(self, show, entityID, timeToStrike, waveDuration):
        ...
    def onDeathZoneDamage(self, vehicleId, vfx):
        ...
    def _playDamageEffect(self, vehicleId, vfx):
        ...
    def set_isActive(self, _):
        ...
    def _onAvatarReady(self):
        ...
    def _onAvatarVehicleChanged(self):
        ...
    def _updateVehicleUnderFire(self):
        ...
    def _getVehicleUnderFire(self):
        ...
    def _onLeaveDeathZone(self, callback):
        ...
    def _createMarker(self):
        ...
    def _removeMarker(self):
        ...
    def __setCallbackOnLeaveDeathZone(self):
        ...

class DeathZoneMarkerHandler(object):
    sessionProvider: Any
    SEARCH_RADIUS_EXTENSION = 2.0
    _zone: Any
    _matrix: Any
    _markerId: Any
    _searchRadius: Any
    _vehiclesInZone: Any
    def __init__(self, zone):
        ...
    def destroy(self):
        ...
    def setVisible(self, visible):
        ...
    def onVehicleEnteredZone(self, vehID):
        ...
    def onVehicleLeftZone(self, vehID):
        ...
    def getBorderModel(self, borderID):
        ...
    def _tickUpdate(self):
        ...
