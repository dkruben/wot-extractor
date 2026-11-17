# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/epic/minimap.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import os as os
from future.utils import viewvalues as viewvalues
from past.utils import old_div as old_div
import BigWorld as BigWorld
import CommandMapping as CommandMapping
import GUI as GUI
import Math as Math
from account_helpers import AccountSettings as AccountSettings
from account_helpers.settings_core.settings_constants import CONTROLS as CONTROLS
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from arena_component_system.sector_base_arena_component import ID_TO_BASENAME as ID_TO_BASENAME
from chat_commands_consts import BATTLE_CHAT_COMMAND_NAMES as BATTLE_CHAT_COMMAND_NAMES, MarkerType as MarkerType, ReplyState as ReplyState
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from coordinate_system import AXIS_ALIGNED_DIRECTION as AAD
from epic_constants import EPIC_BATTLE_TEAM_ID as EPIC_BATTLE_TEAM_ID
from gui.Scaleform.daapi.view.battle.classic.minimap import GlobalSettingsPlugin as GlobalSettingsPlugin
from gui.Scaleform.daapi.view.battle.shared.minimap import settings as settings, plugins as plugins, common as common
from gui.Scaleform.daapi.view.battle.shared.minimap.common import SimplePlugin as SimplePlugin
from gui.Scaleform.daapi.view.battle.shared.minimap.plugins import PersonalEntriesPlugin as PersonalEntriesPlugin, ArenaVehiclesPlugin as ArenaVehiclesPlugin, _LOCATION_PING_RANGE as _LOCATION_PING_RANGE, _EMinimapMouseKey as _EMinimapMouseKey
from gui.Scaleform.daapi.view.meta.EpicMinimapMeta import EpicMinimapMeta as EpicMinimapMeta
from gui.Scaleform.genConsts.BATTLE_MINIMAP_CONSTS import BATTLE_MINIMAP_CONSTS as BATTLE_MINIMAP_CONSTS
from gui.Scaleform.genConsts.LAYER_NAMES import LAYER_NAMES as LAYER_NAMES
from gui.battle_control import minimap_utils as minimap_utils, avatar_getter as avatar_getter
from gui.battle_control.battle_constants import PROGRESS_CIRCLE_TYPE as PROGRESS_CIRCLE_TYPE, SECTOR_STATE_ID as SECTOR_STATE_ID, FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID
from gui.shared.utils.key_mapping import getScaleformKey as getScaleformKey
from helpers import dependency as dependency
from math_common import decimal_round as decimal_round
from messenger_common_chat2 import MESSENGER_ACTION_IDS as _ACTIONS
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
_C_NAME = settings.CONTAINER_NAME
_S_NAME = settings.ENTRY_SYMBOL_NAME
_EPIC_TEAM_POINTS = settings.CONTAINER_NAME.TEAM_POINTS
_EPIC_ZONES = settings.CONTAINER_NAME.ZONES
_EPIC_HQS = settings.CONTAINER_NAME.HQS
_EPIC_PROTECTION_ZONE = settings.CONTAINER_NAME.PROTECTION_ZONE
_EPIC_ICONS = settings.CONTAINER_NAME.ICONS
_RESPAWN_VISUALIZATION_ENTRY_1 = 0
_RESPAWN_VISUALIZATION_ENTRY_2 = 1
_RESPAWN_VISUALIZATION_ENTRY_3 = 2
_IS_COORDINATOR: Any
_FRONT_LINE_DEV_VISUALIZATION_SUPPORTED = IS_DEVELOPMENT
_MINI_MINIMAP_HIGHLIGHT_PATH: Any
_MINI_MINIMAP_SIZE = 46
_ZOOM_MODE_MIN = 1
_ZOOM_MODE_STEP = 0.5
_ZOOM_MULTIPLIER_TEXT = 'x'
_METERS_IN_1X_ZOOM = 1000
EPIC_MINIMAP_HIT_AREA = 210
_EPIC_BASE_PING_RANGE = 145
_DOWN_SCALE = 0.45
_UP_SCALE = 1.0
_MIN_RANGE_SCALE = 1.0
_MIN_BASE_SCALE = 1.0
_MAX_BASE_SCALE = 2.0
_logger: Any

class MINIMAP_SCALE_TYPES(object):
    NO_SCALE = 0
    REAL_SCALE = 1
    ADAPTED_SCALE = 2
    NATIVE = 42
    PROPORTIONAL = 43

class EpicMinimapComponent(EpicMinimapMeta):
    __settingsCore: Any
    __mode: Any
    __minimapCenterPos: Any
    __maxZoomMode: Any
    __rangeScale: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def setMinimapCenterEntry(self, entryID):
        ...
    def changeMinimapZoom(self, mode):
        ...
    def getRangeScale(self):
        ...
    def setEntryParameters(self, entryId, doClip=True, scaleType=...):
        ...
    def getPositionOfEntry(self, vID):
        ...
    def updateZoomMode(self, mode):
        ...
    def onZoomModeChanged(self, change):
        ...
    def getZoomMode(self):
        ...
    def getCenterPosition(self):
        ...
    def getVisualBounds(self):
        ...
    def updateSectorStates(self, states):
        ...
    def _setupPlugins(self, arenaVisitor):
        ...
    def _processMinimapSize(self, minSize, maxSize):
        ...
    def _createFlashComponent(self):
        ...
    def _getMaxZoomMode(self, bl, tr):
        ...
    def __zoomText(self):
        ...
    def __calculateRangeScale(self, minScale, maxScale, current):
        ...
    def __updateMapShortcutLabel(self):
        ...
    def __onSettingsApplied(self, diff):
        ...

class RecoveringVehiclesPlugin(ArenaVehiclesPlugin):
    def start(self):
        ...
    def stop(self):
        ...
    def __arena_onVehicleRecovered(self, vehicleID):
        ...

class RespawningPersonalEntriesPlugin(PersonalEntriesPlugin):
    __slots__: tuple
    RESPAWN_MODES: tuple
    __lastCtrlMode: Any
    def __init__(self, parentObj):
        ...
    def initControlMode(self, mode, available):
        ...
    def updateControlMode(self, mode, vehicleID):
        ...
    def updateSettings(self, diff):
        ...
    def _invalidateMarkup(self, forceInvalidate=False):
        ...
    def _enableCameraEntryInCtrlMode(self, ctrlMode):
        ...
    def _updateCirlcesState(self):
        ...

class CenteredPersonalEntriesPlugin(RespawningPersonalEntriesPlugin):
    __slots__: tuple
    __savedEntry: Any
    __mode: Any
    def __init__(self, parentObj):
        ...
    def initControlMode(self, mode, available):
        ...
    def updateControlMode(self, mode, vehicleID):
        ...
    def _getPostmortemCenterEntry(self):
        ...
    def __centerMapBasedOnMode(self):
        ...

class SectorBaseEntriesPlugin(common.EntriesPlugin):
    __slots__: tuple
    __markerIDs: Any
    __personalTeam: Any
    __symbolAlly: Any
    __symbolEnemy: Any
    __hasActiveCommit: Any
    def __init__(self, parentObj, symbolAlly=..., symbolEnemy=...):
        ...
    def start(self):
        ...
    def fini(self):
        ...
    def __onSectorBaseAdded(self, sectorBase):
        ...
    def __onSectorBaseCaptured(self, baseId, isPlayerTeam):
        ...
    def __onSectorBasePointsUpdate(self, baseId, isPlayerTeam, points, capturingStopped, invadersCount, expectedCaptureTime):
        ...
    def __addPointEntry(self, symbol, sectorBase):
        ...
    def __onActionAddedToObjectiveMarkerReceived(self, senderID, commandID, markerType, objectID):
        ...
    def __onReplyFeedbackReceived(self, ucmdID, replierID, markerType, oldReplyCount, newReplyCount):
        ...
    def __onRemoveCommandReceived(self, removeID, markerType):
        ...

class SectorStatusEntriesPlugin(SimplePlugin):
    __slots__: tuple
    _zonesDict: Any
    _posDict: Any
    __personalTeam: Any
    _symbol: Any
    def __init__(self, parentObj):
        ...
    def start(self):
        ...
    def fini(self):
        ...
    def _onPlayerSectorGroupChanged(self, newSectorGroupID, isAllowed, oldSectorGroupID, wasAllowed):
        ...
    def __onSectorGroupUpdated(self, sectorGroupId, state, center, bounds):
        ...
    def __addZoneEntry(self, symbol, position):
        ...

class HeadquartersStatusEntriesPlugin(SimplePlugin):
    __slots__: tuple
    __hqsDict: Any
    __symbolAlly: Any
    __symbolEnemy: Any
    __hasActiveCommit: Any
    def __init__(self, parentObj, symbolAlly=..., symbolEnemy=...):
        ...
    def start(self):
        ...
    def fini(self):
        ...
    def __onDestructibleEntityAdded(self, entity):
        ...
    def __onDestructibleEntityHealthChanged(self, destructibleEntityID, newHealth, maxHealth, atkID, atkReason, hitFlags):
        ...
    def __addHQEntry(self, symbol, position):
        ...
    def __onMinimapFeedbackReceived(self, eventID, entityID, value):
        ...
    def __onActionAddedToMarkerReceived(self, senderID, hqId, duration, cmdName):
        ...
    def __onReplyFeedbackReceived(self, ucmdID, replierID, markerType, oldReplyCount, newReplyCount):
        ...
    def __onRemoveCommandReceived(self, removeID, markerType):
        ...

class DevelopmentRespawnEntriesPlugin(SimplePlugin):
    __slots__: tuple
    __markers: Any
    def __init__(self, parentObj):
        ...
    def start(self):
        ...
    def fini(self):
        ...
    def __onFrontLineInfoUpdated(self, frontlinePoints, attackerIntruder, defenderIntruder):
        ...
    def __addRPEntry(self, symbol, pos):
        ...

class EpicGlobalSettingsPlugin(GlobalSettingsPlugin):
    def _toogleVisible(self):
        ...

class StepRepairPointEntriesPlugin(SimplePlugin):
    __slots__: tuple
    __ptDict: Any
    def __init__(self, parentObj):
        ...
    def start(self):
        ...
    def fini(self):
        ...
    def __onCircleStatusChanged(self, type_, pointId, state):
        ...
    def __onStepRepairPointAdded(self, stepRepairPoint):
        ...
    def __onStepRepairPointActiveStateChanged(self, pointId, isActive):
        ...
    def __addRPEntry(self, symbol, position):
        ...

class ProtectionZoneEntriesPlugin(SimplePlugin):
    __slots__: tuple
    _zonesDict: Any
    __personalTeam: Any
    _symbol: Any
    def __init__(self, parentObj):
        ...
    def start(self):
        ...
    def fini(self):
        ...
    def __onProtZoneAdded(self, protZone, center, bounds):
        ...
    def __addProtectionZoneEntry(self, symbol, position):
        ...

class SectorOverlayEntriesPlugin(SectorStatusEntriesPlugin):
    _symbol: Any
    def __init__(self, parentObj):
        ...
    def start(self):
        ...
    def fini(self):
        ...
    def _onPlayerSectorGroupChanged(self, newSectorGroupID, isAllowed, oldSectorGroupID, wasAllowed):
        ...
    def __onOverlayTriggered(self, isActive):
        ...
    def __onRespawnVisibility(self, visible):
        ...

class EpicMinimapPingPlugin(plugins.MinimapPingPlugin):
    __baseInteractionList: Any
    __hqInteractionActive: Any
    _hitAreaSize: Any
    def __init__(self, parentObj):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def _onPlayerMissionUpdated(self, mission, _):
        ...
    def _getClickPosition(self, x, y):
        ...
    def _getIdByBaseNumber(self, team, number):
        ...
    def _processCommandByPosition(self, commands, locationCommand, position, minimapScaleIndex):
        ...
    def __make3DPingHQ(self, commands, bases):
        ...
    def __onSectorBaseAdded(self, sectorBase):
        ...
    def __getNearestHQForPosition(self, clickPos, range_):
        ...
    def __getNearestBaseForPosition(self, clickPos, range_):
        ...

class EpicTeleportPlugin(EpicMinimapPingPlugin):
    def onMinimapClicked(self, x, y, buttonIdx, minimapScaleIndex):
        ...

def makeMousePositionToEpicWorldPosition(clickedX, clickedY, bounds, hitArea=...):
    ...
