# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/entitlements/entitlements_requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import copy as copy
import logging as logging
import typing as typing
from adisp import adisp_process as adisp_process
from gui.wgcg.agate.contexts import AgateGetInventoryEntitlementsCtx as AgateGetInventoryEntitlementsCtx
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from skeletons.gui.web import IWebController as IWebController
from typing import List as List
_logger: Any

class EntitlementsRequester(object):
    __requests: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def requestByCodes(self, codes, retryTimes=None, callback=None):
        ...
    def __onRequestDone(self, ctx):
        ...
    def __findRequest(self, ctx):
        ...

class _EntitlementsRequest(object):
    __DEFAULT_RETRY_TIMES: list
    __web: Any
    __ctx: Any
    __retryTimes: Any
    __callbacks: Any
    __onFinished: Any
    __delayer: Any
    def __init__(self, ctx, callback, retryTimes, finishedCallback):
        ...
    def clear(self):
        ...
    def hasSameContext(self, ctx):
        ...
    def addCallback(self, callback):
        ...
    # decorador original: @adisp_process
    def send(self):
        ...
    def __getDelayer(self):
        ...
    def __sendResult(self, isSuccess, result):
        ...
    def __skipRetry(self, response):
        ...
    def __getNextRetryTime(self):
        ...
    def __clear(self):
        ...
    @staticmethod
    def __formatResult(result):
        ...
