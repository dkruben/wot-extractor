# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/prb_control/entities/pre_queue/ctx.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.prb_control.entities.base.pre_queue.ctx import QueueCtx as QueueCtx
from gui.shared.utils.decorators import ReprInjector as ReprInjector

# decorador original: @ReprInjector.withParent(...)
class Comp7QueueCtx(QueueCtx):
    __vInventoryID: Any
    def __init__(self, entityType, vInventoryID, waitingID=''):
        ...
    def getVehicleInventoryID(self):
        ...
