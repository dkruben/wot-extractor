# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/page/header/navigation_bar_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.page.header.navigation_bar_info_button import NavigationBarInfoButton as NavigationBarInfoButton

class NavigationBarModel(ViewModel):
    __slots__: tuple
    BACK_NAVIGATION = 'back'
    GARAGE_NAVIGATION = 'garage'
    onNavigate: Any
    onInfoAction: Any
    def __init__(self, properties=4, commands=2):
        ...
    def getPageTitle(self):
        ...
    def setPageTitle(self, value):
        ...
    def getBackNavigationDescription(self):
        ...
    def setBackNavigationDescription(self, value):
        ...
    def getBackNavigationAllowed(self):
        ...
    def setBackNavigationAllowed(self, value):
        ...
    def getInfoButtons(self):
        ...
    def setInfoButtons(self, value):
        ...
    @staticmethod
    def getInfoButtonsType():
        ...
    def _initialize(self):
        ...
