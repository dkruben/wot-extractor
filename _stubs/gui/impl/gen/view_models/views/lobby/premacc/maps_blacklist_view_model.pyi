# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/premacc/maps_blacklist_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel as ListModel

class MapsBlacklistViewModel(ViewModel):
    __slots__: tuple
    onBackAction: Any
    onCloseEvent: Any
    onMapAddToBlacklistEvent: Any
    onMapRemoveFromBlacklistEvent: Any
    onFilterReset: Any
    onInitialized: Any
    onFilterClick: Any
    onShopOpenWotPlus: Any
    onShopOpenPremium: Any
    def __init__(self, properties=7, commands=9):
        ...
    @property
    def disabledMaps(self):
        ...
    @staticmethod
    def getDisabledMapsType():
        ...
    @property
    def mapsFilters(self):
        ...
    @staticmethod
    def getMapsFiltersType():
        ...
    @property
    def maps(self):
        ...
    @staticmethod
    def getMapsType():
        ...
    def getCooldownTime(self):
        ...
    def setCooldownTime(self, value):
        ...
    def getMapsSelected(self):
        ...
    def setMapsSelected(self, value):
        ...
    def getMapsTotal(self):
        ...
    def setMapsTotal(self, value):
        ...
    def getIsFilterApplied(self):
        ...
    def setIsFilterApplied(self, value):
        ...
    def _initialize(self):
        ...
