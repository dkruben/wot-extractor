# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/maps_training/pre_queue/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from constants import QUEUE_TYPE as QUEUE_TYPE
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui.prb_control.entities.base.pre_queue.entity import PreQueueEntity as PreQueueEntity, PreQueueEntryPoint as PreQueueEntryPoint, PreQueueSubscriber as PreQueueSubscriber
from gui.prb_control.entities.maps_training.pre_queue.actions_validator import MapsTrainingActionsValidator as MapsTrainingActionsValidator
from gui.prb_control.entities.maps_training.pre_queue.ctx import MapsTrainingQueueCtx as MapsTrainingQueueCtx
from gui.prb_control.entities.maps_training.pre_queue.permissions import MapsTrainingPermissions as MapsTrainingPermissions
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.items import SelectResult as SelectResult
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from gui.prb_control.storages import prequeue_storage_getter as prequeue_storage_getter
from helpers import dependency as dependency
from skeletons.gui.game_control import IMapsTrainingController as IMapsTrainingController

class MapsTrainingEntryPoint(PreQueueEntryPoint):
    def __init__(self):
        ...

class MapsTrainingEntity(PreQueueEntity):
    _QUEUE_TIMEOUT_MSG_KEY = '#maps_training:arena_start_errors/prb/kick/timeout'
    mapsTrainingController: Any
    storage: Any
    def __init__(self):
        ...
    def init(self, ctx=None):
        ...
    def leave(self, ctx, callback=None):
        ...
    def doSelectAction(self, action):
        ...
    def getPermissions(self, pID=None, **kwargs):
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
    def _createActionsValidator(self):
        ...
    def _isNeedToShowSystemMessage(self):
        ...
