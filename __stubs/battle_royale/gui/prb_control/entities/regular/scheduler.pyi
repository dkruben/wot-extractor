# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/prb_control/entities/regular/scheduler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui import SystemMessages as SystemMessages
from gui.prb_control.entities.base.scheduler import BaseScheduler as BaseScheduler
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController

class RoyaleScheduler(BaseScheduler):
    __battleRoyaleController: Any
    __isPrimeTime: Any
    def __init__(self, entity):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def __update(self, status):
        ...
