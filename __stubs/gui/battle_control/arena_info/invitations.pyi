# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/arena_info/invitations.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from builtins import zip as zip
import BattleReplay as BattleReplay
from adisp import adisp_process as adisp_process
from constants import INVITATION_TYPE as INVITATION_TYPE
from BattleReplay import CallbackDataNames as CallbackDataNames
from gui.battle_control.arena_info.settings import INVITATION_DELIVERY_STATUS as _STATUS
from gui.battle_control.requests.context import SendInvitesCtx as SendInvitesCtx
from gui.prb_control import prbInvitesProperty as prbInvitesProperty
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from skeletons.gui.battle_session import ISquadInvitationsHandler as ISquadInvitationsHandler
from unit_roster_config import SquadRoster as SquadRoster, EpicRoster as EpicRoster
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class SquadInvitationsFilter(object):
    __slots__: tuple
    __arenaUniqueID: Any
    __isReceivingProhibited: Any
    __isSendingProhibited: Any
    __received: Any
    __sent: Any
    def __init__(self):
        ...
    def setArenaUniqueID(self, arenaUniqueID):
        ...
    def isReceivingProhibited(self):
        ...
    def isSendingProhibited(self):
        ...
    def updatePersonalInfo(self, arenaDP):
        ...
    def addReceivedInvite(self, invite):
        ...
    def addSentInvite(self, invite):
        ...
    def filterReceivedInvites(self, getter, added, changed, deleted):
        ...
    def filterSentInvites(self, getter, added, changed, deleted):
        ...
    def __isInviteValid(self, invite):
        ...

class _SquadInvitationsHandler(ISquadInvitationsHandler):
    __slots__: tuple
    __sessionProvider: Any
    def __init__(self, setup):
        ...
    # decorador original: @prbInvitesProperty
    def prbInvites(self):
        ...
    def clear(self):
        ...
    def send(self, sessionID):
        ...
    def accept(self, sessionID):
        ...
    def reject(self, sessionID):
        ...
    # decorador original: @adisp_process
    def __onSendInviteToSquad(self, sessionID):
        ...
    def __getInviteID(self, sessionID, isCreator, incomingInvites):
        ...

class _SquadInvitationsRecorder(_SquadInvitationsHandler):
    __slots__: tuple
    __idGen: Any
    def __init__(self, setup):
        ...
    def send(self, sessionID):
        ...
    def accept(self, sessionID):
        ...
    def reject(self, sessionID):
        ...

class _SquadInvitationsPlayer(_SquadInvitationsHandler):
    __slots__: tuple
    def __init__(self, setup):
        ...
    def clear(self):
        ...
    def __onSend(self, _, sessionID):
        ...
    def __onAccept(self, _, sessionID):
        ...
    def __onReject(self, _, sessionID):
        ...

def createInvitationsHandler(setup):
    ...
