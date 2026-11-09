# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/gift_system/requesters/history_requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BigWorld as BigWorld
from adisp import adisp_async as adisp_async
from constants import REQUEST_COOLDOWN as REQUEST_COOLDOWN
from gui.gift_system.requesters.base_requester import GiftSystemBaseRequester as GiftSystemBaseRequester

class GiftSystemHistoryRequester(GiftSystemBaseRequester):
    __slots__: tuple
    def _getInvokeDelay(self):
        ...
    # decorador original: @adisp_async
    def _doExternalRequest(self, reqEventIds, callback):
        ...
