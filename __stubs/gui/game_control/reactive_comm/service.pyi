# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/reactive_comm/service.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from collections import deque as deque
import typing as typing
import wg_async as wg_async
from gui.game_control.reactive_comm.constants import SubscriptionClientStatus as SubscriptionClientStatus
from gui.game_control.reactive_comm.channel import SubscriptionStatus as SubscriptionStatus, ChannelsEventsSender as ChannelsEventsSender
from gui.game_control.reactive_comm.manager import ChannelsManager as ChannelsManager
from helpers import dependency as dependency
from skeletons.gui.game_control import IReactiveCommunicationService as IReactiveCommunicationService
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from gui.game_control.reactive_comm.channel import Subscription as Subscription
from gui.game_control.reactive_comm.packer import ServiceMessage as ServiceMessage

class ReactiveCommunicationService(IReactiveCommunicationService, ChannelsEventsSender):
    __lobbyContext: Any
    __manager: Any
    def __init__(self):
        ...
    @property
    def isChannelSubscriptionAvailable(self):
        ...
    # decorador original: @wg_async.wg_async
    def subscribeToChannel(self, subscription):
        ...
    def unsubscribeFromChannel(self, subscription):
        ...
    def getLastMessageFromChannel(self, subscription):
        ...
    def getChannelHistory(self, name):
        ...
    def getChannelStatus(self, name):
        ...
    def fini(self):
        ...
    def onLobbyStarted(self, ctx):
        ...
    def onDisconnected(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def __clear(self):
        ...
    def __update(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onServerSettingsChanged(self, _):
        ...
