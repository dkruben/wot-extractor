# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/goodies/goodie_multiple_resources.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
import goodies.GoodieResources as res
from goodies.GoodieValue import GoodieValue as GoodieValue
from typing import Generator as Generator, TypeVar as TypeVar
GoodieResource: Any

class GoodieMultiValueDescr(GoodieValue):
    def increase(self, xList):
        ...
    def reduce(self, xList):
        ...
    def delta(self, xList):
        ...

class MultiValueResourceObject(object):
    __slots__: tuple
    __values: Any
    def __init__(self, values):
        ...
    def __hash__(self):
        ...
    def __eq__(self, number):
        ...
    def __sub__(self, other):
        ...
    def __lt__(self, other):
        ...
    @property
    def values(self):
        ...

class GoodieMultiResourceList(res.GoodieResource):
    __slots__: tuple
    _subResources: Any
    def __init__(self, values):
        ...
    @classmethod
    def provideCompatibleValueDescr(cls, actualVal, isPercent):
        ...
    @classmethod
    def _getSupportedResourceSubTypes(cls):
        ...
    def iterate(self):
        ...

class FreeXpCrewXpMultiResourceList(GoodieMultiResourceList):
    @classmethod
    def _getSupportedResourceSubTypes(cls):
        ...

class FreeXpMainXpMultiResourceList(GoodieMultiResourceList):
    @classmethod
    def _getSupportedResourceSubTypes(cls):
        ...
