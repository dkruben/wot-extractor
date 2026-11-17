# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/RedundantCache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import collections as collections
from itertools import chain as chain

class RedundantCache(object):
    __cache: Any
    __redundancy: Any
    __callback: Any
    __limit: Any
    def __init__(self, redundancy, callback=None, limit=None):
        ...
    def __repr__(self):
        ...
    def snapshot(self):
        ...
    def flush(self):
        ...
    def fini(self):
        ...
    def add(self, value):
        ...
    def clear(self):
        ...
