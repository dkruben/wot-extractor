# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/classic/minimap.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BattleReplay as BattleReplay
import BigWorld as BigWorld
import CommandMapping as CommandMapping
import Keys as Keys
import Math as Math
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers import AccountSettings as AccountSettings
from account_helpers.settings_core import settings_constants as settings_constants
from chat_commands_consts import BATTLE_CHAT_COMMAND_NAMES as BATTLE_CHAT_COMMAND_NAMES, getBaseTeamAndIDFromUniqueID as getBaseTeamAndIDFromUniqueID, MarkerType as MarkerType, getUniqueTeamOrControlPointID as getUniqueTeamOrControlPointID
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui import GUI_SETTINGS as GUI_SETTINGS, g_repeatKeyHandlers as g_repeatKeyHandlers
from gui.Scaleform.daapi.view.battle.shared.minimap import common as common, plugins as plugins
from gui.Scaleform.daapi.view.battle.shared.minimap import component as component
from gui.Scaleform.daapi.view.battle.shared.minimap import settings as settings
from gui.Scaleform.daapi.view.battle.shared.minimap.plugins import _LOCATION_PING_RANGE as _LOCATION_PING_RANGE, _BASE_PING_RANGE as _BASE_PING_RANGE, _EMinimapMouseKey as _EMinimapMouseKey
from gui.Scaleform.genConsts.BATTLE_MINIMAP_CONSTS import BATTLE_MINIMAP_CONSTS as BATTLE_MINIMAP_CONSTS
from gui.battle_control import minimap_utils as minimap_utils, avatar_getter as avatar_getter
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from messenger import MessengerEntry as MessengerEntry
from messenger.proto.bw_chat2.battle_chat_cmd import BASE_CMD_NAMES as BASE_CMD_NAMES
from messenger_common_chat2 import MESSENGER_ACTION_IDS as _ACTIONS
_C_NAME = settings.CONTAINER_NAME
_S_NAME = settings.ENTRY_SYMBOL_NAME
_MIN_BASE_SCALE = 1.0
_MAX_BASE_SCALE = 0.6
_logger: Any
_CLASSIC_MINIMAP_DIMENSIONS = 10

class ClassicMinimapComponent(component.MinimapComponent):
    def _setupPlugins(self, arenaVisitor):
        ...
    def hasMinimapGrid(self):
        ...
    def getMinimapDimensions(self):
        ...

class GlobalSettingsPlugin(common.SimplePlugin):
    __slots__: tuple
    _AccountSettingsClass = AccountSettings
    _currentSizeSettings: Any
    _isVisible: Any
    _sizeIndex: Any
    __canChangeAlpha: Any
    def __init__(self, parentObj):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def setSettings(self):
        ...
    def updateSettings(self, diff):
        ...
    def applyNewSize(self, sizeIndex):
        ...
    def _changeSizeSettings(self, newSizeSettings):
        ...
    def _toogleVisible(self):
        ...
    def _saveSettings(self):
        ...
    def __setSizeByStep(self, step):
        ...
    def __handleKey(self, key):
        ...
    def __handleRepeatKeyEvent(self, event):
        ...
    def _handleMinimapCmd(self, event):
        ...
    def __updateAlpha(self):
        ...

class TeamsOrControlsPointsPlugin(common.EntriesPlugin):
    __slots__: tuple
    __personalTeam: Any
    __entries: Any
    __markerIDs: Any
    __hasActiveCommit: Any
    def __init__(self, parentObj):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def restart(self):
        ...
    def __onActionAddedToMarkerReceived(self, senderID, commandID, markerType, objectID):
        ...
    def __onReplyFeedbackReceived(self, ucmdID, replierID, markerType, oldReplyCount, newReplyCount):
        ...
    def __onRemoveCommandReceived(self, removeID, markerType):
        ...
    def __onTeamChanged(self, teamID):
        ...
    def __addBaseEntry(self, symbol, position, uid):
        ...
    def __addPointEntry(self, symbol, position, number):
        ...
    def __addTeamSpawnPoints(self):
        ...
    def __addTeamBasePositions(self):
        ...
    def __addControlPoints(self):
        ...

class ClassicMinimapPingPlugin(plugins.MinimapPingPlugin):
    def _getClickPosition(self, x, y):
        ...
    def _getIdByBaseNumber(self, team, number):
        ...
    def _processCommandByPosition(self, commands, locationCommand, position, minimapScaleIndex):
        ...
    def __getNearestBaseForPosition(self, inPosition, range_):
        ...

class ClassicTeleportPlugin(ClassicMinimapPingPlugin):
    def onMinimapClicked(self, x, y, buttonIdx, minimapScaleIndex):
        ...
