# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/mechanic_commands/mechanic_interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from events_containers.common.containers import IClientEventsContainer as IClientEventsContainer, IClientEventsContainerListener as IClientEventsContainerListener
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand

class IMechanicCommandsComponent(object):
    @property
    def commandsEvents(self):
        ...

class IMechanicCommandsEventsLogic(object):
    onMechanicCommand = None
    def processMechanicCommand(self, command):
        ...

class IMechanicCommandsEvents(IClientEventsContainer, IMechanicCommandsEventsLogic):
    ...

class IMechanicCommandsListenerLogic(object):
    def onMechanicCommand(self, command):
        ...

class IMechanicCommandsListener(IClientEventsContainerListener, IMechanicCommandsListenerLogic):
    ...
