# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/game_control/battle_royale_tournament_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import calendar as calendar
from collections import Counter as Counter
from future.utils import listitems as listitems
import BigWorld as BigWorld
from gui.prb_control.items import prb_seqs as prb_seqs
import AccountCommands as AccountCommands
import Event as Event
from adisp import adisp_process as adisp_process
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from gui import SystemMessages as SystemMessages
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.game_control import IBattleRoyaleTournamentController as IBattleRoyaleTournamentController
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from BattleRoyaleTournament import BattleRoyaleTourmanentToken as BattleRoyaleTourmanentToken
_logger: Any
_R_BR_TOURNAMENT_TYPE = R.strings.battle_royale.tournament.type
_INVITE_START_ID = 1000000000

class BattleRoyaleTournamentController(IBattleRoyaleTournamentController):
    __itemsCache: Any
    __lobbyContext: Any
    __isAvailable: Any
    __tokens: Any
    __currentToken: Any
    __participants: Any
    __isReJoin: Any
    __isChangingInternalState: Any
    __previousInviteIDs: Any
    __isReady: Any
    __em: Any
    onUpdatedParticipants: Any
    onSelectBattleRoyaleTournament: Any
    def __init__(self):
        ...
    def onLobbyInited(self, event):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onDisconnected(self):
        ...
    def getSelectedToken(self):
        ...
    def isAvailable(self):
        ...
    def getTokens(self):
        ...
    def updateParticipants(self, participants):
        ...
    def getParticipants(self):
        ...
    def selectBattleRoyaleTournament(self, token):
        ...
    def join(self, tokenStr):
        ...
    def leave(self):
        ...
    def ready(self, vehicleID):
        ...
    def notReady(self):
        ...
    def leaveCurrentAndJoinToAnotherTournament(self, tournamentID):
        ...
    def leaveBattleRoyaleTournament(self, isChangingToBattleRoyaleHangar=False):
        ...
    def isSelected(self):
        ...
    def resetReady(self):
        ...
    @property
    def __tournamentComponent(self):
        ...
    def __selectRandom(self):
        ...
    # decorador original: @adisp_process
    def __doSelectRandomPrb(self, dispatcher):
        ...
    def __clear(self):
        ...
    def __clearInternalData(self):
        ...
    def __onClientUpdated(self, diff, _):
        ...
    def __onPrebattleAutoInvitesChanged(self):
        ...
    def __onCollectPrebattleInvites(self, autoInvites):
        ...
    def __joinResult(self, requestID, resultID, errorStr):
        ...
    def __leaveResult(self, requestID, resultID, errorStr):
        ...
    def __readyResult(self, requestID, resultID, errorStr):
        ...
    def __notReadyResult(self, requestID, resultID, errorStr):
        ...
    def __pushErrorSystemMessage(self, stringCode):
        ...
