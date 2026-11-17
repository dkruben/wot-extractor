# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/processors/module.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
from future.utils import viewitems as viewitems
import AccountCommands as AccountCommands
import BigWorld as BigWorld
from constants import EquipSideEffect as EquipSideEffect
from gui import makeHtmlString as makeHtmlString
from gui.SystemMessages import SM_TYPE as SM_TYPE, CURRENCY_TO_SM_TYPE as CURRENCY_TO_SM_TYPE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus
from gui.shared.events import ItemRemovalByDemountKitEvent as ItemRemovalByDemountKitEvent
from gui.shared.formatters import formatPrice as formatPrice, icons as icons, getBWFormatter as getBWFormatter
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.gui_item_economics import ITEM_PRICE_EMPTY as ITEM_PRICE_EMPTY
from gui.shared.gui_items.gui_item_economics import getItemBuyPrice as getItemBuyPrice
from gui.shared.gui_items.processors import ItemProcessor as ItemProcessor, makeI18nSuccess as makeI18nSuccess, makeI18nError as makeI18nError, VehicleItemProcessor as VehicleItemProcessor, plugins as plugins, makeSuccess as makeSuccess, Processor as Processor
from gui.shared.gui_items.processors.messages.items_processor_messages import OptDevicesDemountProcessorMessage as OptDevicesDemountProcessorMessage, OptDeviceRemoveProcessorMessage as OptDeviceRemoveProcessorMessage, ItemDestroyProcessorMessage as ItemDestroyProcessorMessage
from gui.shared.gui_items.vehicle_modules import VehicleTurret as VehicleTurret, VehicleGun as VehicleGun
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from items import vehicles as vehicles
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared.gui_items import IGuiItemsFactory as IGuiItemsFactory
MULTIPLE_SELLING_TEMPLATE = 'multipleSelling/{}'
_logger: Any

class ModuleProcessor(ItemProcessor):
    ITEMS_MSG_PREFIXES: dict
    DEFAULT_PREFIX = 'module'
    opType: Any
    def __init__(self, item, opType, plugs=...):
        ...
    def _getMsgCtx(self):
        ...
    def _formMessage(self, msg):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...

class ModuleTradeProcessor(ModuleProcessor):
    count: Any
    def __init__(self, item, count, opType, plugs=...):
        ...
    def _getMsgCtx(self):
        ...
    def _getOpPrice(self):
        ...

class ModuleBuyer(ModuleTradeProcessor):
    _currency: Any
    _itemPrice: Any
    def __init__(self, item, count, currency):
        ...
    def _getItemCurrencyAndPrice(self, currency):
        ...
    def _getOpPrice(self):
        ...
    def _getSysMsgType(self):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...

class BookBuyer(ModuleBuyer):
    def _getMsgCtx(self):
        ...

class ModuleSeller(ModuleTradeProcessor):
    def __init__(self, item, count):
        ...
    def _getOpPrice(self):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...

class ModuleDeconstruct(ModuleSeller):
    def _successHandler(self, code, ctx=None):
        ...

class MultipleModulesSeller(Processor):
    __items: Any
    def __init__(self, items, plugs=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _getPrice(self):
        ...
    def _getMsgCtx(self):
        ...
    def _request(self, callback):
        ...

class ModuleInstallProcessor(ModuleProcessor, VehicleItemProcessor):
    install: Any
    slotIdx: Any
    def __init__(self, vehicle, item, itemType, slotIdx, install=True, conflictedEqs=None, plugs=..., skipConfirm=False):
        ...
    def _getMsgCtx(self):
        ...
    def _successHandler(self, code, ctx=None):
        ...

class OptDeviceInstaller(ModuleInstallProcessor):
    lobbyContext: Any
    removalPrice: Any
    showWaiting: Any
    financeOperation: Any
    allSetups: Any
    def __init__(self, vehicle, item, slotIdx, install=True, allSetups=True, financeOperation=False, conflictedEqs=None, skipConfirm=False, showWaiting=True):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...
    def _response(self, code, callback, errStr='', ctx=None):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...

class EquipmentInstaller(ModuleInstallProcessor):
    def __init__(self, vehicle, item, slotIdx, install=True, conflictedEqs=None, skipConfirm=False):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...

class CommonModuleInstallProcessor(ModuleProcessor, VehicleItemProcessor):
    install: Any
    def __init__(self, vehicle, item, itemType, install=True, conflictedEqs=None, plugs=..., skipConfirm=False):
        ...
    def _getMsgCtx(self):
        ...
    def _successHandler(self, code, ctx=None):
        ...

class EquippedModernizedDeviceDestroyProcessor(CommonModuleInstallProcessor):
    def __init__(self, vehicle, item):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...

class TurretInstaller(CommonModuleInstallProcessor):
    gunCD: Any
    def __init__(self, vehicle, item, conflictedEqs=None, skipConfirm=False):
        ...
    def _findAvailableGun(self, vehicle, item):
        ...
    def _request(self, callback):
        ...
    def _successHandler(self, code, ctx=None):
        ...

class PreviewVehicleTurretInstaller(TurretInstaller):
    gunCD: Any
    def _findAvailableGun(self, vehicle, item):
        ...
    def _request(self, callback):
        ...

class OtherModuleInstaller(CommonModuleInstallProcessor):
    def __init__(self, vehicle, item, conflictedEqs=None, skipConfirm=False):
        ...
    def _request(self, callback):
        ...

class PreviewVehicleModuleInstaller(OtherModuleInstaller):
    OTHER_PREVIEW_MODULES: dict
    itemsFactory: Any
    def _request(self, callback):
        ...

class BuyAndInstallItemProcessor(ModuleBuyer):
    lobbyContext: Any
    _installConfirmatorPluginCls = plugins.BuyAndInstallConfirmator
    _storeConfirmatorPluginCls = plugins.BuyAndInstallConfirmator
    __vehInvID: Any
    __slotIdx: Any
    __gunCompDescr: Any
    __vehicle: Any
    _installedModuleCD: Any
    __mayInstall: Any
    _installReason: Any
    def __init__(self, vehicle, item, slotIdx, gunCompDescr, conflictedEqs=None, skipConfirm=False):
        ...
    def _getItemConfirmationData(self, conflictMsg):
        ...
    def __makeConflictMsg(self, conflictedText):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def __getAdditionalMessages(self, ctx):
        ...
    def _formApplyMessage(self, msg):
        ...
    def _request(self, callback):
        ...
    def _response(self, code, callback, errStr='', ctx=None):
        ...

class ModuleUpgradeProcessor(ModuleProcessor):
    __upgradePrice: Any
    vehicle: Any
    slotIdx: Any
    setupIdx: Any
    def __init__(self, item, vehicle, setupIdx, slotIdx, validateMoney=True, plugs=...):
        ...
    def _getMsgCtx(self):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...

class BattleAbilityInstaller(ModuleInstallProcessor):
    __epicMetaGameCtrl: Any
    def __init__(self, vehicle, item, slotIdx, install=True, conflictedEqs=None, skipConfirm=False):
        ...
    def _request(self, callback):
        ...
    def _successHandler(self, code, ctx=None):
        ...

def _getIconHtmlTagForCurrency(currency):
    ...
def _formatCurrencyValue(currency, value):
    ...
def _wrapHtmlMessage(key, message):
    ...
def getInstallerProcessor(vehicle, newComponentItem, slotIdx=0, install=True, isUseMoney=False, conflictedEqs=None, skipConfirm=False):
    ...
def getPreviewInstallerProcessor(vehicle, newComponentItem, conflictedEqs=None):
    ...
