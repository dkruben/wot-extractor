# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/base/controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import wg_async as wg_async
from BWUtil import AsyncReturn as AsyncReturn
from gui.platform.base import logger as logger
from gui.platform.base.requester import PlatformRequester as PlatformRequester
from gui.platform.base.settings import REQUEST_TIMEOUT as REQUEST_TIMEOUT
from helpers import dependency as dependency
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.platform.controller import IPlatformRequestController as IPlatformRequestController
from gui.platform.base.request import Params as Params

class PlatformRequestController(IPlatformRequestController):
    connectionMgr: Any
    _requester: Any
    _logger: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    # decorador original: @wg_async.wg_async
    def _request(self, params, timeout=..., waitingID=None):
        ...
    def _start(self):
        ...
    def _stop(self):
        ...
