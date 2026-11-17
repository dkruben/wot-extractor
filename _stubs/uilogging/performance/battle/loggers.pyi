# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/performance/battle/loggers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import iteritems as iteritems
import BigWorld as BigWorld
from helpers import dependency as dependency
from skeletons.helpers.statistics import IStatisticsCollector as IStatisticsCollector
from uilogging.base.logger import _BaseLogger as Logger
from uilogging.constants import DEFAULT_LOGGER_NAME as DEFAULT_LOGGER_NAME
from uilogging.performance.battle.constants import Features as Features, Groups as Groups, LogActions as LogActions
from uilogging.helpers import getClientSessionID as getClientSessionID
from wotdecorators import noexcept as noexcept
from uilogging.types import GroupType as GroupType, PartnerIdType as PartnerIdType
_logger: Any

class _BaseBattleMetricsLogger(Logger):
    __slots__: tuple
    def __init__(self, group):
        ...
    # decorador original: @noexcept
    def log(self, data, partnerID=None, sessionID=''):
        ...

class _ClientSessionLogger(_BaseBattleMetricsLogger):
    __slots__: tuple
    def __init__(self):
        ...

class _ClientSystemLogger(_BaseBattleMetricsLogger):
    __slots__: tuple
    def __init__(self):
        ...

class BattleMetricsLogger(object):
    __slots__: tuple
    statsCollector: Any
    _loggers: Any
    _defaultLogger: Any
    def __init__(self):
        ...
    def initialize(self):
        ...
    # decorador original: @noexcept
    def log(self):
        ...
