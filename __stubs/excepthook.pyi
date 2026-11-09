# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/excepthook.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import sys as sys
import linecache as linecache
from functools import wraps as wraps
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from traceback import format_exception_only as format_exception_only
import BigWorld as BigWorld
from constants import IS_BASEAPP as IS_BASEAPP
_MAX_OBJECT_SIZE = 16384
_MAX_DEPTH = 10
_SEQUENCE_TYPES: tuple
_LINE_LIMIT = 25
_ENABLE_EXTENDED_TRACEBACK = False

def getLocationFromCode(fileNameToTrim, code, lineno=None):
    ...
def formatLocation(filename, lineno, name):
    ...
def extendedTracebackAsString(fileNameToTrim, wrapperName, orgName, etype, value, tb):
    ...
def extendedTracebackAsList(fileNameToTrim, wrapperName, orgName, exctype, value, traceback):
    ...
def __processVar(k, v, localsProcessorCache):
    ...
def __checkObjectSize(d, meta):
    ...
def __processLocals(locals, localsProcessorCache):
    ...
def __excepthook(excepthook, fileNameToTrim):
    ...
def init(enableExtendedTraceBack, fileNameToTrim):
    ...
