# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/wotdecorators.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import time as time
from functools import update_wrapper as update_wrapper, wraps as wraps
from typing import TypeVar as TypeVar, Type as Type, Generic as Generic, Callable as Callable, Any as Any
import time_tracking as time_tracking
from constants import IS_BASEAPP as IS_BASEAPP, IS_CELLAPP as IS_CELLAPP, IS_DEVELOPMENT as IS_DEVELOPMENT, SERVER_TICK_LENGTH as SERVER_TICK_LENGTH
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION, CRITICAL_ERROR as CRITICAL_ERROR, LOG_ERROR as LOG_ERROR
from py2to3.backport import inspect as inspect
from soft_exception import SoftException as SoftException
from time_tracking import LOG_TIME_WARNING as LOG_TIME_WARNING
CLASS: _Any
logger: _Any

def incrTickOverspends():
    ...
def _argsToLogID(args):
    ...
def _logErrorMessageFromArgs(prefix, args):
    ...
def noexcept(func):
    ...
def noexceptReturn(returnOnExcept):
    ...
def nofail(func):
    ...
def exposedtoclient(func):
    ...
def singleton(cls):
    ...
def decorate(func, dec):
    ...
def decorator(dec):
    ...
def condition(attributeName, logFunc=None, logStack=True):
    ...
def limitExposedToClientCalls(cooldown=..., periodLength=1.0, errorThreshold=1, storageAttr='__exposedCallsStorage__'):
    ...
