# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/user_cm_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import long as long
import math as math
from Event import Event as Event
from adisp import adisp_process as adisp_process
from constants import DENUNCIATIONS_PER_DAY as DENUNCIATIONS_PER_DAY, ARENA_GUI_TYPE as ARENA_GUI_TYPE, IS_CHINA as IS_CHINA, PREBATTLE_TYPE as PREBATTLE_TYPE, QUEUE_TYPE as QUEUE_TYPE
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui import SystemMessages as SystemMessages, DialogsInterface as DialogsInterface
from gui.Scaleform.daapi.view.lobby.lobby_constants import USER as USER
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity as EventSystemEntity
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuCollectEventsHandler as AbstractContextMenuCollectEventsHandler
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as SYSTEM_MESSAGES
from gui.clans.clan_helpers import showClanInviteSystemMsg as showClanInviteSystemMsg
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from gui.prb_control import prbDispatcherProperty as prbDispatcherProperty, prbEntityProperty as prbEntityProperty
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction, SendInvitesCtx as SendInvitesCtx
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from gui.shared import event_dispatcher as shared_events, events as events, g_eventBus as g_eventBus, utils as utils
from gui.clans.clan_cache import ClanInfo as ClanInfo
from gui.shared.denunciator import LobbyDenunciator as LobbyDenunciator, DENUNCIATIONS as DENUNCIATIONS, DENUNCIATIONS_MAP as DENUNCIATIONS_MAP
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.utils.functions import showSentInviteMessage as showSentInviteMessage
from gui.shared.system_factory import registerLobbyContexMenuHandler as registerLobbyContexMenuHandler, collectLobbyContexMenuOptionBuilders as collectLobbyContexMenuOptionBuilders, collectLobbyContexMenuHandler as collectLobbyContexMenuHandler
from gui.wgcg.clan.contexts import CreateInviteCtx as CreateInviteCtx
from helpers import i18n as i18n, dependency as dependency
from helpers.i18n import makeString as makeString
from messenger import g_settings as g_settings
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE, USER_TAG as USER_TAG, UserEntityScope as UserEntityScope
from messenger.proto import proto_getter as proto_getter
from messenger.proto.entities import ClanInfo as UserClanInfo
from messenger.proto.entities import SharedUserEntity as SharedUserEntity
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage
from nation_change_helpers.client_nation_change_helper import getValidVehicleCDForNationChange as getValidVehicleCDForNationChange
from shared_utils import findFirst as findFirst
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket, IBattleRoyaleController as IBattleRoyaleController, IMapboxController as IMapboxController, IEventBattlesController as IEventBattlesController, IPlatoonController as IPlatoonController, IEpicBattleMetaGameController as IEpicBattleMetaGameController, IWinbackController as IWinbackController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.web import IWebController as IWebController
from uilogging.player_satisfaction_rating.loggers import PostBattleContextMenuLogger as PostBattleContextMenuLogger
_CM_ICONS: dict
_CM_TEXT_COLOR_GOLD = 13347959

class _EXTENDED_OPT_IDS(object):
    VEHICLE_COMPARE = 'userVehicleCompare'

class BaseUserCMHandler(AbstractContextMenuCollectEventsHandler, EventSystemEntity):
    itemsCache: Any
    eventsCache: Any
    clanCtrl: Any
    lobbyContext: Any
    platoonCtrl: Any
    __battleRoyale: Any
    __mapboxCtrl: Any
    __eventBattlesCtrl: Any
    __epicCtrl: Any
    __winbackController: Any
    usersStorage: Any
    databaseID: Any
    userName: Any
    wasInBattle: Any
    showClanProfile: Any
    clanAbbrev: Any
    # decorador original: @prbDispatcherProperty
    def prbDispatcher(self):
        ...
    # decorador original: @prbEntityProperty
    def prbEntity(self):
        ...
    def doSelect(self, prebattleActionName, accountsToInvite=None, extData=None):
        ...
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    def canInvite(self):
        ...
    def isSquadCreator(self):
        ...
    def getOptions(self, ctx=None):
        ...
    def createSquad(self, prbActionName=...):
        ...
    def isSquadAlreadyCreated(self, prbType):
        ...
    def _initFlashValues(self, ctx):
        ...
    def _clearFlashValues(self):
        ...
    def _getContexMenuHandler(self):
        ...
    def _getUseCmInfo(self):
        ...
    def _generateOptions(self, ctx=None):
        ...
    def _addIgnoreInfo(self, options, userCMInfo):
        ...
    def _addFriendshipInfo(self, options, userCMInfo):
        ...
    def _addChannelInfo(self, options, userCMInfo):
        ...
    def _addSquadInfo(self, options, userCMInfo):
        ...
    def _addPrebattleInfo(self, options, userCMInfo):
        ...
    def _addRemoveFriendInfo(self, options, userCMInfo):
        ...
    def _addVehicleInfo(self, options):
        ...
    def _addContactsNoteInfo(self, options, userCMInfo):
        ...
    def _addAppealInfo(self, options):
        ...
    def _addMutedInfo(self, options, userCMInfo):
        ...
    def _addRemoveFromGroupInfo(self, options, isIgnored):
        ...
    def _addRejectFriendshipInfo(self, options, userCMInfo):
        ...
    def _addClanProfileInfo(self, options, userCMInfo):
        ...
    def _addInviteClanInfo(self, options, userCMInfo):
        ...
    def _makeAIBotOptions(self):
        ...

class AppealCMHandler(BaseUserCMHandler):
    _denunciator: Any
    _vehicleCD: Any
    arenaUniqueID: Any
    _arenaGuiType: Any
    _isAlly: Any
    def __init__(self, cmProxy, ctx=None):
        ...
    def fini(self):
        ...
    @property
    def vehicleCD(self):
        ...
    @property
    def denunciator(self):
        ...
    def _initFlashValues(self, ctx):
        ...
    def _clearFlashValues(self):
        ...
    def _addAppealInfo(self, options):
        ...
    def _addVehicleInfo(self, options):
        ...
    def _isAppealsForTopicEnabled(self, topic):
        ...
    def _getSubmenuData(self):
        ...
    def _createSubMenuItem(self):
        ...

class UserVehicleCMHandler(AppealCMHandler):
    comparisonBasket: Any
    _uiPlayerSatisfactionRatingLogger: Any
    def __init__(self, cmProxy, ctx=None):
        ...
    def fini(self):
        ...
    def onOptionSelect(self, optionId):
        ...
    def _generateOptions(self, ctx=None):
        ...
    def _manageVehCompareOptions(self, options):
        ...

class CustomUserCMHandler(BaseUserCMHandler):
    __customOptions: Any
    __excludedOptions: Any
    __customOptionsAfterEnd: Any
    __optionSelected: Any
    onSelected: Any
    def __init__(self, cmProxy, ctx=None):
        ...
    def fini(self):
        ...
    def onOptionSelect(self, optionId):
        ...
    def _generateOptions(self, ctx=None):
        ...
    def _addCustomInfo(self, options):
        ...
    def _excludeOptions(self, options):
        ...

class UserContextMenuInfo(object):
    lobbyContext: Any
    usersStorage: Any
    user: Any
    databaseID: Any
    isBot: Any
    canAddToIgnore: Any
    canDoDenunciations: Any
    isFriend: Any
    isIgnored: Any
    isTemporaryIgnored: Any
    isMuted: Any
    hasClan: Any
    userName: Any
    displayName: Any
    isOnline: Any
    isCurrentPlayer: Any
    def __init__(self, databaseID, userName, clanAbbrev):
        ...
    @property
    def isSameRealm(self):
        ...
    @property
    def canCreateChannel(self):
        ...
    def getTags(self):
        ...
    def getNote(self):
        ...
    def __getUser(self, dbId, username, clanAbbrev):
        ...

def showUserInfo(cm):
    ...
def showClanInfo(cm):
    ...
# decorador original: @adisp_process
def sendClanInvite(cm):
    ...
def createPrivateChannel(cm):
    ...
def addFriend(cm):
    ...
def requestFriendship(cm):
    ...
def removeFriend(cm):
    ...
def setMuted(cm):
    ...
def unsetMuted(cm):
    ...
def setIgnored(cm):
    ...
def unsetIgnored(cm):
    ...
def copyToClipboard(cm):
    ...
def createSquad(cm):
    ...
def createEventSquad(cm):
    ...
def createBattleRoyaleSquad(cm):
    ...
def createMapboxSquad(cm):
    ...
def invite(cm):
    ...
def appealIncorrectBehavior(cm):
    ...
def appealNotFairPlay(cm):
    ...
def appealForbiddenNick(cm):
    ...
def appealBot(cm):
    ...
def showVehicleInfo(cm):
    ...
def compareVehicle(cm):
    ...
