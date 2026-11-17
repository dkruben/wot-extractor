# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/prb_control/entities/scheduler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process
from gui import SystemMessages as SystemMessages
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from gui.prb_control import prbDispatcherProperty as prbDispatcherProperty
from gui.prb_control.entities.base.ctx import LeavePrbAction as LeavePrbAction
from gui.prb_control.entities.base.scheduler import BaseScheduler as BaseScheduler
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

class Comp7Scheduler(BaseScheduler):
    comp7Controller: Any
    __isPrimeTime: Any
    __hasPrimeTimePeripheries: Any
    def __init__(self, entity):
        ...
    # decorador original: @prbDispatcherProperty
    def prbDispatcher(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def __checkLeave(self):
        ...
    # decorador original: @adisp_process
    def __doLeave(self):
        ...
    def __update(self, status):
        ...
