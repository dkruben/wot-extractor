# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/platform/products_fetcher/wot_shop/descriptors/product_descriptor.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/platform/products_fetcher/wot_shop/descriptors/product_descriptor.py
from gui.platform.products_fetcher.product_descriptor import ProductDescriptor as BaseDescriptor

class ProductDescriptor(BaseDescriptor):

    @property
    def productID(self):
        return self._getFromParams('id', '')

    @property
    def productCode(self):
        return self._getFromParams('code', '')

    @property
    def categories(self):
        return self._getFromParams('categories', [])

    @property
    def category(self):
        return self.categories[0]

    @property
    def purchasable(self):
        return self._getFromParams('purchasable', False)

    @property
    def price(self):
        return self._getFromParams('price', {})

    @property
    def currencyName(self):
        return self.price.get('currency')

    @property
    def originalPrice(self):
        return self.price.get('value')

    @property
    def promotion(self):
        return self._getFromParams('promotion', {})

    @property
    def discountPrice(self):
        if self.promotion:
            return self.promotion.get('discounted_cost', 0)
        return 0

    @property
    def entitlements(self):
        return self._getFromParams('entitlements', [])

    @property
    def description(self):
        return self._getFromParams('description', '')
