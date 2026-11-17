# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/personal_progress/formatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
from constants import QUEST_PROGRESS_STATE as QUEST_PROGRESS_STATE
from gui.Scaleform.genConsts.QUEST_PROGRESS_BASE import QUEST_PROGRESS_BASE as QUEST_PROGRESS_BASE
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS as PERSONAL_MISSIONS
from gui.Scaleform.locale.PERSONAL_MISSIONS_30 import PERSONAL_MISSIONS_30 as PERSONAL_MISSIONS_30
from gui.Scaleform.locale.BATTLE_RESULTS import BATTLE_RESULTS as BATTLE_RESULTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.server_events.personal_progress.storage import PostBattleProgressStorage as PostBattleProgressStorage, LobbyProgressStorage as LobbyProgressStorage
from gui.shared.formatters import text_styles as text_styles
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import i18n as i18n
from personal_missions import PM_BRANCH as PM_BRANCH
from personal_missions_constants import DISPLAY_TYPE as DISPLAY_TYPE, MULTIPLIER_SCOPE as MULTIPLIER_SCOPE
from shared_utils import first as first, findFirst as findFirst

class ProgressesFormatter(object):
    __slots__: tuple
    _storage: Any
    _dummyHeaderType: Any
    def __init__(self, storage, dummyHeaderType=...):
        ...
    def bodyFormat(self, isMain=None):
        ...
    def headerFormat(self, isMain=None, isCompleted=False, isBranchWithoutAwardListQuests=False):
        ...
    @classmethod
    def _makeBodyProgressData(cls, progress, isLastProgress=False):
        ...
    def _bodyFormat(self, isMain):
        ...
    def __addUniqueHeaderProgress(self, isCompleted, data):
        ...
    def __addDummyHeaderProgress(self, isMain):
        ...

class DetailedProgressFormatter(ProgressesFormatter):
    def __init__(self, storage, personalMission):
        ...
    def hasProgressForReset(self):
        ...
    @classmethod
    def _makeBodyProgressData(cls, progress, isLastProgress=False):
        ...

class PostBattleConditionsFormatter(object):
    __slots__: tuple
    __event: Any
    __storage: Any
    __wasMultiplied: Any
    __wasFailed: Any
    def __init__(self, event, progressData):
        ...
    def getConditionsData(self, isMain):
        ...
    def getMultiplierDescription(self):
        ...
    def getFailedDescription(self):
        ...
    def __getPureConditionsData(self, isMain):
        ...
    def __getPureConditionStatusValues(self, progress):
        ...
    def __getTitleStatusValues(self, isMain):
        ...
    def __packBlock(self, text, statusValues=None):
        ...
    def __packCondition(self, conditionText, statusValues=None):
        ...
    def __packTitle(self, titleText, titleStatusValues=None):
        ...
    def __packStatusText(self, statusConditionValues):
        ...

class PMTooltipConditionsFormatters(object):
    _CONDITION: Any
    def format(self, event, isMain=None, isForNewTooltip=False):
        ...

class PMAwardScreenConditionsFormatter(ProgressesFormatter):
    MAIN_PROGRESS_DATA = 'mainHeaderProgressData'
    ADD_PROGRESS_DATA = 'addHeaderProgressData'
    MAIN_VALUE_DATA = 'mainConditions'
    ADD_VALUE_DATA = 'addConditions'
    def __init__(self, event):
        ...
    def getConditionsData(self, main, add):
        ...
    def _getIterateData(self, headerProgress, bodyProgresses):
        ...
    def _getValueData(self, progresses):
        ...
    @classmethod
    def _getIcon(cls, key):
        ...
    @classmethod
    def _makeBodyProgressData(cls, progress, isLastProgress=False):
        ...

class PMCardConditionsFormatter(DetailedProgressFormatter):
    def __init__(self, event):
        ...
