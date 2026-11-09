# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/cond_formatters/tokens.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from gui.server_events.cond_formatters.formatters import ConditionFormatter as ConditionFormatter, ConditionsFormatter as ConditionsFormatter
from gui.server_events.formatters import TOKEN_SIZES as TOKEN_SIZES
from gui.shared.formatters import text_styles as text_styles
from helpers import dependency as dependency
from skeletons.gui.server_events import IEventsCache as IEventsCache
from soft_exception import SoftException as SoftException
_PreFormattedTokenCondition: Any

class PreFormattedTokenCondition(_PreFormattedTokenCondition):
    eventsCache: Any
    @property
    def gotCount(self):
        ...
    @property
    def title(self):
        ...
    def getCounterText(self):
        ...
    def getImage(self, size):
        ...

class TokenConditionFormatter(ConditionFormatter):
    def format(self, condition, event):
        ...

class TokensConditionFormatter(ConditionsFormatter):
    def __init__(self):
        ...
    def format(self, conditions, event):
        ...
    def _packCondition(self, *args, **kwargs):
        ...
    def _getFormattedField(self, *args, **kwargs):
        ...
    def _packConditions(self, *args, **kwargs):
        ...

class TokensMarathonFormatter(object):
    BIG_ICONS_COUNT = 2
    __tokensConditionsFormatter: Any
    def __init__(self):
        ...
    def format(self, event):
        ...
