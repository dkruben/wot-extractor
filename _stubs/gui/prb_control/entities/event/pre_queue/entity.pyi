# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/event/pre_queue/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from constants import QUEUE_TYPE as QUEUE_TYPE
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.entities.base.pre_queue.entity import PreQueueEntryPoint as PreQueueEntryPoint, PreQueueEntity as PreQueueEntity, PreQueueSubscriber as PreQueueSubscriber
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from gui.prb_control.items import SelectResult as SelectResult
from gui.prb_control.entities.event.pre_queue.ctx import EventBattleQueueCtx as EventBattleQueueCtx
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.prb_control.storages import prequeue_storage_getter as prequeue_storage_getter
from gui.prb_control.entities.event.pre_queue.scheduler import EventScheduler as EventScheduler
from helpers import dependency as dependency
from skeletons.gui.game_control import IEventBattlesController as IEventBattlesController

class EventBattleEntryPoint(PreQueueEntryPoint):
    def __init__(self):
        ...

class EventBattleEntity(PreQueueEntity):
    __eventBattlesCtrl: Any
    storage: Any
    def __init__(self):
        ...
    def init(self, ctx=None):
        ...
    def fini(self, ctx=None, woEvents=False):
        ...
    def doSelectAction(self, action):
        ...
    def leave(self, ctx, callback=None):
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
    def _createScheduler(self):
        ...
