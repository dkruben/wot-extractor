# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/factories/PreQueueFactory.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.prb_control import prb_getters as prb_getters
from constants import QUEUE_TYPE as QUEUE_TYPE
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.shared.system_factory import registerQueueEntity as registerQueueEntity, collectQueueEntity as collectQueueEntity
from gui.shared.system_factory import registerEntryPoint as registerEntryPoint, collectEntryPoint as collectEntryPoint
from gui.prb_control.entities.maps_training.pre_queue.entity import MapsTrainingEntryPoint as MapsTrainingEntryPoint, MapsTrainingEntity as MapsTrainingEntity
from gui.prb_control.factories.ControlFactory import ControlFactory as ControlFactory
from gui.prb_control.entities.winback.pre_queue.entity import WinbackEntryPoint as WinbackEntryPoint, WinbackEntity as WinbackEntity
from gui.prb_control.entities.base.pre_queue.entity import PreQueueEntity as PreQueueEntity
from gui.prb_control.entities.base.pre_queue.ctx import LeavePreQueueCtx as LeavePreQueueCtx
from gui.prb_control.entities.random.pre_queue.entity import RandomEntity as RandomEntity, RandomEntryPoint as RandomEntryPoint
from gui.prb_control.entities.ranked.pre_queue.entity import RankedEntity as RankedEntity, RankedEntryPoint as RankedEntryPoint
from gui.prb_control.entities.mapbox.pre_queue.entity import MapboxEntity as MapboxEntity, MapboxEntryPoint as MapboxEntryPoint
from gui.prb_control.entities.event.pre_queue.entity import EventBattleEntity as EventBattleEntity, EventBattleEntryPoint as EventBattleEntryPoint
from gui.prb_control.items import FunctionalState as FunctionalState
from gui.prb_control.settings import FUNCTIONAL_FLAG as _FLAG
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, CTRL_ENTITY_TYPE as CTRL_ENTITY_TYPE
from gui.prb_control.storages import prequeue_storage_getter as prequeue_storage_getter, storage_getter as storage_getter, RECENT_PRB_STORAGE as RECENT_PRB_STORAGE
__all__: tuple

class PreQueueFactory(ControlFactory):
    rankedStorage: Any
    frontlineStorage: Any
    battleRoyaleStorage: Any
    mapboxStorage: Any
    mapsTrainingStorage: Any
    eventBattlesStorage: Any
    funRandomStorage: Any
    comp7Storage: Any
    comp7LightStorage: Any
    recentPrbStorage: Any
    winbackStorage: Any
    def __init__(self):
        ...
    def createEntry(self, ctx):
        ...
    def createEntryByAction(self, action):
        ...
    def createEntity(self, ctx):
        ...
    def createStateEntity(self, entity):
        ...
    def createLeaveCtx(self, flags=..., entityType=0):
        ...
    def __createByQueueType(self, queueType):
        ...
    def __createDefaultEntity(self):
        ...
