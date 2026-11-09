# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/goodies/GoodieResources.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING, TypeVar as TypeVar
from goodies.GoodieValue import GoodieValue as GoodieValue
from typing import Generator as Generator
GoodieResourceType: Any

class GoodieResource(object):
    __slots__: tuple
    _value: Any
    def __init__(self, value):
        ...
    def __eq__(self, other):
        ...
    def __hash__(self):
        ...
    def __repr__(self):
        ...
    @property
    def value(self):
        ...
    @classmethod
    def provideCompatibleValueDescr(cls, actualVal, isPercent):
        ...
    def iterate(self):
        ...

class Gold(GoodieResource):
    def __init__(self, value):
        ...

class Credits(GoodieResource):
    def __init__(self, value):
        ...

class Experience(GoodieResource):
    def __init__(self, value):
        ...

class CrewExperience(GoodieResource):
    def __init__(self, value):
        ...

class FreeExperience(GoodieResource):
    def __init__(self, value):
        ...

class FrontlineExperience(GoodieResource):
    def __init__(self, value):
        ...
