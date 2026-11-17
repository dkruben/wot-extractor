# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/persistent_data_cache_common/manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import OrderedDict as OrderedDict
import typing as typing
from future.utils import itervalues as itervalues
import wg_async as wg_async
from persistent_data_cache_common.common import getLogger as getLogger, MeasureExecutionTime as MeasureExecutionTime, DEFAULT_SAVING_TIMEOUT as DEFAULT_SAVING_TIMEOUT
from persistent_data_cache_common.data_providers import PDProvider as PDProvider
from soft_exception import SoftException as SoftException
from persistent_data_cache_common.caches import BasePDCache as BasePDCache
from persistent_data_cache_common.types import TData as TData, TDataFactory as TDataFactory
from persistent_data_cache_common.serializers import ISerializer as ISerializer

class DefaultPDCManager(object):
    __slots__: tuple
    _logger: Any
    _cache: Any
    _started: Any
    _dataProviders: Any
    _dataCreateTiming: Any
    def __init__(self, cache):
        ...
    def fini(self):
        ...
    def load(self, name, factory, serializer):
        ...
    def start(self):
        ...
    # decorador original: @wg_async.wg_async
    def save(self, timeout=...):
        ...
    def _start(self):
        ...
    def _register(self, name, factory, serializer):
        ...
    def _loadData(self, dataProvider):
        ...

class ForceCreatingPDCManager(DefaultPDCManager):
    __slots__: tuple
    def _loadData(self, dataProvider):
        ...
