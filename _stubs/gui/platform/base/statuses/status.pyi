# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/base/statuses/status.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.platform.base.statuses.constants import StatusTypes as StatusTypes

class Status(object):
    __slots__: tuple
    _type: Any
    _data: Any
    def __init__(self, statusType=..., data=None):
        ...
    @property
    def data(self):
        ...
    @property
    def type(self):
        ...
    @property
    def isUndefined(self):
        ...
    def typeIs(self, statusType):
        ...
    def __eq__(self, other):
        ...
    def __str__(self):
        ...
    def __repr__(self):
        ...
