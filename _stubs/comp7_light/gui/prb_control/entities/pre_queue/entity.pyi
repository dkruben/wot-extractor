# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/prb_control/entities/pre_queue/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import typing as typing
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from comp7_light.gui.comp7_light_constants import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from comp7_light.gui.prb_control.entities.comp7_light_prb_helpers import Comp7LightViewPresenter as Comp7LightViewPresenter
from comp7_light.gui.prb_control.entities.pre_queue.actions_validator import Comp7LightActionsValidator as Comp7LightActionsValidator
from comp7_light.gui.prb_control.entities.pre_queue.ctx import Comp7LightQueueCtx as Comp7LightQueueCtx
from comp7_light.gui.prb_control.entities.pre_queue.permissions import Comp7LightPermissions as Comp7LightPermissions
from comp7_light.gui.prb_control.entities.pre_queue.vehicles_watcher import Comp7LightVehiclesWatcher as Comp7LightVehiclesWatcher
from comp7_light.gui.prb_control.entities.scheduler import Comp7LightScheduler as Comp7LightScheduler
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
from skeletons.gui.game_control import IComp7LightController as IComp7LightController
from soft_exception import SoftException as SoftException
from comp7_light.gui.prb_control.storages.comp7_light_storage import Comp7LightStorage as Comp7LightStorage

class Comp7LightEntryPoint(PreQueueEntryPoint):
    __comp7LightController: Any
    def __init__(self):
        ...
    def select(self, ctx, callback=None):
        ...
    @staticmethod
    def _getUnavailableStates():
        ...

class Comp7LightEntity(PreQueueEntity):
    __comp7LightController: Any
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
    def _createActionsValidator(self):
        ...
    def _createScheduler(self):
        ...
    def _makeQueueCtxByAction(self, action=None):
        ...
    def _doQueue(self, ctx):
        ...
    def _doDequeue(self, ctx):
        ...
    def _goToQueueUI(self):
        ...
    def _exitFromQueueUI(self):
        ...
