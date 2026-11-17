# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/personal_progress/metrics_wrappers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from constants import QUEST_PROGRESS_STATE as QUEST_PROGRESS_STATE
from gui.Scaleform.genConsts.QUESTSPROGRESS import QUESTSPROGRESS as QUESTSPROGRESS
from gui.Scaleform.genConsts.QUEST_PROGRESS_BASE import QUEST_PROGRESS_BASE as QUEST_PROGRESS_BASE
from gui.Scaleform.locale.QUESTS import QUESTS as QUESTS
from gui.impl import backport as backport
from helpers.time_utils import ONE_MINUTE as ONE_MINUTE

class METRICS_TYPES(object):
    SIMPLE = QUEST_PROGRESS_BASE.QP_METRIC_TYPE_SIMPLE
    SIMPLE_VALUE = QUEST_PROGRESS_BASE.QP_METRIC_TYPE_SIMPLE_VALUE
    RANGE_VALUE = QUEST_PROGRESS_BASE.QP_METRIC_TYPE_RANGE
    VEHICLES_VALUE = QUEST_PROGRESS_BASE.QP_METRIC_TYPE_VEHICLES
    TIMER_VALUE = QUEST_PROGRESS_BASE.QP_METRIC_TYPE_TIMER

def wrapSimple(_):
    ...
def wrapRangeValue(progress):
    ...
def wrapCurrentValue(progress):
    ...
def wrapVehiclesValue(progress):
    ...
def wrapLimiterValue(progress):
    ...
def wrapTimerValue(progress):
    ...
def _formatValue(value):
    ...
def _wrapSimpleValue(title, value):
    ...
def _wrapVehiclesValue(title, current, targets):
    ...
def _wrapTimerValue(timeLeft):
    ...
