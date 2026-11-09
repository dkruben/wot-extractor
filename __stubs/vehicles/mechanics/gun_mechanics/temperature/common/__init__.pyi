# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/temperature/common/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from constants import SERVER_TICK_LENGTH as SERVER_TICK_LENGTH
from events_containers.common.container_wrappers import activateEventsContainer as activateEventsContainer
from vehicles.mechanics.gun_mechanics.temperature.common.mechanic_interfaces import ITemperatureComponentParams as ITemperatureComponentParams, ITemperatureMechanicState as ITemperatureMechanicState
from vehicles.mechanics.gun_mechanics.temperature.common.mechanic_events import TemperatureStatesEvents as TemperatureStatesEvents
from vehicles.mechanics.gun_mechanics.temperature.common.mechanic_models import TemperatureComponentParams as TemperatureComponentParams, TemperatureMechanicState as TemperatureMechanicState
from vehicles.mechanics.mechanic_states import IMechanicStatesComponent as IMechanicStatesComponent
__all__: tuple

# decorador original: @activateEventsContainer(...)
def createTemperatureStatesEvents(component, tickInterval=..., **_):
    ...
