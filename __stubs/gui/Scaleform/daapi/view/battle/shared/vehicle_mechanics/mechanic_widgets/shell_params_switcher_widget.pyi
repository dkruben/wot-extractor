# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/shell_params_switcher_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
import CommandMapping as CommandMapping
from constants import SHELL_PARAMS_SWITCHER_STATE as SHELL_PARAMS_SWITCHER_STATE
from events_containers.common.containers import ContainersListener as ContainersListener
from events_handler import eventHandler as eventHandler
from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import HotKeyData as HotKeyData
from gui.Scaleform.daapi.view.meta.ShellParamsSwitcherWidgetMeta import ShellParamsSwitcherWidgetMeta as ShellParamsSwitcherWidgetMeta
from gui.Scaleform.genConsts.SHELL_PARAMS_SWITCHER_WIDGET_CONSTS import SHELL_PARAMS_SWITCHER_WIDGET_CONSTS as SHELL_PARAMS_SWITCHER_WIDGET_CONSTS
from gui.veh_mechanics.battle.updaters.hotkey_updaters import HotKeysViewUpdater as HotKeysViewUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater as VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater as VehicleMechanicStatesUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater as IViewUpdater
from vehicles.mechanics.gun_mechanics.shell_params_switcher import IShellParamsSwitcherMechanicState as IShellParamsSwitcherMechanicState
_MECHANIC_STATE_UI_MAP: dict

class ShellParamsSwitcherWidget(ShellParamsSwitcherWidgetMeta, ContainersListener, IMechanicStatesListenerLogic):
    _HOT_KEY_MAP: dict
    # decorador original: @eventHandler
    def onStatePrepared(self, state):
        ...
    # decorador original: @eventHandler
    def onStateObservation(self, state):
        ...
    # decorador original: @eventHandler
    def onStateTick(self, state):
        ...
    def _getViewUpdaters(self):
        ...
    def __invalidateState(self, state, isInstantly=False):
        ...

def _getWidgetState(state):
    ...
