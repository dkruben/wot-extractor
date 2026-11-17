# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/prb_control/entities/epic/pre_queue/scheduler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from gui.prb_control.entities.base.pre_queue.ctx import LeavePreQueueCtx as LeavePreQueueCtx
from gui.prb_control.entities.base.scheduler import BaseScheduler as BaseScheduler
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class EpicMetaScheduler(BaseScheduler):
    __epicController: Any
    __lobbyContext: Any
    __isPrimeTime: Any
    __isCycle: Any
    __validVehicleLevels: Any
    __unlockableInBattleVehicleLevels: Any
    def __init__(self, entity):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def __onPrimeTimeUpdated(self, status):
        ...
    def __onEpicSettingsUpdated(self, diff):
        ...
    def __checkEpicIsEnabled(self):
        ...
    def __doLeave(self):
        ...
