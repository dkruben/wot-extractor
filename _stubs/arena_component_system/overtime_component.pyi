# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/arena_component_system/overtime_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from arena_component_system.client_arena_component_system import ClientArenaComponent as ClientArenaComponent
from constants import ARENA_SYNC_OBJECTS as ARENA_SYNC_OBJECTS
import Event as Event
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer

class OvertimeComponent(ClientArenaComponent, CallbackDelayer):
    duration: Any
    endTime: Any
    isActive: Any
    __duration: Any
    __endTime: Any
    __isActive: Any
    __cbId: Any
    onOvertimeStart: Any
    onOvertimeOver: Any
    def __init__(self, componentSystem):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def destroy(self):
        ...
    def __onDurationUpdated(self, duration):
        ...
    def __onEndTimeUpdated(self, endTime):
        ...
    def __onDataChanged(self):
        ...
    def __startOvertime(self):
        ...
    def __endOvertime(self):
        ...
