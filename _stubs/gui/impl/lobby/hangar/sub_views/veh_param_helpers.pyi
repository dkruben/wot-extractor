# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/sub_views/veh_param_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import json as json
from builtins import round as round
from past.builtins import basestring as basestring
from gui.impl import backport as backport
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicle_param_base_view_model import HighlightType as HighlightType
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicle_param_group_view_model import BuffIconType as BuffIconType
from gui.shared.gui_items import KPI as KPI, kpiFormatValue as kpiFormatValue
from gui.shared.items_parameters import MAX_RELATIVE_VALUE as MAX_RELATIVE_VALUE
from gui.shared.items_parameters.comparator import PARAM_STATE as PARAM_STATE
from gui.shared.items_parameters.formatters import FORMAT_SETTINGS as FORMAT_SETTINGS, KPI_FORMATTERS as KPI_FORMATTERS, SMART_ROUND_PARAMS as SMART_ROUND_PARAMS
from gui.shared.items_parameters.params_helper import hasPositiveEffect as hasPositiveEffect, hasNegativeEffect as hasNegativeEffect, hasGroupPenalties as hasGroupPenalties
_EQUAL_TO_ZERO_LITERAL = '~0'
_NUMBER_DIGITS = 2
_STATE_COLOR_MAP: dict

def getGroupIcon(parameter, comparator):
    ...
def getMaxValue(value, delta):
    ...
def _applyFormat(value, state, settings, doSmartRound, isColorize, nDigits=...):
    ...
def colorize(paramStr, state):
    ...
def _cutDigits(value, nDigits=...):
    ...
def _mapStateToHighlight(state):
    ...
def formatParameterValue(parameterName, paramValue, applyFormatting=True, parameterState=None, formatSettings=None, allowSmartRound=True, showZeroDiff=False, isColorize=True, nDigits=...):
    ...
def formatAdditionalParameter(parameter, isApproximately=False):
    ...
