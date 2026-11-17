# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/prb_control/entities/pre_queue/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import typing as typing
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from comp7.gui.comp7_constants import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from comp7.gui.prb_control.entities.comp7_prb_helpers import Comp7ViewPresenter as Comp7ViewPresenter
from comp7.gui.prb_control.entities.pre_queue.actions_validator import Comp7ActionsValidator as Comp7ActionsValidator
from comp7.gui.prb_control.entities.pre_queue.ctx import Comp7QueueCtx as Comp7QueueCtx
from comp7.gui.prb_control.entities.pre_queue.permissions import Comp7Permissions as Comp7Permissions
from comp7.gui.prb_control.entities.pre_queue.vehicles_watcher import Comp7VehiclesWatcher as Comp7VehiclesWatcher
from comp7.gui.prb_control.entities.scheduler import Comp7Scheduler as Comp7Scheduler
from constants import QUEUE_TYPE as QUEUE_TYPE
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from gui.prb_control.ctrl_events import g_prbCtrlEvents as g_prbCtrlEvents
from gui.prb_control.entities.base import vehicleAmmoCheck as vehicleAmmoCheck
from gui.prb_control.entities.base.pre_queue.entity import PreQueueEntity as PreQueueEntity, PreQueueEntryPoint as PreQueueEntryPoint, PreQueueSubscriber as PreQueueSubscriber
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.items import SelectResult as SelectResult
from gui.prb_control.settings import PRE_QUEUE_JOIN_ERRORS as PRE_QUEUE_JOIN_ERRORS
from gui.prb_control.storages import prequeue_storage_getter as prequeue_storage_getter
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from soft_exception import SoftException as SoftException
from comp7.gui.prb_control.storages.comp7_storage import Comp7Storage as Comp7Storage

class Comp7EntryPoint(PreQueueEntryPoint):
    __comp7Controller: Any
    def __init__(self):
        ...
    def select(self, ctx, callback=None):
        ...
    @staticmethod
    def _getUnavailableStates():
        ...

class Comp7Entity(PreQueueEntity):
    __comp7Controller: Any
    __watcher: Any
    __introPresenter: Any
    storage: Any
    def __init__(self):
        ...
    def init(self, ctx=None):
        ...
    def fini(self, ctx=None, woEvents=False):
        ...
    def leave(self, ctx, callback=None):
        ...
    def doSelectAction(self, action):
        ...
    def getPermissions(self, *_):
        ...
    # decorador original: @vehicleAmmoCheck
    def queue(self, ctx, callback=None):
        ...
    def _makeQueueCtxByAction(self, action=None):
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
