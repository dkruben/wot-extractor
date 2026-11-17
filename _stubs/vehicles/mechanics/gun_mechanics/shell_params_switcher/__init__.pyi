# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/shell_params_switcher/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import SERVER_TICK_LENGTH as SERVER_TICK_LENGTH, SHELL_PARAMS_SWITCHER_STATE as SHELL_PARAMS_SWITCHER_STATE
from events_containers.common.container_wrappers import activateEventsContainer as activateEventsContainer
from vehicles.mechanics.gun_mechanics.shell_params_switcher.mechanic_interfaces import IShellParamsSwitcherMechanicState as IShellParamsSwitcherMechanicState, IShellParamsSwitcherComponentParams as IShellParamsSwitcherComponentParams
from vehicles.mechanics.gun_mechanics.shell_params_switcher.mechanic_models import ShellParamsSwitcherMechanicState as ShellParamsSwitcherMechanicState, ShellParamsSwitcherComponentParams as ShellParamsSwitcherComponentParams, ShellParamsSwitcherAmmoState as ShellParamsSwitcherAmmoState, ShellParamsSwitcherAmmoMode as ShellParamsSwitcherAmmoMode
from vehicles.mechanics.gun_mechanics.shell_params_switcher.mechanic_events import ShellParamsSwitcherStatesEvents as ShellParamsSwitcherStatesEvents
from vehicles.mechanics.mechanic_states import IMechanicStatesComponent as IMechanicStatesComponent
__all__: tuple
DEFAULT_SHELL_PARAMS_SWITCHER_PARAMS: Any
DEFAULT_SHELL_PARAMS_SWITCHER_STATE: Any

# decorador original: @activateEventsContainer(...)
def createShellParamsSwitcherStatesEvents(component, tickInterval=..., **_):
    ...
