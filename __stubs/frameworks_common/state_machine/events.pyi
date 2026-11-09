# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/frameworks_common/state_machine/events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing

class StateEvent(object):
    __slots__: tuple
    __arguments: Any
    def __init__(self, *args, **kwargs):
        ...
    def __repr__(self):
        ...
    def getArgument(self, name, default=None):
        ...

class StringEvent(StateEvent):
    __slots__: tuple
    __token: Any
    def __init__(self, token, **kwargs):
        ...
    def __repr__(self):
        ...
    @property
    def token(self):
        ...
