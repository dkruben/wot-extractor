# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_preview/top_panel/top_panel_tabs_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum
from frameworks.wulf import Array as Array, ViewModel as ViewModel

class TabID(IntEnum):
    NONE = 0
    VEHICLE = 1
    STYLE = 2
    BASE_VEHICLE = 3
    PERSONAL_NUMBER_VEHICLE = 4

class TopPanelTabsModel(ViewModel):
    __slots__: tuple
    onTabChanged: Any
    def __init__(self, properties=3, commands=1):
        ...
    def getTabIDs(self):
        ...
    def setTabIDs(self, value):
        ...
    @staticmethod
    def getTabIDsType():
        ...
    def getTabCustomNames(self):
        ...
    def setTabCustomNames(self, value):
        ...
    @staticmethod
    def getTabCustomNamesType():
        ...
    def getCurrentTabID(self):
        ...
    def setCurrentTabID(self, value):
        ...
    def _initialize(self):
        ...
