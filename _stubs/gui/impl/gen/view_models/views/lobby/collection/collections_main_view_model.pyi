# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/collection/collections_main_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.collection.collection_model import CollectionModel as CollectionModel

class CollectionsMainViewModel(ViewModel):
    __slots__: tuple
    onOpenCollection: Any
    onClose: Any
    setCompletionWasShown: Any
    onSetNewCollectionShown: Any
    def __init__(self, properties=2, commands=4):
        ...
    def getIsViewActive(self):
        ...
    def setIsViewActive(self, value):
        ...
    def getCollections(self):
        ...
    def setCollections(self, value):
        ...
    @staticmethod
    def getCollectionsType():
        ...
    def _initialize(self):
        ...
