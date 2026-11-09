# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgcg/wot_shop/contexts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.wgcg.base.contexts import CommonWebRequestCtx as CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType as WebRequestDataType

class WotShopGetStorefrontProductsCtx(CommonWebRequestCtx):
    __slots__: tuple
    __storefront: Any
    def __init__(self, ctx, waitingID=''):
        ...
    def getRequestType(self):
        ...
    def isClanSyncRequired(self):
        ...
    def isCaching(self):
        ...
    def getStorefront(self):
        ...

class WotShopPurchaseStorefrontProductCtx(CommonWebRequestCtx):
    __slots__: tuple
    __storefront: Any
    __productCode: Any
    __expectedPrice: Any
    def __init__(self, storefront, productCode, expectedPrice, waitingID=''):
        ...
    def getRequestType(self):
        ...
    def isClanSyncRequired(self):
        ...
    def isCaching(self):
        ...
    def getStorefront(self):
        ...
    def getProductCode(self):
        ...
    def getExpectedPrice(self):
        ...
