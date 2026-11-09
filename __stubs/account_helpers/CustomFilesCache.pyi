# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/CustomFilesCache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import os as os
import time as time
import binascii as binascii
import threading as threading
import random as random
import shelve as provider
from functools import partial as partial
from future.moves import queue as queue
from future.moves.urllib import request as request, response as response, error as error
from future.utils import listitems as listitems, viewitems as viewitems
from pickle import HIGHEST_PROTOCOL as HIGHEST_PICKLE_PROTOCOL, UnpicklingError as UnpicklingError
import BigWorld as BigWorld
from debug_utils import LOG_WARNING as LOG_WARNING, LOG_ERROR as LOG_ERROR, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION, LOG_DEBUG as LOG_DEBUG, LOG_DEBUG_DEV as LOG_DEBUG_DEV
from helpers import getFullClientVersion as getFullClientVersion
from shared_utils import safeCancelCallback as safeCancelCallback
from soft_exception import SoftException as SoftException
from helpers import isPlayerAccount as isPlayerAccount
from external_strings_utils import unicode_from_utf8 as unicode_from_utf8
from py2to3.compat import base64compat as base64compat
INFINITE_QUEUE_SIZE = 0
_MIN_LIFE_TIME = 900
_MAX_LIFE_TIME = 86400
_LIFE_TIME_IN_MEMORY = 1200
_CACHE_VERSION = 2
_CLIENT_VERSION = None
_DEFAULT_REQUEST_TIMEOUT = 10

class NotModifiedHandler(request.BaseHandler):
    def http_error_304(self, req, fp, code, message, headers):
        ...

class CFC_OP_TYPE(object):
    DOWNLOAD = 1
    READ = 2
    WRITE = 3
    CHECK = 4

class WorkerThread(threading.Thread):
    input_queue: Any
    __terminate: Any
    isBusy: Any
    def __init__(self, queueLimit=...):
        ...
    def add_task(self, task):
        ...
    def close(self):
        ...
    def run(self):
        ...
    def __run(self, callback, **_):
        ...

class ThreadPool(object):
    __workers: Any
    def __init__(self, workersLimit=8):
        ...
    def start(self):
        ...
    def close(self):
        ...
    def add_task(self, task):
        ...

class CustomFilesCache(object):
    __cacheDir: Any
    __mutex: Any
    __cache: Any
    __accessedCache: Any
    __processedCache: Any
    __written_cache: Any
    __db: Any
    __worker: Any
    __timer: Any
    def __init__(self, cacheFolder):
        ...
    def close(self):
        ...
    def __startTimer(self):
        ...
    def get(self, url, callback, showImmediately=False, headers=None):
        ...
    def __get(self, url, showImmediately, checkedInCache, headers=None):
        ...
    def __idle(self):
        ...
    def __readLocalFile(self, url, showImmediately):
        ...
    def __onReadLocalFile(self, url, showImmediately):
        ...
    def __checkFile(self, url, showImmediately, headers=None):
        ...
    def __onCheckFile(self, url, showImmediately, headers):
        ...
    def __readRemoteFile(self, url, modified_time, showImmediately, headers):
        ...
    def __onReadRemoteFile(self, url, showImmediately, modified_time, headers):
        ...
    def __prepareCache(self, recreate=False):
        ...
    def __writeCache(self, name, packet):
        ...
    def __onWriteCache(self, name, packet):
        ...
    def __postTask(self, url, remote_file, invokeAndReleaseCallbacks):
        ...
    def __onPostTask(self, url, invokeAndReleaseCallbacks, remote_file):
        ...

def _getClientVersion():
    ...
def _LOG_EXECUTING_TIME(startTime, methodName, deltaTime=0.1):
    ...
def parseHttpTime(t):
    ...
def makeHttpTime(dt):
    ...
def getSafeDstUTCTime():
    ...
