# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/base/request.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import copy as copy
import hashlib as hashlib
import httplib as httplib
import json as json
import urllib as urllib
import urlparse as urlparse
from functools import partial as partial
from enum import Enum as Enum
import adisp as adisp
import wg_async as wg_async
import BigWorld as BigWorld
import soft_exception as soft_exception
from BWUtil import AsyncReturn as AsyncReturn
from constants import WG_GAMES as WG_GAMES, CURRENT_REALM as CURRENT_REALM
from gui.platform.base.settings import REQUEST_TIMEOUT as REQUEST_TIMEOUT, POLLING_PERIOD as POLLING_PERIOD, POLLING_REQUEST_TIMEOUT as POLLING_REQUEST_TIMEOUT, SOLVE_POW_TIMEOUT as SOLVE_POW_TIMEOUT, ACCEPTED_HTTP_CODES as ACCEPTED_HTTP_CODES
from gui.platform.base import logger as logger
from gui.platform.base.response import PlatformResponse as PlatformResponse
from helpers import dependency as dependency, getClientVersion as getClientVersion
from skeletons.gui.web import IWebController as IWebController
from wotdecorators import noexceptReturn as noexceptReturn

class ContentType(str, Enum):
    JSON = 'application/json'
    FORM_URLENCODED = 'application/x-www-form-urlencoded'
    FORM_DATA = 'multipart/form-data'

class Params(object):
    response = PlatformResponse
    url = ''
    queryParams = None
    headers = None
    method = 'GET'
    postData = None
    auth = True
    proofOfWorkURL = ''
    addUserAgentHeader = True
    _logger: Any
    def __init__(self, urlHost='', powHost=''):
        ...
    def getHash(self):
        ...
    def encodePostData(self):
        ...
    def _prepareUrl(self):
        ...
    def _prepareHeaders(self):
        ...
    def _addHost(self, host, url):
        ...
    def __str__(self):
        ...

class Request(object):
    __slots__: tuple
    webCtrl: Any
    requestId: Any
    isCanceled: Any
    params: Any
    _logger: Any
    def __init__(self, requestId, params):
        ...
    def cancel(self):
        ...
    # decorador original: @wg_async.wg_async
    def send(self):
        ...
    # decorador original: @adisp.adisp_process
    def _getAccessTokenData(self, callback):
        ...
    # decorador original: @wg_async.wg_async
    def _solvePoW(self, response, timeout=None):
        ...
    def _fetchUrl(self, url, headers=None, method='GET', postData=None, callback=...):
        ...
    # decorador original: @wg_async.wg_async
    def _pollResponseCallback(self, callback, response):
        ...
    # decorador original: @noexceptReturn(...)
    def __loadResponse(self, response):
        ...

def _urlFetcher(url, callback, headers=None, timeout=..., method='GET', postData=None):
    ...
def _solvePow(version, complexity, timestamp, resource, extension, randomString, timeout, callback):
    ...
