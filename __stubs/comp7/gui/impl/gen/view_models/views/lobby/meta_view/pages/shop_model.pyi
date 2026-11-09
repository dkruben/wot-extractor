# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/meta_view/pages/shop_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum
from comp7.gui.impl.gen.view_models.views.lobby.enums import Rank as Rank
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.base_product_model import BaseProductModel as BaseProductModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.rank_discount_model import RankDiscountModel as RankDiscountModel

class ShopState(IntEnum):
    INITIAL = 0
    SUCCESS = 1
    ERROR = 2

class ShopModel(ViewModel):
    __slots__: tuple
    onProductSeen: Any
    onProductSelect: Any
    onProductPurchase: Any
    onProductRestore: Any
    onGoToHangar: Any
    onGoToPreview: Any
    onGoToCustomization: Any
    onAddToVehicleCompare: Any
    onMouseOver3dScene: Any
    onMoveSpace: Any
    def __init__(self, properties=8, commands=10):
        ...
    def getShopState(self):
        ...
    def setShopState(self, value):
        ...
    def getIsVehiclesCompareEnabled(self):
        ...
    def setIsVehiclesCompareEnabled(self, value):
        ...
    def getVehicleCompareTooltipId(self):
        ...
    def setVehicleCompareTooltipId(self, value):
        ...
    def getSelectedProductId(self):
        ...
    def setSelectedProductId(self, value):
        ...
    def getCurrentRank(self):
        ...
    def setCurrentRank(self, value):
        ...
    def getMaxAchievedRank(self):
        ...
    def setMaxAchievedRank(self, value):
        ...
    def getRankDiscounts(self):
        ...
    def setRankDiscounts(self, value):
        ...
    @staticmethod
    def getRankDiscountsType():
        ...
    def getProducts(self):
        ...
    def setProducts(self, value):
        ...
    @staticmethod
    def getProductsType():
        ...
    def _initialize(self):
        ...
