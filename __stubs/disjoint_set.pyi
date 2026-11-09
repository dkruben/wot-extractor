# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/disjoint_set.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import typing as typing
from future.utils import viewvalues as viewvalues
from typing import Any as Any, Iterable as Iterable
_logger: _Any

class DisjointSet(object):
    _root: _Any
    _set: _Any
    def __init__(self):
        ...
    def __contains__(self, item):
        ...
    def __len__(self):
        ...
    @property
    def subsets(self):
        ...
    @property
    def nsubsets(self):
        ...
    @classmethod
    def fromIterables(cls, iterables):
        ...
    def add(self, element):
        ...
    def clear(self):
        ...
    def getRoot(self, element):
        ...
    def getSubset(self, element):
        ...
    def inSameSubset(self, elementA, elementB):
        ...
    def union(self, elementA, elementB):
        ...
