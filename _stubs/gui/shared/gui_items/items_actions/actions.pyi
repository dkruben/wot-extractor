# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/items_actions/actions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from collections import namedtuple as namedtuple
from functools import partial as partial
from future.utils import listvalues as listvalues, viewitems as viewitems
from itertools import chain as chain
from typing import Callable as Callable
import wg_async as future_async
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import NATION_CHANGE_VIEWED as NATION_CHANGE_VIEWED
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from debug_utils import LOG_ERROR as LOG_ERROR
from gui import SystemMessages as SystemMessages, DialogsInterface as DialogsInterface
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.daapi.view.dialogs.ConfirmModuleMeta import BuyModuleMeta as BuyModuleMeta
from gui.Scaleform.daapi.view.dialogs.ConfirmModuleMeta import LocalSellModuleMeta as LocalSellModuleMeta
from gui.Scaleform.daapi.view.dialogs.ConfirmModuleMeta import MAX_ITEMS_FOR_OPERATION as MAX_ITEMS_FOR_OPERATION
from gui.Scaleform.daapi.view.dialogs.ExchangeDialogMeta import ExchangeCreditsSingleItemMeta as ExchangeCreditsSingleItemMeta, ExchangeCreditsForSlotMeta as ExchangeCreditsForSlotMeta
from gui.Scaleform.daapi.view.dialogs.ExchangeDialogMeta import ExchangeXpMeta as ExchangeXpMeta
from gui.Scaleform.daapi.view.dialogs.ExchangeDialogMeta import RestoreExchangeCreditsMeta as RestoreExchangeCreditsMeta
from gui.Scaleform.daapi.view.lobby.techtree import unlock as unlock
from gui.Scaleform.daapi.view.lobby.techtree.settings import RequestState as RequestState
from gui.Scaleform.daapi.view.lobby.techtree.settings import UnlockStats as UnlockStats
from gui.Scaleform.daapi.view.lobby.techtree.techtree_dp import g_techTreeDP as g_techTreeDP
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as SYSTEM_MESSAGES
from gui.SystemMessages import pushMessagesFromResult as pushMessagesFromResult
from gui.goodies.demount_kit import getDemountKitForOptDevice as getDemountKitForOptDevice
from gui.impl import backport as backport
from gui.impl.common.personal_reserves.personal_reserves_shared_constants import PREMIUM_BOOSTER_IDS as PREMIUM_BOOSTER_IDS, BUY_AND_ACTIVATE_TIMEOUT as BUY_AND_ACTIVATE_TIMEOUT
from gui.impl.gen import R as R
from gui.impl.lobby.dialogs.auxiliary.buy_and_exchange_state_machine import BuyAndExchangeStateEnum as BuyAndExchangeStateEnum
from gui.impl.lobby.personal_reserves import personal_reserves_dialogs as personal_reserves_dialogs
from gui.impl.lobby.personal_reserves.personal_reserves_utils import canBuyBooster as utilsCanBuyBooster
from gui.shared import event_dispatcher as shared_events
from gui.shared.economics import getGUIPrice as getGUIPrice
from gui.shared.event_dispatcher import showDeconstructionMultDeviceDialog as showDeconstructionMultDeviceDialog, showDeconstructionDeviceDialog as showDeconstructionDeviceDialog
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, GUI_ITEM_ECONOMY_CODE as GUI_ITEM_ECONOMY_CODE
from gui.shared.gui_items.Tankman import NO_TANKMAN as NO_TANKMAN
from gui.shared.gui_items.fitting_item import canBuyWithGoldExchange as canBuyWithGoldExchange
from gui.shared.gui_items.gui_item_economics import getVehicleShellsLayoutPrice as getVehicleShellsLayoutPrice
from gui.shared.gui_items.processors import makeSuccess as makeSuccess
from gui.shared.gui_items.processors.common import ConvertBlueprintFragmentProcessor as ConvertBlueprintFragmentProcessor, BuyBattleAbilitiesProcessor as BuyBattleAbilitiesProcessor
from gui.shared.gui_items.processors.common import TankmanBerthsBuyer as TankmanBerthsBuyer
from gui.shared.gui_items.processors.common import UseCrewBookProcessor as UseCrewBookProcessor, FillingAllUntrainedPerksProcessor as FillingAllUntrainedPerksProcessor
from gui.shared.gui_items.processors.goodies import BoosterBuyer as BoosterBuyer, BoosterActivator as BoosterActivator
from gui.shared.gui_items.processors.messages.items_processor_messages import ItemDeconstructionProcessorMessage as ItemDeconstructionProcessorMessage, MultItemsDeconstructionProcessorMessage as MultItemsDeconstructionProcessorMessage
from gui.shared.gui_items.processors.module import BuyAndInstallItemProcessor as BuyAndInstallItemProcessor, OptDeviceInstaller as OptDeviceInstaller, ModuleDeconstruct as ModuleDeconstruct, EquippedModernizedDeviceDestroyProcessor as EquippedModernizedDeviceDestroyProcessor
from gui.shared.gui_items.processors.module import ModuleSeller as ModuleSeller
from gui.shared.gui_items.processors.module import ModuleUpgradeProcessor as ModuleUpgradeProcessor
from gui.shared.gui_items.processors.module import MultipleModulesSeller as MultipleModulesSeller
from gui.shared.gui_items.processors.module import getInstallerProcessor as getInstallerProcessor
from gui.shared.gui_items.processors.tankman import TankmanFreeToOwnXpConvertor as TankmanFreeToOwnXpConvertor, TankmanRetraining as TankmanRetraining, TankmanUnload as TankmanUnload, TankmanEquip as TankmanEquip, TankmanChangePassport as TankmanChangePassport, TankmanDismiss as TankmanDismiss, TankmanRestore as TankmanRestore, TankmanChangeRole as TankmanChangeRole, TankmenJunkConverter as TankmenJunkConverter, TankmanAddSkills as TankmanAddSkills, ResetAllTankmenSkills as ResetAllTankmenSkills, TransferTankmanXP as TransferTankmanXP, TankmanRecruitAndEquip as TankmanRecruitAndEquip, QuickServiceTankmanEquip as QuickServiceTankmanEquip
from gui.shared.gui_items.processors.veh_post_progression import ChangeVehicleSetupEquipments as ChangeVehicleSetupEquipments, DiscardPairsProcessor as DiscardPairsProcessor, PurchasePairProcessor as PurchasePairProcessor, PurchaseStepsProcessor as PurchaseStepsProcessor, SetEquipmentSlotTypeProcessor as SetEquipmentSlotTypeProcessor, SwitchPrebattleAmmoPanelAvailability as SwitchPrebattleAmmoPanelAvailability, PurchaseVehSkillTreeStepsProcessor as PurchaseVehSkillTreeStepsProcessor
from gui.shared.gui_items.processors.vehicle import OptDevicesInstaller as OptDevicesInstaller, BuyAndInstallConsumablesProcessor as BuyAndInstallConsumablesProcessor, AutoFillVehicleLayoutProcessor as AutoFillVehicleLayoutProcessor, BuyAndInstallBattleBoostersProcessor as BuyAndInstallBattleBoostersProcessor, BuyAndInstallShellsProcessor as BuyAndInstallShellsProcessor, VehicleRepairer as VehicleRepairer, InstallBattleAbilitiesProcessor as InstallBattleAbilitiesProcessor
from gui.shared.gui_items.processors.vehicle import VehicleSlotBuyer as VehicleSlotBuyer
from gui.shared.gui_items.processors.vehicle import tryToLoadDefaultShellsLayout as tryToLoadDefaultShellsLayout
from gui.shared.money import ZERO_MONEY as ZERO_MONEY, Money as Money, Currency as Currency
from gui.shared.utils import decorators as decorators
from gui.shared.utils.requesters import RequestCriteria as RequestCriteria, REQ_CRITERIA as REQ_CRITERIA
from gui.shop import showBuyGoldForPersonalReserves as showBuyGoldForPersonalReserves, showBuyGoldForSlot as showBuyGoldForSlot
from gui.veh_post_progression.models.ext_money import EXT_MONEY_ZERO as EXT_MONEY_ZERO
from helpers import dependency as dependency
from items import vehicles as vehicles, ITEM_TYPE_NAMES as ITEM_TYPE_NAMES, parseIntCompactDescr as parseIntCompactDescr
from shared_utils import first as first, allEqual as allEqual
from skeletons.gui.game_control import ITradeInController as ITradeInController
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
from skeletons.gui.game_control import IExchangeRatesWithDiscountsProvider as IExchangeRatesWithDiscountsProvider
from exchange.personal_discounts_constants import EXCHANGE_RATE_FREE_XP_NAME as EXCHANGE_RATE_FREE_XP_NAME
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.goodies.goodie_items import Booster as Booster
_logger: Any
ItemSellSpec: Any
ItemDeconstructSpec: Any

class IGUIItemAction(object):
    __slots__: tuple
    __skipConfirm: Any
    def __init__(self):
        ...
    @property
    def skipConfirm(self):
        ...
    @skipConfirm.setter
    def skipConfirm(self, value):
        ...
    def doAction(self):
        ...
    def isAsync(self):
        ...

class CachedItemAction(IGUIItemAction):
    _itemsCache: Any

class GroupedItemAction(CachedItemAction):
    __slots__: tuple
    _groupID: Any
    _groupSize: Any
    def __init__(self, groupID, groupSize):
        ...
    @staticmethod
    def _pushGroupedMessages(result):
        ...

class BuyAction(CachedItemAction):
    tradeIn: Any
    def _mayObtainForMoney(self, item):
        ...
    def _mayObtainWithMoneyExchange(self, item):
        ...

class SellItemAction(CachedItemAction):
    __itemTypeCD: Any
    def __init__(self, itemTypeCD):
        ...
    # decorador original: @adisp_process
    def doAction(self):
        ...

class SellMultipleItems(IGUIItemAction):
    _itemsCache: Any
    __items: Any
    def __init__(self, itemSellSpecs):
        ...
    # decorador original: @adisp_process
    def doAction(self):
        ...

class ModuleBuyAction(BuyAction):
    __intCD: Any
    def __init__(self, intCD):
        ...
    # decorador original: @adisp_process
    def doAction(self):
        ...

class ChangeVehicleNationAction(IGUIItemAction):
    __vehCD: Any
    def __init__(self, vehCD):
        ...
    # decorador original: @adisp_process
    def doAction(self):
        ...

class VehicleBuyAction(BuyAction):
    __vehCD: Any
    __isTradeIn: Any
    __previousAlias: Any
    __returnCallback: Any
    __returnAlias: Any
    __actionType: Any
    def __init__(self, vehCD, isTradeIn=False, actionType=None, previousAlias=None, returnAlias=None, returnCallback=None):
        ...
    # decorador original: @adisp_process
    def doAction(self):
        ...
    def _showVehicleBuyDialog(self, item):
        ...
    def _mayObtainForMoney(self, item):
        ...
    def _mayObtainWithMoneyExchange(self, item):
        ...

class _UnlockItem(CachedItemAction):
    _itemConfirmatorCls = unlock.UnlockItemConfirmator
    _itemValidatorCls = unlock.UnlockItemValidator
    __costCtx: Any
    _item: Any
    _unlockProps: Any
    def __init__(self, itemCD, unlockProps):
        ...
    def _isEnoughXpToUnlock(self):
        ...
    def _createPlugins(self):
        ...
    def _showResult(self, result):
        ...
    def __getCostCtx(self):
        ...
    def __onBlueprintsModeChanged(self, _):
        ...
    def __clear(self):
        ...

class UnlockItemAction(_UnlockItem):
    # decorador original: @adisp_process
    def doAction(self):
        ...
    def __unlockItem(self):
        ...
    # decorador original: @decorators.adisp_process(...)
    def __doUnlockItem(self, plugins):
        ...

class UnlockItemActionWithResult(_UnlockItem):
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def doAsyncAction(self, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def __unlockAsyncItem(self, callback):
        ...

class InstallItemAction(BuyAction):
    _itemCD: Any
    _rootCD: Any
    def __init__(self, itemCD, rootCD):
        ...
    def doAction(self):
        ...
    # decorador original: @adisp_process
    def installItem(self, itemCD, rootCD, state):
        ...

class BuyAndInstallItemAction(InstallItemAction):
    _buyAndInstallItemProcessorCls = BuyAndInstallItemProcessor
    # decorador original: @adisp_process
    def doAction(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def buyAndInstallItem(self, itemCD, rootCD, state, callback):
        ...

class BuyAndInstallWithOptionalSellItemAction(BuyAndInstallItemAction):
    AUTO_SELL_KEY = 'sellPreviousModule'
    # decorador original: @adisp_process
    def doAction(self):
        ...
    def _getItemToBeReplaced(self, itemCD):
        ...
    # decorador original: @adisp_process
    def sellModule(self, moduleToSellCD):
        ...

class VehicleAutoFillLayoutAction(IGUIItemAction):
    __vehicle: Any
    def __init__(self, vehicle):
        ...
    # decorador original: @decorators.adisp_process(...)
    def doAction(self):
        ...
    @staticmethod
    def _showResult(result):
        ...

class AsyncGUIItemAction(IGUIItemAction):
    __slots__: tuple
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def doAction(self, callback):
        ...
    def isAsync(self):
        ...
    # decorador original: @adisp_async
    def _confirm(self, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def _action(self, callback):
        ...
    def _showResult(self, result):
        ...

class AmmunitionBuyAndInstall(AsyncGUIItemAction):
    __slots__: tuple
    __itemsCache: Any
    _vehicle: Any
    _changedItems: Any
    __confirmOnlyExchange: Any
    def __init__(self, vehicle, changeItems, confirmOnlyExchange=False):
        ...
    # decorador original: @adisp_async
    # decorador original: @future_async.wg_async
    def _confirm(self, callback):
        ...

class BuyAndInstallOptDevices(AmmunitionBuyAndInstall):
    __slots__: tuple
    def __init__(self, vehicle, confirmOnlyExchange=False):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def _action(self, callback):
        ...

class BuyAndInstallConsumables(AmmunitionBuyAndInstall):
    __slots__: tuple
    def __init__(self, vehicle, confirmOnlyExchange=False):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def _action(self, callback):
        ...

class BuyAndInstallBattleBoosters(AmmunitionBuyAndInstall):
    __slots__: tuple
    def __init__(self, vehicle, confirmOnlyExchange=False):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def _action(self, callback):
        ...

class BuyAndInstallShells(AsyncGUIItemAction):
    __slots__: tuple
    __itemsCache: Any
    __vehicle: Any
    __confirmOnlyExchange: Any
    __price: Any
    def __init__(self, vehicle, confirmOnlyExchange=False):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def _action(self, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @future_async.wg_async
    def _confirm(self, callback):
        ...

class VehicleRepairAction(AsyncGUIItemAction):
    __vehicle: Any
    __wrappedViewClass: Any
    __repairClazz: Any
    def __init__(self, vehicle, wrappedViewClass, repairClazz):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def _action(self, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @future_async.wg_async
    def _confirm(self, callback):
        ...

class BuyVehicleSlotAction(CachedItemAction):
    __itemsCache: Any
    __DEFAULT_FLOW = -1
    __NO_ENOUGH_CREDITS_FLOW = 0
    __NO_ENOUGH_GOLD_FLOW = 1
    __price: Any
    __currency: Any
    def __init__(self):
        ...
    # decorador original: @decorators.adisp_process(...)
    def doAction(self):
        ...
    def __checkMoney(self):
        ...

class BuyBerthsAction(CachedItemAction):
    __berthPrice: Any
    __countPacksBerths: Any
    def __init__(self, berthPrice, countPacksBerths, groupID=0, groupSize=1):
        ...
    # decorador original: @decorators.adisp_process(...)
    def doAction(self):
        ...

class TankmanRestoreAction(GroupedItemAction):
    __tankmanInvID: Any
    def __init__(self, tankmanInvID, groupID=0, groupSize=1):
        ...
    # decorador original: @decorators.adisp_process(...)
    def doAction(self):
        ...

class ConvertJunkTankmenAction(IGUIItemAction):
    # decorador original: @decorators.adisp_process(...)
    def doAction(self):
        ...

class TransferTankmanXPAction(IGUIItemAction):
    _sourceID: Any
    _targetID: Any
    def __init__(self, sourceID, targetID):
        ...
    # decorador original: @decorators.adisp_process(...)
    def doAction(self):
        ...

class BuyBoosterAction(CachedItemAction):
    booster: Any
    count: Any
    currency: Any
    doActivation: Any
    def __init__(self, booster, count, currency, doActivation=False):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def doAction(self, callback):
        ...

class ActivateBoosterAction(CachedItemAction):
    goodiesCache: Any
    booster: Any
    def __init__(self, booster):
        ...
    # decorador original: @adisp_process
    def doAction(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def canActivate(self, callback):
        ...
    def isReplacement(self):
        ...
    def isPremium(self, booster):
        ...
    def isUpgrade(self, newBooster, currentBooster):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def canReplace(self, callback):
        ...

class BuyAndActivateBooster(ActivateBoosterAction):
    goodiesCache: Any
    currency: Any
    __asyncEvent: Any
    def __init__(self, booster):
        ...
    def canBuyBooster(self, booster):
        ...
    # decorador original: @adisp_process
    def doAction(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def handleGoldPurchase(self, booster, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @future_async.wg_async
    def waitForClientUpdate(self, callback):
        ...
    def __checkBoosterCount(self, diff, _):
        ...

class ConvertBlueprintFragmentAction(IGUIItemAction):
    __vehicleCD: Any
    __fragmentPosition: Any
    __fragmentCount: Any
    __usedNationalFragments: Any
    def __init__(self, vehicleCD, fragmentCount=1, fragmentPosition=-1, usedNationalFragments=None):
        ...
    # decorador original: @decorators.adisp_process(...)
    def doAction(self):
        ...

class TmanAddSkillsAction(CachedItemAction):
    __skillRole: Any
    __skillNames: Any
    __utilizationType: Any
    __tmanInvID: Any
    def __init__(self, tmanInvID, utilizationType, skillRole, skillNames):
        ...
    # decorador original: @decorators.adisp_process(...)
    def doAction(self):
        ...

class FillAllTankmenSkillsAction(IGUIItemAction):
    _fillInBarracks: Any
    def __init__(self, fillInBarracks):
        ...
    # decorador original: @decorators.adisp_process(...)
    def doAction(self):
        ...

class ResetAllTankmenSkillsAction(IGUIItemAction):
    # decorador original: @decorators.adisp_process(...)
    def doAction(self):
        ...

class UseCrewBookAction(GroupedItemAction):
    __bookCD: Any
    __bookCount: Any
    __vehicleInvID: Any
    __tankmanInvID: Any
    def __init__(self, bookCD, vehicleInvID, bookCount, tankmanInvID, groupID=0, groupSize=1):
        ...
    # decorador original: @decorators.adisp_process(...)
    def doAction(self):
        ...

class UseFreeXpToTankman(GroupedItemAction):
    __tankmanInvID: Any
    __selectedXpForConvert: Any
    def __init__(self, selectedXpForConvert, tankmanInvID, groupID=0, groupSize=1):
        ...
    # decorador original: @decorators.adisp_process(...)
    def doAction(self):
        ...
    @staticmethod
    def _pushGroupedMessages(result):
        ...

class TankmanRetrainingAction(GroupedItemAction):
    __tankmanInvID: Any
    __vehicleIntCD: Any
    __tmanCostTypeIdx: Any
    __isRoleChange: Any
    def __init__(self, tankmanInvID, vehicleIntCD, tmanCostTypeIdx, isRoleChange, groupID=0, groupSize=1):
        ...
    # decorador original: @decorators.adisp_process(...)
    def doAction(self):
        ...

class TankmanChangeRoleAction(GroupedItemAction):
    __tankmanInvID: Any
    __vehicleIntCD: Any
    __role: Any
    __vehSlotIdx: Any
    def __init__(self, tankmanInvID, role, vehicleIntCD, vehSlotIdx=-1, groupID=0, groupSize=1):
        ...
    # decorador original: @decorators.adisp_process(...)
    def doAction(self):
        ...

class TankmanChangePassportAction(IGUIItemAction):
    __tankmanInvID: Any
    __firstNameID: Any
    __firstNameGroup: Any
    __lastNameID: Any
    __lastNameGroup: Any
    __iconID: Any
    __iconGroup: Any
    def __init__(self, tankmanInvID, firstNameID, firstNameGroup, lastNameID, lastNameGroup, iconID, iconGroup):
        ...
    # decorador original: @decorators.adisp_process(...)
    def doAction(self):
        ...

class TankmanUnloadAction(GroupedItemAction):
    __vehicleInvID: Any
    __vehicleSlotIdx: Any
    def __init__(self, vehicleInvID, vehicleSlotIdx, groupID=0, groupSize=1):
        ...
    # decorador original: @decorators.adisp_process(...)
    def doAction(self):
        ...

class TankmanEquipAction(GroupedItemAction):
    _tankmanInvID: Any
    _vehicleInvID: Any
    _vehicleSlotIdx: Any
    def __init__(self, tankmanInvID, vehicleInvID, vehicleSlotIdx, groupID=0, groupSize=1):
        ...
    # decorador original: @decorators.adisp_process(...)
    def doAction(self):
        ...

class QuickServiceTankmanEquipAction(TankmanEquipAction):
    # decorador original: @decorators.adisp_process(...)
    def doAction(self):
        ...

class TankmanDismissAction(CachedItemAction):
    __tankmanInvID: Any
    def __init__(self, tankmanInvID):
        ...
    # decorador original: @decorators.adisp_process(...)
    def doAction(self):
        ...

class TankmanBuyAndEquipAction(IGUIItemAction):
    _FREE_INDEX = 0
    __vehicle: Any
    __slot: Any
    def __init__(self, vehicle, slot):
        ...
    # decorador original: @decorators.adisp_process(...)
    def doAction(self):
        ...

class UpgradeOptDeviceAction(AsyncGUIItemAction):
    __itemsCache: Any
    __parent: Any
    __device: Any
    __vehicle: Any
    __setupIdx: Any
    __slotIdx: Any
    __onDeconstructed: Any
    def __init__(self, module, vehicle, setupIdx, slotIdx, onDeconstructed=None, parent=None):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def _action(self, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @future_async.wg_async
    def _confirm(self, callback):
        ...

class DeconstructOptDevice(AsyncGUIItemAction):
    __itemsCache: Any
    __module: Any
    __parent: Any
    __vehicle: Any
    __slotIdx: Any
    __deconstructStorageProcessor: Any
    __deconstructOnVehicleProcessor: Any
    def __init__(self, module, vehicle, slotIdx, parent=None):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def _action(self, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @future_async.wg_async
    def _confirm(self, callback):
        ...
    def _showResult(self, result):
        ...

class DeconstructMultOptDevice(AsyncGUIItemAction):
    _itemsCache: Any
    ctx: Any
    __sellItems: Any
    __vehItems: Any
    __upgradeDevicePair: Any
    def __init__(self, ctx):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def _action(self, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @future_async.wg_async
    def _confirm(self, callback):
        ...
    def __sortItemsKey(self, item):
        ...

class InstallBattleAbilities(AsyncGUIItemAction):
    __slots__: tuple
    __vehicle: Any
    __classVehs: Any
    __setupItems: Any
    def __init__(self, vehicle, classVehs=False, setupItems=None):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def _action(self, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @future_async.wg_async
    def _confirm(self, callback):
        ...

class FrontlineInstallReserves(AsyncGUIItemAction):
    __slots__: tuple
    __vehicle: Any
    __skillsInteractor: Any
    __applyForAllOfType: Any
    def __init__(self, vehicle, skillsInteractor=None):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def _action(self, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @future_async.wg_async
    def _confirm(self, callback):
        ...

class BuyBattleAbilities(AsyncGUIItemAction):
    __slots__: tuple
    __skillIDs: Any
    def __init__(self, skillIDs):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def _action(self, callback):
        ...

class RemoveOptionalDevice(AsyncGUIItemAction):
    __slots__: tuple
    __goodiesCache: Any
    __wotPlusController: Any
    __vehicle: Any
    __device: Any
    __slotID: Any
    __destroy: Any
    __forFitting: Any
    __everywhere: Any
    __removeProcessor: Any
    def __init__(self, vehicle, device, slotID, destroy=False, forFitting=False, everywhere=True):
        ...
    # decorador original: @adisp_async
    # decorador original: @future_async.wg_async
    def _confirm(self, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def _action(self, callback):
        ...

class ChangeSetupEquipmentsIndex(AsyncGUIItemAction):
    __slots__: tuple
    __vehicle: Any
    __groupID: Any
    __layoutIdx: Any
    def __init__(self, vehicle, groupID, layoutIdx):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def _action(self, callback):
        ...

class SwitchPrebattleAmmoPanelAvailabilityAction(AsyncGUIItemAction):
    __slots__: tuple
    __vehicle: Any
    __groupID: Any
    __enabled: Any
    def __init__(self, vehicle, groupID, enabled):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def _action(self, callback):
        ...

class DiscardPostProgressionPairs(AsyncGUIItemAction):
    __slots__: tuple
    __vehicle: Any
    __stepIDs: Any
    __modIDs: Any
    def __init__(self, vehicle, stepIDs, modIDs):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def _action(self, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @future_async.wg_async
    def _confirm(self, callback):
        ...

class PurchasePostProgressionPair(AsyncGUIItemAction):
    __slots__: tuple
    __vehicle: Any
    __stepID: Any
    __modificationID: Any
    def __init__(self, vehicle, stepID, modificationID):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def _action(self, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @future_async.wg_async
    def _confirm(self, callback):
        ...

class PurchasePostProgressionSteps(AsyncGUIItemAction):
    __slots__: tuple
    __vehicle: Any
    __stepIDs: Any
    def __init__(self, vehicle, stepIDs):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def _action(self, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @future_async.wg_async
    def _confirm(self, callback):
        ...

class SetEquipmentSlotType(AsyncGUIItemAction):
    __slots__: tuple
    __uiLoader: Any
    __vehicle: Any
    __slotID: Any
    def __init__(self, vehicle):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def _action(self, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @future_async.wg_async
    def _confirm(self, callback):
        ...

class PurchaseVehSkillTreeSteps(AsyncGUIItemAction):
    __itemsCache: Any
    __exchangeRatesProvider: Any
    __vehicle: Any
    __stepIDs: Any
    __responseDelayedCallback: Any
    __delay: Any
    def __init__(self, vehicle, stepIDs, responseDelayedCallback, delay):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def _action(self, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @future_async.wg_async
    def _confirm(self, callback):
        ...
    def __getXPShortage(self):
        ...
    def __formatValue(self, value):
        ...

def showMessage(scopeMsg, msg, item, msgType=..., **kwargs):
    ...
def showInventoryMsg(msg, item, msgType=..., **kwargs):
    ...
def showUnlockMsg(msg, item, msgType=..., **kwargs):
    ...
def showShopMsg(msg, item, msgType=..., **kwargs):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getGunCD(item, vehicle, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _needExchangeForBuy(price, itemsCache=None):
    ...
