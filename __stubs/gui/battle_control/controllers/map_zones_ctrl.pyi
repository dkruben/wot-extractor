# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/map_zones_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Event as Event
import SoundGroups as SoundGroups
from cgf_components.zone_components import RandomEventZoneUINotificationType as RandomEventZoneUINotificationType, WeatherZoneUINotificationType as WeatherZoneUINotificationType
from gui.battle_control.arena_info.interfaces import IMapZonesController as IMapZonesController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID, VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE, DestroyTimerViewState as DestroyTimerViewState, TIMER_VIEW_STATE as TIMER_VIEW_STATE
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_randomEventsNotificationMapping: dict
_weatherNotificationMapping: dict

class SoundNotifications(object):
    DANGER_ZONE_MARKER_START = 'dstrct_death_zone_marker_start'
    DANGER_ZONE_MARKER_STOP = 'dstrct_death_zone_marker_stop'
    DANGER_ZONE_ENTER = 'dstrct_death_zone_enter'
    DANGER_ZONE_EXIT = 'dstrct_death_zone_exit'

class MapZonesController(IMapZonesController):
    sessionProvider: Any
    __eManager: Any
    onMarkerToZoneAdded: Any
    onMarkerFromZoneRemoved: Any
    onMarkerProgressUpdated: Any
    onZoneTransformed: Any
    onTransformedZoneRemoved: Any
    __activeRandomEventZones: Any
    __activeWeatherZones: Any
    __zoneMarkers: Any
    __transformedZones: Any
    def __init__(self, setup):
        ...
    def startControl(self, *args):
        ...
    def stopControl(self):
        ...
    def getControllerID(self):
        ...
    def addMarkerToZone(self, zoneMarkerAccess, matrix):
        ...
    def removeMarkerFromZone(self, zoneMarker):
        ...
    def addTransformedZone(self, zoneAccess):
        ...
    def removeTransformedZone(self, zone):
        ...
    def enterRandomEventZone(self, zone):
        ...
    def exitRandomEventZone(self, zone):
        ...
    def removeRandomEventZone(self, zone):
        ...
    def enterWeatherZone(self, zone):
        ...
    def exitWeatherZone(self, zone):
        ...
    def removeWeatherZone(self, zone):
        ...
    def getZoneMarkers(self):
        ...
    def getTransformedZones(self):
        ...
