# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/RemoteDataDownloader.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
import threading as threading
from builtins import map as map
from collections import namedtuple as namedtuple
from functools import partial as partial
from future.utils import viewvalues as viewvalues
from http import client as httplib
from debug_utils import LOG_DEBUG as LOG_DEBUG
from helpers import threads as threads, http as http, time_utils as time_utils, local_cache as local_cache
from py2to3.compat import base64compat as base64compat
_TIMEOUT = 10.0
g_remoteCache: Any

class LIFE_TIME(object):
    MIN = time_utils.QUARTER_HOUR
    MAX = time_utils.ONE_DAY
    @classmethod
    def isExpired(cls, expires):
        ...

class _HttpOpenPageJob(threads.Job):
    __page: Any
    __lastModified: Any
    __callback: Any
    def __init__(self, page, lastModified, callback):
        ...
    def doWork(self, worker):
        ...

class _HttpOpenUrlJob(threads.Job):
    __url: Any
    __lastModified: Any
    __callback: Any
    def __init__(self, url, lastModified, callback):
        ...
    def doWork(self, worker):
        ...

class _HttpConnectionWorker(threads.Worker):
    __host: Any
    __conn: Any
    def __init__(self, jobsQueue, host):
        ...
    def terminate(self):
        ...
    def closeConnection(self):
        ...
    def getConnection(self):
        ...

class _HttpHostDownloader(threads.ThreadPool):
    _host: Any
    def __init__(self, host, workersLimit):
        ...
    def _createNewWorker(self):
        ...

class _LocalCache(local_cache.ShelfLocalCache):
    # base nao representavel no stub: namedtuple(...)
    class _Record:
        def __repr__(self):
            ...
    def __init__(self):
        ...
    def get(self, tags):
        ...
    def has(self, tags):
        ...
    def put(self, tags, data, lastModified, expires):
        ...
    def update(self, tags, data, lastModified, expires):
        ...
    def _get(self, key):
        ...
    def _put(self, key, data, lastModified, expires):
        ...
    @classmethod
    def _makeKey(cls, tags):
        ...

class _RemoteDataDownloader(object):
    __storageCache: Any
    __lock: Any
    _pools: Any
    def __init__(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def getClanVehicleDecal(self, clanDbID, callback):
        ...
    def getClanEmblem32x32(self, clanDbID, callback):
        ...
    def getClanEmblem64x64(self, clanDbID, callback):
        ...
    def getUrlData(self, url, callback):
        ...
    def __getFromCache(self, poolName, page):
        ...
    def __getRemoteFileByConnection(self, poolName, page, callback):
        ...
    def __getRemoteFile(self, poolName, page, callback, jobType):
        ...
    def __onResponseReceived(self, poolName, page, callback, data, lastModified, expires):
        ...
    def __cache_onRead(self):
        ...
