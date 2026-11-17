# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/persistent_data_cache_common/common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import time as time
import logging as logging
from contextlib import contextmanager as contextmanager
LOGGER_NAME = 'PersistentDataCache'
DEFAULT_SAVING_TIMEOUT = 120.0
_logger: Any

class MeasureExecutionTime(object):
    __slots__: tuple
    _logger: Any
    _metricName: Any
    _totalTime: Any
    def __init__(self, metricName, logger=None):
        ...
    def printTotalTime(self, reset=True):
        ...
    # decorador original: @contextmanager
    def start(self, section=''):
        ...
    def _createMetricName(self, section=''):
        ...
    def __call__(self, func, section=''):
        ...

def getLogger(*names):
    ...
