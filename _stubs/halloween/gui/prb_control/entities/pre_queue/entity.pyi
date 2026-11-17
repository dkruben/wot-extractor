# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/prb_control/entities/pre_queue/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from halloween.gui.prb_control.entities import vehicleAbilitiesCheck as vehicleAbilitiesCheck
from halloween.gui.prb_control.entities.pre_queue.actions_validator import HalloweenActionsValidator as HalloweenActionsValidator
from halloween.gui.prb_control.entities.pre_queue.ctx import HalloweenQueueCtx as HalloweenQueueCtx
from halloween.gui.prb_control.entities.pre_queue.scheduler import HalloweenBattleScheduler as HalloweenBattleScheduler
from halloween.gui.halloween_gui_constants import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from halloween.gui.prb_control.entities.vehicle_switcher import VehicleSwitcher as VehicleSwitcher
from halloween.gui.prb_control.entities.vehicles_watcher import HalloweenVehiclesWatcher as HalloweenVehiclesWatcher
from halloween.gui.shared.event_dispatcher import showHangar as showHangar
from halloween.skeletons.difficulty_level_controller import IDifficultyLevelController as IDifficultyLevelController
from halloween_common.halloween_constants import QUEUE_TYPE as QUEUE_TYPE
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.storages import storage_getter as storage_getter, RECENT_PRB_STORAGE as RECENT_PRB_STORAGE
from gui.prb_control.entities.base.pre_queue.entity import PreQueueSubscriber as PreQueueSubscriber, PreQueueEntryPoint as PreQueueEntryPoint, PreQueueEntity as PreQueueEntity
from gui.prb_control.items import SelectResult as SelectResult
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from helpers import dependency as dependency
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController

class HalloweenEntryPoint(PreQueueEntryPoint):
    __difficultyLevelCtrl: Any
    def __init__(self):
        ...

class HalloweenEntity(PreQueueEntity, VehicleSwitcher):
    __halloweenCtrl: Any
    __difficultyLevelCtrl: Any
    __watcher: Any
    _queueType: Any
    def __init__(self):
        ...
    # decorador original: @storage_getter(...)
    def storage(self):
        ...
    @property
    def currentQueueType(self):
        ...
    def init(self, ctx=None):
        ...
    def fini(self, ctx=None, woEvents=False):
        ...
    # decorador original: @vehicleAbilitiesCheck
    def queue(self, ctx, callback=None):
        ...
    def doSelectAction(self, action):
        ...
    @property
    def _accountComponent(self):
        ...
    def _doQueue(self, ctx):
        ...
    def _doDequeue(self, ctx):
        ...
    def _goToQueueUI(self):
        ...
    def _exitFromQueueUI(self):
        ...
    def _goToHangar(self):
        ...
    def _makeQueueCtxByAction(self, action=None):
        ...
    def _createActionsValidator(self):
        ...
    def _createScheduler(self):
        ...
    def _updateEntityType(self, *args, **kwargs):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def canSelectPrbEntity(ctrl=None):
    ...
