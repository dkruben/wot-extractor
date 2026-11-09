# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/propellant_gun/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import PROPELLANT_GUN_STATE as PROPELLANT_GUN_STATE, SERVER_TICK_LENGTH as SERVER_TICK_LENGTH
from events_containers.common.container_wrappers import activateEventsContainer as activateEventsContainer
from vehicles.mechanics.gun_mechanics.propellant_gun.mechanic_interfaces import IPropellantGunComponentParams as IPropellantGunComponentParams, IPropellantGunMechanicState as IPropellantGunMechanicState
from vehicles.mechanics.gun_mechanics.propellant_gun.mechanic_models import PropellantGunComponentParams as PropellantGunComponentParams, PropellantGunMechanicState as PropellantGunMechanicState
from vehicles.mechanics.gun_mechanics.propellant_gun.mechanic_events import PropellantStatesEvents as PropellantStatesEvents
from vehicles.mechanics.mechanic_states import IMechanicStatesComponent as IMechanicStatesComponent
__all__: tuple
DEFAULT_PROPELLANT_GUN_PARAMS: Any
DEFAULT_PROPELLANT_GUN_MECHANIC_STATE: Any

# decorador original: @activateEventsContainer(...)
def createPropellantStatesEvents(component, tickInterval=..., **_):
    ...
