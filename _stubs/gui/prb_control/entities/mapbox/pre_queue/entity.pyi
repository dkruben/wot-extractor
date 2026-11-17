# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/mapbox/pre_queue/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import QUEUE_TYPE as QUEUE_TYPE
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui.prb_control.ctrl_events import g_prbCtrlEvents as g_prbCtrlEvents
from gui.prb_control.entities.base import vehicleAmmoCheck as vehicleAmmoCheck
from gui.prb_control.entities.base.pre_queue.entity import PreQueueEntity as PreQueueEntity, PreQueueEntryPoint as PreQueueEntryPoint, PreQueueSubscriber as PreQueueSubscriber
from gui.prb_control.entities.mapbox.pre_queue.vehicles_watcher import MapboxVehiclesWatcher as MapboxVehiclesWatcher
from gui.prb_control.entities.mapbox.pre_queue.actions_validator import MapboxActionsValidator as MapboxActionsValidator
from gui.prb_control.entities.mapbox.pre_queue.permissions import MapboxPermissions as MapboxPermissions
from gui.prb_control.entities.mapbox.scheduler import MapboxScheduler as MapboxScheduler
from gui.prb_control.entities.special_mode.pre_queue.ctx import SpecialModeQueueCtx as SpecialModeQueueCtx
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.items import SelectResult as SelectResult
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, PRE_QUEUE_JOIN_ERRORS as PRE_QUEUE_JOIN_ERRORS
from gui.prb_control.storages import prequeue_storage_getter as prequeue_storage_getter
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from helpers import dependency as dependency
from skeletons.gui.game_control import IMapboxController as IMapboxController
from gui.prb_control.storages.mapbox_storage import MapboxStorage as MapboxStorage

class MapboxEntryPoint(PreQueueEntryPoint):
    __mapboxController: Any
    def __init__(self):
        ...
    def select(self, ctx, callback=None):
        ...
    def _getFilterStates(self):
        ...

class MapboxEntity(PreQueueEntity):
    __watcher: Any
    storage: Any
    def __init__(self):
        ...
    def init(self, ctx=None):
        ...
    def fini(self, ctx=None, woEvents=False):
        ...
    # decorador original: @vehicleAmmoCheck
    def queue(self, ctx, callback=None):
        ...
    def doSelectAction(self, action):
        ...
    def getPermissions(self, pID=None, **kwargs):
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
