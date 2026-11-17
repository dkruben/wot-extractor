# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/buy_vehicle_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
from functools import partial as partial
from typing import TYPE_CHECKING as TYPE_CHECKING, List as List, NamedTuple as NamedTuple
import BigWorld as BigWorld
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import EasyTankEquip as EasyTankEquip
import Settings as Settings
import adisp as adisp
import constants as constants
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import QUEUE_TYPE as QUEUE_TYPE
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags, ViewEvent as ViewEvent
from gui import SystemMessages as SystemMessages
from gui.DialogsInterface import showI18nConfirmDialog as showI18nConfirmDialog
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.dialogs import I18nConfirmDialogMeta as I18nConfirmDialogMeta, DIALOG_BUTTON_ID as DIALOG_BUTTON_ID
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity as EventSystemEntity
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as SYSTEM_MESSAGES
from gui.impl import backport as backport
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, createTooltipData as createTooltipData
from gui.impl.backport.backport_pop_over import BackportPopOverContent as BackportPopOverContent, createPopOverData as createPopOverData
from gui.impl.dialogs.sub_views.top_right.money_balance import MoneyBalance as MoneyBalance
from gui.impl.gen.resources import R as R
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencyViewModel as CurrencyViewModel, CurrencyType as CurrencyType, CurrencySize as CurrencySize
from gui.impl.gen.view_models.views.lobby.hangar.buy_vehicle_option_model import BuyVehicleOptionModel as BuyVehicleOptionModel, OptionState as OptionState
from gui.impl.gen.view_models.views.lobby.hangar.buy_vehicle_view_model import BuyVehicleViewModel as BuyVehicleViewModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from gui.prb_control.entities.base.listener import IPrbListener as IPrbListener
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from gui.shared import event_dispatcher as event_dispatcher, events as events, g_eventBus as g_eventBus
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import LoadViewEvent as LoadViewEvent, ShopEvent as ShopEvent, VehicleBuyEvent as VehicleBuyEvent, OpenLinkEvent as OpenLinkEvent
from gui.shared.formatters.text_styles import neutral as neutral
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.Vehicle import VEHICLE_TAGS as VEHICLE_TAGS
from gui.shared.gui_items.gui_item_economics import ITEM_PRICE_EMPTY as ITEM_PRICE_EMPTY, ItemPrice as ItemPrice, ITEM_PRICE_ZERO as ITEM_PRICE_ZERO
from gui.shared.gui_items.processors.vehicle import VehicleBuyer as VehicleBuyer, VehicleSlotBuyer as VehicleSlotBuyer, VehicleRenter as VehicleRenter, VehicleTradeInProcessor as VehicleTradeInProcessor, VehicleRestoreProcessor as VehicleRestoreProcessor, showVehicleReceivedResultMessages as showVehicleReceivedResultMessages
from gui.shared.money import Currency as Currency, Money as Money, ZERO_MONEY as ZERO_MONEY
from gui.shared.utils import decorators as decorators
from gui.shared.utils.vehicle_collector_helper import getCollectibleVehiclesInInventory as getCollectibleVehiclesInInventory
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.shop import showBuyGoldForVehicleWebOverlay as showBuyGoldForVehicleWebOverlay, showTradeOffOverlay as showTradeOffOverlay
from helpers import dependency as dependency
from items import UNDEFINED_ITEM_CD as UNDEFINED_ITEM_CD
from rent_common import parseRentID as parseRentID
from shared_utils import CONST_CONTAINER as CONST_CONTAINER, first as first
from skeletons.gui.game_control import IRentalsController as IRentalsController, ITradeInController as ITradeInController, IRestoreController as IRestoreController, IWalletController as IWalletController, ISoundEventChecker as ISoundEventChecker
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
from uilogging.shop.loggers import ShopBuyVehicleMetricsLogger as ShopBuyVehicleMetricsLogger
from uilogging.shop.logging_constants import ShopLogItemStates as ShopLogItemStates
from typing import Optional as Optional
from gui.shared.money import CURRENCY_TYPE as CURRENCY_TYPE
from gui.shared.gui_items.artefacts import Equipment as Equipment
from gui.impl.gen.view_models.views.lobby.hangar.buy_vehicle_price_model import BuyVehiclePriceModel as BuyVehiclePriceModel
_logger: Any
_TooltipExtraData: Any
_RentPopoverData: Any
_TradeInPopoverData: Any
_ConsumableTagsInfo: Any
_VP_SHOW_PREVIOUS_SCREEN_ON_SUCCESS_ALIASES: tuple
_COLLECTIBLE_VEHICLE_TUTORIAL = 'collectibleVehicle'

class VehicleBuyActionTypes(CONST_CONTAINER):
    DEFAULT = 0
    BUY = 1
    RESTORE = 2
    RENT = 3

class VehicleOptions(CONST_CONTAINER):
    AMMO = 'ammo'
    SLOT = 'slot'
    CREW = 'crew'
    CONSUMABLES = 'consumables'
    ORDER: tuple
    __FOR_SAVE: tuple
    __SECTION_KEY = Settings.KEY_BUY_VEHICLE_VIEW_PREFERENCES
    __defaultKeys: Any
    def __init__(self, defaultKeys=...):
        ...
    def __contains__(self, value):
        ...
    def __getitem__(self, idx):
        ...
    def write(self, key, value, needToSave=True):
        ...
    def toggle(self, value):
        ...
    def read(self):
        ...
    def save(self):
        ...
    def getDataSection(self):
        ...
    def _validateValue(self, value):
        ...
    def __ensureDataSectionExists(self):
        ...

class BuyVehicleView(ViewImpl, EventSystemEntity, IPrbListener):
    __itemsCache: Any
    __rentals: Any
    __tradeIn: Any
    __wallet: Any
    __restore: Any
    __soundEventChecker: Any
    __CREW_NOT_SELECTED_IDX = -1
    __REPAIR_KIT_CONFIG_INDEX = 1
    __consumablesConfig: list
    __slots__: tuple
    __shop: Any
    __stats: Any
    __nationID: Any
    __inNationID: Any
    __previousAlias: Any
    __actionType: Any
    __returnAlias: Any
    __returnCallback: Any
    __selectedCardIdx: Any
    __vehicle: Any
    __uiMetricsLogger: Any
    __tradeInVehicleToSell: Any
    __isGoldAutoPurchaseEnabled: Any
    __confirmGoldPrice: Any
    __tradeInInProgress: Any
    __hasFreePremiumCrew: Any
    __purchaseInProgress: Any
    __usePreviousAlias: Any
    __tradeInProgress: Any
    __selectedOptions: Any
    __crewPrice: Any
    __moneyBalanceWidget: Any
    __tooltipPriceData: Any
    __consumables: Any
    __selectedRentIdx: Any
    __selectedRentID: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def isWithSlot(self):
        ...
    @property
    def isWithAmmo(self):
        ...
    @property
    def isWithConsumables(self):
        ...
    @property
    def isWithCrew(self):
        ...
    @property
    def consumablesPrice(self):
        ...
    @property
    def consumablesToBuy(self):
        ...
    def createToolTip(self, event):
        ...
    def createPopOverContent(self, event):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def __onItemCacheSyncCompleted(self, *_):
        ...
    # decorador original: @adisp.adisp_process
    def __showVehicleInHangar(self, *_):
        ...
    def __onBuyBtnClick(self):
        ...
    def __onSelectTradeInVehicleToSell(self, _=None):
        ...
    def __onWalletStatusChanged(self, *_):
        ...
    def __onTradeInVehicleToSellSelected(self, _=None):
        ...
    def __onClearTradeInVehicleToSell(self, _=None):
        ...
    def __onDisclaimerClick(self):
        ...
    def __onTradeInConfirmed(self, *_):
        ...
    def __onRestoreChange(self, _):
        ...
    def __onRentTermSelected(self, event):
        ...
    def __onSuccess(self):
        ...
    def __onWindowClose(self, *_):
        ...
    def __destroyWindow(self):
        ...
    def __processReturnCallback(self):
        ...
    # decorador original: @decorators.adisp_process(...)
    def __requestForMoneyObtain(self):
        ...
    # decorador original: @adisp.adisp_async
    # decorador original: @adisp.adisp_process
    def __requestForMoneyObtainImpl(self, callback):
        ...
    def __getTradeInCTX(self, vehicle):
        ...
    def __fillTradeInInfo(self):
        ...
    def __fillRentInfo(self):
        ...
    def __updateIsEnoughStatus(self, *_):
        ...
    def __fillTotalPrice(self):
        ...
    def __updateBuyBtnData(self, totalPrice):
        ...
    def __fillBuyButtonLabel(self):
        ...
    def __fillTitle(self):
        ...
    def __getAmmoItemPrice(self):
        ...
    def __getAmmoIsAvailable(self, ammoPrice):
        ...
    def __hasFreeSlots(self):
        ...
    def __getSlotIsAvailable(self, slotPrice):
        ...
    def __getCrewIsAvailable(self):
        ...
    def __getTotalItemPrice(self):
        ...
    def __getVehiclePrice(self):
        ...
    def __getObtainVehicleProcessor(self, crewType):
        ...
    def __getRestoreVehicleProcessor(self, crewType):
        ...
    def __getBackportTooltipData(self, event):
        ...
    def __isAvailablePrice(self, money, reservedMoney=...):
        ...
    def __isPurchaseCurrencyAvailable(self, currencyType):
        ...
    @property
    def __isTradeIn(self):
        ...
    @property
    def __hasTradeInWidget(self):
        ...
    @property
    def __isRentVisible(self):
        ...
    @property
    def __isRestore(self):
        ...
    def __isToggleRentAndTradeInState(self):
        ...
    def __isValidTradeOffSelected(self):
        ...
    def __isRenting(self):
        ...
    def __isBuying(self):
        ...
    def __startTutorial(self):
        ...
    def __updateFreePremiumCrew(self):
        ...
    def __onClientUpdated(self, diff, *_):
        ...
    # decorador original: @args2params(...)
    def __onOptionClick(self, name):
        ...
    def __fillInfo(self):
        ...
    def __canBuyConsumables(self):
        ...
    def __setConsumables(self):
        ...
    def __getConsumable(self, tags):
        ...
    def __fillOptions(self):
        ...
    def __createAmmoOptionModel(self):
        ...
    def __createConsumablesOptionModel(self):
        ...
    def __createSlotOptionModel(self):
        ...
    def __createCrewOptionModel(self):
        ...
    def __createOptionModel(self, optionName, itemPrice, icon, title, customState=None, tooltipHeader=None, tooltipBody=None, isPriceVisible=True, needToSave=True):
        ...
    def __fillPriceModel(self, priceModel, itemPrice, tooltipKey):
        ...

class BuyVehicleWindow(LobbyWindow):
    __slots__: tuple
    def __init__(self, **kwargs):
        ...

def getItemPriceCurrencies(itemPrice):
    ...
