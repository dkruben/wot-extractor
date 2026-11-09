# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_obtain_windows.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from soft_exception import SoftException as SoftException
import constants as constants
from rent_common import parseRentID as parseRentID, isWithinMaxRentTime as isWithinMaxRentTime
from debug_utils import LOG_ERROR as LOG_ERROR
from gui import SystemMessages as SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.DialogsInterface import showI18nConfirmDialog as showI18nConfirmDialog
from gui.Scaleform.daapi.view.dialogs import I18nConfirmDialogMeta as I18nConfirmDialogMeta, DIALOG_BUTTON_ID as DIALOG_BUTTON_ID
from gui.Scaleform.daapi.view.lobby.rally.vo_converters import makeVehicleVO as makeVehicleVO
from gui.Scaleform.daapi.view.meta.VehicleBuyWindowMeta import VehicleBuyWindowMeta as VehicleBuyWindowMeta
from gui.Scaleform.genConsts.VEHICLE_BUY_WINDOW_ALIASES import VEHICLE_BUY_WINDOW_ALIASES as VEHICLE_BUY_WINDOW_ALIASES
from gui.Scaleform.locale.DIALOGS import DIALOGS as DIALOGS
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as SYSTEM_MESSAGES
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.shop import showBuyGoldForVehicleWebOverlay as showBuyGoldForVehicleWebOverlay
from gui.shared.events import VehicleBuyEvent as VehicleBuyEvent
from gui.shared.formatters import text_styles as text_styles, moneyWithIcon as moneyWithIcon
from gui.shared.formatters.text_styles import neutral as neutral
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice, ITEM_PRICE_EMPTY as ITEM_PRICE_EMPTY
from gui.shared.gui_items.processors.vehicle import VehicleBuyer as VehicleBuyer, VehicleSlotBuyer as VehicleSlotBuyer, VehicleRenter as VehicleRenter, VehicleRestoreProcessor as VehicleRestoreProcessor, VehicleTradeInProcessor as VehicleTradeInProcessor, showVehicleReceivedResultMessages as showVehicleReceivedResultMessages
from gui.shared.money import Money as Money, Currency as Currency
from gui.shared.tooltips import ACTION_TOOLTIPS_TYPE as ACTION_TOOLTIPS_TYPE
from gui.shared.tooltips.formatters import packActionTooltipData as packActionTooltipData
from gui.shared.tooltips.formatters import packItemActionTooltipData as packItemActionTooltipData, packItemRentActionTooltipData as packItemRentActionTooltipData
from gui.shared.utils import decorators as decorators
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import i18n as i18n, dependency as dependency
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.gui.game_control import IRentalsController as IRentalsController, ITradeInController as ITradeInController, IRestoreController as IRestoreController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
VehicleBuyWindowState: Any

class _TABS(CONST_CONTAINER):
    UNDEFINED = -1
    BUY = 0
    TRADE = 1

class VehicleBuyWindow(VehicleBuyWindowMeta):
    itemsCache: Any
    rentals: Any
    tradeIn: Any
    lobbyContext: Any
    nationID: Any
    inNationID: Any
    vehicle: Any
    tradeInVehicleToSell: Any
    __state: Any
    selectedTab: Any
    def __init__(self, ctx=None):
        ...
    def onWindowClose(self):
        ...
    def submit(self, data):
        ...
    def stateChange(self, data):
        ...
    def onTradeInClearVehicle(self):
        ...
    def selectTab(self, tabIndex):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _getGuiFields(self, vehicle):
        ...
    def _isTradeIn(self):
        ...
    def __getTradeInGuiFields(self, vehicle):
        ...
    def _getContentFields(self, vehicle):
        ...
    def __getTradeInContentFields(self, vehicle):
        ...
    def _isSubmitBtnEnabled(self):
        ...
    def _initData(self, *args):
        ...
    def _getContentLinkageFields(self):
        ...
    def _getOptainHeaderData(self, vehicle):
        ...
    def _getBuyContentData(self, vehicle, stats, isTradeIn):
        ...
    def _getSetupPrice(self):
        ...
    def _getAmmoPrice(self):
        ...
    def _getSlotPrice(self):
        ...
    def _getCrewPrice(self):
        ...
    def _getVehiclePrice(self, vehicle):
        ...
    def _getItemPriceActionData(self, vehicle):
        ...
    def _getRentData(self, vehicle, vehiclePricesActionData):
        ...
    def _addPriceBlock(self, result, vehicle, vehiclePricesActionData):
        ...
    def _getObtainVehicleProcessor(self, vehicle, data):
        ...
    def __onRentChange(self, vehicles):
        ...
    def __updateButtons(self):
        ...
    # decorador original: @decorators.adisp_process(...)
    def __requestForMoneyObtain(self, data):
        ...
    def __setGoldCallBack(self, gold):
        ...
    def __setCreditsCallBack(self, credit):
        ...
    def __setTradeOffVehicle(self, _=None):
        ...

class VehicleRestoreWindow(VehicleBuyWindow):
    restore: Any
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _addPriceBlock(self, result, vehicle, vehiclePricesActionData):
        ...
    def _getObtainVehicleProcessor(self, vehicle, data):
        ...
    def _getVehiclePrice(self, vehicle):
        ...
    def _getItemPriceActionData(self, vehicle):
        ...
    def _getGuiFields(self, vehicle):
        ...
    def _getContentFields(self, vehicle):
        ...
    def _isTradeIn(self):
        ...
    def __onRestoreChange(self, _):
        ...
