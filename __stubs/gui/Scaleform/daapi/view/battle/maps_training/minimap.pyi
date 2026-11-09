# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/maps_training/minimap.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
from helpers import isPlayerAvatar as isPlayerAvatar
from account_helpers.settings_core.settings_constants import GAME as GAME
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak
from items.vehicles import getVehicleClassFromVehicleType as getVehicleClassFromVehicleType
from battleground.location_point_manager import g_locationPointManager as g_locationPointManager
from chat_commands_consts import MarkerType as MarkerType, LocationMarkerSubType as LocationMarkerSubType
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.battle_control import minimap_utils as minimap_utils, matrix_factory as matrix_factory
from gui.battle_control.battle_constants import PLAYER_GUI_PROPS as PLAYER_GUI_PROPS
from gui.Scaleform.daapi.view.battle.shared.minimap import common as common, settings as settings, plugins as plugins
from gui.Scaleform.daapi.view.battle.shared.minimap.entries import VehicleEntry as VehicleEntry
from gui.Scaleform.daapi.view.battle.classic.minimap import ClassicMinimapComponent as ClassicMinimapComponent, GlobalSettingsPlugin as GlobalSettingsPlugin
_C_NAME = settings.CONTAINER_NAME
_LOCATION_PING_RANGE = 30
_MINIMAP_MIN_SCALE_INDEX = 0
_MINIMAP_MAX_SCALE_INDEX = 5
_MINIMAP_SIZE_SETTING = 'mapsTrainingMinimapSize'
_MINIMAP_ENTRY_DEAD_TIME = 1
_MINIMAP_LOCATION_MARKER_MIN_SCALE = 1.0
_MINIMAP_LOCATION_MARKER_MAX_SCALE = 0.72
_ANIMATION_NAME = 'firstEnemy'
_LOCATION_SUBTYPE_TO_FLASH_SYMBOL_NAME: dict

class MapsTrainingVehicleEntry(VehicleEntry):
    __slots__: tuple
    _isPlayerAtAim: Any
    _isGoal: Any
    _vehicleID: Any
    def __init__(self, entryID, active, matrix=None):
        ...
    def setPlayerAtAim(self, isPlayerAtAim):
        ...
    def setGoalForPlayer(self, isGoal):
        ...
    def isPlayerAtAim(self):
        ...
    def isGoalForPlayer(self):
        ...
    def setOwnVehicleID(self, vehicleID):
        ...
    def getOwnVehicleID(self):
        ...

class BotAppearNotificationPlugin(common.EntriesPlugin):
    _curScale: Any
    __localGoals: Any
    __callbacksIDs: Any
    __delayedVehicleMarkers: Any
    def __init__(self, parent):
        ...
    def stop(self):
        ...
    def start(self):
        ...
    def _getModel(self, targetID):
        ...
    def __addSpottedVehicleStaticMarker(self, areaID, creatorID, position, locationMarkerSubtype, markerText='', numberOfReplies=0, isTargetForPlayer=False):
        ...
    def __updateSpottedVehicleStaticMarker(self, targetID, replierVehicleID, markerType, oldReplyCount, newReplycount):
        ...
    def __updateVehInfo(self, targetID, wasSpotted=True):
        ...
    def __removeSpottedVehicleStaticMarker(self, targetID):
        ...
    def __onLocalKillGoalsUpdated(self, localGoals):
        ...
    def __onArenaVehicleAdded(self, vehID):
        ...
    def __onArenaVehicleKilled(self, victimID, attackerID, equipmentID, reason, numVehiclesAffected):
        ...
    def __onMinimapVehicleAdded(self, vProxy, vInfo, guiProps):
        ...
    def __onMinimapVehicleRemoved(self, vehicleID):
        ...
    def __switchVehicleVisualState(self, vehicleID, isVisualStarted):
        ...
    def __setVehicleMatrixAndLocation(self, model, vehicleID, positions):
        ...
    @staticmethod
    def _calculateMarkerScale(minimapSizeIndex):
        ...
    @staticmethod
    def _getCombinedModelStates(entry):
        ...

class MapsTrainingGlobalSettingsPlugin(GlobalSettingsPlugin):
    def __init__(self, parentObj):
        ...

class MapsTrainingAreaStaticMarkerPlugin(plugins.AreaStaticMarkerPlugin):
    __slots__: tuple
    def _onReplyFeedbackReceived(self, ucmdID, replierID, markerType, oldReplyCount, newReplyCount):
        ...

class MapsTrainingMinimapComponent(ClassicMinimapComponent):
    def _setupPlugins(self, arenaVisitor):
        ...
