# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/random/pre_queue/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import ArenaType as ArenaType
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from account_helpers import gameplay_ctx as gameplay_ctx
from constants import QUEUE_TYPE as QUEUE_TYPE
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.entities.base import vehicleAmmoCheck as vehicleAmmoCheck
from gui.prb_control.entities.base.pre_queue.entity import PreQueueEntryPoint as PreQueueEntryPoint, PreQueueEntity as PreQueueEntity, PreQueueSubscriber as PreQueueSubscriber
from gui.prb_control.entities.base.pre_queue.vehicles_watcher import BaseVehiclesWatcher as BaseVehiclesWatcher
from gui.prb_control.entities.random.pre_queue.ctx import RandomQueueCtx as RandomQueueCtx
from gui.prb_control.items import SelectResult as SelectResult
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from soft_exception import SoftException as SoftException

class RandomEntryPoint(PreQueueEntryPoint):
    def __init__(self):
        ...

class RandomEntity(PreQueueEntity):
    __watcher: Any
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
