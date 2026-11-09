# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/uilogging/shop/base_loggers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/shop/base_loggers.py
from __future__ import absolute_import
import logging
from uilogging.base.logger import FlowLogger, MetricsLogger
from uilogging.shop.logging_constants import FEATURE
_logger = logging.getLogger(__name__)

class ShopPreviewFlowLogger(FlowLogger):
    __slots__ = ()

    def __init__(self):
        super(ShopPreviewFlowLogger, self).__init__(FEATURE)

    def logOpenPreview(self):
        raise NotImplementedError


class ShopPreviewMetricsLogger(MetricsLogger):
    __slots__ = ()

    def __init__(self):
        super(ShopPreviewMetricsLogger, self).__init__(FEATURE)

    def onViewOpen(self, *args, **kwargs):
        raise NotImplementedError

    def onViewClosed(self, *args, **kwargs):
        raise NotImplementedError

    def logOpenPurchaseConfirmation(self):
        _logger.warning('[SHOPUILOG] %s not implemented logOpenPurchaseConfirmation.', self.__class__.__name__)

    def logBundlePurchased(self):
        _logger.warning('[SHOPUILOG] %s not implemented logBundlePurchased.', self.__class__.__name__)

    def logPurchaseConfirmationClosed(self):
        _logger.warning('[SHOPUILOG] %s not implemented logPurchaseConfirmationClosed.', self.__class__.__name__)
