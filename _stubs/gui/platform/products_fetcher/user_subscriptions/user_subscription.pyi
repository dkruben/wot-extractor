# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/products_fetcher/user_subscriptions/user_subscription.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from enum import Enum as Enum
from typing import Dict as Dict
from gui.impl.gen.view_models.views.lobby.page.header.wot_plus_subscription_model import WotPlusPeriodicityEnum as WotPlusPeriodicityEnum
from helpers.time_utils import getTimestampFromISO as getTimestampFromISO
SUBSCRIPTION_CANCEL_STATUSES: list
BILLING_PERIOD_DAYS_MAP: dict
_logger: Any

class SubscriptionStatus(Enum):
    NEW = 'NEW'
    WAITING_FOR_PURCHASE = 'WAITING_FOR_PURCHASE'
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    GDPR_SUSPENDED = 'GDPR_SUSPENDED'
    NEXT_PAYMENT_UNAVAILABLE = 'NEXT_PAYMENT_UNAVAILABLE'

class SubscriptionRequestPlatform(Enum):
    WG_PLATFORM = 'wg_platform'
    STEAM = 'steam'
    UNKNOWN = 'unknown'

class UserSubscription(object):
    __slots__: tuple
    subscriptionId: Any
    productCode: Any
    status: Any
    nextBillingTime: Any
    platform: Any
    billingPeriod: Any
    def __init__(self, subscriptionData):
        ...
    def loadFromData(self, subscriptionData):
        ...
    def __str__(self):
        ...
