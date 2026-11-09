# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/markers2d.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from logging import getLogger as getLogger
import BigWorld as BigWorld
import CGF as CGF
from AvatarInputHandler import aih_global_binding as aih_global_binding
from AvatarInputHandler.aih_global_binding import BINDING_ID as BINDING_ID
from story_mode.cgf_components.bunkers import BunkersSystem as BunkersSystem
from Math import Vector4 as Vector4, Vector2 as Vector2, Matrix as Matrix, Vector3 as Vector3
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from gui.Scaleform.daapi.view.battle.shared.markers2d import MarkersManager as MarkersManager, settings as settings
from gui.Scaleform.daapi.view.battle.shared.markers2d.markers import BaseMarker as BaseMarker, VehicleMarker as VehicleMarker
from gui.Scaleform.daapi.view.battle.shared.markers2d.plugins import MarkerPlugin as MarkerPlugin
from gui.Scaleform.daapi.view.battle.shared.markers2d.vehicle_plugins import RespawnableVehicleMarkerPlugin as RespawnableVehicleMarkerPlugin
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID, MARKER_EMPTY_HIT_STATE as MARKER_EMPTY_HIT_STATE, PLAYER_GUI_PROPS as PLAYER_GUI_PROPS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from story_mode.skeletons.voiceover_controller import IVoiceoverManager as IVoiceoverManager
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from story_mode_common.story_mode_constants import LOGGER_NAME as LOGGER_NAME, VEHICLE_BUNKER_TURRET_TAG as VEHICLE_BUNKER_TURRET_TAG
from vehicle_systems.tankStructure import TankNodeNames as TankNodeNames, TankPartIndexes as TankPartIndexes
_MARKER_CRITICAL_HIT_STATES: set
_logger: Any
_MEDIUM_MARKER_MIN_SCALE = 100
_MAX_CULL_DISTANCE = 1000000.0
_BUNKER_BOUNDS_MIN_SCALE: Any
_BUNKER_BOUNDS: Any
_INNER_BUNKER_BOUNDS: Any
_BUNKER_OWNER = 'enemy'
_BUNKER_ALIVE_STATE = 'alive'
BUNKER_SYMBOL = 'BunkerMarkerUI'
_MIN_TURRET_OFFSET = 0.2
_WITHOUT_ZOOM = 1
_ZOOM_x2 = 2
_ZOOM_REDUCER = 1.8

class StoryModeMarkersManager(MarkersManager):
    MARKERS_MANAGER_SWF = 'story_mode|storyModeBattleVehicleMarkersApp.swf'
    __slots__: tuple
    def _setupPlugins(self, arenaVisitor):
        ...
    @property
    def _isMarkerHoveringEnabled(self):
        ...

class MarkerPluginWithOffsetInZoom(MarkerPlugin):
    __slots__: tuple
    def start(self):
        ...
    def stop(self):
        ...
    def _updateMatrixProviders(self, *args):
        ...

class StoryModeVehicleMarker(VehicleMarker):
    sessionProvider: Any
    _vehicleOffsetCache: dict
    @classmethod
    def _calculateGuiOffset(cls, vProxy):
        ...
    @classmethod
    def _getVehicleTurretOffset(cls, vProxy):
        ...
    @classmethod
    def clearCache(cls):
        ...

class StoryModeVehicleMarkerPlugin(RespawnableVehicleMarkerPlugin, MarkerPluginWithOffsetInZoom):
    __slots__: tuple
    _voiceoverManager: Any
    _storyModeCtrl: Any
    def __init__(self, parentObj, clazz=...):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def _getHitState(self, eventID):
        ...
    def _voiceoverHandler(self):
        ...
    def _updateMatrixProviders(self, *args):
        ...
    def _needsMarker(self, vInfo):
        ...

class BunkersPlugin(MarkerPluginWithOffsetInZoom):
    __slots__: tuple
    _DISTANCE_UPDATE_TIME = 1
    _markers: Any
    __clazz: Any
    __entitiesDamageType: Any
    _distanceUpdateCallback: Any
    __offsetCache: Any
    def __init__(self, parentObj, clazz=...):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def _updateMatrixProviders(self, *args):
        ...
    def __onDestructibleEntityAdded(self, entity):
        ...
    def __onDestructibleEntityRemoved(self, entityId):
        ...
    def __onDestructibleEntityStateChanged(self, entityId):
        ...
    def __getMarkerMatrix(self, destructibleEntity):
        ...
    def __getBunkerOffset(self, destructibleEntity):
        ...
    @staticmethod
    def __calculateBunkerOffset(destructibleEntity):
        ...
    def __onDestructibleEntityHealthChanged(self, entityId, newHealth, maxHealth, attackerID, attackReason, hitFlags):
        ...
    def _updateDistanceToEntity(self, entityId, entity):
        ...
    def _distanceUpdate(self):
        ...
    def __getVehicleDamageType(self, attackerInfo):
        ...

def _calculateVehicleTurretOffset(vehicle):
    ...
def _getZoomLevel(sessionProvider):
    ...
def _getReducedY(y, zoom, turretOffset):
    ...
