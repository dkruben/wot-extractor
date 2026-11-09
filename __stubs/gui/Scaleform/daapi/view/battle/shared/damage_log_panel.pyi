# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/damage_log_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import defaultdict as defaultdict
from future.utils import viewitems as viewitems
import BattleReplay as BattleReplay
from BattleFeedbackCommon import BATTLE_EVENT_TYPE as _BET
from account_helpers.settings_core.options import DamageLogDetailsSetting as _VIEW_MODE, DamageLogEventPositionsSetting as _EVENT_POSITIONS, DamageLogEventTypesSetting as _DISPLAYED_EVENT_TYPES
from account_helpers.settings_core.settings_constants import DAMAGE_LOG as DAMAGE_LOG, GRAPHICS as GRAPHICS
from constants import BATTLE_LOG_SHELL_TYPES as BATTLE_LOG_SHELL_TYPES, BOT_DISPLAY_CLASS_NAMES as BOT_DISPLAY_CLASS_NAMES, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE, BATTLE_LOG_MECHANIC_SHOT as BATTLE_LOG_MECHANIC_SHOT
from gui.Scaleform.daapi.view.meta.BattleDamageLogPanelMeta import BattleDamageLogPanelMeta as BattleDamageLogPanelMeta
from gui.Scaleform.genConsts.BATTLEDAMAGELOG_IMAGES import BATTLEDAMAGELOG_IMAGES as _IMAGES
from gui.Scaleform.genConsts.DAMAGE_LOG_SHELL_BG_TYPES import DAMAGE_LOG_SHELL_BG_TYPES as DAMAGE_LOG_SHELL_BG_TYPES
from gui.Scaleform.locale.INGAME_GUI import INGAME_GUI as INGAME_GUI
from gui.battle_control.battle_constants import PERSONAL_EFFICIENCY_TYPE as _ETYPE
from gui.battle_control.controllers.personal_efficiency_ctrl import _DamageEfficiencyInfo as _DamageEfficiencyInfo
from gui.impl import backport as backport
from gui.shared import events as gui_events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.gui_items.Vehicle import VEHICLE_CLASS_NAME as VEHICLE_CLASS_NAME
from helpers import dependency as dependency
from helpers import i18n as i18n
from shared_utils import BitmaskHelper as BitmaskHelper
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_POSITIVE_EVENTS_MASK: Any
_NEGATIVE_EVENTS_MASK: Any
_ALL_EVENTS_MASK: Any
_EVENT_POSITIONS_TO_CONTENT_MASK: dict
_EVENT_POSITIONS_TO_RECORD_STYLE: dict
_DISPLAYED_EVENT_TYPES_TO_CONTENT_MASK: dict
_TOTAL_DAMAGE_SETTINGS_TO_CONTENT_MASK: dict
_LOGS_SETTINGS: tuple
_VEHICLE_CLASS_TAGS_ICONS: dict
_SHELL_TYPES_TO_STR: dict
_MODE_IMAGES: dict
HIDDEN_SHELL = ''
_DEFAULT_VEHICLE_VO_BUILDER: Any
_EMPTY_SHELL_VO_BUILDER: Any
_DAMAGE_VALUE_VO_BUILDER: Any
_ETYPE_TO_RECORD_VO_BUILDER: dict

class _RECORD_STYLE(object):
    FULL = 0
    SHORT = 1

class _VOModel(dict):
    ...

class _VOModelProperty(object):
    __slots__: tuple
    name: Any
    def __init__(self, name):
        ...
    def __get__(self, model, objtype):
        ...
    def __set__(self, model, val):
        ...

class _IVOBuilder(object):
    def buildVO(self, info, arenaDP):
        ...

class _LogRecordVOBuilder(_IVOBuilder):
    __builders: Any
    def __init__(self, *builders):
        ...
    def buildVO(self, info, arenaDP):
        ...

class _VehicleVOModel(_VOModel):
    vehicleTypeImg: Any
    vehicleName: Any
    def __init__(self, vehicleTypeImg='', vehicleName=''):
        ...

class _VehicleVOBuilder(_IVOBuilder):
    def buildVO(self, info, arenaDP):
        ...
    def _populateVO(self, vehicleVO, info, arenaDP):
        ...

class _ReceivedHitVehicleVOBuilder(_VehicleVOBuilder):
    def _populateVO(self, vehicleVO, info, arenaDP):
        ...

class _ShellVOModel(_VOModel):
    shellTypeStr: Any
    shellTypeBG: Any
    def __init__(self, shellTypeStr='', shellTypeBG=''):
        ...

class _ShellVOBuilder(_IVOBuilder):
    def buildVO(self, info, arenaDP):
        ...
    def _getShellTypeStr(self, info):
        ...
    def _getShellTypeBg(self, info, arenaDP=None):
        ...

class _EmptyShellVOBuilder(_ShellVOBuilder):
    def _getShellTypeStr(self, info):
        ...
    def _getShellTypeBg(self, info, arenaDP=None):
        ...

class _StaticDeathZoneVOBuilder(_ShellVOBuilder):
    def _getShellTypeStr(self, info):
        ...
    def _getShellTypeBg(self, info, arenaDP=None):
        ...

class _MinefieldZoneVOBuilder(_ShellVOBuilder):
    def _getShellTypeStr(self, info):
        ...
    def _getShellTypeBg(self, info, arenaDP=None):
        ...

class _EpicDeathZoneVOBuilder(_ShellVOBuilder):
    def _getShellTypeStr(self, info):
        ...
    def _getShellTypeBg(self, info, arenaDP=None):
        ...

class _FireDamageZoneVOBuilder(_ShellVOBuilder):
    def _getShellTypeStr(self, info):
        ...
    def _getShellTypeBg(self, info, arenaDP=None):
        ...

class _DamageShellVOBuilder(_ShellVOBuilder):
    def buildVO(self, info, arenaDP):
        ...

class _CritsShellVOBuilder(_ShellVOBuilder):
    def buildVO(self, info, arenaDP):
        ...

class _ValueVOModel(_VOModel):
    value: Any
    def __init__(self, value=0):
        ...

class _ValueVOBuilder(_IVOBuilder):
    def buildVO(self, info, arenaDP):
        ...
    def _getValue(self, info):
        ...

class _CriticalHitValueVOBuilder(_ValueVOBuilder):
    def _getValue(self, info):
        ...

class _DamageValueVOBuilder(_ValueVOBuilder):
    def _getValue(self, info):
        ...

class _ShellModeImgVOModel(_VOModel):
    shellModeImg: Any
    def __init__(self, image=None):
        ...

class _ShellModeImgVOBuilder(_IVOBuilder):
    __defaultValue: Any
    def __init__(self, defaultValue=None):
        ...
    def buildVO(self, info, arenaDP):
        ...
    def _getShellModeImg(self, info):
        ...

class _ActionImgVOModel(_VOModel):
    actionTypeImg: Any
    def __init__(self, image=''):
        ...

class _ActionImgVOBuilder(_IVOBuilder):
    _image: Any
    def __init__(self, image):
        ...
    def buildVO(self, info, arenaDP):
        ...
    def _getImage(self, info):
        ...

class _DamageActionImgVOBuilder(_ActionImgVOBuilder):
    __slots__: tuple
    __shotIcon: Any
    __fireIcon: Any
    __ramIcon: Any
    __wcIcon: Any
    __berserkerIcon: Any
    __spawnBotDmgIcon: Any
    __mineFieldIcon: Any
    __smokeDmgIcon: Any
    __corrodingShotDmgIcon: Any
    __fireCircleDmgIcon: Any
    __clingBranderDmgIcon: Any
    __thunderStrikeIcon: Any
    __airstrikeIcon: Any
    __artilleryIcon: Any
    __airstrikeZoneIcon: Any
    __deathZoneIcon: Any
    __battleshipIcon: Any
    __destroyerIcon: Any
    __heRocketIcon: Any
    def __init__(self, shotIcon, fireIcon, ramIcon, wcIcon, mineFieldIcon, airstrikeIcon, artilleryIcon, airstrikeZoneIcon=None, deathZoneIcon=None, berserkerIcon=None, spawnBotDmgIcon=None, smokeDmgIcon=None, corrodingShotIcon=None, fireCircleDmgIcon=None, clingBranderDmgIcon=None, thunderStrikeIcon=None, battleshipIcon=None, destroyerIcon=None, heRocketIcon=None):
        ...
    def _getImage(self, info):
        ...

class _AssistActionImgVOBuilder(_ActionImgVOBuilder):
    def __init__(self):
        ...
    def _getImage(self, info):
        ...

class _LogViewComponent(object):
    __setListProxy: Any
    __addToListProxy: Any
    __efficiencyCtrl: Any
    __arenaDP: Any
    _logViewMode: Any
    __isVisible: Any
    __contentMask: Any
    __recordStyle: Any
    def __init__(self):
        ...
    def initialize(self, setListProxyMethod, addToListProxyMethod, efficiencyCtrl, arenaDP):
        ...
    def dispose(self):
        ...
    def clear(self):
        ...
    def invalidate(self):
        ...
    def updateLog(self, contentMask=None, viewMode=None, recordStyle=...):
        ...
    def addToLog(self, events):
        ...
    def _getLogMessages(self, contentMask):
        ...
    def _buildLogMessageVO(self, info):
        ...

class DamageLogPanel(BattleDamageLogPanelMeta):
    sessionProvider: Any
    settingsCore: Any
    lobbyContext: Any
    __efficiencyCtrl: Any
    __arenaDP: Any
    __vehStateCtrl: Any
    _isVisible: Any
    _isFullStatsShown: Any
    _isWinnerScreenShown: Any
    _logViewMode: Any
    __totalDamageContentMask: Any
    __totalValues: Any
    _totalEvents: Any
    _topLog: Any
    _bottomLog: Any
    def __init__(self):
        ...
    def isSwitchToVehicle(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _invalidateContent(self):
        ...
    def _invalidateLogs(self):
        ...
    def _invalidateTotalDamages(self):
        ...
    def _onTotalEfficiencyUpdated(self, diff):
        ...
    def _onPersonalEfficiencyLogSynced(self):
        ...
    def _onEfficiencyReceived(self, events):
        ...
    def _invalidatePanelVisibility(self):
        ...
    def _onSettingsChanged(self, diff):
        ...
    def _onPostMortemSwitched(self, noRespawnPossible, respawnAvailable):
        ...
    def _onVehicleControlling(self, vehicle):
        ...
    def _handleShowExtendedInfo(self, event):
        ...
    def _handleShowCursor(self, _):
        ...
    def _handleHideCursor(self, _):
        ...
    def __handleShowFullStats(self, event):
        ...
    def __onWinnerScreen(self):
        ...
    def _setTotalValue(self, etype, value):
        ...
    def _updateTopLog(self, isVisible, isShortMode, records):
        ...
    def _addToTopLog(self, value, actionTypeImg, vehicleTypeImg, vehicleName, shellTypeStr, shellTypeBG, shellModeImg=None):
        ...
    def _updateBottomLog(self, isVisible, isShortMode, records):
        ...
    def _addToBottomLog(self, value, actionTypeImg, vehicleTypeImg, vehicleName, shellTypeStr, shellTypeBG, shellModeImg=None):
        ...
    def _updateTotalDamageValue(self, value):
        ...
    def _updateTotalBlockedDamageValue(self, value):
        ...
    def _updateTotalAssistValue(self, value):
        ...
    def _updateTotalStunValue(self, value):
        ...
    def _setSettings(self, isVisible, isColorBlind):
        ...
    def __isDamageSettingEnabled(self, settingName):
        ...

def _formatTotalValue(value):
    ...
