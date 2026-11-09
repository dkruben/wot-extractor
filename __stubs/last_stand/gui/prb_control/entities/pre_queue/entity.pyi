# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/prb_control/entities/pre_queue/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from last_stand.gui.prb_control.entities import vehicleAbilitiesCheck as vehicleAbilitiesCheck
from last_stand.gui.prb_control.entities.pre_queue.actions_validator import LastStandActionsValidator as LastStandActionsValidator
from last_stand.gui.prb_control.entities.pre_queue.ctx import LastStandQueueCtx as LastStandQueueCtx
from last_stand.gui.prb_control.entities.pre_queue.scheduler import LastStandBattleScheduler as LastStandBattleScheduler
from last_stand.gui.ls_account_settings import getFirstNewStatusUnlockLevel as getFirstNewStatusUnlockLevel
from last_stand.gui.ls_gui_constants import DifficultyLevel as DifficultyLevel, FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from last_stand.skeletons.ls_vehicle_selection_controller import ILSVehicleSelectionController as ILSVehicleSelectionController
from last_stand.gui.prb_control.entities.vehicles_watcher import VehiclesWatcher as VehiclesWatcher
from last_stand.gui.shared.event_dispatcher import showHangar as showHangar
from last_stand.skeletons.difficulty_level_controller import IDifficultyLevelController as IDifficultyLevelController
from last_stand_common.last_stand_constants import QUEUE_TYPE as QUEUE_TYPE
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.storages import storage_getter as storage_getter, RECENT_PRB_STORAGE as RECENT_PRB_STORAGE
from gui.prb_control.entities.base.pre_queue.entity import PreQueueSubscriber as PreQueueSubscriber, PreQueueEntryPoint as PreQueueEntryPoint, PreQueueEntity as PreQueueEntity
from gui.prb_control.items import SelectResult as SelectResult
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from helpers import dependency as dependency
from last_stand.skeletons.ls_controller import ILSController as ILSController

class LastStandEntryPoint(PreQueueEntryPoint):
    __difficultyLevelCtrl: Any
    def __init__(self):
        ...

class LastStandEntity(PreQueueEntity):
    lsCtrl: Any
    lsVehicleCtrl: Any
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
    def _updateVehiclesWatcher(self):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def canSelectPrbEntity(ctrl=None):
    ...
