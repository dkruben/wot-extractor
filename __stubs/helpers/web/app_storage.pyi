# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/web/app_storage.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import os as os
import shutil as shutil
import logging as logging
from functools import partial as partial
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
from helpers import threads as threads
from helpers.web.storage import IStorage as IStorage
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from soft_exception import SoftException as SoftException
from external_strings_utils import unicode_from_utf8 as unicode_from_utf8
_logger: Any
_CACHE_WARNING_GAP_IN_MB = 750

class _WriteFileJob(threads.Job):
    __filename: Any
    __data: Any
    __callback: Any
    def __init__(self, filename, data, callback):
        ...
    def doWork(self, worker):
        ...

class AsynchFileStorage(IStorage):
    __name: Any
    __worker: Any
    def __init__(self, name, worker):
        ...
    def close(self):
        ...
    def add(self, name, data, callback):
        ...
    def remove(self, name):
        ...
    def isStored(self, name):
        ...
    def getAll(self):
        ...
    def setWorker(self, worker):
        ...
    def __write(self, filename, data, callback):
        ...

class ApplicationStorage(object):
    _prefsDirPath: Any
    __cacheDir: Any
    __worker: Any
    __db: Any
    def __init__(self, name, workersLimit, queueLimit=...):
        ...
    @property
    def stopped(self):
        ...
    def close(self):
        ...
    def stopWorker(self):
        ...
    def restartWorker(self, workersLimit, queueLimit=...):
        ...
    @property
    def rootDirPath(self):
        ...
    def load(self):
        ...
    def getApp(self, appName):
        ...
    def addApp(self, appName):
        ...
    def removeApp(self, appName):
        ...
    def getApps(self):
        ...
    def addAppFile(self, appName, key, data, callback):
        ...
    def removeAppFile(self, appName, filename):
        ...
    def getAppFiles(self, appName):
        ...
    def isAppFileExist(self, appName, filename):
        ...
    def isFileExist(self, filename):
        ...

def _expectDir(path):
    ...
