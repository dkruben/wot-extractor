# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/achievements/views/catalog/catalog_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.achievements.views.catalog.achievement_card_model import AchievementCardModel as AchievementCardModel
from gui.impl.gen.view_models.views.lobby.achievements.views.catalog.breadcrumb_model import BreadcrumbModel as BreadcrumbModel
from gui.impl.gen.view_models.views.lobby.achievements.views.catalog.details_model import DetailsModel as DetailsModel

class CatalogViewModel(ViewModel):
    __slots__: tuple
    onClose: Any
    onBreadcrumbClick: Any
    onCatalogClick: Any
    onCardClick: Any
    onStylePreview: Any
    onDogTagPreview: Any
    onPurchaseVehicleClick: Any
    onHintClose: Any
    onCardHover: Any
    def __init__(self, properties=6, commands=9):
        ...
    @property
    def details(self):
        ...
    @staticmethod
    def getDetailsType():
        ...
    def getBreadcrumbs(self):
        ...
    def setBreadcrumbs(self, value):
        ...
    @staticmethod
    def getBreadcrumbsType():
        ...
    def getAchievementScore(self):
        ...
    def setAchievementScore(self, value):
        ...
    def getMaxAchievementsScore(self):
        ...
    def setMaxAchievementsScore(self, value):
        ...
    def getIsNeededShowHint(self):
        ...
    def setIsNeededShowHint(self, value):
        ...
    def getAchievementsList(self):
        ...
    def setAchievementsList(self, value):
        ...
    @staticmethod
    def getAchievementsListType():
        ...
    def _initialize(self):
        ...
