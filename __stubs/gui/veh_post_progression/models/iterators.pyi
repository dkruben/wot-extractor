# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/veh_post_progression/models/iterators.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import deque as deque
from gui.veh_post_progression.models.progression import PostProgressionItem as PostProgressionItem

class UnorederdStepsIterator(object):
    __slots__: tuple
    _postProgression: Any
    _tree: Any
    def __init__(self, postProgression):
        ...
    def __iter__(self):
        ...

class OrderedStepsIterator(UnorederdStepsIterator):
    __slots__: tuple
    __fifo: Any
    __visited: Any
    def __init__(self, postProgression):
        ...
    def __iter__(self):
        ...
    def next(self):
        ...
    def _getOrderedUnlocks(self, unlocks):
        ...
