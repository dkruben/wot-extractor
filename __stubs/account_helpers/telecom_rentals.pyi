# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/telecom_rentals.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import AccountCommands as AccountCommands
from Event import Event as Event
from account_helpers import AccountSyncData as AccountSyncData
from gui.server_events import settings as settings
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from telecom_rentals_common import PartnershipState as PartnershipState, PARTNERSHIP_BLOCKED_TOKEN_NAME as PARTNERSHIP_BLOCKED_TOKEN_NAME
from telecom_rentals_common import ROSTER_EXPIRATION_TOKEN_NAME as ROSTER_EXPIRATION_TOKEN_NAME, PARTNERSHIP_TOKEN_NAME as PARTNERSHIP_TOKEN_NAME
from Account import PlayerAccount as PlayerAccount
from typing import Set as Set
_logger: Any

class TelecomRentals(object):
    itemsCache: Any
    _lobbyContext: Any
    _account: Any
    _syncData: Any
    _tokens: Any
    onPendingRentChanged: Any
    _ignore: Any
    def __init__(self, syncData):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def setAccount(self, account):
        ...
    def synchronize(self, isFullSync, diff):
        ...
    def togglePartnership(self, partnershipState):
        ...
    def setRentalTokensDev(self, amount):
        ...
    def hasPartnership(self):
        ...
    def isBlocked(self):
        ...
    def isActive(self):
        ...
    def getRosterExpirationTime(self):
        ...
    def getTotalRentCount(self):
        ...
    def getAvailableRentCount(self):
        ...
    def setRentPending(self, vehCD):
        ...
    def getRentsPending(self):
        ...
    def resetRentsPending(self, vehCDs):
        ...
    def simulateRentTank(self, tankId):
        ...
    def _onCmdResponseReceived(self, resultID, requestID, errorStr, errorMsg=None):
        ...
