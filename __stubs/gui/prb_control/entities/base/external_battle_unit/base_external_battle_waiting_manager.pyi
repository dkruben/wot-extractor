# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/base/external_battle_unit/base_external_battle_waiting_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.prb_control.settings import REQUEST_TYPE as REQUEST_TYPE
REQUEST_HANDLER: set
_logger: Any

class BaseExternalUnitWaitingManager(object):
    __waitingRequestID: Any
    __waitingID: Any
    def __init__(self):
        ...
    def processRequest(self, ctx):
        ...
    def stopRequest(self):
        ...
    def onResponseWebReqID(self, webReqID):
        ...
    def onResponseError(self):
        ...
    def __processResponse(self, requestID):
        ...
