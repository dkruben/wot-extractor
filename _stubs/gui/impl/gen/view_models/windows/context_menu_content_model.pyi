# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/windows/context_menu_content_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel as ListModel

class ContextMenuContentModel(ViewModel):
    __slots__: tuple
    onItemClicked: Any
    def __init__(self, properties=3, commands=1):
        ...
    @property
    def contextMenuList(self):
        ...
    @staticmethod
    def getContextMenuListType():
        ...
    def getItemsCount(self):
        ...
    def setItemsCount(self, value):
        ...
    def getSeparatorsCount(self):
        ...
    def setSeparatorsCount(self, value):
        ...
    def _initialize(self):
        ...
