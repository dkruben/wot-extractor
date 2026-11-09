# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/customization/customization_cart/cart_seasons_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/customization/customization_cart/cart_seasons_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.customization.customization_cart.cart_season_model import CartSeasonModel

class CartSeasonsModel(ViewModel):
    __slots__ = ('onSelectItem', )

    def __init__(self, properties=4, commands=1):
        super(CartSeasonsModel, self).__init__(properties=properties, commands=commands)

    @property
    def winter(self):
        return self._getViewModel(0)

    @staticmethod
    def getWinterType():
        return CartSeasonModel

    @property
    def summer(self):
        return self._getViewModel(1)

    @staticmethod
    def getSummerType():
        return CartSeasonModel

    @property
    def desert(self):
        return self._getViewModel(2)

    @staticmethod
    def getDesertType():
        return CartSeasonModel

    @property
    def all(self):
        return self._getViewModel(3)

    @staticmethod
    def getAllType():
        return CartSeasonModel

    def _initialize(self):
        super(CartSeasonsModel, self)._initialize()
        self._addViewModelProperty('winter', CartSeasonModel())
        self._addViewModelProperty('summer', CartSeasonModel())
        self._addViewModelProperty('desert', CartSeasonModel())
        self._addViewModelProperty('all', CartSeasonModel())
        self.onSelectItem = self._addCommand('onSelectItem')
