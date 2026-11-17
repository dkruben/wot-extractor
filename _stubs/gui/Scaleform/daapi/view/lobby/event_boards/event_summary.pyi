# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_summary.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers.time_utils import ONE_MINUTE as ONE_MINUTE
from helpers import dependency as dependency
from helpers import int2roman as int2roman
from helpers.i18n import makeString as _ms
from gui.shared.formatters import text_styles as text_styles
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.Scaleform.daapi.view.lobby.event_boards.formaters import formatVehicleNameWithTypeIcon as formatVehicleNameWithTypeIcon, getNationTextWithIcon as getNationTextWithIcon, formatVehicleNationAndTypeIcon as formatVehicleNationAndTypeIcon, vehicleTypeText as vehicleTypeText, getFullName as getFullName, formatTimeAndDate as formatTimeAndDate, formatUpdateTime as formatUpdateTime
from gui.Scaleform.genConsts.EVENTBOARDS_ALIASES import EVENTBOARDS_ALIASES as EVENTBOARDS_ALIASES
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.Scaleform.locale.EVENT_BOARDS import EVENT_BOARDS as EVENT_BOARDS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.event_boards.event_boards_items import CALCULATION_METHODS as _cm, OBJECTIVE_PARAMETERS as _op, EVENT_TYPE as _et, WOODEN_RIBBON as WOODEN_RIBBON
from skeletons.gui.shared import IItemsCache as IItemsCache
_PARAMETER_VALUE_GETTER: dict
_AVERAGE_ICON_BY_PARAMETER: dict
_MAX_ICON_BY_PARAMETER: dict
_SUM_ICON_BY_PARAMETER: dict
_ICON_BY_PARAMETER: dict
ICON_ALPHA_USED_IN_CALCULATION = 1.0
ICON_ALPHA_NOT_USED_IN_CALCULATION = 0.2
summaryByMethod: dict

class _Summary(object):
    itemsCache: Any
    _excelItem: Any
    _event: Any
    _leaderboard: Any
    _leaderboardId: Any
    _value: Any
    _descriptionByType: Any
    _iconByType: Any
    def __init__(self, event, leaderboard, excelItem, descriptionByType, iconByType):
        ...
    def isTable(self):
        ...
    def getHeader(self):
        ...
    def getExperienceBlock(self):
        ...
    def getStatisticsBlock(self):
        ...
    def getTableData(self):
        ...
    def getTableHeaderData(self):
        ...
    def _getStatisticsBlock(self):
        ...
    def _getDescription(self):
        ...
    def _getDescription2(self):
        ...
    def _getTableData(self):
        ...
    def _getTableHeaderData(self):
        ...
    def __getRibbon(self):
        ...
    def _getStatusTooltip(self):
        ...

class _SummaryMax(_Summary):
    _ParameterOrder: tuple
    def __init__(self, event, leaderboard, excelItem):
        ...
    def _getStatisticsBlock(self):
        ...
    def _getDescription2(self):
        ...

class _SummarySumAll(_Summary):
    def __init__(self, event, leaderboard, excelItem):
        ...
    def _getStatisticsBlock(self):
        ...

class _SummaryTable(_Summary):
    _ParameterOrder: tuple
    _TableIconByParameter: dict
    def isTable(self):
        ...
    def _getTableHeaderData(self):
        ...
    def _getTableData(self):
        ...
    def __getSortedParams(self):
        ...

class _SummarySumN(_SummaryTable):
    def __init__(self, event, leaderboard, excelItem):
        ...

class _SummarySumSeqN(_SummaryTable):
    def __init__(self, event, leaderboard, excelItem):
        ...

class _SummarySumMSeqN(_SummaryTable):
    def __init__(self, event, leaderboard, excelItem):
        ...

def _getParameterValue(op, info):
    ...
def getSummaryInfoData(event, leaderboard, data):
    ...
