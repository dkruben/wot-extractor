# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/product_price_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/product_price_model.py
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel

class ProductPriceModel(PriceItemModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(ProductPriceModel, self).__init__(properties=properties, commands=commands)

    def getDiscountValue(self):
        return self._getNumber(3)

    def setDiscountValue(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(ProductPriceModel, self)._initialize()
        self._addNumberProperty('discountValue', 0)
