# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/cgf_state_machine/transitions_base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import abc as abc
import logging as logging
from py2to3.patched_future import with_metaclass as with_metaclass

# base nao representavel no stub: with_metaclass(...)
class TransitionBase:
    _DEV_ONLY = False
    _logger: Any
    @classmethod
    def isDevOnly(cls):
        ...
    @classmethod
    def transitionTypeName(cls):
        ...
    @classmethod
    def transitionDisplayName(cls):
        ...
    def activate(self, gameObject):
        ...
    def deactivate(self):
        ...
    @abc.abstractmethod
    def update(self):
        ...
