# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_sell_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import typing as typing
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from account_helpers.AccountSettings import AccountSettings as AccountSettings
from goodies.goodie_constants import GOODIE_VARIETY as GOODIE_VARIETY
from gui import SystemMessages as SystemMessages, makeHtmlString as makeHtmlString
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.view.lobby.customization.shared import TYPES_ORDER as TYPES_ORDER
from gui.Scaleform.daapi.view.meta.VehicleSellDialogMeta import VehicleSellDialogMeta as VehicleSellDialogMeta
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS as CURRENCIES_CONSTANTS
from gui.Scaleform.genConsts.FITTING_TYPES import FITTING_TYPES as FITTING_TYPES
from gui.goodies.demount_kit import isDemountKitApplicableTo as isDemountKitApplicableTo, getDemountKitForOptDevice as getDemountKitForOptDevice
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.formatters import text_styles as text_styles, getRoleTextWithLabel as getRoleTextWithLabel
from gui.shared.formatters.tankmen import formatDeletedTankmanStr as formatDeletedTankmanStr
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.processors import plugins as plugins
from gui.shared.gui_items.processors.vehicle import VehicleSeller as VehicleSeller, getCustomizationItemSellCountForVehicle as getCustomizationItemSellCountForVehicle
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.money import Currency as Currency, MONEY_UNDEFINED as MONEY_UNDEFINED
from gui.shared.tooltips import ACTION_TOOLTIPS_TYPE as ACTION_TOOLTIPS_TYPE
from gui.shared.tooltips.formatters import packActionTooltipData as packActionTooltipData
from gui.shared.tooltips.formatters import packItemActionTooltipData as packItemActionTooltipData
from gui.shared.utils import decorators as decorators
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.shop import showBuyGoldForEquipment as showBuyGoldForEquipment
from helpers import int2roman as int2roman, dependency as dependency
from items import ITEM_TYPES as ITEM_TYPES
from items.components.c11n_constants import ItemTags as ItemTags, SeasonType as SeasonType, CustomizationType as CustomizationType
from nation_change.nation_change_helpers import iterVehTypeCDsInNationGroup as iterVehTypeCDsInNationGroup
from post_progression_common import TankSetupGroupsId as TankSetupGroupsId
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import IRestoreController as IRestoreController, IWotPlusController as IWotPlusController
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import List as List, Set as Set, Iterator as Iterator, Optional as Optional, Tuple as Tuple, Dict as Dict, Union as Union, Any as Any
from gui.shared.gui_items.fitting_item import FittingItem as FittingItem
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.gui_items.artefacts import OptionalDevice as OptionalDevice, BattleBooster as BattleBooster
from gui.shared.gui_items.vehicle_modules import Shell as Shell
from gui.shared.gui_items.customization.c11n_items import Customization as Customization
from gui.shared.gui_items.gui_item import GUIItem as GUIItem
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from gui.shared.money import Money as Money
_DK_CURRENCY = GOODIE_VARIETY.DEMOUNT_KIT_NAME
_WP_CURRENCY = 'wotPlusVSD'
_SETTINGS_KEY = 'vehicleSellDialog'
_SETTINGS_OPEN_ENTRY = 'isOpened'
_INVENTORY_SHELLS = 'inventoryShells'
_BARRACKS_DROP_DOWN_DATA_PROVIDER: list
_DEMOUNT_KIT_ONE: _Any
_WOT_PLUS_ONE: _Any

class VehicleSellDialog(VehicleSellDialogMeta):
    __itemsCache: _Any
    __restore: _Any
    __goodiesCache: _Any
    __wotPlus: _Any
    __c11nService: _Any
    __slots__: tuple
    __vehInvID: _Any
    __vehicle: _Any
    __nationGroupVehicles: _Any
    __controlNumber: _Any
    __enteredControlNumber: _Any
    __income: _Any
    __accountMoney: _Any
    __isCrewDismissal: _Any
    __vehicleSellPrice: _Any
    __items: _Any
    __otherVehicleShells: _Any
    __isDemountKitEnabled: _Any
    def __init__(self, ctx=None):
        ...
    def onSelectionChanged(self, itemID, toInventory, currency):
        ...
    def setCrewDismissal(self, value):
        ...
    def setUserInput(self, value):
        ...
    def sell(self):
        ...
    def onWindowClose(self):
        ...
    def setDialogSettings(self, isOpen):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __getCrewData(self):
        ...
    def __addVSDItem(self, item):
        ...
    def __getSellVehicleData(self):
        ...
    def __prepareInventoryModules(self):
        ...
    def __prepareVehicleOptionalDevices(self, vehicle, currentBalance):
        ...
    def __prepareVehicleEquipments(self, vehicle):
        ...
    def __prepareVehicleBoosters(self, vehicle):
        ...
    def __prepareVehicleCustomizations(self, vehicle):
        ...
    def __prepareInventoryShells(self):
        ...
    def __prepareOnVehicleShells(self, vehicle):
        ...
    def __subscribe(self):
        ...
    def __unsubscribe(self):
        ...
    def __onSetGoldHandler(self, gold):
        ...
    def __onSetCrystalHandler(self, crystals):
        ...
    def __onSetEquipCoinHandler(self, equipCoin):
        ...
    def __onSellLimitUpdate(self, *_):
        ...
    def __onSetGoodiesHandler(self, goodies):
        ...
    def __updateMoney(self, currency, value):
        ...
    def __updateSubmitButton(self):
        ...
    def __getControlQuestion(self, usingGold=False):
        ...
    def __shopResyncHandler(self, reason, _):
        ...
    def __updateTotalCost(self):
        ...
    def __sendControlQuestion(self):
        ...
    def __getOtherVehiclesShells(self, vehInvID):
        ...
    def __getIsDemountKitEnabled(self):
        ...
    def __getNationGroupVehicles(self, vehicleCD):
        ...
    @property
    def __useCtrlQuestion(self):
        ...
    # decorador original: @decorators.adisp_process(...)
    def __doSellVehicle(self, vehicle, shells, eqs, optDevicesToSell, inventory, customizationItems, isDismissCrew, itemsForDemountKit, itemsForFreeDemount, boosters):
        ...

class _VSDMoney(dict):
    def __init__(self, money=None, **kwargs):
        ...
    def __getitem__(self, currency):
        ...
    def __add__(self, other):
        ...
    def __iadd__(self, other):
        ...
    def __sub__(self, other):
        ...
    def __isub__(self, other):
        ...
    def __neg__(self):
        ...
    def __mul__(self, n):
        ...
    def __rmul__(self, n):
        ...
    def toDict(self):
        ...
    def extract(self, currency):
        ...
    def isEmpty(self):
        ...
    def getShortage(self, have):
        ...

class _VSDItemData(object):
    __slots__: tuple
    __fittingItem: _Any
    _itemRemovalPrice: _Any
    __itemType: _Any
    _itemSellPrice: _Any
    _flashData: _Any
    def __init__(self, item, itemType=None):
        ...
    def toFlashVO(self):
        ...
    def setItemID(self, value):
        ...
    @property
    def itemSellPrice(self):
        ...
    @property
    def itemRemovalPrice(self):
        ...
    @property
    def guiItem(self):
        ...
    @property
    def toInventory(self):
        ...
    @toInventory.setter
    def toInventory(self, value):
        ...
    @property
    def removeCurrency(self):
        ...
    @removeCurrency.setter
    def removeCurrency(self, value):
        ...
    @property
    def isRemovableForMoney(self):
        ...
    @property
    def itemType(self):
        ...

class _ShellData(_VSDItemData):
    __slots__: tuple
    toInventory: _Any
    def __init__(self, shell, inInventory, onOtherVehicle):
        ...

class _BoosterData(_VSDItemData):
    __slots__: tuple
    def __init__(self, booster):
        ...

class _CustomizationData(_VSDItemData):
    __slots__: tuple
    def __init__(self, customization, count):
        ...

class _ModulesData(_VSDItemData):
    __slots__: tuple
    def __init__(self, module):
        ...

class _OptionalDeviceData(_VSDItemData):
    __slots__: tuple
    __itemsCache: _Any
    __wotPlus: _Any
    __lobbyContext: _Any
    _itemRemovalPrice: _Any
    def __init__(self, optDevice):
        ...
    @classmethod
    def __getAlertIconTooltip(cls, optDevice):
        ...

def _getDialogSettings():
    ...
def _setSlidingComponentOpened(value):
    ...
def _getSlidingComponentOpened():
    ...
def _getCurrencyIterator():
    ...
def _findCurrency(have, price):
    ...
