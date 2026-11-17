# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/propellant_gun_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import CommandMapping as CommandMapping
from events_containers.common.containers import ContainersListener as ContainersListener
from events_containers.components.life_cycle import IComponentLifeCycleListenerLogic as IComponentLifeCycleListenerLogic
from events_handler import eventHandler as eventHandler
from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import HotKeyData as HotKeyData
from gui.Scaleform.daapi.view.meta.PropellantGunWidgetMeta import PropellantGunWidgetMeta as PropellantGunWidgetMeta
from gui.Scaleform.genConsts.PROPELLANT_GUN_WIDGET_CONST import PROPELLANT_GUN_WIDGET_CONST as PROPELLANT_GUN_WIDGET_CONST
from gui.veh_mechanics.battle.updaters.crosshair_type_updater import CrosshairTypeUpdater as CrosshairTypeUpdater
from gui.veh_mechanics.battle.updaters.current_shell_damage_updater import CurrentShellDamageUpdater as CurrentShellDamageUpdater
from gui.veh_mechanics.battle.updaters.hotkey_updaters import HotKeysViewUpdater as HotKeysViewUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_commands_updater import VehicleMechanicCommandsUpdater as VehicleMechanicCommandsUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_life_cycle_updater import VehicleMechanicLifeCycleUpdater as VehicleMechanicLifeCycleUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater as VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater as VehicleMechanicStatesUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.mechanics.gun_mechanics.propellant_gun import DEFAULT_PROPELLANT_GUN_MECHANIC_STATE as DEFAULT_PROPELLANT_GUN_MECHANIC_STATE
from vehicles.mechanics.mechanic_commands import IMechanicCommandsListenerLogic as IMechanicCommandsListenerLogic
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater as IViewUpdater
from vehicles.mechanics.gun_mechanics.propellant_gun import IPropellantGunMechanicState as IPropellantGunMechanicState, IPropellantGunComponentParams as IPropellantGunComponentParams

class PropellantGunMechanicWidget(PropellantGunWidgetMeta, ContainersListener, IComponentLifeCycleListenerLogic, IMechanicStatesListenerLogic, IMechanicCommandsListenerLogic):
    _HOT_KEY_MAP: dict
    _GUI_STATE_MAP: dict
    __overchargeThreshold: Any
    __shellDamage: Any
    __state: Any
    def __init__(self):
        ...
    # decorador original: @eventHandler
    def onComponentParamsCollected(self, params):
        ...
    # decorador original: @eventHandler
    def onStatePrepared(self, state):
        ...
    # decorador original: @eventHandler
    def onStateObservation(self, state):
        ...
    # decorador original: @eventHandler
    def onStateTick(self, state):
        ...
    # decorador original: @eventHandler
    def onMechanicCommand(self, command):
        ...
    def onCurrentShellDamageChanged(self, newDamage):
        ...
    def _getViewUpdaters(self):
        ...
    def __invalidateState(self, isInstantly=False):
        ...
    def __invalidateProgress(self):
        ...
