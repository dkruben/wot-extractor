# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/resources/local/base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import itertools as itertools
from gui.game_loading.resources.base import BaseResources as BaseResources
from gui.game_loading.resources.models import BaseResourceModel as BaseResourceModel

class LocalResources(BaseResources):
    __slots__: tuple
    _source: Any
    _cycle: Any
    _iterator: Any
    def __init__(self, source, cycle=False):
        ...
    def get(self):
        ...
    def reset(self):
        ...
    def destroy(self):
        ...
    def _createIterator(self):
        ...
