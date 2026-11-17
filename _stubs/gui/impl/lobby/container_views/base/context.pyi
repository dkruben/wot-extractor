# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/container_views/base/context.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class ContextBase(object):
    itemsCache: Any
    def __init__(self, *args, **kwargs):
        ...
    def update(self, *args, **kwargs):
        ...

class TankmanContext(ContextBase):
    __slots__: tuple
    _tankmanID: Any
    _tankman: Any
    def __init__(self, tankmanID, *args, **kwargs):
        ...
    @property
    def tankmanID(self):
        ...
    @property
    def tankman(self):
        ...
    def update(self, tankmanID):
        ...
