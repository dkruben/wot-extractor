# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/shop/stats.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import viewitems as viewitems
import adisp as adisp
import nations as nations
from wg_async import wg_async as wg_async, wg_await as wg_await
from constants import PREM_TYPE_TO_ENTITLEMENT as PREM_TYPE_TO_ENTITLEMENT
from gui.shared.money import Currency as Currency
from gui.shared.utils.vehicle_collector_helper import hasCollectibleVehicles as hasCollectibleVehicles
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IEntitlementsController as IEntitlementsController, IWalletController as IWalletController
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils.requesters import IStatsRequester as IStatsRequester
from web.common import formatBalance as formatBalance, formatWalletCurrencyStatuses as formatWalletCurrencyStatuses
from web.web_client_api import Field as Field, W2CSchema as W2CSchema, w2c as w2c
_logger: Any

class _GetInventoryEntitlementsSchema(W2CSchema):
    force: Any
    codes: Any

class BalanceWebApiMixin(object):
    itemsCache: Any
    __entitlementsController: Any
    __wallet: Any
    # decorador original: @w2c(...)
    def getBalance(self, cmd):
        ...
    # decorador original: @w2c(...)
    def getStats(self, cmd):
        ...
    # decorador original: @w2c(...)
    def getPremiumInfo(self, cmd):
        ...
    # decorador original: @w2c(...)
    def getCollectionNations(self, cmd):
        ...
    # decorador original: @w2c(...)
    def getInventoryEntitlements(self, cmd):
        ...
    # decorador original: @adisp.adisp_async
    # decorador original: @wg_async
    def __forceUpdateEntitlementsCache(self, codes, callback):
        ...
