# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/reactive_comm/channel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import re as re
import zlib as zlib
from collections import deque as deque
import typing as typing
import Event as Event
import websocket as websocket
from gui.game_control.reactive_comm import constants as constants
from gui.game_control.reactive_comm import packer as packer
_logger: Any
_channelRegExp: Any

class ChannelsEventsSender(object):
    __em: Any
    onChannelMessage: Any
    onChannelClosed: Any
    onSubscriptionClosed: Any
    def __init__(self):
        ...
    def clear(self):
        ...

class Channel(object):
    __slots__: tuple
    __name: Any
    __clientStatus: Any
    __serverStatus: Any
    __messages: Any
    __subscriptions: Any
    __eventsSender: Any
    def __init__(self, name, eventsSender=None):
        ...
    @property
    def name(self):
        ...
    @property
    def status(self):
        ...
    @property
    def isSubscribed(self):
        ...
    @property
    def hasSubscription(self):
        ...
    @property
    def messages(self):
        ...
    @property
    def lastMessage(self):
        ...
    def clear(self):
        ...
    def close(self):
        ...
    def subscribe(self, client):
        ...
    def unsubscribe(self, client):
        ...
    def getLastMessage(self, client):
        ...
    def addSubscription(self, subscription):
        ...
    def removeSubscription(self, subscription):
        ...
    def setStatus(self, status):
        ...
    def addMessage(self, message):
        ...
    @staticmethod
    def __tryDecompressZip(data):
        ...
    def __clearSubscriptions(self, reason=...):
        ...

class Subscription(object):
    __slots__: tuple
    __channel: Any
    __em: Any
    onMessage: Any
    onClosed: Any
    def __init__(self, channel):
        ...
    @property
    def channel(self):
        ...
    def clear(self):
        ...

class SubscriptionStatus(object):
    __slots__: tuple
    __nonzero__: Any
    __clientStatus: Any
    __serverStatus: Any
    def __init__(self, clientStatus=..., serverStatus=...):
        ...
    def __repr__(self):
        ...
    def __bool__(self):
        ...
    @property
    def isSubscribed(self):
        ...
    @property
    def client(self):
        ...
    @property
    def server(self):
        ...

def isChannelNameValid(name):
    ...
