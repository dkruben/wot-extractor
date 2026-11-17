# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/wallet.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import Event as Event
from gui import SystemMessages as SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as SYSTEM_MESSAGES
from gui.shared.money import Currency as Currency
from gui.SystemMessages import SM_TYPE as SM_TYPE
from helpers import dependency as dependency
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.gui.game_control import IWalletController as IWalletController
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

class WalletController(IWalletController):
    itemsCache: Any
    onWalletStatusChanged: Any
    __currentStatus: Any
    __currentCallbackId: Any
    class STATUS(CONST_CONTAINER):
        SYNCING = 0
        NOT_AVAILABLE = 1
        AVAILABLE = 2
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def onLobbyStarted(self, ctx):
        ...
    @property
    def status(self):
        ...
    @property
    def componentsStatuses(self):
        ...
    @property
    def isSyncing(self):
        ...
    @property
    def isNotAvailable(self):
        ...
    @property
    def isAvailable(self):
        ...
    def __processCallback(self):
        ...
    def __clearCallback(self):
        ...
    def __processStatus(self, status, initialize=False):
        ...
    def __onWalletStatusChanged(self, available):
        ...
    def __checkStatus(self, status):
        ...
    def __notify(self):
        ...
    def __sendNotification(self, status):
        ...
