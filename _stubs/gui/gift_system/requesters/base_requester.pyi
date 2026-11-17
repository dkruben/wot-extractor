# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/gift_system/requesters/base_requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process, adisp_async as adisp_async

class IGiftSystemRequester(object):
    def destroy(self):
        ...
    def isProcessing(self):
        ...
    def request(self, eventIds):
        ...
    def stop(self):
        ...

class GiftSystemBaseRequester(IGiftSystemRequester):
    __slots__: tuple
    __isProcessing: Any
    __reqEventIds: Any
    __callbackID: Any
    __readyCallback: Any
    def __init__(self, readyCallback):
        ...
    def destroy(self):
        ...
    def isProcessing(self):
        ...
    def request(self, eventIds):
        ...
    def stop(self):
        ...
    def _getInvokeDelay(self):
        ...
    # decorador original: @adisp_async
    def _doExternalRequest(self, reqEventIds, callback):
        ...
    # decorador original: @adisp_process
    def __invoke(self):
        ...
