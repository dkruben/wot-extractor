# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/performance/critical/loggers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from uilogging.base.logger import _BaseLogger as Logger
from uilogging.constants import DEFAULT_LOGGER_NAME as DEFAULT_LOGGER_NAME
from uilogging.performance.critical.constants import Features as Features, Groups as Groups, LogActions as LogActions
from uilogging.helpers import getClientSessionID as getClientSessionID
from wotdecorators import noexcept as noexcept
_logger: Any

class MemoryCriticalLogger(Logger):
    __slots__: tuple
    def __init__(self):
        ...
    def initialize(self):
        ...
    # decorador original: @noexcept
    def log(self, sessionStartedAt=0):
        ...
