# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/gift_system_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from constants import Configs as Configs
from Event import Event as Event, EventManager as EventManager
from gifts.gifts_common import ClientReqStrategy as ClientReqStrategy
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.gift_system.hubs import createGiftEventHub as createGiftEventHub
from gui.gift_system.requesters.history_requester import GiftSystemHistoryRequester as GiftSystemHistoryRequester
from gui.gift_system.requesters.state_requester import GiftSystemWebStateRequester as GiftSystemWebStateRequester
from gui.gift_system.wrappers import skipNoHubsAction as skipNoHubsAction
from helpers import dependency as dependency
from helpers.server_settings import GiftSystemConfig as GiftSystemConfig
from skeletons.gui.game_control import IGiftSystemController as IGiftSystemController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.gift_system.hubs.base.hub_core import IGiftEventHub as IGiftEventHub
from gui.gift_system.wrappers import GiftsHistoryData as GiftsHistoryData, GiftsWebState as GiftsWebState
from gui.shared import events as events
from helpers.server_settings import ServerSettings as ServerSettings, GiftEventConfig as GiftEventConfig

class GiftSystemController(IGiftSystemController):
    __itemsCache: Any
    __lobbyContext: Any
    __em: Any
    onEventHubsCreated: Any
    onEventHubsDestroyed: Any
    __isLobbyInited: Any
    __serverSettings: Any
    __giftSystemSettings: Any
    __eventHubs: Any
    __historyRequester: Any
    __webStateRequester: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def onDisconnected(self):
        ...
    def onLobbyInited(self, event=None):
        ...
    def getEventHub(self, eventID):
        ...
    def getSettings(self):
        ...
    def requestWebState(self, eventID):
        ...
    def __clear(self):
        ...
    def __onGiftSettingsChanged(self, diff):
        ...
    def __onHistoryReadyChanged(self, isHistoryReady):
        ...
    def __onHistoryReceived(self, history):
        ...
    def __onWebStateReadyChanged(self, strategy, eventIDs=None):
        ...
    def __onWebStateReceived(self, webState):
        ...
    def __onServerSettingsChanged(self, serverSettings):
        ...
    # decorador original: @skipNoHubsAction
    def __createEventHubs(self, hubsToCreate, eventsSettings):
        ...
    # decorador original: @skipNoHubsAction
    def __destroyEventHubs(self, hubsToDestroy, onDisconnect=False):
        ...
    # decorador original: @skipNoHubsAction
    def __updateEventHubs(self, hubsToUpdate, eventsSettings):
        ...
    def __updateEventHubsSettings(self, prevSettings, newSettings):
        ...
    def __updateGiftSettings(self):
        ...
    def __updateLobbyState(self, isLobbyInited=False):
        ...
    def __updateReadyListening(self):
        ...
