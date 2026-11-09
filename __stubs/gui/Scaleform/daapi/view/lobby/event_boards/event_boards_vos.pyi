# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_boards_vos.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from future.utils import viewitems as viewitems
import nations as nations
from gui import GUI_NATIONS_ORDER_INDEX_REVERSED as GUI_NATIONS_ORDER_INDEX_REVERSED
from gui.impl import backport as backport
from gui.shared.gui_items.Vehicle import getSmallIconPath as getSmallIconPath, Vehicle as Vehicle, VEHICLE_TABLE_TYPES_ORDER_INDICES_REVERSED as VEHICLE_TABLE_TYPES_ORDER_INDICES_REVERSED, getTypeSmallIconPath as getTypeSmallIconPath, getTypeBigIconPath as getTypeBigIconPath
from helpers import int2roman as int2roman, dependency as dependency
from helpers.i18n import makeString as _ms
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.shared.formatters import text_styles as text_styles
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.server_events.awards_formatters import QuestsBonusComposer as QuestsBonusComposer, getEventBoardsAwardPacker as getEventBoardsAwardPacker
from gui.Scaleform.genConsts.EVENTBOARDS_ALIASES import EVENTBOARDS_ALIASES as EVENTBOARDS_ALIASES
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.Scaleform.locale.EVENT_BOARDS import EVENT_BOARDS as EVENT_BOARDS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.daapi.view.lobby.event_boards.formaters import formatErrorTextWithIcon as formatErrorTextWithIcon, formatOkTextWithIcon as formatOkTextWithIcon, formatNotAvailableTextWithIcon as formatNotAvailableTextWithIcon, formatParameters as formatParameters, getFullName as getFullName, getString as getString, getClanTag as getClanTag, getStatusTitleStyle as getStatusTitleStyle, formatAdditionalParameters as formatAdditionalParameters, formatDate as formatDate, formatTime as formatTime
from gui.event_boards.event_boards_items import EVENT_TYPE as EVENT_TYPE, ExcelItem as ExcelItem, PlayerEventsData as PlayerEventsData, EventSettings as EventSettings, OBJECTIVE_PARAMETERS as _op, PLAYER_STATE_REASON as _psr, CALCULATION_METHODS as _cm
from gui.Scaleform import getNationsFilterAssetPath as getNationsFilterAssetPath
from nations import AVAILABLE_NAMES as AVAILABLE_NAMES
from skeletons.gui.shared import IItemsCache as IItemsCache
_CATEGORY_NAMES: dict
FORMATS: dict
_LEADERBOARD_BG_CREATORS: dict
_OBJECTIVE_STRINGS: dict
_METHOD_ICON_NAMES: dict

class EVENT_BOARDS_GROUP_TYPES(object):
    GOLD = 1
    SILVER = 2
    BRONZE = 3
    IRON = 4
    WOOD = 5

def _vehicleHeaderCreator(vehicleCDStr):
    ...
def makeTableViewHeaderVO(eType, value, eventName, status=None, statusTooltip=None):
    ...
def makeTableViewBackgroundVO(eType, value):
    ...
def makeTableHeaderVO(method, objective, eventType):
    ...
def makeEventBoardsTableDataVO(rewardCategories, method):
    ...
def makeParameterTooltipVO(method, amount, parameter):
    ...
def makeEventBoardsTableViewStatusVO(title, tooltip, info, value1, value2, value3, showPoints, buttonLabel, buttonTooltip, buttonVisible, buttonEnabled, titleTooltip, method):
    ...
def makeAwardGroupDataTooltipVO(rewardCategories, enabledAncors):
    ...
def makeFiltersVO(eventType, filters, selected=None, category=None):
    ...
def _makeCantJoinReasonTooltip(stateReasons, playerData, limits):
    ...
def makeCantJoinReasonTextVO(event, playerData):
    ...
def makeVehicleVO(vehicle):
    ...
def makeVehiclePopoverVO(vehicle):
    ...
def vehicleValueGetter(vehicle, field):
    ...
def makePrimeTimesTooltipVO(primeTimes, currentPeripheryID, getNameFunc):
    ...
