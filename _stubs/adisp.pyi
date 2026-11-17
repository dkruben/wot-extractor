# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/adisp.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import os as os
import types as types
from functools import partial as partial, wraps as wraps
from debug_utils import LOG_WRAPPED_CURRENT_EXCEPTION as LOG_WRAPPED_CURRENT_EXCEPTION, LOG_ERROR as LOG_ERROR
from soft_exception import SoftException as SoftException
CLEAR_TRACE = True

class CallbackDispatcher(object):
    g: Any
    stepCallback: Any
    call_count: Any
    results: Any
    def __init__(self, generator, stepCallback):
        ...
    def call(self, callers):
        ...
    def callback(self, index, single, arg):
        ...

class AdispException(SoftException):
    ...

def doCall(func, processor):
    ...
def adisp_process(func, stepCallback=...):
    ...
def adisp_async(func, cbname='callback', cbwrapper=...):
    ...
def isAsync(func):
    ...
