# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/periodic_battles/prb_control/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl import backport as backport
from gui.prb_control.ctrl_events import g_prbCtrlEvents as g_prbCtrlEvents
from gui.prb_control.entities.base.pre_queue.entity import PreQueueEntryPoint as PreQueueEntryPoint
from gui.prb_control.settings import PRE_QUEUE_JOIN_ERRORS as PRE_QUEUE_JOIN_ERRORS
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from gui import SystemMessages as SystemMessages

class PeriodicEntryPoint(PreQueueEntryPoint):
    _RES_ROOT = None
    _controller = None
    def select(self, ctx, callback=None):
        ...
