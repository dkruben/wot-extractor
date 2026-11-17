# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/shop/loggers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
from typing import TYPE_CHECKING as TYPE_CHECKING, Set as Set
from helpers.base64_utils import base64UrlDecode as base64UrlDecode
from uilogging.base.logger import MetricsLogger as MetricsLogger
from uilogging.shop.base_loggers import ShopPreviewFlowLogger as ShopPreviewFlowLogger, ShopPreviewMetricsLogger as ShopPreviewMetricsLogger
from uilogging.shop.logging_constants import FEATURE as FEATURE, ShopLogActions as ShopLogActions, ShopLogKeys as ShopLogKeys, ShopLogButtons as ShopLogButtons, ShopLogItemStates as ShopLogItemStates, ShopCloseItemStates as ShopCloseItemStates
from wotdecorators import noexcept as noexcept
from uilogging.types import ItemType as ItemType, ItemStateType as ItemStateType, InfoType as InfoType
_logger: Any

class ShopMetricsLogger(MetricsLogger):
    __slots__: tuple
    _item: Any
    def __init__(self, item):
        ...
    # decorador original: @noexcept
    def onViewClosed(self):
        ...

class ShopBuyVehicleMetricsLogger(MetricsLogger):
    __slots__: tuple
    _itemStates: Any
    _uniqueItemCode: Any
    def __init__(self, uniqueItemCode):
        ...
    def reset(self):
        ...
    def clearItemStates(self):
        ...
    # decorador original: @noexcept
    def onViewOpen(self):
        ...
    # decorador original: @noexcept
    def onViewClosed(self):
        ...
    # decorador original: @noexcept
    def logVehiclePurchaseButtonClicked(self):
        ...
    def addItemState(self, itemState):
        ...

class ShopVehiclePreviewFlowLogger(ShopPreviewFlowLogger):
    __slots__: tuple
    # decorador original: @noexcept
    def logOpenPreview(self):
        ...

class ShopBundleVehiclePreviewFlowLogger(ShopPreviewFlowLogger):
    __slots__: tuple
    # decorador original: @noexcept
    def logOpenPreview(self):
        ...

class ShopVehicleStylePreviewFlowLogger(ShopPreviewFlowLogger):
    __slots__: tuple
    # decorador original: @noexcept
    def logOpenPreview(self):
        ...

class ShopVehiclePreviewMetricsLogger(ShopPreviewMetricsLogger):
    __slots__: tuple
    _uniqueItemCode: Any
    def __init__(self, uniqueItemCode):
        ...
    # decorador original: @noexcept
    def onViewOpen(self):
        ...
    # decorador original: @noexcept
    def onViewClosed(self, closeItemState):
        ...

class ShopBundleVehiclePreviewMetricsLogger(ShopPreviewMetricsLogger):
    __slots__: tuple
    _uniqueItemCode: Any
    def __init__(self, uniqueItemCode):
        ...
    # decorador original: @noexcept
    def onViewOpen(self):
        ...
    # decorador original: @noexcept
    def onViewClosed(self, closeItemState):
        ...
    # decorador original: @noexcept
    def logOpenPurchaseConfirmation(self):
        ...
    # decorador original: @noexcept
    def logBundlePurchased(self):
        ...
    # decorador original: @noexcept
    def logPurchaseConfirmationClosed(self):
        ...

class ShopVehicleStylePreviewMetricsLogger(ShopPreviewMetricsLogger):
    __slots__: tuple
    _uniqueItemCode: Any
    def __init__(self, uniqueItemCode):
        ...
    # decorador original: @noexcept
    def onViewOpen(self):
        ...
    # decorador original: @noexcept
    def onViewClosed(self):
        ...

def getPreviewUILoggers(isBundlePack, vehicleCD, buyParams):
    ...
# decorador original: @noexcept
def getProductCodeForPreviewLog(buyParams):
    ...
