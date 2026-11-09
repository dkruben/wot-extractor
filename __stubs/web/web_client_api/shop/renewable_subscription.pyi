# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/shop/renewable_subscription.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.server_events.bonuses_wot_plus import getAvailableCoreBonuses as getAvailableCoreBonuses, getAvailableProBonuses as getAvailableProBonuses
from helpers import dependency as dependency
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from uilogging.wot_plus.loggers import WotPlusInfoPageLogger as WotPlusInfoPageLogger
from uilogging.wot_plus.logging_constants import WotPlusInfoPageSource as WotPlusInfoPageSource
from renewable_subscription_common.settings_constants import WotPlusTier as WotPlusTier
from web.web_client_api import W2CSchema as W2CSchema, w2c as w2c
_TIER_TO_STRING: dict

class RenewableSubWebApiMixin(object):
    _wotPlusCtrl: Any
    # decorador original: @w2c(...)
    def getSubscriptionInfo(self, cmd):
        ...
    # decorador original: @w2c(...)
    def handleSubscriptionInfoWindow(self, cmd):
        ...
