# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/random/pre_queue/ctx.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import QUEUE_TYPE as QUEUE_TYPE
from gui.prb_control.entities.base.pre_queue.ctx import QueueCtx as QueueCtx
from gui.shared.utils.decorators import ReprInjector as ReprInjector

# decorador original: @ReprInjector.withParent(...)
class RandomQueueCtx(QueueCtx):
    __vInventoryID: Any
    __arenaTypeID: Any
    __gamePlayMask: Any
    def __init__(self, vInventoryID, arenaTypeID=0, gamePlayMask=0, waitingID=''):
        ...
    def getVehicleInventoryID(self):
        ...
    def getDemoArenaTypeID(self):
        ...
    def getGamePlayMask(self):
        ...
