# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/AwardController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import logging as logging
import typing as typing
import weakref as weakref
from builtins import filter as filter, range as range
from collections import OrderedDict as OrderedDict, namedtuple as namedtuple
from copy import deepcopy as deepcopy
from functools import partial as partial
from future.utils import iteritems as iteritems, itervalues as itervalues, listvalues as listvalues, viewitems as viewitems, viewvalues as viewvalues
from itertools import chain as chain
import BigWorld as BigWorld
from account_helpers.AccountSettings import AccountSettings as AccountSettings, RANKED_CURRENT_AWARDS_BUBBLE_YEAR_REACHED as RANKED_CURRENT_AWARDS_BUBBLE_YEAR_REACHED, RANKED_YEAR_POSITION as RANKED_YEAR_POSITION, SPEAKERS_DEVICE as SPEAKERS_DEVICE
from account_helpers.settings_core.settings_constants import SOUND as SOUND, OnceOnlyHints as OnceOnlyHints
from adisp import adisp_process as adisp_process
from gui.impl.dialogs.dialogs import showRenewableSubscriptionRewardDialog as showRenewableSubscriptionRewardDialog
from shared_utils import first as first, findFirst as findFirst, safeExecute as safeExecute
import ArenaType as ArenaType
import gui.awards.event_dispatcher as award_events
import personal_missions as personal_missions
import wg_async as wg_async
from PlayerEvents import g_playerEvents as g_playerEvents
from achievements20.cache import ALLOWED_ACHIEVEMENT_TYPES as ADVANCED_ACHIEVEMENT_TYPES
from battle_pass_common import BattlePassRewardReason as BattlePassRewardReason, get3DStyleProgressToken as get3DStyleProgressToken, isPostProgressionChapter as isPostProgressionChapter
from challenges_common import ChallengeMainRewardTypes as ChallengeMainRewardTypes, ChallengeTokenType as ChallengeTokenType, isChallengeQuest as isChallengeQuest, CHALLENGES_FAIL_QUEST_POSTFIX as CHALLENGES_FAIL_QUEST_POSTFIX
from battle_results import ARENA_BONUS_TYPE_TO_SM_TYPE_BATTLE_RESULT as ARENA_BONUS_TYPE_TO_SM_TYPE_BATTLE_RESULT
from blueprints.BlueprintTypes import BlueprintTypes as BlueprintTypes
from blueprints.FragmentTypes import getFragmentType as getFragmentType
from chat_shared import SYS_MESSAGE_TYPE as SYS_MESSAGE_TYPE
from collector_vehicle import CollectorVehicleConsts as CollectorVehicleConsts
from constants import DOSSIER_TYPE as DOSSIER_TYPE, EVENT_TYPE as EVENT_TYPE, INVOICE_ASSET as INVOICE_ASSET, PREMIUM_TYPE as PREMIUM_TYPE, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE, PENALTY_TYPES as PENALTY_TYPES
from dossiers2.custom.collector20 import COLLECTOR20_MEDAL_ID as COLLECTOR20_MEDAL_ID, COLLECTOR20_BADGE_IDS as COLLECTOR20_BADGE_IDS
from dossiers2.custom.records import DB_ID_TO_RECORD as DB_ID_TO_RECORD
from dossiers2.ui.achievements import BADGES_BLOCK as BADGES_BLOCK
from dossiers2.ui.layouts import PERSONAL_MISSIONS_GROUP as PERSONAL_MISSIONS_GROUP
from fairplay_violation_types import getPenaltyTypeAndViolationName as getPenaltyTypeAndViolationName, getFairplayViolationLocale as getFairplayViolationLocale, FAIRPLAY_EXCLUDED_ARENA_BONUS_TYPES as FAIRPLAY_EXCLUDED_ARENA_BONUS_TYPES
from goodies.goodie_constants import GOODIE_VARIETY as GOODIE_VARIETY, GOODIE_TARGET_TYPE as GOODIE_TARGET_TYPE
from gui import DialogsInterface as DialogsInterface, SystemMessages as SystemMessages
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.framework.managers.view_lifecycle_watcher import IViewLifecycleHandler as IViewLifecycleHandler, ViewLifecycleWatcher as ViewLifecycleWatcher
from gui.Scaleform.locale.MESSENGER import MESSENGER as MESSENGER
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as SYSTEM_MESSAGES
from gui.awards.event_dispatcher import showDynamicAward as showDynamicAward
from gui.battle_pass.battle_pass_constants import MIN_LEVEL as MIN_LEVEL
from gui.battle_pass.battle_pass_helpers import getStyleInfoForChapter as getStyleInfoForChapter
from gui.battle_pass.state_machine.state_machine_helpers import packStartEvent as packStartEvent, packToken as packToken, defaultEventMethod as defaultEventMethod, multipleBattlePassPurchasedEventMethod as multipleBattlePassPurchasedEventMethod
from gui.customization.shared import checkIsFirstProgressionDecalOnVehicle as checkIsFirstProgressionDecalOnVehicle
from gui.impl import backport as backport
from gui.impl.auxiliary.rewards_helper import getProgressiveRewardBonuses as getProgressiveRewardBonuses, BlueprintBonusTypes as BlueprintBonusTypes
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.loot_box_view.loot_congrats_types import LootCongratsTypes as LootCongratsTypes
from gui.impl.lobby.awards.items_collection_provider import MultipleProductAwardRewardsMainPacker as MultipleProductAwardRewardsMainPacker
from gui.impl.lobby.challenges.views_helpers import parseChallengeQuestId as parseChallengeQuestId
from gui.impl.lobby.clan_supply.bonus_packers import extractBonuses as extractBonuses
from gui.impl.lobby.clan_supply.clan_supply_helpers import showClanSupplyRewardWindow as showClanSupplyRewardWindow
from gui.impl.lobby.gf_notifications import pushGFNotification as pushGFNotification, GFNotificationTemplates as GFNotificationTemplates
from gui.impl.lobby.mapbox.map_box_awards_view import MapBoxAwardsViewWindow as MapBoxAwardsViewWindow
from gui.impl.lobby.personal_missions_30.personal_mission_constants import REWARDS_VIEW_TYPES as REWARDS_VIEW_TYPES
from gui.impl.lobby.winback.winback_reward_view import WinbackRewardWindow as WinbackRewardWindow
from gui.impl.pub.notification_commands import WindowNotificationCommand as WindowNotificationCommand
from gui.limited_ui.lui_rules_storage import LUI_RULES as LUI_RULES
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.prestige.prestige_helpers import hasVehiclePrestige as hasVehiclePrestige, showPrestigeRewardWindow as showPrestigeRewardWindow, needShowPrestigeRewardWindow as needShowPrestigeRewardWindow, openRewardScreens as openRewardScreens, needShowPrestigeMilestonesRewardWindow as needShowPrestigeMilestonesRewardWindow
from gui.ranked_battles import ranked_helpers as ranked_helpers
from gui.ranked_battles.constants import YEAR_AWARD_SELECTABLE_OPT_DEVICE_PREFIX as YEAR_AWARD_SELECTABLE_OPT_DEVICE_PREFIX
from gui.server_events import awards as awards, events_dispatcher as quests_events, recruit_helper as recruit_helper
from gui.server_events.bonuses import getServiceBonuses as getServiceBonuses, getMergedBonusesFromDicts as getMergedBonusesFromDicts, GoodiesBonus as GoodiesBonus, VehiclesBonus as VehiclesBonus
from gui.server_events.events_dispatcher import showCurrencyReserveAwardWindow as showCurrencyReserveAwardWindow, showPiggyBankRewardWindow as showPiggyBankRewardWindow, showBanWindow as showBanWindow, showPenaltyWindow as showPenaltyWindow, showWarningWindow as showWarningWindow
from gui.server_events.events_helpers import isACEmailConfirmationQuest as isACEmailConfirmationQuest, isDailyQuest as isDailyQuest, getIdxFromQuestID as getIdxFromQuestID, isPMAdvancedOperationFinishedQuest as isPMAdvancedOperationFinishedQuest
from gui.server_events.finders import CHAMPION_BADGES_BY_BRANCH as CHAMPION_BADGES_BY_BRANCH, CHAMPION_BADGE_AT_OPERATION_ID as CHAMPION_BADGE_AT_OPERATION_ID, PM_FINAL_TOKEN_QUEST_IDS_BY_OPERATION_ID as PM_FINAL_TOKEN_QUEST_IDS_BY_OPERATION_ID, getBranchByOperationId as getBranchByOperationId, NO_AWARD_LIST_HONOR_POSTFIX as NO_AWARD_LIST_HONOR_POSTFIX, NO_AWARD_LIST_FINISHED_QUEST as NO_AWARD_LIST_FINISHED_QUEST, isPMNoAwardListMilestone as isPMNoAwardListMilestone
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events, g_eventBus as g_eventBus
from gui.shared.account_settings_helper import AccountSettingsHelper as AccountSettingsHelper
from gui.shared.event_dispatcher import showBadgeInvoiceAwardWindow as showBadgeInvoiceAwardWindow, showBattlePass as showBattlePass, showBattlePassAwardsWindow as showBattlePassAwardsWindow, showBattlePassVehicleAwardWindow as showBattlePassVehicleAwardWindow, showChallengesAwardsWindow as showChallengesAwardsWindow, showDedicationRewardWindow as showDedicationRewardWindow, showEliteWindow as showEliteWindow, showMultiAwardWindow as showMultiAwardWindow, showProgressionRequiredStyleUnlockedWindow as showProgressionRequiredStyleUnlockedWindow, showProgressiveItemsRewardWindow as showProgressiveItemsRewardWindow, showProgressiveRewardAwardWindow as showProgressiveRewardAwardWindow, showRankedSeasonCompleteView as showRankedSeasonCompleteView, showRankedSelectableReward as showRankedSelectableReward, showRankedYearAwardWindow as showRankedYearAwardWindow, showRankedYearLBAwardWindow as showRankedYearLBAwardWindow, showSeniorityRewardAwardWindow as showSeniorityRewardAwardWindow, showSteamEmailConfirmRewardsView as showSteamEmailConfirmRewardsView, showSeniorityRewardVehiclesWindow as showSeniorityRewardVehiclesWindow, showCustomizationRarityAwardScreen as showCustomizationRarityAwardScreen, showCollector20RewardWindow as showCollector20RewardWindow, showPMAdvancedRewardsWindow as showPMAdvancedRewardsWindow
from gui.shared.events import CustomizationEvent as CustomizationEvent, PersonalMissionsEvent as PersonalMissionsEvent
from gui.shared.formatters.time_formatters import getTillTimeByResource as getTillTimeByResource
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, GUI_ITEM_TYPE_NAMES as GUI_ITEM_TYPE_NAMES
from gui.shared.gui_items.dossier.factories import getAchievementFactory as getAchievementFactory
from gui.shared.system_factory import registerAwardControllerHandlers as registerAwardControllerHandlers, collectAwardControllerHandlers as collectAwardControllerHandlers
from gui.shared.utils import isPopupsWindowsOpenDisabled as isPopupsWindowsOpenDisabled
from gui.sounds.sound_constants import SPEAKERS_CONFIG as SPEAKERS_CONFIG
from helpers import dependency as dependency, i18n as i18n
from items import ITEM_TYPE_INDICES as ITEM_TYPE_INDICES, vehicles as vehicles_core
from items.components.c11n_constants import Rarity as Rarity
from items.components.crew_books_constants import CREW_BOOK_DISPLAYED_AWARDS_COUNT as CREW_BOOK_DISPLAYED_AWARDS_COUNT
from messenger.formatters import TimeFormatter as TimeFormatter
from messenger.formatters.service_channel import TelecomReceivedInvoiceFormatter as TelecomReceivedInvoiceFormatter, ChallengesAchievesFormatter as ChallengesAchievesFormatter
from messenger.m_constants import SCH_CLIENT_MSG_TYPE as SCH_CLIENT_MSG_TYPE
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from nations import NAMES as NAMES
from potapov_quests import isWithoutAwardListBranchQuest as isWithoutAwardListBranchQuest
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.battle_matters import IBattleMattersController as IBattleMattersController
from skeletons.gui.challenges import IChallengesController as IChallengesController
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import IAwardController as IAwardController, IBattlePassController as IBattlePassController, ILimitedUIController as ILimitedUIController, IMapboxController as IMapboxController, IRankedBattlesController as IRankedBattlesController, IWotPlusController as IWotPlusController, ISeniorityAwardsController as ISeniorityAwardsController, IWinbackController as IWinbackController
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.impl import IGuiLoader as IGuiLoader, INotificationWindowController as INotificationWindowController
from skeletons.gui.platform.catalog_service_controller import IPurchaseCache as IPurchaseCache
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from skeletons.gui.sounds import ISoundsController as ISoundsController
from skeletons.gui.system_messages import ISystemMessages as ISystemMessages
from typing import Tuple as Tuple, Union as Union, Dict as Dict, Literal as Literal, Optional as Optional, Container as Container
from messenger.proto.bw.wrappers import _ServiceChannelData as _ServiceChannelData
from gui.platform.catalog_service.controller import _PurchaseDescriptor as _PurchaseDescriptor
_logger: Any
_POPUP_RECORDS = 'popUpRecords'

class QUEST_AWARD_POSTFIX(object):
    CREW_BOOKS = 'awardcrewbook'

class _NonOverlappingStarBehaviorDescr(object):
    __NON_OVERLAPPING_START_BEHAVIOR: tuple
    @classmethod
    def hasAnyOverlap(cls):
        ...
    def __set__(self, obj, value_):
        ...
    def __get__(self, obj, type=None):
        ...

class _NonOverlappingViewsLifecycleHandler(IViewLifecycleHandler):
    __NON_OVERLAPPING_VIEWS: tuple
    __openedViews: Any
    __postponeAwardsCallback: Any
    __handlePostponedCallback: Any
    def __init__(self, postponeAwardsCallback, handlePostponedCallback):
        ...
    def onViewCreated(self, view):
        ...
    def onViewDestroyed(self, view):
        ...

class AwardController(IAwardController, IGlobalListener):
    appLoader: Any
    eventsCache: Any
    settingsCore: Any
    hasBehaviorOnStart: Any
    __handlers: Any
    _delayedHandlers: Any
    __isLobbyLoaded: Any
    __postpone: Any
    __viewLifecycleWatcher: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def postponeOrCall(self, handler, ctx):
        ...
    def handlePostponed(self, *_):
        ...
    def canShow(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def onConnected(self):
        ...
    def onDisconnected(self):
        ...
    def onLobbyInited(self, *args):
        ...
    def onPlayerStateChanged(self, entity, roster, accountInfo):
        ...
    def onUnitFlagsChanged(self, flags, timeLeft):
        ...
    def onDequeued(self, queueType, *args):
        ...
    def onSettingsChanged(self, diff):
        ...
    def __postponeAwards(self, value):
        ...

class AwardHandler(object):
    itemsCache: Any
    _awardCtrl: Any
    def __init__(self, awardCtrl):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def handle(self, *args):
        ...
    def isShowCongrats(self, quest):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx):
        ...

class ServiceChannelHandler(AwardHandler):
    eventsCache: Any
    __type: Any
    def __init__(self, channelType, awardCtrl):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def _needToShowAward(self, ctx):
        ...

class MultiTypeServiceChannelHandler(ServiceChannelHandler):
    __types: Any
    def __init__(self, handledTypes, awardCtrl):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx):
        ...

class EliteWindowHandler(AwardHandler):
    __gui: Any
    def init(self):
        ...
    def fini(self):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx):
        ...

class PunishWindowHandler(ServiceChannelHandler):
    __notificationMgr: Any
    def __init__(self, awardCtrl):
        ...
    @property
    def channelType(self):
        ...
    def _showAward(self, ctx):
        ...
    def _showBanWindow(self, arenaTypeID, arenaTimeStr, banDurationStr):
        ...
    def _showPenaltyWindow(self, arenaTypeID, arenaTimeStr, punishmentReason, isAFKPenalty):
        ...
    def _showWarningWindow(self, arenaTypeID, arenaTimeStr, punishmentReason, isAFKPenalty):
        ...

class PersonalMissionBonusHandler(ServiceChannelHandler):
    def __init__(self, awardCtrl):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx):
        ...

class PersonalMissionWindowAfterBattleHandler(ServiceChannelHandler):
    def __init__(self, awardCtrl):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx):
        ...

class TokenQuestsWindowHandler(ServiceChannelHandler):
    seniorityAwardCtrl: Any
    def __init__(self, awardCtrl):
        ...
    def _showAward(self, ctx):
        ...
    @staticmethod
    def _showWindow(quest, context):
        ...

class SeniorityAwardsWindowHandler(ServiceChannelHandler):
    eventsCache: Any
    seniorityAwardCtrl: Any
    __completedQuests: Any
    __mergedRewards: Any
    __questsData: Any
    __callback: Any
    def __init__(self, awardCtrl):
        ...
    def fini(self):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx=None):
        ...
    def __update(self):
        ...
    def __onSAConfigReady(self):
        ...
    def __onQuestsReceived(self):
        ...

class PiggyBankOpenHandler(ServiceChannelHandler):
    itemsCache: Any
    def __init__(self, awardCtrl):
        ...
    def _showAward(self, ctx):
        ...
    @staticmethod
    def _showWindow(creditsEarned, goldEarned, isPremium):
        ...
    @staticmethod
    def _canShowWotPlusWindow(goldEarned):
        ...
    def __isPremiumEnable(self):
        ...

class RenewableSubscriptionHandler(ServiceChannelHandler):
    wotPlusCtrl: Any
    __types: Any
    def __init__(self, awardCtrl):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx):
        ...

class MarkByInvoiceHandler(ServiceChannelHandler):
    def __init__(self, awardCtrl):
        ...
    def _showAward(self, ctx):
        ...
    @staticmethod
    def _showMessage(tokenCount):
        ...

class MarkByQuestHandler(MultiTypeServiceChannelHandler):
    def __init__(self, awardCtrl):
        ...
    def _showAward(self, ctx):
        ...
    def __showMessage(self, tokenCount):
        ...
    @staticmethod
    def __extractCount(message):
        ...

class CrewBooksQuestHandler(MultiTypeServiceChannelHandler):
    _qId: Any
    def __init__(self, awardCtrl):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx):
        ...

class CustomizationRewardHandler(MultiTypeServiceChannelHandler):
    __service: Any
    __settingsCore: Any
    _hangarSpace: Any
    _SYS_MESSAGE_TYPES: tuple
    ElementInfo: Any
    _delayedElements: Any
    _rewardScreenInProgress: Any
    def __init__(self, awardCtrl):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    @staticmethod
    def sortedMethod(elemInfo):
        ...
    def _showAward(self, ctx):
        ...
    def _onSpaceCreate(self):
        ...
    @staticmethod
    def _isAllowedByQuest(questID):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _getAttachments(self, ctx):
        ...
    def _showReward(self):
        ...
    def _show(self, element, isFirstEntry):
        ...
    def _onInterruptClosed(self, *_):
        ...

class RecruitHandler(ServiceChannelHandler):
    __questTypes: Any
    def __init__(self, awardCtrl):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx):
        ...
    @staticmethod
    def _showWindow(eventKey):
        ...

class MotiveQuestsWindowHandler(ServiceChannelHandler):
    def __init__(self, awardCtrl):
        ...
    def _showAward(self, ctx):
        ...

class PrestigeAwardWindowHandler(ServiceChannelHandler):
    def __init__(self, awardCtrl):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx):
        ...

class PrestigeMilestonesAwardWindowHandler(ServiceChannelHandler):
    __service: Any
    __settingsCore: Any
    def __init__(self, awardCtrl):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx):
        ...
    @staticmethod
    def __parseMessage(message):
        ...
    @staticmethod
    def __parseReward(message):
        ...

class BattleQuestsAutoWindowHandler(MultiTypeServiceChannelHandler):
    _BRANCHES_SHOW_ORDER: dict
    def __init__(self, awardCtrl):
        ...
    def _getSysMsgTypes(self):
        ...
    def _showAward(self, ctx):
        ...
    @staticmethod
    def _showWindow(quest, context):
        ...
    @staticmethod
    def _isAppropriate(quest):
        ...
    @staticmethod
    def _getContext(uniqueQuestID, completedQuests, completedQuestUniqueIDs):
        ...
    def __questShowOrderKey(self, completedQuest):
        ...

class PersonalMissionAutoWindowHandler(BattleQuestsAutoWindowHandler):
    @staticmethod
    def _showWindow(quest, context):
        ...
    def _needToShowAward(self, ctx):
        ...
    @staticmethod
    def _isAppropriate(quest):
        ...
    @staticmethod
    def _getContext(uniqueQuestID, completedQuests, completedQuestUniqueIDs):
        ...

class PersonalMissionByAwardListHandler(PersonalMissionAutoWindowHandler):
    def _getSysMsgTypes(self):
        ...
    def _needToShowAward(self, ctx):
        ...
    @staticmethod
    def _getContext(uniqueQuestID, completedQuests, completedQuestUniqueIDs):
        ...

class PersonalMissionOperationAwardHandler(BattleQuestsAutoWindowHandler):
    __CHAMPION_BADGES_IDS: Any
    __IGNORED_OPERATIONS: Any
    __postponedAwards: Any
    __openedOperationsAwards: Any
    __delayedWindows: Any
    def __init__(self, awardCtrl):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def _getSysMsgTypes(self):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx):
        ...
    def _showWindow(self, quest, context):
        ...
    @staticmethod
    def __isChampionBadgeQuest(qID, operationID):
        ...
    def __onAwardScreenClose(self, event):
        ...
    def __getFinalTokenQuestIdsByOperationId(self):
        ...

class PersonalMissionOperationUnlockedHandler(BattleQuestsAutoWindowHandler):
    OPERATION_COMPLETION_IDS: dict
    def _getSysMsgTypes(self):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx):
        ...
    @staticmethod
    def _showWindow(quest, context):
        ...

class TelecomHandler(ServiceChannelHandler):
    def __init__(self, awardCtrl):
        ...
    @staticmethod
    def __getVehileDesrs(data):
        ...
    def _showAward(self, ctx):
        ...

class RankedQuestsHandler(ServiceChannelHandler):
    __rankedController: Any
    def __init__(self, awardCtrl):
        ...
    def _showAward(self, ctx):
        ...
    def __showSeasonAward(self, quest, data):
        ...
    def __showFinalAward(self, questIDs, data):
        ...
    def __showFinalLeaderAward(self, _, data):
        ...
    def __processQuests(self, questIDs, data, handler):
        ...

class SoundDeviceHandler(AwardHandler):
    soundsCtrl: Any
    settingsCore: Any
    def start(self):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx):
        ...
    def __callback(self, result):
        ...

class ProgressiveRewardHandler(ServiceChannelHandler):
    def __init__(self, awardCtrl):
        ...
    def _showAward(self, ctx):
        ...

class ProgressiveItemsRewardHandler(ServiceChannelHandler):
    _gui: Any
    _hangarSpace: Any
    _itemsCache: Any
    __limitedUIController: Any
    __message: Any
    def __init__(self, awardCtrl):
        ...
    def fini(self):
        ...
    def _showAward(self, ctx):
        ...
    def __show(self):
        ...

class VehicleCollectorAchievementHandler(ServiceChannelHandler):
    _PATTERN = CollectorVehicleConsts.COLLECTOR_MEDAL_PREFIX
    __nationAwards: Any
    __isCollectionAssembled: Any
    def __init__(self, awardCtrl):
        ...
    def fini(self):
        ...
    def _needToShowAward(self, ctx):
        ...
    def __setAwards(self, ctx):
        ...
    def __isAwardsReceived(self):
        ...
    def _showAward(self, ctx):
        ...
    def __showNationalCollectorAward(self):
        ...
    def __showVehicleCollectorOfEverythingAward(self):
        ...
    def __clear(self):
        ...
    def __isNationCorrect(self, nationID):
        ...

class BattlePassRewardHandler(ServiceChannelHandler):
    __battlePass: Any
    __notificationMgr: Any
    def __init__(self, awardCtrl):
        ...
    def _showAward(self, ctx):
        ...

class BattlePassStyleReceivedHandler(ServiceChannelHandler):
    __battlePassController: Any
    __itemsCache: Any
    __chapter: Any
    def __init__(self, awardCtrl):
        ...
    def fini(self):
        ...
    def _showAward(self, ctx):
        ...
    def __showAward(self, *_):
        ...

class BattlePassBuyEmptyHandler(ServiceChannelHandler):
    __battlePass: Any
    __gui: Any
    __MULTIPLE_CHAPTER = 0
    def __init__(self, awardCtrl):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx):
        ...
    def __onAwardShown(self, chapterID):
        ...
    def __isBattlePassOpen(self):
        ...

class BattlePassCapHandler(ServiceChannelHandler):
    __battlePassController: Any
    def __init__(self, awardCtrl):
        ...
    def _showAward(self, ctx):
        ...

class DynamicBonusHandler(ServiceChannelHandler):
    AVAILABLE_TAGS: list
    def __init__(self, awardCtrl):
        ...
    def _showAward(self, ctx):
        ...

class DedicationReward(ServiceChannelHandler):
    itemsCache: Any
    _hangarSpace: Any
    __pending: Any
    __locked: Any
    def __init__(self, awardCtrl):
        ...
    def fini(self):
        ...
    def _showAward(self, ctx):
        ...
    def __onSpaceCreated(self):
        ...
    def _showDedicationReward(self, rewards, data):
        ...
    def __processOrHold(self, args):
        ...
    def __unlock(self):
        ...

class BadgesInvoiceHandler(ServiceChannelHandler):
    def __init__(self, awardCtrl):
        ...
    def _showAward(self, ctx):
        ...
    @staticmethod
    def _showWindow(badge):
        ...

class MapboxProgressionRewardHandler(AwardHandler):
    __notificationMgr: Any
    __eventsCache: Any
    __mapboxCtrl: Any
    def init(self):
        ...
    def fini(self):
        ...
    def _needToShowAward(self, ctx):
        ...
    # decorador original: @wg_async.wg_async
    def _showAward(self, ctx):
        ...

class PurchaseHandler(ServiceChannelHandler):
    __purchaseCache: Any
    def __init__(self, awardCtrl):
        ...
    def _showAward(self, ctx):
        ...
    # decorador original: @adisp_process
    def __tryToShowAwards(self, invoiceData):
        ...

class ClanSupplyPurchaseHandler(ServiceChannelHandler):
    __purchaseCache: Any
    REGULAR_TAG = 'clansupply.map_product'
    ELITE_TAG = 'clansupply.map_product_elite'
    CLAN_SUPPLY_TAGS: tuple
    def __init__(self, awardCtrl):
        ...
    def _showAward(self, ctx):
        ...
    def _needToShowAward(self, ctx):
        ...
    # decorador original: @wg_async.wg_async
    def __tryToShowAwards(self, invoiceData, isElite):
        ...

class BattleMattersQuestsHandler(MultiTypeServiceChannelHandler):
    __battleMattersCtrl: Any
    __systemMessages: Any
    def __init__(self, awardCtrl):
        ...
    def _showAward(self, ctx, clientCtx=None):
        ...
    def _needToShowAward(self, ctx):
        ...

class DailyQuestHandlerBase(MultiTypeServiceChannelHandler):
    notificationMgr: Any
    winbackController: Any
    quests: Any
    messages: Any
    def __init__(self, awardCtrl):
        ...
    def fini(self):
        ...
    def clear(self):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _filterQuests(self):
        ...
    def _filterDailyQuests(self):
        ...
    def __fillCompletedQuests(self, message):
        ...
    def __checkQuestsData(self):
        ...
    def __onEventCacheSyncCompleted(self, *_):
        ...

class DailyQuestHandler(DailyQuestHandlerBase):
    def _filterQuests(self):
        ...
    def _showAward(self, ctx):
        ...

class WinbackQuestHandler(DailyQuestHandlerBase):
    __goodiesCache: Any
    __systemMessages: Any
    _MAX_COUNT_BONUSES = 4
    def _filterQuests(self):
        ...
    def _showAward(self, ctx):
        ...
    def _splitBonuses(self):
        ...
    def _getMainBonusesList(self, bonuses):
        ...
    def _getDiscounts(self, bonuses):
        ...
    def _calculateMainBonuses(self, bonuses):
        ...

class EmailConfirmationQuestHandler(ServiceChannelHandler):
    __completedQuest: Any
    def __init__(self, awardCtrl):
        ...
    def fini(self):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx=None):
        ...

class PMAdvancedOperationAwardHandler(MultiTypeServiceChannelHandler):
    def __init__(self, awardCtrl):
        ...
    def _showAward(self, ctx, clientCtx=None):
        ...
    def _needToShowAward(self, ctx):
        ...

class PMAdvancedVehicleDetailHandler(MultiTypeServiceChannelHandler):
    def __init__(self, awardCtrl):
        ...
    def _showAward(self, ctx, clientCtx=None):
        ...
    def _needToShowAward(self, ctx):
        ...

class Collector20RewardHandler(ServiceChannelHandler):
    __guiLoader: Any
    __limitedUIController: Any
    __systemMessages: Any
    __ALLOWED_RECORDS: Any
    __awards: Any
    def __init__(self, awardCtrl):
        ...
    def fini(self):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx):
        ...
    def __clear(self):
        ...
    def __isBuyVehicleViewLoaded(self):
        ...
    def __setAwards(self, ctx):
        ...
    def __showCollector20RewardWindow(self, *_):
        ...

class ChallengesFailHandler(ServiceChannelHandler):
    __challenges: Any
    def __init__(self, awardCtrl):
        ...
    def _showAward(self, ctx):
        ...

class ChallengesWinHandler(ServiceChannelHandler):
    __challenges: Any
    def __init__(self, awardCtrl):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx):
        ...

def _showDailyQuestEpicRewardScreen(quest, context):
    ...
def _getBlueprintActualBonus(data, quest):
    ...
