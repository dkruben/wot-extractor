# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/dependency.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import inspect as inspect
import logging as logging
import typing as typing
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from past.builtins import basestring as basestring
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from py2to3.backport.inspect import getargspec as getargspec
from soft_exception import SoftException as SoftException
InterfaceType: Any
_logger: Any
_g_manager = None
_MAX_ORDER_NUMBER = 32767
_orderGen: Any

class replace_none_kwargs(object):
    __services: Any
    def __init__(self, **services):
        ...
    def __call__(self, func):
        ...

class DependencyError(SoftException):
    ...

class DependencyManager(object):
    __slots__: tuple
    __services: Any
    __replacedServices: Any
    def __init__(self):
        ...
    def getService(self, class_):
        ...
    def addInstance(self, class_, obj, finalizer=None):
        ...
    def replaceInstance(self, class_, obj, finalizer=None, force=True):
        ...
    def addRuntime(self, class_, creator, finalizer=None):
        ...
    def addConfig(self, config):
        ...
    def clear(self):
        ...
    def _validate(self, class_):
        ...

class _ServiceDescriptor(object):
    __slots__: tuple
    __class: Any
    def __init__(self, class_):
        ...
    def __set__(self, _, value):
        ...
    def __get__(self, inst, owner=None):
        ...

class _DependencyItem(object):
    __slots__: tuple
    _order: Any
    _service: Any
    _finalizer: Any
    def __init__(self, order=..., service=None, finalizer=None):
        ...
    def value(self):
        ...
    def order(self):
        ...
    def finalize(self):
        ...
    def clear(self):
        ...

class _RuntimeItem(_DependencyItem):
    __slots__: tuple
    __isCreatorInvoked: Any
    __creator: Any
    _service: Any
    _order: Any
    def __init__(self, creator, finalizer=None):
        ...
    def value(self):
        ...
    def clear(self):
        ...

def configure(config):
    ...
def isConfigured():
    ...
def replaceInstance(class_, obj, finalizer=None):
    ...
def clear():
    ...
def instance(class_):
    ...
def descriptor(class_):
    ...
