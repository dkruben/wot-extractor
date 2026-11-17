# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/shared_utils/account_helpers/ClientInvitations.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from functools import partial as partial
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
import AccountCommands as AccountCommands
from constants import INVITATION_STATUS as INVITATION_STATUS
from helpers.time_utils import getCurrentTimestamp as getCurrentTimestamp, getServerUTCTime as getServerUTCTime
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from shared_utils import safeCancelCallback as safeCancelCallback
UniqueId: Any

class InvitationScope(object):
    AVATAR = 0
    ACCOUNT = 1

class ClientInvitations(object):
    __proxy: Any
    __expCbID: Any
    __invitations: Any
    __playerEvents: Any
    def __init__(self, playerEvents):
        ...
    def clear(self):
        ...
    def getInvites(self):
        ...
    def setProxy(self, proxy):
        ...
    def onProxyBecomePlayer(self):
        ...
    def onProxyBecomeNonPlayer(self):
        ...
    def processInvitations(self, invitations, scope):
        ...
    def sendInvitation(self, accountsToInvite, comment='', callback=None):
        ...
    def acceptInvitation(self, invitationID, senderID, callback=None):
        ...
    def declineInvitation(self, invitationID, senderID, callback=None):
        ...
    def _onInvitationResponseReceived(self, newStatus, invitationId, senderID, callback, _, code, errStr):
        ...
    def _cancelInvitations(self, predicate):
        ...
    def _loadExpiryCallback(self):
        ...
    def _clearExpiryCallback(self):
        ...
    def __onInviteExpired(self, inviteId):
        ...

class ReplayClientInvitations(ClientInvitations):
    def processInvitations(self, invitations, scope):
        ...
