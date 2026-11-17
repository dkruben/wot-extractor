# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/event/squad/scheduler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from adisp import adisp_process as adisp_process
from gui.prb_control import prbDispatcherProperty as prbDispatcherProperty
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from gui.prb_control.entities.event.pre_queue.scheduler import EventScheduler as EventScheduler
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME

class EventSquadScheduler(EventScheduler):
    # decorador original: @prbDispatcherProperty
    def prbDispatcher(self):
        ...
    def _doLeave(self):
        ...
    # decorador original: @adisp_process
    def _doSelect(self, actionName):
        ...
