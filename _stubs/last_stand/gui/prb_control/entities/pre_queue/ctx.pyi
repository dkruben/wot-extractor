# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/prb_control/entities/pre_queue/ctx.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.prb_control.entities.base.pre_queue.ctx import QueueCtx as QueueCtx
from gui.shared.utils.decorators import ReprInjector as ReprInjector

# decorador original: @ReprInjector.withParent(...)
class LastStandQueueCtx(QueueCtx):
    __vehInvID: Any
    def __init__(self, vehInvID, entityType, waitingID=''):
        ...
    def getVehicleInventoryID(self):
        ...
