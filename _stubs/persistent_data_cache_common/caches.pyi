# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/persistent_data_cache_common/caches.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import os as os
import enum as enum
import typing as typing
from persistent_data_cache_common import cached_data as cached_data
from persistent_data_cache_common.common import getLogger as getLogger, MeasureExecutionTime as MeasureExecutionTime, DEFAULT_SAVING_TIMEOUT as DEFAULT_SAVING_TIMEOUT
from soft_exception import SoftException as SoftException
from wg_async import wg_async as wg_async, wg_await as wg_await, forwardAsFuture as forwardAsFuture, AsyncReturn as AsyncReturn, TimeoutError as TimeoutError, BrokenPromiseError as BrokenPromiseError
from persistent_data_cache_common.types import TData as TData, TPDCVersion as TPDCVersion
from persistent_data_cache_common.configs import BasePDCConfig as BasePDCConfig
from persistent_data_cache_common.data_providers import PDProvider as PDProvider
from persistent_data_cache_common.events import DefaultPDCEventsDispatcher as DefaultPDCEventsDispatcher

class _SavingPDCStates(enum.IntEnum):
    NOT_STARTED = 1
    IN_PROGRESS = 2
    CANCELED = 3

class SavingCacheCanceledException(SoftException):
    ...

class SavingCacheFailedException(SoftException):
    ...

class BasePDCache(object):
    __slots__: tuple
    _logger: Any
    _config: Any
    _cachedData: Any
    _destroyed: Any
    _savingState: Any
    _events: Any
    def __init__(self, config, eventsDispatcher):
        ...
    def destroy(self):
        ...
    def unload(self):
        ...
    def load(self, dataProvider):
        ...
    # decorador original: @wg_async
    def save(self, dataProviders, timeout=...):
        ...
    # decorador original: @wg_async
    def _save(self, dataProviders):
        ...
    def _getCachedData(self):
        ...
    # decorador original: @MeasureExecutionTime(...)
    def _tryToLoadCachedData(self, filePath, version):
        ...
    def _tryToSerializeData(self, dataProvider):
        ...
    def _tryToSaveCachedData(self, filePath, cachedData):
        ...
    def _tryToDeleteCacheFile(self, filePath):
        ...
    def _loadCachedData(self, filePath):
        ...
    def _saveCachedData(self, filePath, cachedData):
        ...
    def _isFileExist(self, filePath):
        ...
    def _deleteFile(self, filePath):
        ...

class DefaultPDCache(BasePDCache):
    __slots__: tuple
    def _loadCachedData(self, filePath):
        ...
    def _saveCachedData(self, filePath, cachedData):
        ...
    def _isFileExist(self, filePath):
        ...
    def _deleteFile(self, filePath):
        ...
