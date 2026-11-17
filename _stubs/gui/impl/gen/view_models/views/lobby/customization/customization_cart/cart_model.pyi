# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/customization/customization_cart/cart_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.customization.customization_cart.cart_purchase_model import CartPurchaseModel as CartPurchaseModel
from gui.impl.gen.view_models.views.lobby.customization.customization_cart.cart_rent_model import CartRentModel as CartRentModel
from gui.impl.gen.view_models.views.lobby.customization.customization_cart.cart_seasons_model import CartSeasonsModel as CartSeasonsModel
from gui.impl.gen.view_models.views.lobby.customization.customization_cart.cart_style_model import CartStyleModel as CartStyleModel
from gui.impl.gen.view_models.views.lobby.customization.customization_cart.cart_tutorial_model import CartTutorialModel as CartTutorialModel

class CartModel(ViewModel):
    __slots__: tuple
    onCloseAction: Any
    def __init__(self, properties=7, commands=1):
        ...
    @property
    def seasons(self):
        ...
    @staticmethod
    def getSeasonsType():
        ...
    @property
    def style(self):
        ...
    @staticmethod
    def getStyleType():
        ...
    @property
    def purchase(self):
        ...
    @staticmethod
    def getPurchaseType():
        ...
    @property
    def rent(self):
        ...
    @staticmethod
    def getRentType():
        ...
    @property
    def tutorial(self):
        ...
    @staticmethod
    def getTutorialType():
        ...
    def getIsAnySelected(self):
        ...
    def setIsAnySelected(self, value):
        ...
    def getIsRendererPipelineDeferred(self):
        ...
    def setIsRendererPipelineDeferred(self, value):
        ...
    def _initialize(self):
        ...
