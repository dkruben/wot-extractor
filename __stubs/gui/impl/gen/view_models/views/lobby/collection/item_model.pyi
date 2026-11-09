# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/collection/item_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class ItemState(Enum):
    NEW = 'new'
    RECEIVED = 'received'
    UNRECEIVED = 'unreceived'

class ItemModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=4, commands=0):
        ...
    def getItemId(self):
        ...
    def setItemId(self, value):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def getReceivedImagePath(self):
        ...
    def setReceivedImagePath(self, value):
        ...
    def getUnreceivedImagePath(self):
        ...
    def setUnreceivedImagePath(self, value):
        ...
    def _initialize(self):
        ...
