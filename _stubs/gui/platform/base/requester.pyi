# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/base/requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import sys as sys
import wg_async as wg_async
from BWUtil import AsyncReturn as AsyncReturn
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.platform.base import logger as logger
from gui.platform.base.request import Request as Request
from gui.platform.base.settings import REQUEST_TIMEOUT as REQUEST_TIMEOUT
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from gui.platform.base.request import Params as Params

class Pending(object):
    __slots__: tuple
    _event: Any
    _request: Any
    _response: Any
    _logger: Any
    def __init__(self, request):
        ...
    # decorador original: @wg_async.wg_async
    def wait(self):
        ...
    @property
    def requestId(self):
        ...
    def release(self, response=None):
        ...

class PlatformRequester(object):
    _pendings: Any
    _reqIdGen: Any
    _logger: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    # decorador original: @wg_async.wg_async
    def request(self, params, timeout=..., waitingID=None):
        ...
