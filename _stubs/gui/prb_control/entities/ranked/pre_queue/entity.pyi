# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/ranked/pre_queue/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import QUEUE_TYPE as QUEUE_TYPE
from gui.impl.gen import R as R
from gui.prb_control.entities.ranked.pre_queue.actions_validator import RankedActionsValidator as RankedActionsValidator
from gui.prb_control.entities.ranked.pre_queue.ctx import RankedQueueCtx as RankedQueueCtx
from gui.prb_control.entities.ranked.pre_queue.permissions import RankedPermissions as RankedPermissions
from gui.prb_control.entities.ranked.pre_queue.vehicles_watcher import RankedVehiclesWatcher as RankedVehiclesWatcher
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.entities.base import vehicleAmmoCheck as vehicleAmmoCheck
from gui.prb_control.entities.base.pre_queue.entity import PreQueueEntity as PreQueueEntity, PreQueueSubscriber as PreQueueSubscriber
from gui.prb_control.entities.ranked.pre_queue.scheduler import RankedScheduler as RankedScheduler
from gui.prb_control.items import SelectResult as SelectResult
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from account_helpers.AccountSettings import AccountSettings as AccountSettings, GUI_START_BEHAVIOR as GUI_START_BEHAVIOR
from gui.prb_control.storages import prequeue_storage_getter as prequeue_storage_getter
from gui.periodic_battles.prb_control.entity import PeriodicEntryPoint as PeriodicEntryPoint
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
from soft_exception import SoftException as SoftException
_logger: Any

class RankedEntryPoint(PeriodicEntryPoint):
    _RES_ROOT = R.strings.system_messages.ranked
    _controller: Any
    def __init__(self):
        ...

class RankedEntity(PreQueueEntity):
    __settingsCore: Any
    __rankedController: Any
    __watcher: Any
    storage: Any
    def __init__(self):
        ...
    def init(self, ctx=None):
        ...
    def fini(self, ctx=None, woEvents=False):
        ...
    def invalidate(self):
        ...
    def leave(self, ctx, callback=None):
        ...
    # decorador original: @vehicleAmmoCheck
    def queue(self, ctx, callback=None):
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
    def _makeQueueCtxByAction(self, action=None):
        ...
    def _goToQueueUI(self):
        ...
    def _exitFromQueueUI(self):
        ...
    def __processWelcome(self):
        ...
