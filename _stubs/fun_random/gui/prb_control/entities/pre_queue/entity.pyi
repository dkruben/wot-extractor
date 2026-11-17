# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/prb_control/entities/pre_queue/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import QUEUE_TYPE as QUEUE_TYPE
from fun_random_common.fun_constants import FUN_EVENT_ID_KEY as FUN_EVENT_ID_KEY, UNKNOWN_EVENT_ID as UNKNOWN_EVENT_ID
from fun_random.gui.feature.util.fun_helpers import notifyCaller as notifyCaller
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin
from fun_random.gui.fun_gui_constants import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from fun_random.gui.prb_control.entities.pre_queue.actions_validator import FunRandomActionsValidator as FunRandomActionsValidator
from fun_random.gui.prb_control.entities.pre_queue.ctx import FunRandomQueueCtx as FunRandomQueueCtx, JoinFunPreQueueModeCtx as JoinFunPreQueueModeCtx
from fun_random.gui.prb_control.entities.pre_queue.permissions import FunRandomPermissions as FunRandomPermissions
from fun_random.gui.prb_control.entities.pre_queue.scheduler import FunRandomScheduler as FunRandomScheduler
from fun_random.gui.prb_control.entities.pre_queue.vehicles_watcher import FunRandomVehiclesWatcher as FunRandomVehiclesWatcher
from fun_random.gui.prb_control.entities.squad.entity import FunRandomSquadEntryPoint as FunRandomSquadEntryPoint
from gui.prb_control.ctrl_events import g_prbCtrlEvents as g_prbCtrlEvents
from gui.prb_control.entities.base import vehicleAmmoCheck as vehicleAmmoCheck
from gui.prb_control.entities.base.pre_queue.entity import PreQueueEntryPoint as PreQueueEntryPoint, PreQueueSubscriber as PreQueueSubscriber, PreQueueEntity as PreQueueEntity
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.items import SelectResult as SelectResult
from gui.prb_control.settings import PRE_QUEUE_JOIN_ERRORS as PRE_QUEUE_JOIN_ERRORS
from helpers import dependency as dependency
from skeletons.gui.game_control import IFunRandomController as IFunRandomController
_logger: Any

class FunRandomEntryPoint(PreQueueEntryPoint):
    __funRandomController: Any
    __desiredSubModeID: Any
    def __init__(self):
        ...
    def setExtData(self, extData):
        ...
    def makeDefCtx(self):
        ...
    def select(self, ctx, callback=None):
        ...
    def __abortSelection(self, reason, callback=None):
        ...

class FunRandomEntity(PreQueueEntity, FunAssetPacksMixin):
    __watcher: Any
    def __init__(self):
        ...
    def init(self, ctx=None):
        ...
    def fini(self, ctx=None, woEvents=False):
        ...
    def getPermissions(self, pID=None, **kwargs):
        ...
    def doSelectAction(self, action):
        ...
    def leave(self, ctx, callback=None):
        ...
    # decorador original: @vehicleAmmoCheck
    def queue(self, ctx, callback=None):
        ...
    def _createActionsValidator(self):
        ...
    def _createScheduler(self):
        ...
    def _doQueue(self, ctx):
        ...
    def _doDequeue(self, ctx):
        ...
    def _goToQueueUI(self):
        ...
    def _exitFromQueueUI(self):
        ...
    def _makeQueueCtxByAction(self, action=None):
        ...
