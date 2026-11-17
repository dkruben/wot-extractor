# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/formatters/invites.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from constants import PREBATTLE_TYPE_NAMES as PREBATTLE_TYPE_NAMES, PREBATTLE_TYPE as PREBATTLE_TYPE, QUEUE_TYPE as QUEUE_TYPE
from constants import QUEUE_TYPE_NAMES as QUEUE_TYPE_NAMES
from gui import makeHtmlString as makeHtmlString
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.prb_control.formatters import getPrebattleFullDescription as getPrebattleFullDescription, getPrebattleStartTimeString as getPrebattleStartTimeString
from gui.prb_control import prbDispatcherProperty as prbDispatcherProperty, prbAutoInvitesProperty as prbAutoInvitesProperty, prbInvitesProperty as prbInvitesProperty
from gui.prb_control.prb_helpers import getModeNameKwargs as getModeNameKwargs
from gui.prb_control.settings import PRB_INVITE_STATE as PRB_INVITE_STATE
from gui.shared.system_factory import collectPrbInviteHtmlFormatter as collectPrbInviteHtmlFormatter, registerPrbInvitesHtmlFormatter as registerPrbInvitesHtmlFormatter
from helpers import dependency as dependency
from helpers.html import escape as htmlEscape
from messenger.ext import passCensor as passCensor
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.gui.game_control import IWinbackController as IWinbackController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_logger: Any
QUEUE_LEAVE_PREFIX = 'QUEUE_'
PREBATTLE_LEAVE_PREFIX = 'PREBATTLE_'
_R_INVITES = R.strings.invites.invites
_PRB_INVITE_PART_KEYS: dict

class _PrbInvitePart(CONST_CONTAINER):
    TITLE_CREATOR_NAME = 'inviteTitleCreatorName'
    TITLE = 'inviteTitle'
    WARNING = 'inviteWarning'
    COMMENT = 'inviteComment'
    NOTE = 'inviteNote'
    STATE = 'inviteState'

class InviteFormatter(object):
    def getCtx(self, invite):
        ...
    def getNote(self, invite):
        ...
    def getText(self, invite):
        ...

class PrbInviteHtmlTextFormatter(InviteFormatter):
    # decorador original: @prbDispatcherProperty
    def prbDispatcher(self):
        ...
    # decorador original: @prbInvitesProperty
    def prbInvites(self):
        ...
    def canAcceptInvite(self, invite):
        ...
    def getIconName(self, invite):
        ...
    def getIconPath(self, invite, pathMaker=None):
        ...
    def getTitle(self, invite):
        ...
    def getWarning(self, invite):
        ...
    def getComment(self, invite):
        ...
    def getNote(self, invite):
        ...
    def getState(self, invite):
        ...
    def getText(self, invite):
        ...
    def updateTooltips(self, invite, canAccept, message):
        ...
    def _getTitle(self, invite):
        ...

class PrbExternalBattleInviteHtmlTextFormatter(PrbInviteHtmlTextFormatter):
    def getComment(self, invite):
        ...

class PrbInviteTitleFormatter(InviteFormatter):
    def getText(self, _):
        ...

class AutoInviteTextFormatter(InviteFormatter):
    # decorador original: @prbDispatcherProperty
    def prbDispatcher(self):
        ...
    # decorador original: @prbAutoInvitesProperty
    def prbAutoInvites(self):
        ...
    def getNote(self, invite):
        ...
    def getText(self, invite):
        ...

class _PrbInviteInfo(object):
    def as_dict(self):
        ...

class PrbAutoInviteInfo(_PrbInviteInfo):
    __prbID: Any
    def __init__(self, prbID):
        ...
    # decorador original: @prbAutoInvitesProperty
    def prbAutoInvites(self):
        ...
    def getID(self):
        ...
    def getTitle(self):
        ...
    def as_dict(self):
        ...

def _formatInvite(inviteType, values, maySkipValue=False, **kwargs):
    ...
def getPrbName(prbType, lowercase=False):
    ...
def getPreQueueName(queueType, lowercase=False):
    ...
def getPrbInviteStateName(state):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getAcceptNotAllowedText(prbType, peripheryID, isInviteActive=True, isAlreadyJoined=False, lobbyContext=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getLeaveOrChangeText(funcState, invitePrbType, peripheryID, lobbyContext=None, winbackController=None):
    ...
def getPrbInviteHtmlFormatter(invite):
    ...
