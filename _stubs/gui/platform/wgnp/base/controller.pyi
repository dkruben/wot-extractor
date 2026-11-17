# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/wgnp/base/controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import wg_async as wg_async
from BWUtil import AsyncReturn as AsyncReturn
from gui.platform.base.controller import PlatformRequestController as PlatformRequestController
from gui.platform.base.settings import REQUEST_TIMEOUT as REQUEST_TIMEOUT
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.platform.wgnp_controllers import IWGNPRequestController as IWGNPRequestController
from gui.platform.base.request import Params as Params
from helpers.server_settings import _Wgnp as _Wgnp

class WGNPRequestController(PlatformRequestController, IWGNPRequestController):
    lobbyContext: Any
    @property
    def settings(self):
        ...
    # decorador original: @wg_async.wg_async
    def _request(self, params, timeout=..., waitingID=None):
        ...
