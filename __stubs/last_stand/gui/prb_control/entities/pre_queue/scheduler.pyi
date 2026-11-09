# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/prb_control/entities/pre_queue/scheduler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.prb_control.entities.base.scheduler import BaseScheduler as BaseScheduler
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from shared_utils import nextTick as nextTick
from helpers import dependency as dependency
from last_stand.skeletons.ls_controller import ILSController as ILSController

class LastStandBattleScheduler(BaseScheduler):
    lsCtrl: Any
    _isLeaveRequestSent: Any
    def __init__(self, entity):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def _doLeave(self):
        ...
    def _showRandomHangar(self):
        ...
    def __onEventDisabled(self):
        ...
    def __onSettingsUpdate(self):
        ...
