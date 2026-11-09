# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/platform/products_fetcher/wot_shop/descriptors/account_limits_descriptor.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/platform/products_fetcher/wot_shop/descriptors/account_limits_descriptor.py
from gui.platform.products_fetcher.product_descriptor import ProductDescriptor

class AccountLimitsDescriptor(ProductDescriptor):

    @property
    def limitedQuantity(self):
        return self._getFromParams('limited_quantity', {})

    @property
    def purchaseAllowed(self):
        return self.limitedQuantity['purchase_allowed']

    @property
    def personalCount(self):
        return self.limitedQuantity['personal_count']

    @property
    def personalLimit(self):
        return self.limitedQuantity['personal_limit']
