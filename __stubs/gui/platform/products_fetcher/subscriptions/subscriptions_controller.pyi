# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/products_fetcher/subscriptions/subscriptions_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from BWUtil import AsyncReturn as AsyncReturn
from constants import CURRENT_REALM as CURRENT_REALM
from constants import PRIME_GAMING_SUBSCRIPTION_PRODUCT as PRIME_GAMING_SUBSCRIPTION_PRODUCT
from gui.macroses import getLanguageCode as getLanguageCode
from gui.platform.base.statuses.constants import StatusTypes as StatusTypes
from gui.platform.products_fetcher.controller import ProductsFetchController as ProductsFetchController, _PlatformProductListParams as _PlatformProductListParams
from gui.platform.products_fetcher.subscriptions.subscription_descriptors import PrimeGamingDescriptor as PrimeGamingDescriptor, SubscriptionDescriptor as SubscriptionDescriptor, WotPlusDescriptor as WotPlusDescriptor, WotPlusProDescriptor as WotPlusProDescriptor
from helpers import dependency as dependency
from renewable_subscription_common.settings_constants import RS_TIER as RS_TIER
from renewable_subscription_common.settings_constants import WotPlusTier as WotPlusTier
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from skeletons.gui.platform.wgnp_controllers import IWGNPGeneralRequestController as IWGNPGeneralRequestController
from wg_async import wg_async as wg_async, wg_await as wg_await
from gui.platform.wgnp.general.statuses import GeneralAccountCountryStatus as GeneralAccountCountryStatus
from typing import Dict as Dict, Type as Type
_logger: Any
WOT_PLUS_TIER_TO_DESCRIPTOR_MAP: dict
__doc__: str

class PlatformSubscriptionsParams(_PlatformProductListParams):
    storefront = 'subscriptions_general'
    language: Any
    __wgnpCountryController: Any
    country: Any
    # decorador original: @wg_async
    def setCountry(self):
        ...

class SubscriptionProductsFetchController(ProductsFetchController):
    _wotPlusCtrl: Any
    platformParams = PlatformSubscriptionsParams
    defaultProductDescriptor = SubscriptionDescriptor
    productIDToDescriptor: dict
    def init(self):
        ...
    def fini(self):
        ...
    def _updateDescriptorsMap(self):
        ...
    def __onWotPlusChanged(self, diff):
        ...
