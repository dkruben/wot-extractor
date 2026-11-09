# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/threads.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import time as time
import weakref as weakref
import threading as threading
from future.moves.queue import PriorityQueue as PriorityQueue, Empty as QueueEmptyError
from past.builtins import xrange as xrange
_logger: Any
INFINITE_QUEUE_SIZE = 0
_LOW_PRIORITY = 10
_DEFAULT_PRIORITY = 1

class Job(object):
    def doWork(self, worker):
        ...

class TerminateJob(Job):
    def doWork(self, worker):
        ...

class Worker(threading.Thread):
    __queueRef: Any
    _terminated: Any
    def __init__(self, jobsQueue, name=None):
        ...
    def __del__(self):
        ...
    def terminate(self):
        ...
    def run(self):
        ...
    def __repr__(self):
        ...

class ThreadPool(object):
    _jobs: Any
    _running: Any
    _workers: Any
    _workersLimit: Any
    def __init__(self, workersLimit, queueLimit=-1):
        ...
    @property
    def isRunning(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def _createNewWorker(self):
        ...
    def putLowPriorityJob(self, job):
        ...
    def putJob(self, job):
        ...
    def __repr__(self):
        ...
