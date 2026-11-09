# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/personal_progress/strategy.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
from constants import QUEST_PROGRESS_STATE as QUEST_PROGRESS_STATE
from gui.Scaleform.genConsts.QUEST_PROGRESS_BASE import QUEST_PROGRESS_BASE as QUEST_PROGRESS_BASE
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS as PERSONAL_MISSIONS
from gui.shared.formatters import text_styles as text_styles
from helpers import i18n as i18n
_logger: Any

class IProgressGetter(object):
    @classmethod
    def getGoal(cls, progress):
        ...
    @classmethod
    def getCurrent(cls, progress):
        ...

class BinaryProgressGetter(IProgressGetter):
    MAX_GOAL_VALUE = 1
    @classmethod
    def getGoal(cls, progress):
        ...
    @classmethod
    def getCurrent(cls, progress):
        ...

class ValueProgressGetter(IProgressGetter):
    @classmethod
    def getGoal(cls, progress):
        ...
    @classmethod
    def getCurrent(cls, progress):
        ...

class AverageProgressGetter(ValueProgressGetter):
    @classmethod
    def getAverageGoal(cls, progress, counter):
        ...
    @classmethod
    def getAverageValue(cls, progress, counter):
        ...

class CounterProgressGetter(IProgressGetter):
    @classmethod
    def getGoal(cls, progress):
        ...
    @classmethod
    def getCurrent(cls, progress):
        ...

class BiathlonProgressGetter(IProgressGetter):
    @classmethod
    def getGoal(cls, progress):
        ...
    @classmethod
    def getCurrent(cls, progress):
        ...
    @classmethod
    def getBiathlonProgress(cls, progress):
        ...

class ILabelGetter(object):
    @classmethod
    def getBottomLabel(cls, progress):
        ...
    @classmethod
    def _getCompleteLabel(cls, progress):
        ...
    @classmethod
    def getHeaderLabel(cls, progress):
        ...

class BiathlonLabelGetter(ILabelGetter):
    @classmethod
    def getHeaderLabel(cls, progress):
        ...
    @classmethod
    def _getCompleteLabel(cls, progress):
        ...

class CounterLabelGetter(ILabelGetter):
    @classmethod
    def getHeaderLabel(cls, progress):
        ...

class SeriesLabelGetter(ILabelGetter):
    @classmethod
    def getHeaderLabel(cls, progress):
        ...

class LimitedTriesLabelGetter(ILabelGetter):
    @classmethod
    def getHeaderLabel(cls, progress):
        ...
    @classmethod
    def getBottomLabel(cls, progress):
        ...
