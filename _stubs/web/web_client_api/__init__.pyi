# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import inspect as inspect
import logging as logging
import typing as typing
import weakref as weakref
from functools import partial as partial
from future.utils import iteritems as iteritems, itervalues as itervalues
from itertools import chain as chain
from past.builtins import basestring as basestring
from types import FunctionType as FunctionType
from Event import Event as Event
from helpers import uniprof as uniprof
from py2to3.backport.inspect import getargspec as getargspec
from py2to3.patched_future import with_metaclass as with_metaclass
from soft_exception import SoftException as SoftException
from typing import Callable as Callable, Dict as Dict, Iterable as Iterable, NamedTuple as NamedTuple, Optional as Optional, Type as Type, Union as Union
_logger: Any
_TypeType: Any

class CommandHandler(object):
    __hash__: Any
    name: Any
    schema: Any
    handler: Any
    finiHandler: Any
    def __init__(self, name=None, schema=None, handler=None, finiHandler=None):
        ...
    def __eq__(self, other):
        ...
    def __ne__(self, other):
        ...

class SubCommand(object):
    __slots__: tuple
    handler: Any
    subSchema: Any
    def __init__(self, subSchema=None, handler=None):
        ...
    def hasHandler(self):
        ...
    def hasSubSchema(self):
        ...

class ISchemeMeta(type):
    def validate(cls, data):
        ...
    def setDefault(cls, data):
        ...
    def toObject(cls, data):
        ...

# base nao representavel no stub: with_metaclass(...)
class Schema:
    @classmethod
    def instantiate(cls, data):
        ...

class Field(object):
    __slots__: tuple
    required: Any
    type: Any
    default: Any
    deprecated: Any
    validator: Any
    def __init__(self, required=False, type=None, default=None, deprecated=None, validator=None):
        ...
    def hasType(self):
        ...
    def hasValidator(self):
        ...

class W2CSchemaMeta(ISchemeMeta):
    def __init__(cls, *args, **kwargs):
        ...
    def validate(cls, data):
        ...
    def setDefault(cls, data):
        ...
    def toObject(cls, data):
        ...
    @staticmethod
    def __validateField(schema, key, data, required):
        ...

class Schema2Command(object):
    __data: Any
    __methods: Any
    def __init__(self, data, methods=None):
        ...
    def clear(self):
        ...
    def __getattr__(self, name):
        ...

# base nao representavel no stub: with_metaclass(...)
class W2CSchema:
    __unions__ = None

class WebCommandSchema(W2CSchema):
    command: Any
    params: Any
    web_id: Any

class _OverriddenMeta(W2CSchemaMeta):
    def __new__(cls, name, bases, attrs):
        ...

class _W2CApi(object):
    __name: Any
    __key: Any
    __finiHandlerName: Any
    def __init__(self, name, key, finiHandlerName=None):
        ...
    def __call__(self, clazz):
        ...

class _CallbackDispatcher(object):
    gen: Any
    handler: Any
    def __init__(self, generator, handler):
        ...
    def call(self, callers):
        ...
    def callback(self, arg):
        ...

class WebCommandException(SoftException):
    ...

class WebCommandHandler(object):
    __handlers: Any
    __browserID: Any
    __alias: Any
    __browserView: Any
    onCallback: Any
    def __init__(self, browserID, alias, browserView):
        ...
    def fini(self):
        ...
    def handleCommand(self, data):
        ...
    def addHandlers(self, handlers):
        ...
    def addHandler(self, handler):
        ...
    def removeHandler(self, handler):
        ...
    def handleWebCommand(self, webCommand):
        ...
    def __createCtx(self, commandName, webId):
        ...

def instantiateCommand(schema, data):
    ...
def createCommandHandler(commandName, commandSchema, handlerFunc, finiHandlerFunc=None):
    ...
def createSubCommandsHandler(commandName, commandSchema, keyField, subCommands, finiHandlerFunc=None):
    ...
def w2capi(name=None, key=None, finiHandlerName=None):
    ...
def _makeOverriddenSchema(key):
    ...
def w2c(schema, name='', finiHandlerName=None):
    ...
def webApiCollection(*apiProviders):
    ...
