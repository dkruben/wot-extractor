# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/ui_kit/list_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import Array as Array, ViewModel as ViewModel
T: Any

# base nao representavel no stub: typing.Generic[...]
class ListModel(ViewModel):
    __slots__: tuple
    onSelectionChanged: Any
    onItemClicked: Any
    def __init__(self, properties=2, commands=2):
        ...
    def getItems(self):
        ...
    def setItems(self, value):
        ...
    @staticmethod
    def getItemsType():
        ...
    def getSelectedIndices(self):
        ...
    def setSelectedIndices(self, value):
        ...
    @staticmethod
    def getSelectedIndicesType():
        ...
    def _initialize(self):
        ...
