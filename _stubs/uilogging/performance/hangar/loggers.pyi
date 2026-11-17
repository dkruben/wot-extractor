# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/performance/hangar/loggers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
from uilogging.base.logger import _BaseLogger as Logger, createPartnerID as createPartnerID
from uilogging.constants import DEFAULT_LOGGER_NAME as DEFAULT_LOGGER_NAME
from uilogging.performance.hangar.constants import Features as Features, Groups as Groups, LogActions as LogActions
from uilogging.helpers import getClientSessionID as getClientSessionID
from wotdecorators import noexcept as noexcept
from uilogging.types import GroupType as GroupType, PartnerIdType as PartnerIdType
_logger: Any

class _BaseHangarMetricsLogger(Logger):
    __slots__: tuple
    def __init__(self, group):
        ...
    # decorador original: @noexcept
    def log(self, data, partnerID=None, sessionID=''):
        ...

class _HangarSpaceMetricsLogger(_BaseHangarMetricsLogger):
    __slots__: tuple
    def __init__(self):
        ...
    def log(self, data, partnerID=None, sessionID=''):
        ...

class _HangarViewsMetricsLogger(_BaseHangarMetricsLogger):
    __slots__: tuple
    def __init__(self):
        ...
    def log(self, data, partnerID=None, sessionID=''):
        ...

class HangarMetricsLogger(object):
    __slots__: tuple
    _loggers: Any
    _defaultLogger: Any
    def __init__(self):
        ...
    def initialize(self):
        ...
    # decorador original: @noexcept
    def log(self):
        ...
