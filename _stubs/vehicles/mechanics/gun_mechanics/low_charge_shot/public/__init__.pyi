# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/low_charge_shot/public/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import SERVER_TICK_LENGTH as SERVER_TICK_LENGTH, LowChargeShotReloadingState as LowChargeShotReloadingState
from events_containers.common.container_wrappers import activateEventsContainer as activateEventsContainer
from vehicles.mechanics.gun_mechanics.low_charge_shot.public.mechanic_models import LowChargeShotPublicMechanicState as LowChargeShotPublicMechanicState
from vehicles.mechanics.gun_mechanics.low_charge_shot.public.mechanic_events import LowChargeShotPublicStatesEvents as LowChargeShotPublicStatesEvents
__all__: tuple
DEFAULT_MECHANIC_STATE: Any

# decorador original: @activateEventsContainer(...)
def createLowChargeShotPublicStatesEvents(component, tickInterval=..., **_):
    ...
