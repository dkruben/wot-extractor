# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/prb_control/entities/regular/pre_queue/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import QUEUE_TYPE as QUEUE_TYPE
from gui.prb_control.entities.base.pre_queue.ctx import JoinPreQueueModeCtx as JoinPreQueueModeCtx
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from gui.prb_control.ctrl_events import g_prbCtrlEvents as g_prbCtrlEvents
from gui.prb_control.entities.base.pre_queue.entity import PreQueueEntity as PreQueueEntity, PreQueueEntryPoint as PreQueueEntryPoint, PreQueueSubscriber as PreQueueSubscriber
from battle_royale.gui.impl.lobby.br_helpers.utils import isBattleResultsStateEntered as isBattleResultsStateEntered
from battle_royale.gui.prb_control.entities.regular.pre_queue.actions_validator import BattleRoyaleActionsValidator as BattleRoyaleActionsValidator
from battle_royale.gui.prb_control.entities.regular.pre_queue.vehicles_watcher import BattleRoyaleVehiclesWatcher as BattleRoyaleVehiclesWatcher
from battle_royale.gui.prb_control.entities.regular.pre_queue.permissions import BattleRoyalePermissions as BattleRoyalePermissions
from battle_royale.gui.prb_control.entities.regular.scheduler import RoyaleScheduler as RoyaleScheduler
from battle_royale.gui.constants import SUB_MODE_ID_KEY as SUB_MODE_ID_KEY, BattleRoyaleSubMode as BattleRoyaleSubMode
from gui.prb_control.entities.special_mode.pre_queue.ctx import SpecialModeQueueCtx as SpecialModeQueueCtx
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.items import SelectResult as SelectResult
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, PRE_QUEUE_JOIN_ERRORS as PRE_QUEUE_JOIN_ERRORS
from gui.prb_control.storages import prequeue_storage_getter as prequeue_storage_getter
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from helpers import dependency as dependency
_logger: Any

class JoinBRPreQueueModeCtx(JoinPreQueueModeCtx):
    __slots__: tuple
    __selectedSubModeID: Any
    def __init__(self, queueType, selectedSubModeID, flags=..., waitingID=''):
        ...
    def getSelectedSubModeID(self):
        ...

class BRQueueCtx(SpecialModeQueueCtx):
    __currentSubModeID: Any
    def __init__(self, entityType, vInventoryID, currentSubModeID, waitingID=''):
        ...
    def getCurrentSubModeID(self):
        ...

class BattleRoyaleEntryPoint(PreQueueEntryPoint):
    __battleRoyaleController: Any
    __selectedSubModeID: Any
    def __init__(self):
        ...
    def setExtData(self, extData):
        ...
    def select(self, ctx, callback=None):
        ...
    def makeDefCtx(self):
        ...
    def _getFilterStates(self):
        ...

class BattleRoyaleEntity(PreQueueEntity):
    __battleRoyaleController: Any
    __watcher: Any
    storage: Any
    def __init__(self):
        ...
    def init(self, ctx=None):
        ...
    def fini(self, ctx=None, woEvents=False):
        ...
    def resetPlayerState(self):
        ...
    def _makeQueueCtxByAction(self, action=None):
        ...
    def doSelectAction(self, action):
        ...
    def getPermissions(self, pID=None, **kwargs):
        ...
    def _createActionsValidator(self):
        ...
    def _createScheduler(self):
        ...
    def _doQueue(self, ctx):
        ...
    def _doDequeue(self, ctx):
        ...
    def _goToHangar(self):
        ...
    def _goToQueueUI(self):
        ...
    def _exitFromQueueUI(self):
        ...
