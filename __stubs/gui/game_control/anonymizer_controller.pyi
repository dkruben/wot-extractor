# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/anonymizer_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from Event import Event as Event
from gui import SystemMessages as SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.anonymizer.contacts_uploader import ContactsUploader as ContactsUploader
from helpers import dependency as dependency
from skeletons.gui.game_control import IAnonymizerController as IAnonymizerController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any
_RSettingsError = R.strings.messenger.server.errors.settingError

class AnonymizerController(IAnonymizerController):
    __lobbyContext: Any
    __itemsCache: Any
    __slots__: tuple
    onStateChanged: Any
    __isEnabled: Any
    __isRestricted: Any
    __isAnonymized: Any
    __isInBattle: Any
    __uploader: Any
    def __init__(self):
        ...
    def onConnected(self):
        ...
    def onDisconnected(self):
        ...
    def onLobbyInited(self, _):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    @property
    def isInBattle(self):
        ...
    @property
    def isEnabled(self):
        ...
    @property
    def isRestricted(self):
        ...
    @property
    def isAnonymized(self):
        ...
    def setAnonymized(self, value):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __update(self):
        ...
    def __clear(self):
        ...
    def __onServerSettingsChanged(self, *_):
        ...
    def __onCacheSPAChanged(self, *_):
        ...
    def __onAnonymizedStateChanged(self, *_):
        ...
    def __onContactsFeedback(self, *_):
        ...
    def __processContacts(self):
        ...
    def __onSetAnonymizedResponse(self, resultID, errorCode):
        ...
    @staticmethod
    def __pushChangeUnavailableMessage():
        ...
