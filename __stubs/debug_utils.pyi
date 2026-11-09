# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/debug_utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import sys as sys
import re as re
import inspect as inspect
import subprocess as subprocess
import BigWorld as BigWorld
import excepthook as excepthook
import time as time
import traceback as traceback
from GarbageCollectionDebug import gcDump as gcDump
from functools import wraps as wraps
from collections import defaultdict as defaultdict
from future.utils import listitems as listitems, lzip as lzip, viewitems as viewitems
from past.builtins import xrange as xrange, unicode as unicode
from warnings import warn_explicit as warn_explicit
from constants import IS_CLIENT as IS_CLIENT, IS_CELLAPP as IS_CELLAPP, IS_BASEAPP as IS_BASEAPP, CURRENT_REALM as CURRENT_REALM, IS_DEVELOPMENT as IS_DEVELOPMENT, IS_BOT as IS_BOT
from constants import LEAKS_DETECTOR_MAX_EXECUTION_TIME as LEAKS_DETECTOR_MAX_EXECUTION_TIME
from contextlib import contextmanager as contextmanager
from threading import RLock as RLock
_src_file_trim_to: Any
_g_logMapping: dict
_g_logLock: Any
GCDUMP_CROWBAR_SWITCH = False
_logLevel = LOG_LEVEL.SVR_RELEASE
LOG_EXPECTED_EXCEPTION = LOG_CURRENT_EXCEPTION
_PLAIN_LEVEL_CATEGORIES: Any

class LOG_LEVEL:
    DEV = 1
    ST = 2
    CT = 3
    SVR_RELEASE = 4
    RELEASE = 5

class _LogWrapper(object):
    __lvl: Any
    def __init__(self, logLevel):
        ...
    def __call__(self, func):
        ...

class CriticalError(BaseException):
    ...

class HandledError(BaseException):
    ...

class SentryError(BaseException):
    ...

# decorador original: @contextmanager
def suppress(*exceptions):
    ...
def init():
    ...
# decorador original: @_LogWrapper(...)
def CRITICAL_ERROR(msg, *kargs):
    ...
# decorador original: @_LogWrapper(...)
def LOG_CURRENT_EXCEPTION(tags=...):
    ...
# decorador original: @_LogWrapper(...)
def LOG_SENTRY(msg, *kargs):
    ...
# decorador original: @_LogWrapper(...)
def LOG_WRAPPED_CURRENT_EXCEPTION(wrapperName, orgName, orgSource, orgLineno):
    ...
# decorador original: @_LogWrapper(...)
def LOG_CODEPOINT_WARNING(*kargs):
    ...
# decorador original: @_LogWrapper(...)
def LOG_ERROR(msg, *kargs, **kwargs):
    ...
# decorador original: @_LogWrapper(...)
def LOG_ERROR_DEV(msg, *kargs, **kwargs):
    ...
# decorador original: @_LogWrapper(...)
def LOG_WARNING(msg, *kargs, **kwargs):
    ...
def LOG_OBSOLETE(msg, *kargs):
    ...
# decorador original: @_LogWrapper(...)
def LOG_NOTE(msg, *kargs, **kwargs):
    ...
# decorador original: @_LogWrapper(...)
def LOG_DEBUG(msg, *kargs, **kwargs):
    ...
# decorador original: @_LogWrapper(...)
def LOG_DEBUG_DEV(msg, *kargs, **kwargs):
    ...
# decorador original: @_LogWrapper(...)
def LOG_DEBUG_DEV_NICE(msg, *kargs, **kwargs):
    ...
# decorador original: @_LogWrapper(...)
def LOG_UNEXPECTED(msg, *kargs):
    ...
# decorador original: @_LogWrapper(...)
def LOG_WRONG_CLIENT(entity, *kargs):
    ...
def _doLog(category, msg, args=None, kwargs=None, frameDepth=2):
    ...
def _makeMsgHeader(frame):
    ...
def _doLogFmt(prefix, fmt, *args):
    ...
def _addTagsToMsg(tags, msg):
    ...
def makeFuncLocationString(func):
    ...
def trace(func):
    ...
def deprecated(func):
    ...
def disabled(func):
    ...
def disabled_if(checker, msg=''):
    ...
def dump_garbage(source=False):
    ...
def dump_garbage_2(verbose=True, generation=2):
    ...
def memoryLeaksSafeDump(id, _):
    ...
def printConnections(ports):
    ...
def printProcesses():
    ...
def initMemoryLeaksLogging(repeatOffset=300):
    ...
def verify(expression):
    ...
def traceCalls(func):
    ...
def wg_extract_stack(f=None, limit=None):
    ...
def traceMethodCalls(obj, *names):
    ...
def makeVehicleLogTag(vehicle):
    ...
