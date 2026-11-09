# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/core/handler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import json as json
import zlib as zlib
import binascii as binascii
from functools import wraps as wraps, partial as partial
import BigWorld as BigWorld
from Event import SafeEvent as SafeEvent
from helpers import isPlayerAccount as isPlayerAccount
from helpers.log.adapters import getWithContext as getWithContext
from py2to3.compat import base64compat as base64compat
from shared_utils import safeCancelCallback as safeCancelCallback
from uilogging.constants import DEFAULT_LOGGER_NAME as DEFAULT_LOGGER_NAME, LogLevels as LogLevels
from uilogging.core.core_constants import LOGS_SEND_PERIOD as LOGS_SEND_PERIOD, LOGS_FORCE_SEND_PERIOD as LOGS_FORCE_SEND_PERIOD, LOGS_MAX_QUEUE_SIZE as LOGS_MAX_QUEUE_SIZE, HTTP_DEFAULT_TIMEOUT as HTTP_DEFAULT_TIMEOUT, HTTP_OK_STATUS as HTTP_OK_STATUS, HTTP_SESSION_EXPIRED as HTTP_SESSION_EXPIRED, DEFAULT_COMPRESSION_LEVEL as DEFAULT_COMPRESSION_LEVEL, FINAL_FLUSH_TIMEOUT as FINAL_FLUSH_TIMEOUT, HttpHeaders as HttpHeaders
from uilogging.core.log import LogRecord as LogRecord
from uilogging.core.common import grouper as grouper
from uilogging.core.session import Session as Session
from uilogging.core.session import SessionData as SessionData

class Delayer(object):
    __slots__: tuple
    _callbackId: Any
    _destroyed: Any
    def __init__(self, delay, func, *args, **kwargs):
        ...
    def destroy(self):
        ...
    def _call(self, func, *args, **kwargs):
        ...

class FeatureSettings(object):
    __slots__: tuple
    feature: Any
    enabled: Any
    loglevel: Any
    def __init__(self, feature, enabled=True, params=None):
        ...
    @property
    def params(self):
        ...
    def verifyLog(self, log):
        ...
    def __eq__(self, other):
        ...
    def __ne__(self, other):
        ...
    def __hash__(self):
        ...
    def __str__(self):
        ...
    def __repr__(self):
        ...

class FeaturesSettings(object):
    _features: Any
    _destroyed: Any
    _logger: Any
    def __init__(self):
        ...
    def update(self, rejected, accepted):
        ...
    def verifyLog(self, log):
        ...
    def verifyFeature(self, feature):
        ...
    def destroy(self):
        ...

class LogHandler(object):
    _destroyed: Any
    _playerID: Any
    _session: Any
    _features: Any
    _logs: Any
    _sender: Any
    _logsBatchWaitingTime: Any
    onDestroy: Any
    _logger: Any
    def __init__(self, playerID):
        ...
    @property
    def destroyed(self):
        ...
    # decorador original: @_ifDestroyed(...)
    def add(self, log):
        ...
    # decorador original: @_ifDestroyed(...)
    def logImmediately(self, log):
        ...
    # decorador original: @_ifDestroyed(...)
    def isFeatureEnabled(self, feature):
        ...
    # decorador original: @_ifDestroyed(...)
    def getSessionLifetime(self):
        ...
    # decorador original: @_ifDestroyed(...)
    def startSender(self):
        ...
    def destroy(self, flush=False):
        ...
    @property
    def _isPlayer(self):
        ...
    def _getSession(self):
        ...
    def _send(self, session, logs, wait=True):
        ...
    # decorador original: @_ifDestroyed(...)
    def _receive(self, sessionID, logs, response):
        ...
    def _tryToSendBatch(self, incomplete=False):
        ...
    def _periodicSend(self):
        ...
    def _startSender(self, *args, **kwargs):
        ...
    def _stopSender(self):
        ...

def _ifDestroyed(result=None):
    ...
