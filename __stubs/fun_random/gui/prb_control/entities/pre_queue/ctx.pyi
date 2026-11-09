# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/prb_control/entities/pre_queue/ctx.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import QUEUE_TYPE as QUEUE_TYPE
from gui.prb_control.entities.base.pre_queue.ctx import QueueCtx as QueueCtx, JoinPreQueueModeCtx as JoinPreQueueModeCtx
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from gui.shared.utils.decorators import ReprInjector as ReprInjector

# decorador original: @ReprInjector.withParent(...)
class FunRandomQueueCtx(QueueCtx):
    __slots__: tuple
    __desiredSubModeID: Any
    __vInventoryID: Any
    def __init__(self, vInventoryID, desiredSubModeID, waitingID=''):
        ...
    def getDesiredSubModeID(self):
        ...
    def getVehicleInventoryID(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class JoinFunPreQueueModeCtx(JoinPreQueueModeCtx):
    __slots__: tuple
    __desiredSubModeID: Any
    def __init__(self, queueType, desiredSubModeID, flags=..., waitingID=''):
        ...
    def getDesiredSubModeID(self):
        ...
