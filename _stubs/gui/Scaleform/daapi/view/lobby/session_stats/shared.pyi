# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/session_stats/shared.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from future.utils import viewitems as viewitems
import nations as nations
from account_helpers.settings_core.settings_constants import SESSION_STATS as SESSION_STATS
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.daapi.view.lobby.session_stats.session_stats_settings_controller import SessionStatsSettingsController as SessionStatsSettingsController
from gui.Scaleform.genConsts.SESSION_STATS_CONSTANTS import SESSION_STATS_CONSTANTS as SESSION_STATS_CONSTANTS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.utils.functions import makeTooltip as makeTooltip
_INFOTIP_PRECISION = 4
_EFFICIENT_DATA: dict
_VIEW_ECONOMIC_DATA_WITH_SPENIDNG: tuple
_VIEW_ECONOMIC_DATA_WITHOUT_SPENIDNG: tuple
_ECONOMIC_DATA: dict
_PROP_ID_TO_POSITIVE_VALUE_STYLE_MAP: dict

def toNiceNumber(value, coef=1):
    ...
def packTotalPropData(sessionStats, propId):
    ...
def packEfficiencyPropData(randomStats, sessionStats, accountWtr, propId):
    ...
def packLastBattleData(data):
    ...
def packTotalData(data):
    ...
def packBattleEfficiencyData(data, parameters):
    ...
def makeTooltipData(header, resId, total):
    ...
def toIntegral(value):
    ...
def precisionFormat(value, showIntegerOnly=False):
    ...
def getDeltaAsData(deltaVal):
    ...
def getNationIcon(nationID, width, height):
    ...
def getSessionStatsPropImage(propId, width=54, height=54):
    ...
def processRatioValue(value):
    ...
