# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/shop/unified_trade_in.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewvalues as viewvalues
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.shared import event_dispatcher as shared_events
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from helpers import dependency as dependency
from items import UNDEFINED_ITEM_CD as UNDEFINED_ITEM_CD
from skeletons.gui.game_control import ITradeInController as ITradeInController
from skeletons.gui.shared import IItemsCache as IItemsCache
from web.web_client_api import W2CSchema as W2CSchema, w2c as w2c, Field as Field
from web.web_client_api.shop import formatters as formatters
from web.web_client_api.shop.formatters import Field as FormatterField
from typing import Optional as Optional, Dict as Dict, List as List
from web.web_client_api.shop.formatters import Formatter as Formatter

class _SelectedVehicleSchema(W2CSchema):
    vehicleCompactDescriptor: Any

class TradeInFormatter(object):
    _formatter: Any
    _additionalFields: Any
    def __init__(self, formatter, additionalFields):
        ...
    def format(self, item):
        ...

class TradeInShopVehicleStates(object):
    OK = 'OK'
    IN_BATTLE = 'IN_BATTLE'
    UNSUITABLE = 'UNSUITABLE'
    DAMAGED = 'DAMAGED'
    IN_TACTICAL_UNIT = 'IN_TACTICAL_UNIT'

class UnifiedTradeInWebApiMixin(object):
    _tradeIn: Any
    _itemsCache: Any
    CLIENT_TO_SHOP_VEHICLE_STATES: dict
    buyVehicleFormatter: Any
    sellVehicleFormatter: Any
    def __init__(self):
        ...
    # decorador original: @w2c(...)
    def getUnifiedTradeInEnabled(self, cmd):
        ...
    # decorador original: @w2c(...)
    def getUnifiedTradeInInfo(self, cmd):
        ...
    # decorador original: @w2c(...)
    def setUnifiedTradeInVehicleToSell(self, cmd):
        ...
    # decorador original: @w2c(...)
    def setUnifiedTradeInVehicleToBuy(self, cmd):
        ...
    # decorador original: @w2c(...)
    def executeUnifiedTradeIn(self, cmd):
        ...
    def _getBuyVehicleFormatter(self):
        ...
    def _getSellVehicleFormatter(self):
        ...
