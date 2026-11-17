# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/classic/player_menu_handler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from commendations_common import CommendationHelpers as CommendationHelpers
from commendations_common.CommendationHelpers import CommendationsSource as CommendationsSource
from gui.Scaleform.daapi.view.lobby.lobby_constants import USER as USER
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler as AbstractContextMenuHandler
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.battle_control.arena_info.settings import INVITATION_DELIVERY_STATUS as _D_STATUS
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus
from gui.shared.denunciator import DENUNCIATIONS as DENUNCIATIONS, BattleDenunciator as BattleDenunciator, DENUNCIATIONS_MAP as DENUNCIATIONS_MAP
from helpers import dependency as dependency
from helpers import i18n as i18n
from constants import DENUNCIATIONS_PER_DAY as DENUNCIATIONS_PER_DAY, IS_CHINA as IS_CHINA
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE, UserEntityScope as UserEntityScope
from messenger.proto import proto_getter as proto_getter
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import ICommendationsController as ICommendationsController
from uilogging.player_satisfaction_rating.loggers import InBattleContextMenuLogger as InBattleContextMenuLogger
from uilogging.player_satisfaction_rating.logging_constants import PlayerSatisfactionRatingCMActions as PlayerSatisfactionRatingCMActions
from constants import CommendationsState as CommendationsState
_logger: Any
_OPTIONS_HANDLERS: dict
_OPTION_ICONS: dict
_BOT_NO_ACTIONS_OPTION_ID = 'botNoActions'

class DYN_SQUAD_OPTION_ID(object):
    SENT_INVITATION = 'sendInvitationToSquad'
    ACCEPT_INVITATION = 'acceptInvitationToSquad'
    REJECT_INVITATION = 'rejectInvitationToSquad'
    IN_SQUAD = 'inSquad'

class COMMENDATIONS_OPTION_ID(object):
    COMMEND_FIRST = 'commendFirst'
    COMMEND_BACK = 'commendBack'
    OUTGOING_COMMENDATION = 'outgoingCommendation'
    MUTUAL_COMMENDATION = 'mutualCommendation'

class BATTLE_CHAT_OPTION_ID(object):
    ENABLE_COMMUNICATIONS = 'enableCommunications'
    DISABLE_COMMUNICATIONS = 'disableCommunications'

class PlayerContextMenuInfo(object):
    sessionProvider: Any
    usersStorage: Any
    __slots__: tuple
    avatarSessionID: Any
    isBot: Any
    isFriend: Any
    isIgnored: Any
    isTemporaryIgnored: Any
    isMuted: Any
    userName: Any
    isAlly: Any
    battleUser: Any
    def __init__(self, avatarSessionID, userName):
        ...

class PlayerMenuHandler(AbstractContextMenuHandler):
    sessionProvider: Any
    commendationsCtrl: Any
    __denunciator: Any
    __arenaUniqueID: Any
    _uiPlayerSatisfactionRatingLogger: Any
    __vInfo: Any
    __userInfo: Any
    def __init__(self, cmProxy, ctx=None):
        ...
    # decorador original: @proto_getter(...)
    def bwProto(self):
        ...
    @property
    def arenaVisitor(self):
        ...
    def fini(self):
        ...
    def addFriend(self):
        ...
    def removeFriend(self):
        ...
    def setIgnored(self):
        ...
    def unsetIgnored(self):
        ...
    def disableCommunications(self):
        ...
    def enableCommunications(self):
        ...
    def setMuted(self):
        ...
    def commend(self):
        ...
    def unsetMuted(self):
        ...
    def appealIncorrectBehavior(self):
        ...
    def appealNotFairPlay(self):
        ...
    def appealForbiddenNick(self):
        ...
    def appealBot(self):
        ...
    def sendInvitation(self):
        ...
    def acceptInvitation(self):
        ...
    def rejectInvitation(self):
        ...
    def _initFlashValues(self, ctx):
        ...
    def _clearFlashValues(self):
        ...
    def _generateOptions(self, ctx=None):
        ...
    @classmethod
    def _getOptionIcon(cls, optionID):
        ...
    @classmethod
    def _getOptionInitData(cls, optionID, isEnabled=True):
        ...
    def __addDynSquadInfo(self, options):
        ...
    def __addFriendshipInfo(self, options):
        ...
    def __addIgnoreInfo(self, options):
        ...
    def __addCommunicationInfo(self, options):
        ...
    def __addCommendationInfo(self, options):
        ...
    def __addMutedInfo(self, options):
        ...
    def __isAppealsForTopicEnabled(self, topic):
        ...
    def __addDenunciationsInfo(self, options):
        ...
    def __addBotInfo(self, options):
        ...
    def __handleHideCursor(self, _):
        ...
