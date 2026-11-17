# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/shop/base_loggers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from uilogging.base.logger import FlowLogger as FlowLogger, MetricsLogger as MetricsLogger
from uilogging.shop.logging_constants import FEATURE as FEATURE
_logger: Any

class ShopPreviewFlowLogger(FlowLogger):
    __slots__: tuple
    def __init__(self):
        ...
    def logOpenPreview(self):
        ...

class ShopPreviewMetricsLogger(MetricsLogger):
    __slots__: tuple
    def __init__(self):
        ...
    def onViewOpen(self, *args, **kwargs):
        ...
    def onViewClosed(self, *args, **kwargs):
        ...
    def logOpenPurchaseConfirmation(self):
        ...
    def logBundlePurchased(self):
        ...
    def logPurchaseConfirmationClosed(self):
        ...
