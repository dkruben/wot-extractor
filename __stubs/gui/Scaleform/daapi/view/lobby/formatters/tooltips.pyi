# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/formatters/tooltips.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.impl.gen import R as R
from gui.impl import backport as backport
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.shared.formatters.time_formatters import formatDate as formatDate
from gui.shared.tooltips import formatters as formatters
from helpers import time_utils as time_utils, dependency as dependency
from gui.shared.formatters import text_styles as text_styles
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from items.writers.c11n_writers import natsorted as natsorted
from gui.prb_control.settings import SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from season_common import GameSeason as GameSeason
from skeletons.gui.game_control import ISeasonProvider as ISeasonProvider
_MODENAME_TO_PO_FILE: dict

# decorador original: @dependency.replace_none_kwargs(...)
def getTimeTableBlock(modeCtrl, modeName, leftPadding=0, connectionMgr=None):
    ...
def packCalendarBlock(modeCtrl, selectedTime, modeName):
    ...
def packTimeTableHeaderBlock(modeName):
    ...
def _packTimeBlock(message, timeStr):
    ...
def _packPeriods(periods, modeName):
    ...
def __packServerTimeBlock(serverStr, timeStr):
    ...
def getScheduleBlock(modeCtrl, modeName, actualSeason, seasonIsStarted, timeStringGetter):
    ...
def _getTimeBlock(isSeasonStarted, tillEnd, timeStamp, modeName, timeStringGetter, leftPadding=0):
    ...
