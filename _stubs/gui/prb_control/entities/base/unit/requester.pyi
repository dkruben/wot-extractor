# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/base/unit/requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from UnitBase import UNIT_ERROR as UNIT_ERROR
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.prb_control import prb_getters as prb_getters
from gui.prb_control.entities.base.requester import IUnitRequestProcessor as IUnitRequestProcessor

class UnitRequestProcessor(IUnitRequestProcessor):
    __slots__: tuple
    __requests: Any
    __entity: Any
    def __init__(self, entity):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def doRequest(self, ctx, methodName, *args, **kwargs):
        ...
    def doRequestChain(self, ctx, chain):
        ...
    def doRawRequest(self, methodName, *args, **kwargs):
        ...
    def unitMgr_onUnitResponseReceived(self, requestID):
        ...
    def unitMgr_onUnitErrorReceived(self, requestID, unitMgrID, errorCode, errorStr):
        ...
    def _sendRequest(self, ctx, methodName, chain, *args, **kwargs):
        ...
    def _sendNextRequest(self, ctx, chain):
        ...
    def _onResponseReceived(self, requestID, result):
        ...
