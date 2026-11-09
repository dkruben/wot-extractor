# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/resource_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import importlib as importlib
import inspect as inspect
from contextlib import contextmanager as contextmanager
from collections import namedtuple as namedtuple
from past.builtins import basestring as basestring
import ResMgr as ResMgr
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from soft_exception import SoftException as SoftException
ResourceItem: Any
_ITEM_VALUE_READERS: dict

class RESOURCE_ITEM_TYPE(object):
    BOOL = 'bool'
    INTEGER = 'int'
    FLOAT = 'float'
    STRING = 'string'
    URL = 'url'
    VECTOR2 = 'vector2'
    VECTOR3 = 'vector3'
    VECTOR4 = 'vector4'
    LIST = 'list'
    DICT = 'dict'
    SEQ_PAIRS = 'seq-pairs'
    CLASS = 'class'

class ResourceError(SoftException):
    ctx: Any
    errorMessage: Any
    def __init__(self, ctx, message):
        ...
    def __str__(self):
        ...

class ResourceCtx(object):
    __filePath: Any
    __xpath: Any
    def __init__(self, filePath, xpath=None):
        ...
    def next(self, section):
        ...
    def prev(self):
        ...
    def __str__(self):
        ...

def getRoot(filePath, msg='', safe=False):
    ...
def purgeResource(filePath):
    ...
# decorador original: @contextmanager
def root_generator(filePath):
    ...
def root_iterator(filePath, customReaders=None, nameFromSection=False):
    ...
def getSubSection(ctx, section, name, safe=False):
    ...
def getIterator(xmlCtx, section):
    ...
def readItemAttr(xmlCtx, section, attr, default=None, keys=None):
    ...
def readItemName(xmlCtx, section, keys=None, nameFromSection=False):
    ...
def _readItemType(xmlCtx, section, keys=None):
    ...
def readBoolItem(xmlCtx, section, nameFromSection=False):
    ...
def readIntItem(xmlCtx, section, nameFromSection=False):
    ...
def readFloatItem(xmlCtx, section, nameFromSection=False):
    ...
def readStringItem(xmlCtx, section, nameFromSection=False):
    ...
def readVector2Item(xmlCtx, section, nameFromSection=False):
    ...
def readVector3Item(xmlCtx, section, nameFromSection=False):
    ...
def readVector4Item(xmlCtx, section, nameFromSection=False):
    ...
def readList(xmlCtx, section, valueName='value', nameFromSection=False):
    ...
def readDict(xmlCtx, section, valueName='value', nameFromSection=False):
    ...
def readSeqPairs(xmlCtx, section, valueName='value', nameFromSection=False):
    ...
def readClassItem(xmlCtx, section, nameFromSection=False):
    ...
def readItem(ctx, section, name='item', nameFromSection=False):
    ...
