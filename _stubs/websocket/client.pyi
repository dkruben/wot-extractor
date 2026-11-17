# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/websocket/client.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
import Event as Event
from gui.shared.utils import backoff as backoff
from .constants import ConnectionStatus as ConnectionStatus, OpCode as OpCode
_logger: Any
_BACK_OFF_MIN_DELAY = 60
_BACK_OFF_MAX_DELAY = 1200
_BACK_OFF_MODIFIER = 30
_BACK_OFF_EXP_RANDOM_FACTOR = 5

class _websocket(object):
    class PyClient(object):
        def __init__(self, _):
            ...
        def open(self, _):
            ...
        def close(self):
            ...
        def terminate(self):
            ...
        def send(self, code, message):
            ...

class Listener(object):
    __slots__: tuple
    __em: Any
    onOpened: Any
    onFailed: Any
    onClosed: Any
    onMessage: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def _cOnOpened(self, server):
        ...
    def _cOnFailed(self, server, code, reason):
        ...
    def _cOnClosed(self, server, code, reason):
        ...
    def _cOnMessage(self, code, payload):
        ...

class _Reconnection(object):
    __slots__: tuple
    __client: Any
    __callbackID: Any
    __expBackOff: Any
    def __init__(self, client):
        ...
    def init(self):
        ...
    def clear(self):
        ...
    def __doNextOpen(self):
        ...
    def __onOpened(self, server):
        ...
    def __onFailed(self, server, code, reason):
        ...
    def __onClosed(self, server, code, reason):
        ...

class Client(object):
    __slots__: tuple
    __impl: Any
    __reconnection: Any
    __isReadyToDestroy: Any
    def __init__(self):
        ...
    @property
    def status(self):
        ...
    @property
    def url(self):
        ...
    @property
    def listener(self):
        ...
    @property
    def isReadyToDestroy(self):
        ...
    @property
    def raw(self):
        ...
    def open(self, url, reconnect=False):
        ...
    def close(self):
        ...
    def sendText(self, message):
        ...
    def sendBinary(self, message):
        ...
    def terminate(self):
        ...
    def __clearReconnection(self):
        ...
