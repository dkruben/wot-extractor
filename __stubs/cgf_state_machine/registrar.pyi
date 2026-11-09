# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/cgf_state_machine/registrar.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import inspect as inspect
import logging as logging
import types as types
from .actions_base import ActionBase as ActionBase
from .transitions_base import TransitionBase as TransitionBase
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
__all__: list
_logger: Any

class StateActionsRegistrar(object):
    _domainActions: Any
    def __init__(self):
        ...
    def regActionsFromModule(self, module):
        ...
    def getActions(self):
        ...

class TransitionsRegistrar(object):
    _transitions: Any
    def __init__(self):
        ...
    def regTransitionsFromModule(self, module):
        ...
    def getTransitions(self):
        ...

def findClassesInModule(module, baseCls):
    ...
