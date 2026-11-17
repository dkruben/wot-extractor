# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/game_control/comp7_shop_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems
from BWUtil import AsyncReturn as AsyncReturn
from enum import Enum as Enum
from shared_utils import findFirst as findFirst
import Event as Event
from comp7.gui.impl.gen.view_models.views.lobby.enums import Rank as Rank
from comp7.gui.impl.lobby.comp7_helpers import comp7_shared as comp7_shared
from comp7.skeletons.gui.game_control import IComp7ShopController as IComp7ShopController
from gui.SystemMessages import SM_TYPE as SM_TYPE, pushMessage as pushMessage
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.platform.products_fetcher.wot_shop.fetch_result import ResponseData as ResponseData, ResponseStatus as ResponseStatus
from gui.wgcg.wot_shop.controller import IWotShopController as IWotShopController
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.platform.product_purchase_controller import WotShopPrice as WotShopPrice
from wg_async import wg_await as wg_await, wg_async as wg_async
from typing import List as List, Dict as Dict, Optional as Optional, Set as Set
from gui.platform.products_fetcher.wot_shop.descriptors.product_descriptor import ProductDescriptor as ProductDescriptor
from gui.platform.products_fetcher.wot_shop.descriptors.account_limits_descriptor import AccountLimitsDescriptor as AccountLimitsDescriptor
from gui.platform.products_fetcher.wot_shop.descriptors.categories_descriptor import CategoriesDescriptor as CategoriesDescriptor
from comp7.helpers.comp7_server_settings import Comp7RanksConfig as Comp7RanksConfig
_logger: Any
ShopPageProductInfo: Any

class ShopControllerStatus(Enum):
    IDLE = 'idle'
    PENDING = 'pending'
    DATA_READY = 'data_ready'
    ERROR = 'error'

class Comp7ShopController(IComp7ShopController):
    __shopController: Any
    __comp7Controller: Any
    __PRODUCTS_STOREFRONT = 'comp7_shop'
    __products: Any
    __categoriesDiscounts: Any
    __ranksDiscounts: Any
    __categoriesToRanks: Any
    __ranksToCategories: Any
    __notifiedRanks: Any
    __cachedProductsRankNumber: Any
    __status: Any
    __isShopEnabled: Any
    __eventsManager: Any
    onDataUpdated: Any
    onShopStateChanged: Any
    def __init__(self):
        ...
    @property
    def isShopEnabled(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def onConnected(self):
        ...
    def onDisconnected(self):
        ...
    # decorador original: @wg_async
    def __requestProducts(self, force=False):
        ...
    def getProducts(self):
        ...
    # decorador original: @wg_async
    def buyProduct(self, productCode):
        ...
    def hasNewProducts(self, rank):
        ...
    def hasNewDiscounts(self, newRank):
        ...
    def validateCachedProducts(self):
        ...
    # decorador original: @wg_async
    def __onNewMaxRank(self, newMaxRank):
        ...
    def __onConfigChanged(self):
        ...
    def __resetCache(self):
        ...
    def __setStatus(self, status):
        ...
    def __processShopResponse(self, response):
        ...
    def __convertCategoriesToRanks(self, categories):
        ...
    def __processDiscounts(self, categories):
        ...
    def __convertProducts(self, products, accountLimits):
        ...
    def __isResponseReadyToProcess(self, response):
        ...
    def __sendPurchaseErrorSystemMessage(self):
        ...
    def __sendNewProductsForRankMessage(self):
        ...
    def __sendNewDiscountsForRankMessage(self):
        ...
