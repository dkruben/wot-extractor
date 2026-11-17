# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/requesters/TokenRequester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import time as time
from functools import partial as partial
from future.moves import pickle as pickle
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from constants import REQUEST_COOLDOWN as REQUEST_COOLDOWN, TOKEN_TYPE as TOKEN_TYPE
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from gui.shared.utils.requesters.TokenResponse import TokenResponse as TokenResponse
from helpers import isPlayerAccount as isPlayerAccount
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
_logger: Any
_tokenRqs: dict

class TokenRequester(object):
    __idsGen: Any
    __tokenType: Any
    __callback: Any
    __lastResponse: Any
    __requestID: Any
    __cache: Any
    __timeoutCbID: Any
    __lastRequestTime: Any
    __wrapper: Any
    def __init__(self, tokenType, wrapper=..., cache=True):
        ...
    def lastResponseDelta(self):
        ...
    def isInProcess(self):
        ...
    def clear(self):
        ...
    def getReqCoolDown(self):
        ...
    def canAllowRequest(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def request(self, timeout=None, callback=None, allowDelay=False):
        ...
    def _getRequester(self):
        ...
    def _onTokenReceived(self, requestID, tokenType, data):
        ...
    def _loadTimeout(self, requestID, tokenType, timeout):
        ...
    def __clearTimeoutCb(self):
        ...
    def __onTimeout(self, requestID, tokenType):
        ...

def _getAccountRepository():
    ...
def getTokenRequester(tokenType):
    ...
def fini():
    ...
