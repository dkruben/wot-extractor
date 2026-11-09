# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/prb_control/entities/squad/scheduler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from fun_random.gui.feature.util.fun_wrappers import hasSpecifiedSubMode as hasSpecifiedSubMode
from fun_random.gui.prb_control.entities.pre_queue.scheduler import FunRandomScheduler as FunRandomScheduler
from gui import SystemMessages as SystemMessages
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency
from PlayerEvents import g_playerEvents as g_playerEvents
from skeletons.gui.game_control import IPlatoonController as IPlatoonController

class FunRandomSquadScheduler(FunRandomScheduler):
    __platoonCtrl: Any
    _FUN_RES_ROOT = R.strings.fun_random.scheduler
    # decorador original: @hasSpecifiedSubMode(...)
    def notifySubModeSwitching(self, subModeID):
        ...
    def _checkControllerLeave(self, controller):
        ...
    def _doLeave(self):
        ...
    def _startListening(self):
        ...
    def _stopListening(self):
        ...
    def __checkLeave(self, *_, **__):
        ...
