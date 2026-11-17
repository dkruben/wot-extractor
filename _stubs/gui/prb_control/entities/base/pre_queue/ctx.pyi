# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/base/pre_queue/ctx.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.prb_control.entities.base.ctx import PrbCtrlRequestCtx as PrbCtrlRequestCtx
from gui.prb_control.settings import CTRL_ENTITY_TYPE as CTRL_ENTITY_TYPE, REQUEST_TYPE as REQUEST_TYPE
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from gui.shared.utils.decorators import ReprInjector as ReprInjector

class _PreQueueRequestCtx(PrbCtrlRequestCtx):
    def __init__(self, **kwargs):
        ...

class QueueCtx(_PreQueueRequestCtx):
    def getRequestType(self):
        ...

class DequeueCtx(_PreQueueRequestCtx):
    def getRequestType(self):
        ...

class JoinPreQueueModeCtx(_PreQueueRequestCtx):
    def __init__(self, queueType, flags=..., waitingID=''):
        ...
    def getID(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class LeavePreQueueCtx(_PreQueueRequestCtx):
    def getRequestType(self):
        ...
