# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/prb_control/entities/epic/pre_queue/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from frontline.gui.prb_control.entities.epic.pre_queue.actions_validator import EpicActionsValidator as EpicActionsValidator
from frontline.gui.prb_control.entities.epic.pre_queue.ctx import EpicQueueCtx as EpicQueueCtx
from frontline.gui.prb_control.entities.epic.pre_queue.permissions import EpicPermissions as EpicPermissions
from frontline.gui.prb_control.entities.epic.pre_queue.scheduler import EpicMetaScheduler as EpicMetaScheduler
from frontline.gui.prb_control.entities.epic.pre_queue.vehicles_watcher import EpicVehiclesWatcher as EpicVehiclesWatcher
from frontline.gui.prb_control.entities.epic.squad.entity import EpicSquadEntryPoint as EpicSquadEntryPoint
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import QUEUE_TYPE as QUEUE_TYPE
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui import SystemMessages as SystemMessages
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as SYSTEM_MESSAGES
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from gui.prb_control.ctrl_events import g_prbCtrlEvents as g_prbCtrlEvents
from gui.prb_control.entities.base import vehicleAmmoCheck as vehicleAmmoCheck
from gui.prb_control.entities.base.pre_queue.entity import PreQueueEntryPoint as PreQueueEntryPoint, PreQueueEntity as PreQueueEntity, PreQueueSubscriber as PreQueueSubscriber
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.items import SelectResult as SelectResult
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, PRE_QUEUE_JOIN_ERRORS as PRE_QUEUE_JOIN_ERRORS
from gui.prb_control.storages import prequeue_storage_getter as prequeue_storage_getter
from helpers import dependency as dependency, i18n as i18n
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController

class EpicEntryPoint(PreQueueEntryPoint):
    __epicController: Any
    __connectionMgr: Any
    def __init__(self):
        ...
    def select(self, ctx, callback=None):
        ...

class EpicEntity(PreQueueEntity):
    __settingsCore: Any
    __epicController: Any
    __watcher: Any
    storage: Any
    def __init__(self):
        ...
    def init(self, ctx=None):
        ...
    def fini(self, ctx=None, woEvents=False):
        ...
    def leave(self, ctx, callback=None):
        ...
    def getQueueType(self):
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
