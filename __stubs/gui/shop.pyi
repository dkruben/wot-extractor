# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shop.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
from adisp import adisp_process as adisp_process
from constants import GameSeasonType as GameSeasonType, RentType as RentType
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.hangar.BrowserView import makeBrowserParams as makeBrowserParams
from gui.Scaleform.daapi.view.lobby.store.browser import shop_helpers as helpers
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.game_control.links import URLMacros as URLMacros
from gui.impl.gen import R as R
from gui.shared import events as events, g_eventBus as g_eventBus
from gui.shared.economics import getGUIPrice as getGUIPrice
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.game_control import ITradeInController as ITradeInController
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any
_ProductInfo: Any
SHOP_RENT_TYPE_MAP: dict
SHOP_RENT_SEASON_TYPE_MAP: dict

class GoldPurchaseReason(object):
    VEHICLE = 'vehicle'
    RENT = 'rent'
    XP = 'experience'
    SLOT = 'slot'
    BERTH = 'barracks'
    CREW = 'crew'
    EQUIPMENT = 'equipment'
    CUSTOMIZATION = 'customization'
    BUNDLE = 'bundle'
    BATTLE_PASS = 'battle_pass'
    BATTLE_PASS_LEVELS = 'battle_pass_levels'
    PERSONAL_RESERVES = 'personal_reserves'

class Source(object):
    EXTERNAL = 'external'

class Origin(object):
    STORAGE = 'storage'
    HERO_TANK = 'hero_tank'
    BATTLE_BOOSTERS = 'battle_boosters'
    CONSUMABLES = 'consumables'
    WITHOUT_NAME = 'without_name'
    HANGAR_TOP_MENU = 'hangar_top_menu'
    HANGAR_BONS_SCREEN = 'hangar_bons_screen'

def _getParams(reason, price, itemId=None):
    ...
def _makeBuyItemUrl(categoryUrl, itemId=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def canBuyGoldForItemThroughWeb(itemID, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def canBuyGoldForVehicleThroughWeb(vehicle, itemsCache=None, tradeIn=None):
    ...
def showBuyPersonalReservesOverlay(itemId, source=None, origin=None):
    ...
def showBuyCreditsBattleBooster(itemId, source=None, origin=None):
    ...
def showBuyBonBattleBooster(itemId, source=None, origin=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showBattleBooster(itemId, source=None, origin=None, itemsCache=None):
    ...
def showBuyEquipment(itemId, source=None, origin=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showBuyOptionalDevice(itemId, source=None, origin=None, itemsCache=None):
    ...
def showTradeOffOverlay(parent=None):
    ...
def showBuyGoldForVehicleWebOverlay(fullPrice, intCD, parent=None):
    ...
def showBuyGoldForRentWebOverlay(fullPrice, intCD):
    ...
def showBuyGoldForXpWebOverlay(fullPrice):
    ...
def showBuyGoldForSlot(fullPrice):
    ...
def showBuyGoldForBerth(fullPrice):
    ...
def showBuyGoldForCrew(fullPrice):
    ...
def showBuyGoldForEquipment(fullPrice):
    ...
def showBuyGoldForCustomization(fullPrice):
    ...
def showBuyGoldForBattlePass(fullPrice):
    ...
def showBuyGoldForBattlePassLevels(fullPrice):
    ...
def showBuyGoldForPersonalReserves(fullPrice):
    ...
def showBuyGoldForLootboxReroll(fullPrice):
    ...
def showBuyGoldForBundle(fullPrice, params=None):
    ...
def showBlueprintsExchangeOverlay(url=None, parent=None):
    ...
# decorador original: @adisp_process
def _showBlurredWebOverlay(url, params=None, parent=None, isClientCloseControl=False):
    ...
# decorador original: @adisp_process
def showBuyItemWebView(url, itemId, source=None, origin=None):
    ...
# decorador original: @adisp_process
def showBuyItemOverlayWebView(url, itemId, source=None, origin=None, alias=...):
    ...
# decorador original: @adisp_process
def showBuyGoldWebOverlay(params=None, parent=None):
    ...
def showIngameShop(url, origin=None):
    ...
def showBuyProductOverlay(params=None):
    ...
def showRentProductOverlay(params=None):
    ...
# decorador original: @adisp_process
def _showOverlayWebStoreDefault(url, params=None):
    ...
