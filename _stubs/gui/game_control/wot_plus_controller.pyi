# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/wot_plus_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
from time import time as time
import typing as typing
from enum import Enum as Enum
import AccountCommands as AccountCommands
import BigWorld as BigWorld
import constants as constants
from BWUtil import AsyncReturn as AsyncReturn
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from Event import Event as Event
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import RENEWABLE_SUBSCRIPTION_ENTITLEMENTS as RENEWABLE_SUBSCRIPTION_ENTITLEMENTS
from debug_utils import LOG_ERROR_DEV as LOG_ERROR_DEV
from gui import SystemMessages as SystemMessages
from gui.Scaleform.daapi.view.lobby.missions.awards_formatters import CurtailingAwardsComposer as CurtailingAwardsComposer
from gui.game_control.wot_plus.service_record_customization.service_record_customization import ServiceRecordAssetManager as ServiceRecordAssetManager
from gui.game_control.wot_plus.wot_plus_assistant import WotPlusAssistant as WotPlusAssistant
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.page.header.wot_plus_subscription_model import WotPlusPeriodicityEnum as WotPlusPeriodicityEnum
from gui.platform.products_fetcher.user_subscriptions.controller import SubscriptionStatus as SubscriptionStatus
from gui.platform.products_fetcher.user_subscriptions.user_subscription import UserSubscription as UserSubscription, SUBSCRIPTION_CANCEL_STATUSES as SUBSCRIPTION_CANCEL_STATUSES, SubscriptionRequestPlatform as SubscriptionRequestPlatform
from gui.server_events import settings as settings
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES
from gui.server_events.bonuses import SimpleBonus as SimpleBonus
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from helpers.time_utils import ONE_MINUTE as ONE_MINUTE, ONE_DAY as ONE_DAY
from messenger.m_constants import SCH_CLIENT_MSG_TYPE as SCH_CLIENT_MSG_TYPE
from piggy_bank_common.settings_constants import PIGGY_BANK_PDATA_KEY as PIGGY_BANK_PDATA_KEY
from renewable_subscription_common.schema import renewableSubscriptionsConfigSchema as renewableSubscriptionsConfigSchema
from renewable_subscription_common.settings_constants import IDLE_CREW_XP_PDATA_KEY as IDLE_CREW_XP_PDATA_KEY, SUBSCRIPTION_DURATION_LENGTH as SUBSCRIPTION_DURATION_LENGTH, IDLE_CREW_VEH_INV_ID as IDLE_CREW_VEH_INV_ID, RS_EXPIRATION_TIME as RS_EXPIRATION_TIME, WotPlusState as WotPlusState, RS_TIER as RS_TIER, PRO_BOOST_PDATA_KEY as PRO_BOOST_PDATA_KEY, WotPlusTier as WotPlusTier, RS_SR_BACKGROUND as RS_SR_BACKGROUND, RS_SR_RIBBON as RS_SR_RIBBON, PRO_BOOST_ACTIVATION_TIME as PRO_BOOST_ACTIVATION_TIME, PRO_BOOSTED_VEHICLE as PRO_BOOSTED_VEHICLE
from renewable_subscription_common.settings_helpers import SubscriptionSettingsStorage as SubscriptionSettingsStorage
from shared_utils import findFirst as findFirst
from shared_utils.account_helpers.diff_utils import synchronizeDicts as synchronizeDicts
from skeletons.gui.game_control import IWotPlusController as IWotPlusController, ISteamCompletionController as ISteamCompletionController
from skeletons.gui.platform.product_fetch_controller import IUserSubscriptionsFetchController as IUserSubscriptionsFetchController
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.system_messages import ISystemMessages as ISystemMessages
from wg_async import wg_async as wg_async, wg_await as wg_await
from wotdecorators import condition as condition
from typing import Dict as Dict, Optional as Optional, Callable as Callable, Any as Any, List as List, Tuple as Tuple, Generator as Generator
from gui.shared.gui_items import ItemsCollection as ItemsCollection
from gui.game_control.account_completion import SteamCompletionController as SteamCompletionController
from gui.platform.products_fetcher.user_subscriptions.controller import UserSubscriptionsFetchController as UserSubscriptionsFetchController
from gui.platform.products_fetcher.user_subscriptions.fetch_result import UserSubscriptionFetchResult as UserSubscriptionFetchResult
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from renewable_subscription_common.optional_devices_usage_config import VehicleLoadout as VehicleLoadout
from Account import Account as Account
from gui.shared.gui_items.artefacts import OptionalDevice as OptionalDevice
_logger: _Any

class NotificationTypeTemplate(Enum):
    PASSIVE_XP: tuple
    GOLD_RESERVES: tuple
    DAILY_ATTENDACES: tuple
    FREE_DEMOUNT: tuple
    EXCLUDED_MAPS: tuple
    BATTLE_BONUSES: tuple
    BADGE: tuple
    ADDITIONAL_XP: tuple
    OPTIONAL_DEVICES_ASSISTANT: tuple
    CREW_ASSISTANT: tuple
    SERVICE_RECORD: tuple
    PRO_BOOST: tuple
    BATTLE_PASS: tuple
    @property
    def getEnable(self):
        ...
    @property
    def getDisable(self):
        ...

class _ProBoostMixin(object):
    ifAccount: _Any
    _delay: _Any
    onProBoostCooldownIsFinished: _Any
    def __init__(self):
        ...
    def startProBoostTimer(self, remainingTime):
        ...
    def stopProBoostTimer(self):
        ...
    def isProBoostTimerRunning(self):
        ...
    def _callOnCooldownIsFinishedEvent(self):
        ...

class WotPlusController(IWotPlusController, _ProBoostMixin, CallbackDelayer):
    _steamCompletionCtrl: _Any
    _itemsCache: _Any
    _systemMessages: _Any
    _userSubscriptionsFetchController: _Any
    ifAccount: _Any
    _SUBSCRIPTION_INVALIDATE_TIMEOUT: _Any
    _cache: _Any
    _account: _Any
    _state: _Any
    _billingPeriod: _Any
    _hasSteamSubscription: _Any
    _activeSubscriptionPlatform: _Any
    _assistant: _Any
    _srcAssetManager: _Any
    onDataChanged: _Any
    onAttendanceUpdated: _Any
    onPendingRentChanged: _Any
    onEnabledStatusChanged: _Any
    _invalidationInProgress: _Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def onLobbyStarted(self, _):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def _invalidateProBoost(self):
        ...
    def onDisconnected(self):
        ...
    def selectIdleCrewXPVehicle(self, vehicleInvID, successCallback=None, errorCallback=None):
        ...
    def activateProBoostOnVehicle(self, vehicleInvID=-1, successCallback=None, errorCallback=None):
        ...
    def hasSubscription(self):
        ...
    def getTier(self):
        ...
    def getBillingPeriod(self):
        ...
    def getProBoostedVehicleInvID(self):
        ...
    def getProBoostActivationTime(self):
        ...
    def isFreeToDemount(self, device):
        ...
    def getState(self):
        ...
    def hasSteamSubscription(self):
        ...
    def getActiveSubscriptionPlatform(self):
        ...
    def isSubscriptionBoughtViaPlatform(self):
        ...
    def getExpiryTime(self):
        ...
    def getNextBillingTime(self):
        ...
    def getStartTime(self):
        ...
    def getGoldReserve(self):
        ...
    def hasVehicleCrewIdleXP(self, vehicleInvID):
        ...
    def getVehicleIDWithIdleXP(self):
        ...
    def getExclusiveVehicles(self):
        ...
    def hasOptDeviceAssistLoadout(self, vehicle):
        ...
    def getOptDeviceAssistPresets(self, vehicle):
        ...
    def getMostPopularOptDevicesLoadout(self, vehicle):
        ...
    def isCrewAssistEnabled(self):
        ...
    def hasCrewAssistOrderSets(self, vehIntCD, tankmanRole):
        ...
    def getCrewAssistOrderSets(self, vehIntCD, tankmanRole):
        ...
    def validateCrewAssistOrderSets(self, orderSets):
        ...
    def getServiceRecordBackgroundID(self):
        ...
    def getServiceRecordRibbonID(self):
        ...
    def getSRCAssetManager(self):
        ...
    # decorador original: @ifAccount
    def toggleWotPlusDev(self, tier=...):
        ...
    # decorador original: @ifAccount
    def giveAttendanceRewardDev(self):
        ...
    # decorador original: @ifAccount
    def activateProBoostOnCurrentVehicleDev(self):
        ...
    # decorador original: @ifAccount
    def refreshProBoostCooldownDev(self):
        ...
    def setWotPlusStateDev(self, state):
        ...
    # decorador original: @ifAccount
    def simulateWGMoneyBalanceUpdate(self):
        ...
    # decorador original: @ifAccount
    def activateWotPlusDev(self, expirySecondsInFuture=..., entitlementName=...):
        ...
    def simulateNewGameDay(self):
        ...
    # decorador original: @ifAccount
    def setReservesDev(self, creditsVal, goldVal):
        ...
    # decorador original: @ifAccount
    def smashPiggyBankDev(self):
        ...
    def isWotPlusVisible(self):
        ...
    def onDailyAttendanceUpdate(self):
        ...
    def isDailyAttendanceQuest(self, questID):
        ...
    def getFormattedDailyAttendanceBonuses(self, bonuses):
        ...
    def processSwitchNotifications(self):
        ...
    def _notifyClient(self, lastSeenStatus, currentStatus, notifications):
        ...
    # decorador original: @wg_async
    def _resolveSubscriptionAndSteamState(self, clearCache=False):
        ...
    def shouldRedirectToSteam(self):
        ...
    def getSettingsStorage(self):
        ...
    def canBeProBoosted(self, vehicleCD):
        ...
    def _onClientUpdate(self, diff, _):
        ...
    def _onCmdResponseReceived(self, resultID, requestID, errorStr, errorMsg=None):
        ...
    def _onRenewableSubscriptionStatusChanged(self):
        ...
    def _scheduleInvalidation(self):
        ...
    def _cancelScheduledInvalidation(self):
        ...
    # decorador original: @wg_async
    def _invalidateSubscriptionState(self, stateChanged=False):
        ...
    def _invalidateCallback(self):
        ...
    def _refreshAssistance(self):
        ...
    def _onConfigModelUpdated(self, gpKey):
        ...
