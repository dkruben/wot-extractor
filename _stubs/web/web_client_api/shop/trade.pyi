# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/shop/trade.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems
from gui import SystemMessages as SystemMessages
from gui.SystemMessages import pushMessagesFromResult as pushMessagesFromResult
from gui.shared.gui_items.processors.common import GoldToCreditsExchanger as GoldToCreditsExchanger, PremiumAccountBuyer as PremiumAccountBuyer
from gui.shared.gui_items.processors.goodies import BoosterBuyer as BoosterBuyer
from gui.shared.gui_items.processors.module import ModuleBuyer as ModuleBuyer
from gui.shared.gui_items.processors.vehicle import VehicleBuyer as VehicleBuyer, showVehicleReceivedResultMessages as showVehicleReceivedResultMessages
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
from web.web_client_api import Field as Field, W2CSchema as W2CSchema, w2c as w2c
from web.web_client_api.common import ShopItemType as ShopItemType
_ItemBuySpec: Any
_EXCHANGER: dict

class _BuyItemsSchema(W2CSchema):
    items: Any

class _CurrencyExchangeSchema(W2CSchema):
    currencies: Any

class TradeWebApiMixin(object):
    _goodiesCache: Any
    _itemsCache: Any
    # decorador original: @w2c(...)
    def exchange(self, cmd):
        ...
    # decorador original: @w2c(...)
    def buyItems(self, cmd):
        ...
    @staticmethod
    def __makeResult(itemType, itemId, success, result='error'):
        ...

def parseItemsSpec(specList):
    ...
def itemsSpecValidator(specList):
    ...
def _currencyExchangeValidator(_, data):
    ...
