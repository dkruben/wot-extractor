# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/skeletons/gui/platform/product_fetch_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/platform/product_fetch_controller.py
from __future__ import absolute_import
import typing
from skeletons.gui.platform.controller import IPlatformRequestController
if typing.TYPE_CHECKING:
    from gui.platform.products_fetcher.fetch_result import FetchResult

class IProductFetchController(IPlatformRequestController):

    def reset(self):
        raise NotImplementedError

    def getProducts(self, showWaiting=True, **kwargs):
        raise NotImplementedError


class ISubscriptionProductsFetchController(IProductFetchController):
    pass


class IUserSubscriptionsFetchController(IPlatformRequestController):
    pass


class IWotShopFetchController(IProductFetchController):

    def getProducts(self, showWaiting=True, **kwargs):
        raise NotImplementedError
