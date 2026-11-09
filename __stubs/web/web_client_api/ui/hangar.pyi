# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/hangar.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from past.builtins import basestring as basestring
import adisp as adisp
from gui import DialogsInterface as DialogsInterface
from gui.Scaleform.daapi.view.dialogs.ExchangeDialogMeta import ExchangeCreditsWebProductMeta as ExchangeCreditsWebProductMeta
from gui.impl.dialogs.dialogs import showExchangeToBuyItemsDialog as showExchangeToBuyItemsDialog
from gui.shared import event_dispatcher as shared_events
from gui.shared.event_dispatcher import showCrystalWindow as showCrystalWindow
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.items_actions import factory as ActionsFactory
from helpers import dependency as dependency
from skeletons.gui.game_control import IBrowserController as IBrowserController
from skeletons.gui.shared import IItemsCache as IItemsCache
from web.web_client_api import Field as Field, W2CSchema as W2CSchema, w2c as w2c
from wg_async import wg_async as wg_async, wg_await as wg_await
_logger: Any
_EXCHANGE_WINDOW_SIMPLE = 'simple'
_EXCHANGE_WINDOW_PLATFORM = 'platform'
_EXCHANGE_WINDOW_TYPES: Any

class _OpenHangarTabSchema(W2CSchema):
    vehicle_id: Any

class _ExchangeWindowSchema(W2CSchema):
    id: Any
    amount: Any
    price: Any
    name: Any
    type: Any
    windowLayerTop: Any

class HangarTabWebApiMixin(object):
    # decorador original: @w2c(...)
    def openHangar(self, cmd):
        ...

class HangarWindowsWebApiMixin(object):
    itemsCache: Any
    __browserController: Any
    # decorador original: @w2c(...)
    def openCurrencyExchangeWindow(self, cmd):
        ...
    # decorador original: @w2c(...)
    def openXPExchangeWindow(self, _):
        ...
    # decorador original: @w2c(...)
    def openBuySlotWindow(self, _):
        ...
    # decorador original: @w2c(...)
    def openBuyBerthWindow(self, _):
        ...
    # decorador original: @w2c(...)
    def openCrystalInfoWindow(self, _):
        ...
    def validateItems(self, itemCD):
        ...
    # decorador original: @adisp.adisp_async
    # decorador original: @wg_async
    def __showExchangeItemDialog(self, itemCD, count, callback):
        ...
