# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/stationary_reloading_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import STATIONARY_RELOAD_STATE as STATIONARY_RELOAD_STATE, GUN_LOCK_REASONS as GUN_LOCK_REASONS
from events_containers.common.containers import ContainersListener as ContainersListener
from events_handler import eventHandler as eventHandler
from gui.Scaleform.daapi.view.meta.StationaryReloadWidgetMeta import StationaryReloadWidgetMeta as StationaryReloadWidgetMeta
from gui.Scaleform.genConsts.MECHANICS_WIDGET_CONST import MECHANICS_WIDGET_CONST as MECHANICS_WIDGET_CONST
from gui.Scaleform.genConsts.STATIONARY_RELOAD_WIDGET_CONSTS import STATIONARY_RELOAD_WIDGET_CONSTS as SR_CONSTS
from gui.battle_control.battle_constants import DEVICE_STATE_CRITICAL as DEVICE_STATE_CRITICAL, DEVICE_STATE_NORMAL as DEVICE_STATE_NORMAL
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater as VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater as VehicleMechanicStatesUpdater
from gui.veh_mechanics.battle.updaters.vehicle_device_view_updater import VehicleDeviceStatusUpdater as VehicleDeviceStatusUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from StationaryReloadController import StationaryReloadModeState as StationaryReloadModeState
from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater as IViewUpdater

class StationaryReloadingMechanicWidget(StationaryReloadWidgetMeta, ContainersListener, IMechanicStatesListenerLogic):
    _STATIONARY_RELOADING_UI_STATES: dict
    __isTurretDamaged: Any
    __state: Any
    def __init__(self):
        ...
    def vehicleDeviceStatusChanged(self, devicesStatuses):
        ...
    # decorador original: @eventHandler
    def onStatePrepared(self, state):
        ...
    # decorador original: @eventHandler
    def onStateTransition(self, prevState, newState):
        ...
    # decorador original: @eventHandler
    def onStateTick(self, state):
        ...
    def _getViewUpdaters(self):
        ...
    def __invalidateState(self, state, isInstantly=False):
        ...
    def __invalidateTimer(self):
        ...
    def __updateVehicleCondition(self):
        ...
