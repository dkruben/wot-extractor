# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/notification/actions_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import defaultdict as defaultdict
from past.builtins import long as long
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from battle_pass_common import isPostProgressionChapter as isPostProgressionChapter
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE, PENALTY_TYPES as PENALTY_TYPES, FAIRPLAY_VIOLATION_SYS_MSG_SAVED_DATA as FAIRPLAY_VIOLATION_SYS_MSG_SAVED_DATA, IS_CHINA as IS_CHINA
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR
from gui import DialogsInterface as DialogsInterface, SystemMessages as SystemMessages, makeHtmlString as makeHtmlString
from wg_async import wg_async as wg_async, wg_await as wg_await
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.customization.shared import CustomizationTabs as CustomizationTabs
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getIntegratedAuctionUrl as getIntegratedAuctionUrl, getWotPlusShopUrl as getWotPlusShopUrl
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.genConsts.BARRACKS_CONSTANTS import BARRACKS_CONSTANTS as BARRACKS_CONSTANTS
from gui.Scaleform.genConsts.FORTIFICATION_ALIASES import FORTIFICATION_ALIASES as FORTIFICATION_ALIASES
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES as QUESTS_ALIASES
from gui.battle_results import RequestResultsContext as RequestResultsContext
from gui.clans.clan_helpers import showAcceptClanInviteDialog as showAcceptClanInviteDialog
from gui.customization.constants import CustomizationModeSource as CustomizationModeSource, CustomizationModes as CustomizationModes
from gui.impl import backport as backport
from gui.impl.auxiliary.crew_books_helper import crewBooksViewedCache as crewBooksViewedCache
from gui.impl.gen import R as R
from gui.impl.lobby.achievements.profile_utils import createAdvancedAchievementsCatalogInitAchievementIDs as createAdvancedAchievementsCatalogInitAchievementIDs
from gui.impl.lobby.battle_pass.common import isExtraChapterSeen as isExtraChapterSeen
from gui.lootbox_system.base.common import ViewID as ViewID, Views as Views
from gui.platform.base.statuses.constants import StatusTypes as StatusTypes
from gui.prb_control import prbDispatcherProperty as prbDispatcherProperty, prbInvitesProperty as prbInvitesProperty
from gui.prestige.prestige_helpers import showPrestigeOnboardingWindow as showPrestigeOnboardingWindow, showPrestigeVehicleStats as showPrestigeVehicleStats
from gui.ranked_battles import ranked_helpers as ranked_helpers
from gui.server_events.events_dispatcher import showMissionsMapboxProgression as showMissionsMapboxProgression, showPersonalMission as showPersonalMission, showBanWindow as showBanWindow, showPenaltyWindow as showPenaltyWindow, showWarningWindow as showWarningWindow, showBattleMatters as showBattleMatters, showChallenges as showChallenges
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, actions as actions, event_dispatcher as shared_events, events as events, g_eventBus as g_eventBus
from gui.shared.event_dispatcher import hideWebBrowserOverlay as hideWebBrowserOverlay, showBattlePass as showBattlePass, showBlueprintsSalePage as showBlueprintsSalePage, showCollectionAwardsWindow as showCollectionAwardsWindow, showCollectionWindow as showCollectionWindow, showCollectionsMainPage as showCollectionsMainPage, showDelayedReward as showDelayedReward, showEpicBattlesAfterBattleWindow as showEpicBattlesAfterBattleWindow, showProgressiveRewardWindow as showProgressiveRewardWindow, showRankedYearAwardWindow as showRankedYearAwardWindow, showShop as showShop, showSteamConfirmEmailOverlay as showSteamConfirmEmailOverlay, showWinbackSelectRewardView as showWinbackSelectRewardView, showBarracks as showBarracks, showSeniorityRewardVehiclesWindow as showSeniorityRewardVehiclesWindow, showAdvancedAchievementsView as showAdvancedAchievementsView, showTrophiesView as showTrophiesView, showAdvancedAchievementsCatalogView as showAdvancedAchievementsCatalogView, showExchangeGoldWindow as showExchangeGoldWindow, showExchangeFreeXPWindow as showExchangeFreeXPWindow, showCrewPostProgressionView as showCrewPostProgressionView, showPersonalMissionMainWindow as showPersonalMissionMainWindow, showPetStorageView as showPetStorageView, showSubscriptionsPage as showSubscriptionsPage
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.processors.common import ClaimRewardForPostProgression as ClaimRewardForPostProgression
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from gui.shared.system_factory import registerNotificationsActionsHandlers as registerNotificationsActionsHandlers, collectAllNotificationsActionsHandlers as collectAllNotificationsActionsHandlers
from gui.shared.utils import decorators as decorators
from gui.wgcg.clan import contexts as clan_ctxs
from gui.wgnc import g_wgncProvider as g_wgncProvider
from helpers import dependency as dependency
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE
from messenger.proto import proto_getter as proto_getter
from notification.settings import NOTIFICATION_BUTTON_STATE as NOTIFICATION_BUTTON_STATE, NOTIFICATION_TYPE as NOTIFICATION_TYPE
from predefined_hosts import g_preDefinedHosts as g_preDefinedHosts
from shared_utils import first as first
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from skeletons.gui.challenges import IChallengesController as IChallengesController
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import IBattlePassController as IBattlePassController, IBattleRoyaleController as IBattleRoyaleController, IBrowserController as IBrowserController, ICollectionsSystemController as ICollectionsSystemController, IMapboxController as IMapboxController, IRankedBattlesController as IRankedBattlesController, ISeniorityAwardsController as ISeniorityAwardsController, IWinbackController as IWinbackController, ILootBoxSystemController as ILootBoxSystemController
from skeletons.gui.impl import INotificationWindowController as INotificationWindowController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.platform.wgnp_controllers import IWGNPSteamAccRequestController as IWGNPSteamAccRequestController
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from skeletons.gui.web import IWebController as IWebController
from soft_exception import SoftException as SoftException
from uilogging.advanced_achievement.logger import AdvancedAchievementLogger as AdvancedAchievementLogger
from uilogging.advanced_achievement.logging_constants import AdvancedAchievementButtons as AdvancedAchievementButtons, AdvancedAchievementViewKey as AdvancedAchievementViewKey
from uilogging.seniority_awards.loggers import VehicleSelectionNotificationLogger as VehicleSelectionNotificationLogger
from web.web_client_api import webApiCollection as webApiCollection
from web.web_client_api.sound import HangarSoundWebApi as HangarSoundWebApi
from typing import Tuple as Tuple
from notification.NotificationsModel import NotificationsModel as NotificationsModel
from gui.platform.wgnp.steam_account.statuses import SteamAccEmailStatus as SteamAccEmailStatus
_AVAILABLE_HANDLERS: list

class ActionHandler(object):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...

class NavigationDisabledActionHandler(ActionHandler):
    # decorador original: @prbDispatcherProperty
    def prbDispatcher(self):
        ...
    def handleAction(self, model, entityID, action):
        ...
    def doAction(self, model, entityID, action):
        ...
    def _canNavigate(self):
        ...
    @staticmethod
    def __showMessage():
        ...

class _OpenEventBoardsHandler(ActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...

class _ShowArenaResultHandler(NavigationDisabledActionHandler):
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    @classmethod
    def getNotType(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...
    def _updateNotification(self, notification):
        ...
    def _showWindow(self, notification, data):
        ...
    def _showI18nMessage(self, key, msgType):
        ...

class _ShowClanSettingsHandler(ActionHandler):
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...

class _ShowClanSettingsFromAppsHandler(_ShowClanSettingsHandler):
    @classmethod
    def getNotType(cls):
        ...

class _ShowClanSettingsFromInvitesHandler(_ShowClanSettingsHandler):
    @classmethod
    def getNotType(cls):
        ...

class _ShowClanAppsHandler(ActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...

class _ShowClanInvitesHandler(ActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...

class _ClanAppHandler(ActionHandler):
    clanCtrl: Any
    def _getAccountID(self, model, entityID):
        ...
    def _getApplicationID(self, model, entityID):
        ...

class _AcceptClanAppHandler(_ClanAppHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    # decorador original: @adisp_process
    def handleAction(self, model, entityID, action):
        ...

class _DeclineClanAppHandler(_ClanAppHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    # decorador original: @adisp_process
    def handleAction(self, model, entityID, action):
        ...

class _ShowClanAppUserInfoHandler(_ClanAppHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...

class _ClanInviteHandler(ActionHandler):
    clanCtrl: Any
    def _getInviteID(self, model, entityID):
        ...

class _AcceptClanInviteHandler(_ClanInviteHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    # decorador original: @adisp_process
    def handleAction(self, model, entityID, action):
        ...

class _DeclineClanInviteHandler(_ClanInviteHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    # decorador original: @adisp_process
    def handleAction(self, model, entityID, action):
        ...

class _ShowClanProfileHandler(ActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...

class ShowRankedSeasonCompleteHandler(ActionHandler):
    rankedController: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...
    def __showSeasonAward(self, quest, data):
        ...

class ShowRankedFinalYearHandler(ActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...
    def __showFinalAward(self, questID, data):
        ...

class ShowRankedYearPositionHandler(ActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...

class ShowRankedBattlePageHandler(ActionHandler):
    __rankedController: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...

class SelectBattleRoyaleMode(ActionHandler):
    battleRoyale: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...

class ShowBattleResultsHandler(_ShowArenaResultHandler):
    battleResults: Any
    def _updateNotification(self, notification):
        ...
    @classmethod
    def getActions(cls):
        ...
    def _canNavigate(self):
        ...
    # decorador original: @decorators.adisp_process(...)
    def _showWindow(self, notification, data):
        ...

class ShowFortBattleResultsHandler(_ShowArenaResultHandler):
    @classmethod
    def getActions(cls):
        ...
    def _updateNotification(self, notification):
        ...
    def _showWindow(self, notification, data):
        ...

class OpenPollHandler(ActionHandler):
    browserCtrl: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...
    # decorador original: @adisp_process
    def __doOpen(self, link, title):
        ...

class AcceptPrbInviteHandler(ActionHandler):
    __winbackController: Any
    # decorador original: @prbDispatcherProperty
    def prbDispatcher(self):
        ...
    # decorador original: @prbInvitesProperty
    def prbInvites(self):
        ...
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    # decorador original: @adisp_process
    def handleAction(self, model, entityID, action):
        ...

class DeclinePrbInviteHandler(ActionHandler):
    # decorador original: @prbInvitesProperty
    def prbInvites(self):
        ...
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...

class ApproveFriendshipHandler(ActionHandler):
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...

class CancelFriendshipHandler(ActionHandler):
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...

class WGNCActionsHandler(ActionHandler):
    # decorador original: @prbDispatcherProperty
    def prbDispatcher(self):
        ...
    @classmethod
    def getNotType(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...
    def _canNavigate(self):
        ...
    @staticmethod
    def __showMessage():
        ...

class SecurityLinkHandler(ActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...

class ClanRulesHandler(ActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...

class OpenCustomizationHandler(ActionHandler):
    service: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...

class ProlongStyleRent(ActionHandler):
    service: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...

class _OpenMissingEventsHandler(ActionHandler):
    __notification: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...
    @staticmethod
    def __showErrorMessage():
        ...

class _OpenNotrecruitedHandler(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenNotrecruitedSysMessageHandler(_OpenNotrecruitedHandler):
    @classmethod
    def getNotType(cls):
        ...

class _OpenBarracksHandler(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenConfirmEmailHandler(NavigationDisabledActionHandler):
    __wgnpSteamAccCtrl: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    # decorador original: @wg_async
    def doAction(self, model, entityID, action):
        ...

class OpenPersonalMissionHandler(ActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...

class _OpenLootBoxesHandler(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _LootBoxesAutoOpenHandler(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenLootBoxSystemHandler(NavigationDisabledActionHandler):
    _lootBoxes: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _LootBoxSystemAutoOpenHandler(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenProgressiveRewardView(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenBattlePassProgressionView(NavigationDisabledActionHandler):
    __battlePass: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenBattlePassChapterChoiceView(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenBPExtraWillEndSoon(NavigationDisabledActionHandler):
    __battlePassController: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpentBlueprintsConvertSale(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenMapboxProgression(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenMapboxSurvey(NavigationDisabledActionHandler):
    __mapboxCtrl: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenDelayedReward(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenChapterChoiceView(_OpenBattlePassProgressionView):
    @classmethod
    def getNotType(cls):
        ...

class _OpenEpicBattlesAfterBattleWindow(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenCustomizationStylesSection(NavigationDisabledActionHandler):
    __customizationService: Any
    __hangarSpace: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenIntegratedAuction(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenIntegratedAuctionStart(_OpenIntegratedAuction):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...

class _OpenIntegratedAuctionFinish(_OpenIntegratedAuction):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...

class _OpenPersonalReservesHandler(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenSeniorityAwardsVehicleSelection(NavigationDisabledActionHandler):
    __slots__: tuple
    __seniorityAwardCtrl: Any
    __uiVehicleSelectionNotificationLogger: Any
    def __init__(self):
        ...
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenWinbackSelectableRewardView(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenWinbackSelectableRewardViewFromQuest(_OpenWinbackSelectableRewardView):
    @classmethod
    def getNotType(cls):
        ...

class _OpenAchievementsScreen(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenAdvancedAchievementsScreen(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenCollectionHandler(NavigationDisabledActionHandler):
    __collections: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenCollectionEntryHandler(_OpenCollectionHandler):
    __collections: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...

class _OpenCollectionRenewHandler(_OpenCollectionHandler):
    __collections: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...

class _OpenCollectionRewardHandler(NavigationDisabledActionHandler):
    __collections: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenPrestigeVehicleStats(NavigationDisabledActionHandler):
    __lobbyContext: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenCrewPostProgression(NavigationDisabledActionHandler):
    __lobbyContext: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _ClaimRewardPostProgression(NavigationDisabledActionHandler):
    __lobbyContext: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    # decorador original: @decorators.adisp_process(...)
    def doAction(self, model, entityID, action):
        ...

class _OpenPrestigeOnboardingWindow(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenPunishmentWindowHandler(ActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def handleAction(self, model, entityID, action):
        ...

class _OpenGoldExchangeWindow(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenXpExchangeWindow(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _OpenPM3Operation(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _AffirmativePM3Notification(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _BattleMattersTaskReminder(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _PetSystemPetAddedNotification(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _WotPlusExpiredNotification(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class _ChallengesReminderNotification(NavigationDisabledActionHandler):
    __challenges: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class NotificationsActionsHandlers(object):
    __slots__: tuple
    __single: Any
    __multi: Any
    def __init__(self, handlers=None):
        ...
    def handleAction(self, model, typeID, entityID, actionName):
        ...
    def cleanUp(self):
        ...
