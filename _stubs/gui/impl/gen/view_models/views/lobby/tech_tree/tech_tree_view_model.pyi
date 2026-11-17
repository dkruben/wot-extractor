# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tech_tree/tech_tree_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, Map as Map, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel as RouterModel

class NationEnum(Enum):
    CHINA = 'china'
    CZECHOSLOVAKIA = 'czech'
    FRANCE = 'france'
    GERMANY = 'germany'
    ITALY = 'italy'
    JAPAN = 'japan'
    POLAND = 'poland'
    SWEDEN = 'sweden'
    UK = 'uk'
    USA = 'usa'
    USSR = 'ussr'

class TechTreeViewModel(ViewModel):
    __slots__: tuple
    onOpenAboutVehicle: Any
    onAddToCompare: Any
    onOpenCollectableVehicles: Any
    onOpenPremiumShop: Any
    def __init__(self, properties=8, commands=4):
        ...
    @property
    def router(self):
        ...
    @staticmethod
    def getRouterType():
        ...
    def getFirstHighlightedLevel(self):
        ...
    def setFirstHighlightedLevel(self, value):
        ...
    def getShowWelcomeAnimation(self):
        ...
    def setShowWelcomeAnimation(self, value):
        ...
    def getCollectableVehiclesAvailable(self):
        ...
    def setCollectableVehiclesAvailable(self, value):
        ...
    def getSelectedNation(self):
        ...
    def setSelectedNation(self, value):
        ...
    def getAvailableNations(self):
        ...
    def setAvailableNations(self, value):
        ...
    @staticmethod
    def getAvailableNationsType():
        ...
    def getTechTreeNodes(self):
        ...
    def setTechTreeNodes(self, value):
        ...
    @staticmethod
    def getTechTreeNodesType():
        ...
    def getNodeOverrides(self):
        ...
    def setNodeOverrides(self, value):
        ...
    @staticmethod
    def getNodeOverridesType():
        ...
    def _initialize(self):
        ...
