# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/crew_helpers/sort_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import heapq as heapq
import math as math
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA, RequestCriteria as RequestCriteria

class SortRequestCriteria(RequestCriteria):
    __slots__: tuple
    MAX_MASK = 4294967295
    MAX_CONDITIONS_NUM: Any
    def __init__(self, other):
        ...
    def __call__(self, item):
        ...

class KeySortRequestCriteria(RequestCriteria):
    __slots__: tuple
    def __init__(self, other):
        ...
    def __call__(self, item):
        ...

class SortHeap(object):
    __slot__: tuple
    condition: Any
    key: Any
    data: Any
    def __init__(self, items=None, criteria=..., keys=...):
        ...
    def rebuild(self):
        ...
    def push(self, item):
        ...
    def pop(self):
        ...
    def remove(self, item):
        ...
    def updateRoot(self, item=None, criteria=..., keys=...):
        ...
    def getSortedList(self):
        ...
