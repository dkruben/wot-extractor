# wot-extractor: STUB (.pyi) gerado a partir de sources/res/server_side_replay/scripts/client/server_side_replay/gui/wgcg/providers/base_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import time as time
from collections import defaultdict as defaultdict, namedtuple as namedtuple
from enum import Enum as Enum
from typing import Dict as Dict, Optional as Optional, NamedTuple as NamedTuple, Type as Type, TYPE_CHECKING as TYPE_CHECKING
import BigWorld as BigWorld
import Event as Event
import ResMgr as ResMgr
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from data_structures import DictObj as DictObj
from client_request_lib.requester import Requester as WebRequester
from gui.wgcg.base.contexts import CommonWebRequestCtx as CommonWebRequestCtx
from AccountCommands import CMD_GENERATE_SSR_JWT_TOKEN as CMD_GENERATE_SSR_JWT_TOKEN
from server_side_replay.gui.wgcg.requests import ServerSideReplayRequester as ServerSideReplayRequester, ServerSideReplayRequestsController as ServerSideReplayRequestsController, ServerSideReplayRequestResponse as ServerSideReplayRequestResponse
from helpers import time_utils as time_utils, getClientLanguage as getClientLanguage
from typing import DefaultDict as DefaultDict, Any as Any
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
_logger: _Any
RequestSettings: _Any
ServerSideReplayServerSettings: _Any
_g_jwtRequestor: _Any

class UpdatePeriodType(Enum):
    BY_TIME = 'BY_TIME'
    AFTER_BATTLE = 'AFTER_BATTLE'
    NONE = 'NONE'

class IBaseProvider(object):
    def start(self):
        ...
    def stop(self, withClear=False):
        ...

class JwtRequestor(object):
    __jwtData: _Any
    __waitAnswer: _Any
    __callbacks: _Any
    def __init__(self):
        ...
    # decorador original: @adisp_async
    def requestJwt(self, callback):
        ...

class BaseProvider(IBaseProvider):
    _eManager: _Any
    onDataReceived: _Any
    onDataFailed: _Any
    __isStarted: _Any
    __data: _Any
    __webRequester: _Any
    __requester: _Any
    __serverSideRequestsController: _Any
    def __init__(self):
        ...
    def start(self):
        ...
    def stop(self, withClear=False):
        ...
    @property
    def _isEnabled(self):
        ...
    @property
    def _dataNameContainer(self):
        ...
    @property
    def _fakeDataStorage(self):
        ...
    def _getSettings(self):
        ...
    def _dataReceived(self, dataName, data):
        ...
    def _getData(self, dataName, useFake=False, *args, **kwargs):
        ...
    # decorador original: @adisp_process
    def _requestData(self, dataName, useFake=False, *args, **kwargs):
        ...
    # decorador original: @adisp_async
    def _sendRequest(self, ctx, callback, allowDelay=None):
        ...
    def _getSettingsByDataName(self, dataName):
        ...
    def _updateDataCache(self, dataName, updater):
        ...
    @staticmethod
    def __isRequestingAvailable(settings, dataObj):
        ...

def _webUrlFetcher(url, callback, headers=None, timeout=30.0, method='GET', postData=''):
    ...
