# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/generic_mechanics/bustle_feed/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import SERVER_TICK_LENGTH as SERVER_TICK_LENGTH
from events_containers.common.container_wrappers import activateEventsContainer as activateEventsContainer
from vehicles.mechanics.generic_mechanics.bustle_feed.mechanic_events import BustleFeedStatesEvents as BustleFeedStatesEvents
from vehicles.mechanics.generic_mechanics.bustle_feed.mechanic_models import BustleFeedComponentParams as BustleFeedComponentParams, BustleFeedState as BustleFeedState, BustleFeedAmmoState as BustleFeedAmmoState, BustleFeedAmmoMode as BustleFeedAmmoMode
from vehicles.mechanics.mechanic_states.mechanic_interfaces import IMechanicStatesComponent as IMechanicStatesComponent
__all__: tuple
DEFAULT_BUSTLE_FEED_PARAMS: Any

# decorador original: @activateEventsContainer(...)
def createBustleFeedStatesEvents(component, tickInterval=..., **_):
    ...
