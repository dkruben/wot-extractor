# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/shell_params_switcher/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/gun_mechanics/shell_params_switcher/__init__.py
from __future__ import absolute_import
import typing
from constants import SERVER_TICK_LENGTH, SHELL_PARAMS_SWITCHER_STATE
from events_containers.common.container_wrappers import activateEventsContainer
from vehicles.mechanics.gun_mechanics.shell_params_switcher.mechanic_interfaces import IShellParamsSwitcherMechanicState, IShellParamsSwitcherComponentParams
from vehicles.mechanics.gun_mechanics.shell_params_switcher.mechanic_models import ShellParamsSwitcherMechanicState, ShellParamsSwitcherComponentParams, ShellParamsSwitcherAmmoState, ShellParamsSwitcherAmmoMode
from vehicles.mechanics.gun_mechanics.shell_params_switcher.mechanic_events import ShellParamsSwitcherStatesEvents
if typing.TYPE_CHECKING:
    from vehicles.mechanics.mechanic_states import IMechanicStatesComponent
__all__ = ('IShellParamsSwitcherComponentParams', 'IShellParamsSwitcherMechanicState',
           'ShellParamsSwitcherComponentParams', 'ShellParamsSwitcherMechanicState',
           'ShellParamsSwitcherStatesEvents', 'DEFAULT_SHELL_PARAMS_SWITCHER_PARAMS',
           'DEFAULT_SHELL_PARAMS_SWITCHER_STATE', 'createShellParamsSwitcherStatesEvents',
           'ShellParamsSwitcherAmmoMode', 'ShellParamsSwitcherAmmoState')
DEFAULT_SHELL_PARAMS_SWITCHER_PARAMS = ShellParamsSwitcherComponentParams({})
DEFAULT_SHELL_PARAMS_SWITCHER_STATE = ShellParamsSwitcherMechanicState(state=SHELL_PARAMS_SWITCHER_STATE.NOT_CHARGED, endTime=0.0, isActive=False, lastActiveShotTimestamp=0.0, params=DEFAULT_SHELL_PARAMS_SWITCHER_PARAMS, shellCD=0)

@activateEventsContainer()
def createShellParamsSwitcherStatesEvents(component, tickInterval=SERVER_TICK_LENGTH, **_):
    return ShellParamsSwitcherStatesEvents(component, tickInterval)
