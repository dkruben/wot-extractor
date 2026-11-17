# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/mechanic_commands/mechanic_events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import weakref as weakref
from events_containers.common.containers import ClientEventsContainer as ClientEventsContainer
from events_containers.components.common import ClientComponentEventsDebugger as ClientComponentEventsDebugger
from vehicles.mechanics.mechanic_commands.mechanic_interfaces import IMechanicCommandsEventsLogic as IMechanicCommandsEventsLogic
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_commands.mechanic_interfaces import IMechanicCommandsComponent as IMechanicCommandsComponent

class MechanicCommandsEvents(ClientEventsContainer, IMechanicCommandsEventsLogic):
    __componentRef: Any
    onMechanicCommand: Any
    def __init__(self, component):
        ...
    def destroy(self):
        ...
    def processMechanicCommand(self, command):
        ...
    def _getComponent(self):
        ...
    def _createEventsDebugger(self):
        ...

class MechanicCommandsEventsDebugger(ClientComponentEventsDebugger):
    _EVENTS_DEBUG_PREFIX = 'MECHANIC_CMD'
