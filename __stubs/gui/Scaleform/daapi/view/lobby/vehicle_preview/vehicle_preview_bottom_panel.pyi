# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/vehicle_preview_bottom_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import time as time
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from collector_vehicle import CollectorVehicleConsts as CollectorVehicleConsts
from constants import GameSeasonType as GameSeasonType, RentType as RentType
from gui import DialogsInterface as DialogsInterface
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.dialogs import DIALOG_BUTTON_ID as DIALOG_BUTTON_ID, I18nConfirmDialogMeta as I18nConfirmDialogMeta
from gui.Scaleform.daapi.view.dialogs.ExchangeDialogMeta import ExchangeCreditsWebProductMeta as ExchangeCreditsWebProductMeta
from gui.Scaleform.daapi.view.lobby.techtree.techtree_dp import g_techTreeDP as g_techTreeDP
from gui.Scaleform.daapi.view.lobby.vehicle_preview.hero_tank_preview_constants import getHeroTankPreviewParams as getHeroTankPreviewParams
from gui.Scaleform.daapi.view.lobby.vehicle_preview.items_kit_helper import BOX_TYPE as BOX_TYPE, OFFER_CHANGED_EVENT as OFFER_CHANGED_EVENT, getActiveOffer as getActiveOffer, lookupItem as lookupItem, mayObtainForMoney as mayObtainForMoney, mayObtainWithMoneyExchange as mayObtainWithMoneyExchange, showItemTooltip as showItemTooltip
from gui.Scaleform.daapi.view.lobby.vehicle_preview.preview_bottom_panel_constants import ObtainingMethodInfo as ObtainingMethodInfo, ObtainingMethods as ObtainingMethods, getItemPackObtainingInfo as getItemPackObtainingInfo
from gui.Scaleform.daapi.view.lobby.vehicle_preview.vehicle_preview_dp import DefaultVehPreviewDataProvider as DefaultVehPreviewDataProvider
from gui.Scaleform.daapi.view.meta.VehiclePreviewBottomPanelMeta import VehiclePreviewBottomPanelMeta as VehiclePreviewBottomPanelMeta
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.Scaleform.locale.VEHICLE_PREVIEW import VEHICLE_PREVIEW as VEHICLE_PREVIEW
from gui.game_control.links import URLMacros as URLMacros
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.referral_program import showGetVehiclePage as showGetVehiclePage
from gui.shared import event_dispatcher as event_dispatcher, events as events, g_eventBus as g_eventBus
from gui.shared.event_dispatcher import showVehicleRentDialog as showVehicleRentDialog, showLootBoxEntry as showLootBoxEntry, showLootBoxBuyWindow as showLootBoxBuyWindow
from gui.shared.events import HasCtxEvent as HasCtxEvent
from gui.shared.formatters import chooseItemPriceVO as chooseItemPriceVO, formatPrice as formatPrice, getItemPricesVO as getItemPricesVO, getItemUnlockPricesVO as getItemUnlockPricesVO, icons as icons, text_styles as text_styles, time_formatters as time_formatters
from gui.shared.gui_items.gui_item_economics import ActualPrice as ActualPrice, ITEM_PRICE_EMPTY as ITEM_PRICE_EMPTY, ItemPrice as ItemPrice, getPriceTypeAndValue as getPriceTypeAndValue
from gui.shared.gui_items.items_actions import factory as factory
from gui.shared.money import Currency as Currency, MONEY_UNDEFINED as MONEY_UNDEFINED, Money as Money
from gui.shared.tooltips.formatters import getActionPriceData as getActionPriceData
from gui.shared.utils import vehicle_collector_helper as vehicle_collector_helper
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shop import canBuyGoldForVehicleThroughWeb as canBuyGoldForVehicleThroughWeb, showBuyGoldForBundle as showBuyGoldForBundle, showBuyProductOverlay as showBuyProductOverlay
from helpers import dependency as dependency, int2roman as int2roman, time_utils as time_utils
from helpers.i18n import makeString as _ms
from shared_utils import findFirst as findFirst
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import IExternalLinksController as IExternalLinksController, IHeroTankController as IHeroTankController, IMarathonEventsController as IMarathonEventsController, IRestoreController as IRestoreController, ITradeInController as ITradeInController, IVehicleComparisonBasket as IVehicleComparisonBasket, ILootBoxSystemController as ILootBoxSystemController, IWalletController as IWalletController
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
from uilogging.shop.loggers import ShopBundleVehiclePreviewMetricsLogger as ShopBundleVehiclePreviewMetricsLogger
from web.web_client_api.common import ItemPackEntry as ItemPackEntry, ItemPackTypeGroup as ItemPackTypeGroup
_ButtonState: Any
_logger: Any

class _CouponData(object):
    __slots__: tuple
    __item: Any
    __selected: Any
    __discount: Any
    def __init__(self, item=None, selected=False):
        ...
    @property
    def item(self):
        ...
    @item.setter
    def item(self, value):
        ...
    @property
    def selected(self):
        ...
    @selected.setter
    def selected(self, value):
        ...
    @property
    def discount(self):
        ...

class VehiclePreviewBottomPanel(VehiclePreviewBottomPanelMeta):
    appLoader: Any
    _itemsCache: Any
    _goodiesCache: Any
    _comparisonBasket: Any
    _tradeIn: Any
    _restores: Any
    _heroTanks: Any
    _lobbyContext: Any
    _marathonsCtrl: Any
    _lootBoxesCtrl: Any
    __linksCtrl: Any
    __wallet: Any
    _vehicleCD: Any
    _vehicleLevel: Any
    _actionType: Any
    _skipConfirm: Any
    _disableBuyButton: Any
    _marathonEvent: Any
    __previewDP: Any
    __isHeroTank: Any
    __price: Any
    __title: Any
    __description: Any
    __items: Any
    __offers: Any
    __currentOffer: Any
    __styleByGroup: Any
    __vehicleByGroup: Any
    __endTime: Any
    __oldPrice: Any
    __buyParams: Any
    __obtainingInfo: Any
    __backAlias: Any
    __backCallback: Any
    __timeCallbackID: Any
    __timeLeftIcon: Any
    __cachedVehiclesVOs: Any
    __cachedItemsVOs: Any
    __cachedCollapsedItemsVOs: Any
    __couponInfo: Any
    __hasSSEDiscount: Any
    __urlMacros: Any
    __bundlePreviewMetricsLogger: Any
    def __init__(self, skipConfirm=False):
        ...
    def onBuyOrResearchClick(self):
        ...
    def onCouponSelected(self, isActive):
        ...
    def setMarathonEvent(self, prefix):
        ...
    def setTimerData(self, endTime):
        ...
    def setInfoTooltip(self):
        ...
    def setBuyParams(self, buyParams):
        ...
    def setObtainingInfo(self, obtainingMethod):
        ...
    def setBundlePreviewMetricsLogger(self, bundlePreviewMetricsLogger):
        ...
    def setBackAlias(self, backAlias):
        ...
    def setBackCallback(self, backCallback):
        ...
    def setIsHeroTank(self, isHero):
        ...
    def setPackItems(self, packItems, price, oldPrice, title):
        ...
    def onCarouselVehicleSelected(self, intCD):
        ...
    def setOffers(self, offers, title, description):
        ...
    def onOfferSelected(self, offerID):
        ...
    def showTooltip(self, intCD, itemType):
        ...
    def updateData(self, useCompactData):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __update(self, collapseItems=False):
        ...
    def __getOfferByID(self, offerID):
        ...
    def __isReferralWindow(self):
        ...
    def __isStoreWindow(self):
        ...
    def __getConfirmationDialogKey(self):
        ...
    def __buyRequestConfirmation(self, key='buyConfirmation'):
        ...
    def __onVehicleLoading(self, ctxEvent):
        ...
    # decorador original: @adisp_process
    def __updateBtnState(self, *_):
        ...
    def __onVehicleChanged(self, *_):
        ...
    def __onRestoreChanged(self, vehicles):
        ...
    def __onServerSettingsChanged(self, diff):
        ...
    def __onSyncCompleted(self, *_):
        ...
    def __onBlueprintsModeChanged(self, _):
        ...
    def __getBtnData(self):
        ...
    def __checkBtnEnableByPrice(self, price):
        ...
    def __getBtnDataPack(self):
        ...
    def __getPackPrice(self):
        ...
    def __getBtnDataUnlockedVehicle(self, vehicle):
        ...
    def __getBtnDataCollectibleVehicle(self, vehicle):
        ...
    def __getBtnDataLockedVehicle(self, vehicle):
        ...
    @staticmethod
    def __getBestOfferTooltipData(eventType=None):
        ...
    def __getCurrentOfferTitle(self):
        ...
    def __getCurrentOfferDescription(self):
        ...
    def __startTimer(self, interval):
        ...
    def __stopTimer(self):
        ...
    def __setUsageLeftTime(self, leftTime):
        ...
    def __setShortLeftTime(self, leftTime):
        ...
    def __setDateLeftTime(self):
        ...
    def __timeOver(self):
        ...
    def __onLeftTimeUpdated(self):
        ...
    # decorador original: @adisp_process
    def __purchasePackage(self):
        ...
    def __purchaseOffer(self):
        ...
    def __purchaseSingleVehicle(self, vehicle):
        ...
    # decorador original: @adisp_process
    def __purchaseHeroTank(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def __hasExternalLink(self, callback=None):
        ...
    # decorador original: @adisp_process
    def __purchaseMarathonPackage(self):
        ...
    def __research(self):
        ...
    def __getUnlockedVehicleBtnLabel(self, priceType):
        ...
    @staticmethod
    def __updateEnabledState(collection, enabled):
        ...
    def __isHeroTankFromBoxes(self):
        ...

def _buildBuyButtonTooltip(key):
    ...
def _buildRestoreButtonTooltip(timeLeft):
    ...
def _getCollectibleWarningStr(mainString, vehicle):
    ...
