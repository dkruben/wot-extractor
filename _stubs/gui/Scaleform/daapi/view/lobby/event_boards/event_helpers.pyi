# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from io import BufferedIOBase as BufferedIOBase, TextIOWrapper as TextIOWrapper
from functools import wraps as wraps
from future.utils import lrange as lrange, viewitems as viewitems
from past.builtins import unicode as unicode
import xmltodict as xmltodict
from ResMgr import DataSection as DataSection
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE, MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL, MIN_VEHICLE_LEVEL as MIN_VEHICLE_LEVEL
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_DEBUG as LOG_DEBUG
from gui.impl import backport as backport
from helpers.i18n import makeString as _ms
from helpers import int2roman as int2roman, dependency as dependency
from nations import NAMES as NationNames
from bonus_readers import readBonusSection as readBonusSection
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.gui_items.Vehicle import VEHICLE_CLASS_NAME as VEHICLE_CLASS_NAME
from gui.server_events.bonuses import getEventBoardsBonusObj as getEventBoardsBonusObj
from gui.event_boards import event_boards_timer as event_boards_timer
from gui.event_boards.event_boards_items import CALCULATION_METHODS as _cm, OBJECTIVE_PARAMETERS as _op, EVENT_TYPE as _et, PLAYER_STATE_REASON as _psr, EVENT_STATE as _es, EVENT_DATE_TYPE as EVENT_DATE_TYPE, WOODEN_RIBBON as WOODEN_RIBBON
from gui.Scaleform.genConsts.EVENTBOARDS_ALIASES import EVENTBOARDS_ALIASES as EVENTBOARDS_ALIASES
from gui.Scaleform.locale.EVENT_BOARDS import EVENT_BOARDS as EVENT_BOARDS
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.Scaleform.daapi.view.lobby.event_boards.event_boards_vos import makeCantJoinReasonTextVO as makeCantJoinReasonTextVO, makeParameterTooltipVO as makeParameterTooltipVO, makePrimeTimesTooltipVO as makePrimeTimesTooltipVO
from gui.Scaleform.daapi.view.lobby.event_boards.formaters import formatVehicleNameWithTypeIcon as formatVehicleNameWithTypeIcon, getNationEmblemIcon as getNationEmblemIcon, getNationBigFlagIcon as getNationBigFlagIcon, getNationText as getNationText, vehicleTypeText as vehicleTypeText, formatTimeToEnd as formatTimeToEnd, formatErrorTextWithIcon as formatErrorTextWithIcon, formatOkTextWithIcon as formatOkTextWithIcon, formatTimeAndDate as formatTimeAndDate, formatUpdateTime as formatUpdateTime, formatAllertTextWithIcon as formatAllertTextWithIcon, formatAttentionTextWithIcon as formatAttentionTextWithIcon, timeEndStyle as timeEndStyle, getLevelBackgroundIcon as getLevelBackgroundIcon
from gui import GUI_NATIONS as GUI_NATIONS
from helpers.time_utils import ONE_MINUTE as ONE_MINUTE
LEVELS_RANGE: Any
BONUS_PRIORITY: tuple

class _Task(object):
    _event: Any
    def __init__(self, event):
        ...
    def getInfo(self):
        ...
    def getTooltip(self):
        ...

class _ObjectiveTask(_Task):
    _tooltipParameterMap: dict
    def getInfo(self):
        ...
    def getTooltip(self):
        ...

class _SelectionTask(_Task):
    selectionWithCardinality: tuple
    def getInfo(self):
        ...
    def getTooltip(self):
        ...

class _EventTypeTask(_Task):
    def getInfo(self):
        ...
    def getTooltip(self):
        ...

class _Condition(object):
    _event: Any
    def __init__(self, event):
        ...
    def getInfo(self):
        ...
    def getTooltip(self):
        ...

class _BattleTypeCondition(_Condition):
    def getInfo(self):
        ...
    def getTooltip(self):
        ...

class _PrimeTimeCondition(_Condition):
    _lobbyContext: Any
    _connectionMgr: Any
    def getInfo(self):
        ...
    def getTooltip(self):
        ...

class _VehiclesCondition(_Condition):
    itemsCache: Any
    def getInfo(self):
        ...
    def getTooltip(self):
        ...

class _TopLeaderboard(object):
    itemsCache: Any
    _event: Any
    _top: Any
    __eventType: Any
    __leaderboardId: Any
    __value: Any
    __rewardByRank: Any
    __notFull: Any
    __notInTop: Any
    def __init__(self, event, top):
        ...
    def getValue(self):
        ...
    def getInfo(self):
        ...
    def __getTitle(self):
        ...
    def __getDecoration(self):
        ...
    def __getRibbonTooltip(self):
        ...
    def __getDescriptionTooltip(self):
        ...
    def __getAmountTooltip(self):
        ...
    def __getPicture(self):
        ...
    def __getRaitingType(self):
        ...
    def __getRibbon(self):
        ...
    def __getMyPosititon(self):
        ...
    def __getStatusValue(self):
        ...

class EventInfo(object):
    _connectionMgr: Any
    _lobbyContext: Any
    _event: Any
    _playerData: Any
    _playerState: Any
    _top: Any
    _topMeta: Any
    topInfos: Any
    _objectiveTask: Any
    _selectionTask: Any
    _eventTypeTask: Any
    _battleTypeCondition: Any
    _primeTimeCondition: Any
    _vehiclesCondition: Any
    _state: Any
    _stateReasons: Any
    _canJoin: Any
    _joined: Any
    def __init__(self, event, playerData, eventsTop):
        ...
    def getTopInfo(self):
        ...
    def getTaskInfo(self):
        ...
    def getConditionInfo(self):
        ...
    def getAwardInfo(self):
        ...
    def isRegistration(self):
        ...
    def getServerData(self):
        ...
    def getStatusData(self):
        ...
    def getPopoverAlias(self):
        ...
    def __getTaskIcon(self, iconNum):
        ...
    def __getConditionIcon(self, iconNum):
        ...
    def __getPrimeTimesTooltip(self):
        ...

class EventHeader(object):
    _cantJoinReason: dict
    _event: Any
    _playerData: Any
    _playerState: Any
    _state: Any
    _joined: Any
    _stateReasons: Any
    _canJoin: Any
    def __init__(self, event, playerData):
        ...
    def getInfo(self):
        ...
    def getTimerInfo(self):
        ...
    def getParticipateInfo(self):
        ...

class CustomXMLGenerator(xmltodict.XMLGenerator):
    _write: Any
    _flush: Any
    _ns_contexts: Any
    _current_context: Any
    _undeclared_ns_maps: Any
    _encoding: Any
    def __init__(self, out=None, encoding='iso-8859-1', short_empty_elements=False):
        ...
    def startDocument(self):
        ...

def _readEventBoardsRewards(rewards):
    ...
def convertRewardsDictToBonusObjects(dictData, key='rewards'):
    ...
def checkEventExist(method):
    ...
