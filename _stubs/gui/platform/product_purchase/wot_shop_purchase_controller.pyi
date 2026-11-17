# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/product_purchase/wot_shop_purchase_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
from BWUtil import AsyncReturn as AsyncReturn
from adisp import adisp_process as adisp_process
from gui.wgcg.wot_shop.contexts import WotShopPurchaseStorefrontProductCtx as WotShopPurchaseStorefrontProductCtx
from helpers import dependency as dependency
from skeletons.gui.platform.product_purchase_controller import IWotShopPurchaseController as IWotShopPurchaseController, WotShopPrice as WotShopPrice
from skeletons.gui.web import IWebController as IWebController
from wg_async import wg_async as wg_async, await_callback as await_callback
_logger: Any

class WotShopPurchaseController(IWotShopPurchaseController):
    __webCtrl: Any
    # decorador original: @wg_async
    def purchaseProduct(self, storefront, productCode, expectedPrice):
        ...
    # decorador original: @adisp_process
    def __purchaseProduct(self, ctx, callback):
        ...
