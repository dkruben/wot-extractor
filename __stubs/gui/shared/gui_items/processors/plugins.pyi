# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/processors/plugins.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from collections import namedtuple as namedtuple
from functools import partial as partial
from future.utils import lrange as lrange, viewvalues as viewvalues
import BigWorld as BigWorld
import wg_async as future_async
from account_helpers import isLongDisconnectedFromCenter as isLongDisconnectedFromCenter
from account_helpers.AccountSettings import AccountSettings as AccountSettings
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from constants import IS_EDITOR as IS_EDITOR
from exchange.personal_discounts_constants import MAX_DISCOUNT_VALUE as MAX_DISCOUNT_VALUE
from gui import DialogsInterface as DialogsInterface, makeHtmlString as makeHtmlString, SystemMessages as SystemMessages
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.daapi.view.dialogs import CheckBoxDialogMeta as CheckBoxDialogMeta, DIALOG_BUTTON_ID as DIALOG_BUTTON_ID, HtmlMessageDialogMeta as HtmlMessageDialogMeta, HtmlMessageLocalDialogMeta as HtmlMessageLocalDialogMeta, I18nConfirmDialogMeta as I18nConfirmDialogMeta, I18nInfoDialogMeta as I18nInfoDialogMeta, IconDialogMeta as IconDialogMeta, IconPriceDialogMeta as IconPriceDialogMeta, PMConfirmationDialogMeta as PMConfirmationDialogMeta
from gui.Scaleform.daapi.view.dialogs.missions_dialogs_meta import UseAwardSheetDialogMeta as UseAwardSheetDialogMeta
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.SystemMessages import SM_TYPE as SM_TYPE
from gui.goodies.demount_kit import getDemountKitForOptDevice as getDemountKitForOptDevice
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.server_events.pm_constants import PM_SUIT_OP_PLUGIN_ERR_RESPONSE as PM_SUIT_OP_PLUGIN_ERR_RESPONSE, PAUSABLE_OPERATIONS_IDS as PAUSABLE_OPERATIONS_IDS
from gui.shared.formatters.tankmen import formatDeletedTankmanStr as formatDeletedTankmanStr
from gui.shared.gui_items import GUI_ITEM_ECONOMY_CODE as GUI_ITEM_ECONOMY_CODE, GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.Vehicle import VEHICLE_TAGS as VEHICLE_TAGS
from gui.shared.gui_items.artefacts import OptionalDevice as OptionalDevice
from gui.shared.gui_items.vehicle_equipment import EMPTY_ITEM as EMPTY_ITEM
from gui.shared.money import Currency as Currency
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.shared.utils.vehicle_collector_helper import isAvailableForPurchase as isAvailableForPurchase
from gui.veh_post_progression.models.ext_money import EXT_MONEY_UNDEFINED as EXT_MONEY_UNDEFINED, ExtendedGuiItemEconomyCode as ExtendedGuiItemEconomyCode
from gui.veh_post_progression.models.purchase import PurchaseProvider as PurchaseProvider
from helpers import dependency as dependency
from items import tankmen as tankmen
from items.components import skills_constants as skills_constants
from items.components.c11n_constants import SeasonType as SeasonType
from personal_missions import PM_BRANCH as PM_BRANCH
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController, IWotPlusController as IWotPlusController
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
from gui.impl.pub.dialog_window import DialogResult as DialogResult, DialogButtons as DialogButtons, SingleDialogResult as SingleDialogResult
from gui.impl.dialogs.gf_builders import ResDialogBuilder as ResDialogBuilder
from gui.goodies.goodie_items import DemountKit as DemountKit
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from post_progression_common import ACTION_TYPES as ACTION_TYPES
_logger: Any
PluginResult: Any

class ProcessorPlugin(object):
    itemsCache: Any
    type: Any
    isAsync: Any
    isEnabled: Any
    logWarnings: Any
    class TYPE(object):
        VALIDATOR = 0
        CONFIRMATOR = 1
    def __init__(self, pluginType, isAsync=False, isEnabled=True):
        ...

class SyncValidator(ProcessorPlugin):
    def __init__(self, isEnabled=True):
        ...
    def validate(self):
        ...
    def _validate(self):
        ...

class AsyncValidator(ProcessorPlugin):
    def __init__(self, isEnabled=True):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def validate(self, callback):
        ...
    # decorador original: @adisp_async
    def _validate(self, callback):
        ...

class AsyncConfirmator(ProcessorPlugin):
    def __init__(self, isEnabled=True):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def confirm(self, callback):
        ...
    # decorador original: @adisp_async
    def _confirm(self, callback):
        ...

class AwaitConfirmator(ProcessorPlugin):
    def __init__(self, isEnabled=True):
        ...
    # decorador original: @adisp_async
    # decorador original: @future_async.wg_async
    def confirm(self, callback):
        ...
    # decorador original: @future_async.wg_async
    def _confirm(self, callback):
        ...

class PreviousCrewValidator(SyncValidator):
    __vehicle: Any
    logWarnings: Any
    def __init__(self, vehicle):
        ...
    def _validate(self):
        ...

class AutoReturnValidator(SyncValidator):
    vehicle: Any
    logWarnings: Any
    def __init__(self, vehicle, isEnabled=True):
        ...
    def getCrewData(self):
        ...
    def _validate(self):
        ...

class VehicleValidator(SyncValidator):
    vehicle: Any
    isBroken: Any
    isLocked: Any
    isInInventory: Any
    def __init__(self, vehicle, setAll=True, prop=None, isEnabled=True):
        ...
    def _validate(self):
        ...

class VehicleRoleValidator(SyncValidator):
    vehicle: Any
    role: Any
    tankman: Any
    def __init__(self, vehicle, role, tankman, isEnabled=True):
        ...
    def _validate(self):
        ...

class VehicleSellValidator(SyncValidator):
    vehicle: Any
    def __init__(self, vehicle, isEnabled=True):
        ...
    def _validate(self):
        ...

class VehicleTradeInValidator(SyncValidator):
    vehicleToBuy: Any
    vehicleToTradeOff: Any
    def __init__(self, vehicleToBuy, vehicleToTradeOff, isEnabled=True):
        ...
    def _validate(self):
        ...

class VehicleLockValidator(SyncValidator):
    vehicle: Any
    def __init__(self, vehicle, setAll=True, isEnabled=True):
        ...
    def _validate(self):
        ...

class ModuleValidator(SyncValidator):
    module: Any
    def __init__(self, module):
        ...
    def _validate(self):
        ...

class ModuleTypeValidator(SyncValidator):
    module: Any
    allowableTypes: Any
    def __init__(self, module, allowableTypes):
        ...
    def _validate(self):
        ...

class ModuleConfigValidator(SyncValidator):
    module: Any
    def __init__(self, module):
        ...
    def _validate(self):
        ...

class EliteVehiclesValidator(SyncValidator):
    vehiclesCD: Any
    def __init__(self, vehiclesCD):
        ...
    def _validate(self):
        ...

class CollectibleVehiclesValidator(SyncValidator):
    __vehicleCD: Any
    def __init__(self, vehicleCD):
        ...
    def _validate(self):
        ...

class CompatibilityValidator(SyncValidator):
    vehicle: Any
    module: Any
    slotIdx: Any
    def __init__(self, vehicle, module, slotIdx=0):
        ...
    def _checkCompatibility(self):
        ...
    def _validate(self):
        ...

class CompatibilityInstallValidator(CompatibilityValidator):
    def _checkCompatibility(self):
        ...

class TurretCompatibilityInstallValidator(SyncValidator):
    vehicle: Any
    module: Any
    gunCD: Any
    def __init__(self, vehicle, module, gunCD=0):
        ...
    def _checkCompatibility(self):
        ...
    def _validate(self):
        ...

class CompatibilityRemoveValidator(CompatibilityValidator):
    def _checkCompatibility(self):
        ...

class MoneyValidator(SyncValidator):
    price: Any
    __byCurrencyError: Any
    def __init__(self, price, byCurrencyError=True):
        ...
    def _validate(self):
        ...

class WalletValidator(SyncValidator):
    def _validate(self):
        ...

class VehicleSellsLeftValidator(SyncValidator):
    vehicle: Any
    def __init__(self, vehicle, isEnabled=True):
        ...
    def _validate(self):
        ...

class FreeTankmanValidator(SyncValidator):
    def _validate(self):
        ...

class TankmanDropSkillValidator(SyncValidator):
    __tankman: Any
    def __init__(self, tankman, isEnabled=True):
        ...
    def _validate(self):
        ...

class GroupOperationsValidator(SyncValidator):
    AVAILABLE_OPERATIONS: Any
    group: Any
    operation: Any
    def __init__(self, group, operation=0, isEnabled=True):
        ...
    def _validate(self):
        ...

class DialogAbstractConfirmator(AsyncConfirmator):
    _dialogsInterfaceMethod: Any
    activeHandler: Any
    def __init__(self, activeHandler=None, isEnabled=True):
        ...
    def __del__(self):
        ...
    def _makeMeta(self):
        ...
    def _gfMakeMeta(self):
        ...
    # decorador original: @adisp_async
    def _showDialog(self, callback):
        ...
    def _activeHandler(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def _confirm(self, callback):
        ...

class I18nMessageAbstractConfirmator(DialogAbstractConfirmator):
    localeKey: Any
    ctx: Any
    def __init__(self, localeKey, ctx=None, activeHandler=None, isEnabled=True):
        ...

class MessageConfirmator(I18nMessageAbstractConfirmator):
    def _makeMeta(self):
        ...

class ModuleBuyerConfirmator(I18nMessageAbstractConfirmator):
    def _makeMeta(self):
        ...

class BuyAndInstallConfirmator(ModuleBuyerConfirmator):
    item: Any
    def __init__(self, localeKey, ctx=None, activeHandler=None, isEnabled=True, item=None):
        ...
    def _gfMakeMeta(self):
        ...

class HtmlMessageConfirmator(I18nMessageAbstractConfirmator):
    metaPath: Any
    metaKey: Any
    sourceKey: Any
    ctx: Any
    def __init__(self, localeKey, metaPath, metaKey, ctx=None, activeHandler=None, isEnabled=True, sourceKey='text'):
        ...
    def _makeMeta(self):
        ...

class BufferOverflowConfirmator(I18nMessageAbstractConfirmator):
    def __init__(self, ctx, isEnabled=True):
        ...
    def _makeMeta(self):
        ...

class IconPriceMessageConfirmator(I18nMessageAbstractConfirmator):
    def _makeMeta(self):
        ...

class DemountDeviceConfirmator(IconPriceMessageConfirmator):
    _goodiesCache: Any
    item: Any
    __vehicleToInstall: Any
    def __init__(self, isEnabled=True, item=None, vehicle=None):
        ...
    def _gfMakeMeta(self):
        ...

class IconMessageConfirmator(I18nMessageAbstractConfirmator):
    def _makeMeta(self):
        ...

class DestroyDeviceConfirmator(IconMessageConfirmator):
    item: Any
    def __init__(self, isEnabled=True, item=None):
        ...
    def _gfMakeMeta(self):
        ...

class MessageInformator(I18nMessageAbstractConfirmator):
    def _makeMeta(self):
        ...

class VehicleSlotsConfirmator(MessageInformator):
    def __init__(self, isEnabled=True):
        ...
    def _activeHandler(self):
        ...

class VehicleFreeLimitConfirmator(MessageInformator):
    vehicle: Any
    crewType: Any
    def __init__(self, vehicle, crewType):
        ...
    def _activeHandler(self):
        ...

class PMValidator(SyncValidator):
    quests: Any
    def __init__(self, quests):
        ...
    def _validate(self):
        ...

class PMPawnValidator(SyncValidator):
    quests: Any
    def __init__(self, quests):
        ...
    def _validate(self):
        ...

class _EventsCacheValidator(SyncValidator):
    eventsCache: Any

class PMLockedByVehicle(_EventsCacheValidator):
    _messageKeyPrefix: Any
    quests: Any
    _lockedChains: Any
    def __init__(self, branch, quests, messageKeyPrefix=''):
        ...
    def _validate(self):
        ...

class PMLockedByOperation(_EventsCacheValidator):
    _messageKeyPrefix: Any
    operationID: Any
    branch: Any
    _lockedChains: Any
    def __init__(self, operationID, branch, messageKeyPrefix='', isEnabled=True):
        ...
    def _validate(self):
        ...

class PMSlotsValidator(SyncValidator):
    __removedCount: Any
    _questsProgress: Any
    def __init__(self, questsProgress, isEnabled=True, removedCount=0):
        ...
    def _validate(self):
        ...

class PMRewardValidator(SyncValidator):
    quest: Any
    def __init__(self, quest):
        ...
    def _validate(self):
        ...

class PMFreeTokensValidator(_EventsCacheValidator):
    quest: Any
    _branch: Any
    def __init__(self, quest, isEnabled=True):
        ...
    def _validate(self):
        ...

class PMActiveCampaignValidator(_EventsCacheValidator):
    _quest: Any
    def __init__(self, quest, isEnabled=True):
        ...
    def _validate(self):
        ...

class PMActivateSameCampaignValidator(_EventsCacheValidator):
    _branch: Any
    def __init__(self, branch, isEnabled=True):
        ...
    def _validate(self):
        ...

class CheckBoxConfirmator(DialogAbstractConfirmator):
    __ACC_SETT_MAIN_KEY = 'checkBoxConfirmator'
    settingFieldName: Any
    def __init__(self, settingFieldName, activeHandler=None, isEnabled=True):
        ...
    def _activeHandler(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def _confirm(self, callback):
        ...
    def _getSetting(self):
        ...
    def _setSetting(self, value):
        ...

class TmenXPAcceleratorConfirmator(AwaitConfirmator):
    # decorador original: @future_async.wg_async
    def _confirm(self, callback):
        ...

class PMSelectConfirmator(CheckBoxConfirmator):
    quest: Any
    oldQuest: Any
    def __init__(self, quest, oldQuest, settingFieldName, activeHandler=None, isEnabled=True):
        ...
    def _makeMeta(self):
        ...

class PMProgressResetConfirmator(DialogAbstractConfirmator):
    quest: Any
    oldQuest: Any
    def __init__(self, quest, oldQuest, activeHandler=None, isEnabled=True):
        ...
    def _makeMeta(self):
        ...

class PMDismissWithProgressConfirmator(DialogAbstractConfirmator):
    quest: Any
    def __init__(self, quest, activeHandler=None, isEnabled=True):
        ...
    def _makeMeta(self):
        ...

class PMDiscardConfirmator(DialogAbstractConfirmator):
    curQuest: Any
    def __init__(self, curQuest, activeHandler=None, isEnabled=True):
        ...
    def _makeMeta(self):
        ...

class PMPawnConfirmator(DialogAbstractConfirmator):
    eventsCache: Any
    quest: Any
    _branch: Any
    def __init__(self, quest, activeHandler=None, isEnabled=True):
        ...
    def _activeHandler(self):
        ...
    def _makeMeta(self):
        ...

class DiscardSuitableOperationValidator(SyncValidator):
    isSuitableOperation: Any
    operationID: Any
    def __init__(self, isSuitableOperation, operationID):
        ...
    def _validate(self):
        ...

class PauseSuitableOperationValidator(SyncValidator):
    curQuest: Any
    def __init__(self, curQuest):
        ...
    def _validate(self):
        ...

class BoosterActivateValidator(SyncValidator):
    booster: Any
    def __init__(self, booster):
        ...
    def _validate(self):
        ...

class TankmanAddSkillValidator(SyncValidator):
    tmanDscr: Any
    utilizationType: Any
    skillName: Any
    def __init__(self, tankmanDscr, utilizationType, skillName):
        ...
    def _validate(self):
        ...

class TankmanAddSkillsValidator(TankmanAddSkillValidator):
    skillNames: Any
    skillName: Any
    def __init__(self, tmanDscr, utilizationType, skillNames):
        ...
    def _validate(self):
        ...

class IsLongDisconnectedFromCenter(SyncValidator):
    def _validate(self):
        ...

class VehicleCrewLockedValidator(SyncValidator):
    __vehicle: Any
    def __init__(self, vehicle):
        ...
    def _validate(self):
        ...

class TankmanLockedValidator(SyncValidator):
    _tankman: Any
    def __init__(self, tankman):
        ...
    def _validate(self):
        ...

class TankmanChangePassportValidator(TankmanLockedValidator):
    def _validate(self):
        ...

class BattleBoosterConfirmator(I18nMessageAbstractConfirmator):
    __notSuitableLocaleKey: Any
    __vehicle: Any
    __battleBooster: Any
    def __init__(self, localeKey, notSuitableLocaleKey, vehicle, battleBooster, isEnabled=True):
        ...
    def _activeHandler(self):
        ...
    def _makeMeta(self):
        ...

class BadgesValidator(SyncValidator):
    badges: Any
    def __init__(self, badges):
        ...
    def _validate(self):
        ...

class BattleBoosterValidator(SyncValidator):
    __lobbyContext: Any
    boosters: Any
    def __init__(self, boosters, isEnabled=True):
        ...
    def _validate(self):
        ...

class DismountForDemountKitValidator(SyncValidator):
    goodiesCache: Any
    vehicle: Any
    itemsForDemountKit: Any
    def __init__(self, vehicle, itemsForDemountKit):
        ...
    def _validate(self):
        ...

class FreeToDemountValidator(SyncValidator):
    _wotPlusCtrl: Any
    itemsFreeToDemount: Any
    def __init__(self, itemsFreeToDemount):
        ...
    def _validate(self):
        ...

class LayoutInstallValidator(SyncValidator):
    _vehicle: Any
    def __init__(self, vehicle, isEnabled=True):
        ...
    def _validate(self):
        ...
    def _getLayout(self):
        ...
    def _getInstalled(self):
        ...
    def _getItemType(self):
        ...

class OptionalDevicesInstallValidator(LayoutInstallValidator):
    def _getLayout(self):
        ...
    def _getInstalled(self):
        ...
    def _getItemType(self):
        ...

class BattleAbilitiesValidator(LayoutInstallValidator):
    __epicMetaGameCtrl: Any
    def _validate(self):
        ...
    def _getLayout(self):
        ...
    def _getInstalled(self):
        ...
    def _getItemType(self):
        ...

class ConsumablesInstallValidator(LayoutInstallValidator):
    def _getLayout(self):
        ...
    def _getInstalled(self):
        ...
    def _getItemType(self):
        ...

class ShellsInstallValidator(LayoutInstallValidator):
    def _getLayout(self):
        ...
    def _getInstalled(self):
        ...
    def _getItemType(self):
        ...

class BattleBoostersInstallValidator(LayoutInstallValidator):
    def _getLayout(self):
        ...
    def _getInstalled(self):
        ...
    def _getItemType(self):
        ...

class CustomizationPurchaseValidator(SyncValidator):
    outfitData: Any
    def __init__(self, outfitData):
        ...
    def _validate(self):
        ...

class PostProgressionStateValidator(SyncValidator):
    __slots__: tuple
    __vehicle: Any
    __skipRentalIsOver: Any
    def __init__(self, vehicle, skipRentalIsOver, isEnabled=True):
        ...
    def _validate(self):
        ...

class PostProgressionStepsValidator(SyncValidator):
    __slots__: tuple
    __vehicle: Any
    __stepIDs: Any
    __actionTypes: Any
    def __init__(self, vehicle, stepIDs, actionTypes, isEnabled=True):
        ...
    def _validate(self):
        ...

class PostProgressionChangeSetupValidator(SyncValidator):
    __slots__: tuple
    __vehicle: Any
    __groupID: Any
    def __init__(self, vehicle, groupID, isEnabled=True):
        ...
    def _validate(self):
        ...

class PostProgressionDiscardPairsValidator(SyncValidator):
    __slots__: tuple
    __vehicle: Any
    __stepIDs: Any
    def __init__(self, vehicle, stepIDs, isEnabled=True):
        ...
    def _validate(self):
        ...

class PostProgressionPurchasePairValidator(SyncValidator):
    __itemsCache: Any
    __slots__: tuple
    __vehicle: Any
    __stepID: Any
    __modificationID: Any
    def __init__(self, vehicle, stepID, modificationID, isEnabled=True):
        ...
    def _validate(self):
        ...

class PostProgressionPurchaseStepsValidator(SyncValidator):
    __itemsCache: Any
    __slots__: tuple
    __vehicle: Any
    __stepIDs: Any
    def __init__(self, vehicle, stepIDs, isEnabled=True):
        ...
    def _validate(self):
        ...

class PostProgressionSetSlotTypeValidator(SyncValidator):
    __slots__: tuple
    __vehicle: Any
    __slotID: Any
    def __init__(self, vehicle, slotID, isEnabled=True):
        ...
    def _validate(self):
        ...

class AsyncDialogConfirmator(AsyncConfirmator):
    __dialogMethod: Any
    __dialogArgs: Any
    __dialogKwargs: Any
    __dialogResult: Any
    def __init__(self, dialogMethod, *args, **kwargs):
        ...
    def getResult(self):
        ...
    # decorador original: @adisp_async
    def _confirm(self, callback):
        ...
    # decorador original: @future_async.wg_async
    def _makeConfirm(self, callback):
        ...

class ExchangeValidator(SyncValidator):
    __exchangeAmount: Any
    def __init__(self, exchangeAmount):
        ...
    def _validate(self):
        ...

class ExperiencePostProgressionValidator(SyncValidator):
    __itemsCache: Any
    __xppToConvert: Any
    def __init__(self, xppToConvert):
        ...
    def _validate(self):
        ...

def makeSuccess(**kwargs):
    ...
def makeError(msg='', **kwargs):
    ...
def showWarning(text, type=...):
    ...
def _wrapHtmlMessage(message):
    ...
