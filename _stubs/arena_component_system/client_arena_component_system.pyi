# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/arena_component_system/client_arena_component_system.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from future.moves import pickle as pickle
from future.utils import viewitems as viewitems
import Event as Event
from arena_component_system.arena_sync_object import ArenaSyncObject as ArenaSyncObject
from components_base.component import Component as Component
from components_base.component_controller import ComponentController as ComponentController
from constants import ARENA_UPDATE as ARENA_UPDATE, ARENA_SYNC_OBJECT_NAMES as ARENA_SYNC_OBJECT_NAMES
from debug_utils import LOG_ERROR as LOG_ERROR

class ClientArenaComponent(Component):
    _componentSystem: Any
    _onUpdate: Any
    _eventManager: Any
    def __init__(self, componentSystem):
        ...
    def destroy(self):
        ...
    def update(self, updateType, argStr):
        ...
    def addSyncDataCallback(self, syncDataObjectType, key, handler):
        ...
    def removeSyncDataCallback(self, syncDataObjectType, key, handler):
        ...
    def getSyncDataObjectData(self, syncDataObjectType, key):
        ...

class ClientArenaComponentSystem(ComponentController):
    bonusType: Any
    arenaType: Any
    arena: Any
    _onUpdate: Any
    __syncDataObjects: Any
    def __init__(self, arena, bonusType, arenaType):
        ...
    def destroy(self):
        ...
    def update(self, updateType, argStr):
        ...
    def addSyncDataObjectCallback(self, syncDataObjectType, key, handler):
        ...
    def removeSyncDataObjectCallback(self, syncDataObjectType, key, handler):
        ...
    def getSyncDataObjectData(self, syncDataObjectType, key):
        ...
    def __onFullSyncObjectReceived(self, argStr):
        ...
    def __onSyncObjectUpdateReceived(self, argStr):
        ...
