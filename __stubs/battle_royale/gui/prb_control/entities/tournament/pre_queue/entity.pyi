# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/prb_control/entities/tournament/pre_queue/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from battle_royale.gui.impl.lobby.views.states import BattleRoyaleTournamentQueueState as BattleRoyaleTournamentQueueState
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from CurrentVehicle import g_currentVehicle as g_currentVehicle, g_currentPreviewVehicle as g_currentPreviewVehicle
from constants import QUEUE_TYPE as QUEUE_TYPE
from helpers import dependency as dependency
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from skeletons.gui.game_control import IBattleRoyaleTournamentController as IBattleRoyaleTournamentController
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from gui.prb_control.ctrl_events import g_prbCtrlEvents as g_prbCtrlEvents
from gui.prb_control.entities.base.pre_queue.entity import PreQueueEntity as PreQueueEntity, PreQueueEntryPoint as PreQueueEntryPoint, PreQueueSubscriber as PreQueueSubscriber
from battle_royale.gui.prb_control.entities.tournament.pre_queue.action_validator import BattleRoyaleTournamentActionsValidator as BattleRoyaleTournamentActionsValidator
from battle_royale.gui.prb_control.entities.regular.pre_queue.vehicles_watcher import BattleRoyaleVehiclesWatcher as BattleRoyaleVehiclesWatcher
from battle_royale.gui.prb_control.entities.tournament.pre_queue.permissions import BattleRoyaleTournamentPermissions as BattleRoyaleTournamentPermissions
from gui.prb_control.entities.special_mode.pre_queue.ctx import SpecialModeQueueCtx as SpecialModeQueueCtx
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, PRE_QUEUE_JOIN_ERRORS as PRE_QUEUE_JOIN_ERRORS
from gui.prb_control.storages import prequeue_storage_getter as prequeue_storage_getter
_logger: Any

class BattleRoyaleTournamentEntryPoint(PreQueueEntryPoint):
    __battleRoyaleTournamentController: Any
    def __init__(self):
        ...
    def select(self, ctx, callback=None):
        ...
    def _getFilterStates(self):
        ...

class BattleRoyaleTournamentEntity(PreQueueEntity):
    __battleRoyaleTournamentController: Any
    __gui: Any
    __watcher: Any
    __prebatleWindow: Any
    storage: Any
    def __init__(self):
        ...
    def init(self, ctx=None):
        ...
    def isPlayerJoined(self, ctx):
        ...
    def canInvite(self, prbType):
        ...
    def resetPlayerState(self):
        ...
    def showGUI(self, ctx=None):
        ...
    def fini(self, ctx=None, woEvents=False):
        ...
    def _makeQueueCtxByAction(self, action=None):
        ...
    def getPermissions(self, pID=None, **kwargs):
        ...
    def _createActionsValidator(self):
        ...
    def _doQueue(self, ctx):
        ...
    def _doDequeue(self, ctx):
        ...
    def _goToQueueUI(self):
        ...
    def _exitFromQueueUI(self):
        ...
    @staticmethod
    def __findSpectatorPreBattleView(view):
        ...
