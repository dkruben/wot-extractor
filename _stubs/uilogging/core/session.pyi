# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/core/session.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import adisp as adisp
import wg_async as wg_async
from BWUtil import AsyncReturn as AsyncReturn
from gui.wgcg.uilogging.contexts import UILoggingSessionCtx as UILoggingSessionCtx
from helpers import dependency as dependency, time_utils as time_utils
from helpers.log.adapters import getWithContext as getWithContext
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from skeletons.gui.web import IWebController as IWebController
from soft_exception import SoftException as SoftException
from uilogging.constants import DEFAULT_LOGGER_NAME as DEFAULT_LOGGER_NAME
from uilogging.core.core_constants import LOGS_MAX_COUNT_PER_SEND as LOGS_MAX_COUNT_PER_SEND, LOG_RECORD_MAX_PROPERTIES_COUNT as LOG_RECORD_MAX_PROPERTIES_COUNT, MAX_SESSION_GET_RETRIES as MAX_SESSION_GET_RETRIES, MIN_SESSION_LIFE_TIME as MIN_SESSION_LIFE_TIME, REQUEST_SESSION_TIMEOUT as REQUEST_SESSION_TIMEOUT, RETRY_REQUEST_SESSION_DELAY as RETRY_REQUEST_SESSION_DELAY
from gui.wgcg.requests import WgcgRequestResponse as WgcgRequestResponse
from uilogging.core.log import LogRecord as LogRecord

class WaitingSessionData(SoftException):
    ...

class SessionData(object):
    __slots__: tuple
    __id: Any
    __auth: Any
    __logging: Any
    def __init__(self, sessionID, data):
        ...
    @property
    def id(self):
        ...
    @property
    def token(self):
        ...
    @property
    def expiration(self):
        ...
    @property
    def lifetime(self):
        ...
    @property
    def isExpired(self):
        ...
    @property
    def maxLogsCount(self):
        ...
    @property
    def maxLogPropertiesCount(self):
        ...
    @property
    def isValid(self):
        ...
    @property
    def url(self):
        ...
    def verifyLog(self, log):
        ...
    def __repr__(self):
        ...

class Session(object):
    webController: Any
    _requesting: Any
    _destroyed: Any
    _sessionData: Any
    _initialized: Any
    _idGen: Any
    _logger: Any
    def __init__(self):
        ...
    def get(self):
        ...
    def remove(self, sessionID):
        ...
    def update(self):
        ...
    # decorador original: @wg_async.wg_async
    def request(self):
        ...
    def destroy(self):
        ...
    # decorador original: @wg_async.wg_async
    def _update(self):
        ...
    @property
    def _isInitialized(self):
        ...
    def _clear(self):
        ...
    # decorador original: @adisp.adisp_process
    def _getSessionData(self, callback):
        ...
