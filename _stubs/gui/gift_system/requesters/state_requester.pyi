# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/gift_system/requesters/state_requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from gui.gift_system.requesters.base_requester import GiftSystemBaseRequester as GiftSystemBaseRequester
from gui.wgcg.gift_system.contexts import GiftSystemStateCtx as GiftSystemStateCtx
from helpers import dependency as dependency
from helpers.time_utils import ONE_MINUTE as ONE_MINUTE
from skeletons.gui.web import IWebController as IWebController
_WGCG_AVAILABILITY = 2
_WGGG_AVAILABILITY = ONE_MINUTE

class GiftSystemWebStateRequester(GiftSystemBaseRequester):
    __slots__: tuple
    __webController: Any
    def _getInvokeDelay(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def _doExternalRequest(self, reqEventIds, callback):
        ...
