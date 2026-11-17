# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/prb_control/entities/pre_queue/ctx.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from fort_rush_common.fort_rush_constants import QUEUE_TYPE as QUEUE_TYPE
from gui.prb_control.entities.base.pre_queue.ctx import QueueCtx as QueueCtx
from gui.shared.utils.decorators import ReprInjector as ReprInjector

# decorador original: @ReprInjector.withParent(...)
class FortRushBattleQueueCtx(QueueCtx):
    __vehInvID: Any
    def __init__(self, vehInvID, waitingID=''):
        ...
    def getVehicleInventoryID(self):
        ...
