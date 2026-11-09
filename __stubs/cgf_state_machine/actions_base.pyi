# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/cgf_state_machine/actions_base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import abc as abc
import logging as logging
import CGF as CGF
from py2to3.patched_future import with_metaclass as with_metaclass

# base nao representavel no stub: with_metaclass(...)
class ActionBase:
    _DEV_ONLY = False
    _logger: Any
    @classmethod
    def isDevOnly(cls):
        ...
    @classmethod
    def actionTypeName(cls):
        ...
    @classmethod
    def actionDisplayName(cls):
        ...
    @abc.abstractmethod
    def execute(self, gameObject):
        ...
