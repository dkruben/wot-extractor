# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/persistent_data_cache/caches.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from functools import partial as partial
import BigWorld as BigWorld
import wg_async as wg_async
from helpers.threads import ThreadPool as ThreadPool, Job as Job
from persistent_data_cache_common.caches import DefaultPDCache as DefaultPDCache
from persistent_data_cache_common.common import getLogger as getLogger, DEFAULT_SAVING_TIMEOUT as DEFAULT_SAVING_TIMEOUT
from persistent_data_cache_common import cached_data as cached_data
from persistent_data_cache_common.configs import BasePDCConfig as BasePDCConfig
from persistent_data_cache_common.data_providers import PDProvider as PDProvider
from persistent_data_cache_common.events import DefaultPDCEventsDispatcher as DefaultPDCEventsDispatcher
_logger: Any

class _ThreadJob(Job):
    _func: Any
    _callback: Any
    def __init__(self, func, callback):
        ...
    def doWork(self, worker):
        ...

class ThreadSavingPDCache(DefaultPDCache):
    __slots__: tuple
    _threadWorker: Any
    def __init__(self, config, eventsDispatcher):
        ...
    def destroy(self):
        ...
    # decorador original: @wg_async.wg_async
    def save(self, dataProviders, timeout=...):
        ...
    # decorador original: @wg_async.wg_async
    def _tryToDeleteCacheFile(self, filePath):
        ...
    # decorador original: @wg_async.wg_async
    def _tryToSerializeData(self, dataProvider):
        ...
    # decorador original: @wg_async.wg_async
    def _tryToSaveCachedData(self, filePath, cachedData):
        ...
    def _startJob(self, func, callback, errorResult=None):
        ...
