# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/instructions/booster_buy_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/instructions/booster_buy_model.py
from gui.impl.gen.view_models.views.lobby.common.buy_sell_items_dialog_model import BuySellItemsDialogModel

class BoosterBuyModel(BuySellItemsDialogModel):
    __slots__ = ('onSetIsRearm', )

    def __init__(self, properties=27, commands=4):
        super(BoosterBuyModel, self).__init__(properties=properties, commands=commands)

    def getIsRearm(self):
        return self._getBool(24)

    def setIsRearm(self, value):
        self._setBool(24, value)

    def getIsDiscount(self):
        return self._getBool(25)

    def setIsDiscount(self, value):
        self._setBool(25, value)

    def getDiscountValue(self):
        return self._getNumber(26)

    def setDiscountValue(self, value):
        self._setNumber(26, value)

    def _initialize(self):
        super(BoosterBuyModel, self)._initialize()
        self._addBoolProperty('isRearm', False)
        self._addBoolProperty('isDiscount', False)
        self._addNumberProperty('discountValue', 0)
        self.onSetIsRearm = self._addCommand('onSetIsRearm')
