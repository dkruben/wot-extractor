# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/battle_results/packers/fun_progression_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
from future.utils import listvalues as listvalues, viewitems as viewitems, viewvalues as viewvalues
import math_utils as math_utils
from fun_random.gui.feature.fun_constants import FEP_PROGRESSION_BASE_TEMPLATE as FEP_PROGRESSION_BASE_TEMPLATE, FEP_PROGRESSION_TRIGGER_QUEST_ID as FEP_PROGRESSION_TRIGGER_QUEST_ID, FEP_PROGRESSION_ALT_TRIGGER_QUEST_ID as FEP_PROGRESSION_ALT_TRIGGER_QUEST_ID, FEP_PROGRESSION_UNLIMITED_TRIGGER_QUEST_ID as FEP_PROGRESSION_UNLIMITED_TRIGGER_QUEST_ID, FEP_PROGRESSION_UNLIMITED_ALT_TRIGGER_QUEST_ID as FEP_PROGRESSION_UNLIMITED_ALT_TRIGGER_QUEST_ID, FEP_PROGRESSION_EXECUTOR_QUEST_ID as FEP_PROGRESSION_EXECUTOR_QUEST_ID, FEP_PROGRESSION_UNLIMITED_EXECUTOR_QUEST_ID as FEP_PROGRESSION_UNLIMITED_EXECUTOR_QUEST_ID, FEP_PROGRESSION_COUNTER_ID as FEP_PROGRESSION_COUNTER_ID, FEP_PROGRESSION_UNLIMITED_COUNTER_ID as FEP_PROGRESSION_UNLIMITED_COUNTER_ID
from shared_utils import first as first, findFirst as findFirst
from fun_random.gui.feature.models.progressions import FunProgression as FunProgression
_START_STAGE = 0
_PbsProgress: Any

class _PostbattleProgressionHelper(object):
    __slots__: tuple
    _TRIGGER_QUEST_ID = None
    _ALT_TRIGGER_QUEST_ID = None
    _EXECUTOR_QUEST_ID = None
    _COUNTER_ID = None
    _triggers: Any
    _altTriggers: Any
    _executors: Any
    _countersProgress: Any
    def __init__(self):
        ...
    def getProgressionData(self, progression, questsProgress, questsTokens):
        ...
    def _collectProgressionData(self, progression):
        ...
    def _getBonuses(self, progression, diffStage=None):
        ...
    def _getPoints(self):
        ...
    def _hasProgress(self):
        ...
    def __parseProgress(self, progression, questsProgress, questsTokens):
        ...

class FunPbsProgressionHelper(_PostbattleProgressionHelper):
    __slots__: tuple
    _TRIGGER_QUEST_ID = FEP_PROGRESSION_TRIGGER_QUEST_ID
    _ALT_TRIGGER_QUEST_ID = FEP_PROGRESSION_ALT_TRIGGER_QUEST_ID
    _EXECUTOR_QUEST_ID = FEP_PROGRESSION_EXECUTOR_QUEST_ID
    _COUNTER_ID = FEP_PROGRESSION_COUNTER_ID
    def _collectProgressionData(self, progression):
        ...
    def _getBonuses(self, progression):
        ...
    def __getActiveQuests(self, triggers):
        ...

class FunPbsUnlimitedProgressionHelper(_PostbattleProgressionHelper):
    __slots__: tuple
    _TRIGGER_QUEST_ID = FEP_PROGRESSION_UNLIMITED_TRIGGER_QUEST_ID
    _ALT_TRIGGER_QUEST_ID = FEP_PROGRESSION_UNLIMITED_ALT_TRIGGER_QUEST_ID
    _EXECUTOR_QUEST_ID = FEP_PROGRESSION_UNLIMITED_EXECUTOR_QUEST_ID
    _COUNTER_ID = FEP_PROGRESSION_UNLIMITED_COUNTER_ID
    def _collectProgressionData(self, progression):
        ...
    def _getBonuses(self, progression, diffStage=None):
        ...
