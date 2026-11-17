# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gui_decorators.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import inspect as inspect
import logging as logging
from frameworks.wulf import View as View, ViewStatus as ViewStatus
from helpers.uniprof import regions as regions
from py2to3.backport.inspect import getargspec as getargspec
_REGION_FORMAT = 'view.{}.{}'
_logger: Any

class ViewLifeCycleToRegions(object):
    __slots__: tuple
    __uniqueName: Any
    __viewStatus: Any
    def __init__(self, uniqueName):
        ...
    def __call__(self, clazz):
        ...
    def __enter(self):
        ...
    def __exit(self):
        ...
    def __trigger(self, newState):
        ...

def args2params(*types):
    ...
def trackLifeCycle(uniqueName):
    ...
