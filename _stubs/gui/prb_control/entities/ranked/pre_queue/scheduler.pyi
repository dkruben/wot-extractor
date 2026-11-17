# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/ranked/pre_queue/scheduler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen import R as R
from gui.periodic_battles.prb_control.scheduler import PeriodicScheduler as PeriodicScheduler
from helpers import dependency as dependency
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController

class RankedScheduler(PeriodicScheduler):
    __rankedController: Any
    def _getController(self):
        ...
    def _getResRoot(self):
        ...
