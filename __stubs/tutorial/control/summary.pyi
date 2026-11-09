# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/control/summary.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import listvalues as listvalues, viewvalues as viewvalues
from tutorial.control.functional import FunctionalVarSet as FunctionalVarSet
from tutorial.logger import LOG_ERROR as LOG_ERROR, LOG_DEBUG as LOG_DEBUG

class _Flag(object):
    name: Any
    active: Any
    store: Any
    def __init__(self, name, active, store=True):
        ...
    def __repr__(self):
        ...
    def isActive(self):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...

class FlagSummary(object):
    __flags: Any
    def __init__(self, flagNames, initial=None):
        ...
    def __repr__(self):
        ...
    def deactivateFlag(self, flagName):
        ...
    def activateFlag(self, flagName):
        ...
    def isActiveFlag(self, flagName):
        ...
    def addFlag(self, flagName):
        ...
    def getDict(self):
        ...

class VarSummary(object):
    __runtime: Any
    __varSets: Any
    def __init__(self, varSets, runtime=None):
        ...
    def get(self, varID, default=None):
        ...
    def set(self, varID, value):
        ...
