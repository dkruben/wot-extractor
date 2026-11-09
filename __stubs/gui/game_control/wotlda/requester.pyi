# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/wotlda/requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
from BWUtil import AsyncReturn as AsyncReturn
from typing import Dict as Dict, Callable as Callable, Optional as Optional, Tuple as Tuple, Set as Set
import adisp as adisp
from gui.wgcg.loadouts_assistant.context import LoadoutsAssistantCtx as LoadoutsAssistantCtx, EasyTankEquipCtx as EasyTankEquipCtx, GenericLoadoutAssistanceCtx as GenericLoadoutAssistanceCtx
from gui.game_control.wotlda.constants import SupportedWotldaLoadoutType as SupportedWotldaLoadoutType
from gui.game_control.wotlda.response import WotldaResponse as WotldaResponse
from helpers import dependency as dependency
from helpers.time_utils import QUARTER as QUARTER
from skeletons.gui.web import IWebController as IWebController
from wg_async import wg_async as wg_async, await_callback as await_callback, wg_await as wg_await, BrokenPromiseError as BrokenPromiseError, TimeoutError as TimeoutError, delay as delay
_logger: Any

class WotldaRequester(object):
    MAX_REQUEST_RETRIES = 3
    _webController: Any
    _destroyed: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    # decorador original: @wg_async
    def getEasyTankEquipLoadouts(self, clientCacheUpdatedAt):
        ...
    # decorador original: @wg_async
    def getSubscriptionLoadouts(self, clientCacheUpdatedAt, loadoutTypes):
        ...
    # decorador original: @wg_async
    def _getLoadouts(self, context):
        ...
    # decorador original: @adisp.adisp_process
    def _requestLoadouts(self, context, callback):
        ...
