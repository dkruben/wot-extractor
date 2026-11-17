# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/pillbox_siege_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
import typing as typing
import CommandMapping as CommandMapping
from PillboxSiegeComponent import PillboxSiegeComponent as PillboxSiegeComponent
from constants import VEHICLE_SIEGE_STATE as PILLBOX_STATES, VEHICLE_MISC_STATUS as VEHICLE_MISC_STATUS
from events_containers.common.containers import ContainersListener as ContainersListener
from events_handler import eventHandler as eventHandler
from helpers import dependency as dependency
from gui.battle_control.battle_constants import DEVICE_STATE_CRITICAL as DEVICE_STATE_CRITICAL, DEVICE_STATE_DESTROYED as DEVICE_STATE_DESTROYED
from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import HotKeyData as HotKeyData
from gui.Scaleform.daapi.view.meta.PillboxSiegeWidgetMeta import PillboxSiegeWidgetMeta as PillboxSiegeWidgetMeta
from gui.Scaleform.genConsts.PILLBOX_SIEGE_WIDGET_CONST import PILLBOX_SIEGE_WIDGET_CONST as PILLBOX_SIEGE_WIDGET_CONST
from gui.veh_mechanics.battle.updaters.hotkey_updaters import HotKeysViewUpdater as HotKeysViewUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_commands_updater import VehicleMechanicCommandsUpdater as VehicleMechanicCommandsUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater as VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater as VehicleMechanicStatesUpdater
from gui.veh_mechanics.battle.updaters.vehicle_device_view_updater import IVehicleDeviceStatusView as IVehicleDeviceStatusView, VehicleDeviceStatusUpdater as VehicleDeviceStatusUpdater, makeUIDeviceState as makeUIDeviceState
from gui.veh_mechanics.battle.updaters.vehicle_misc_status_view_updater import VehicleMiscStatusUpdater as VehicleMiscStatusUpdater, IVehicleMiscStatusView as IVehicleMiscStatusView, MISC_STATUS_LEVEL_CRITICAL as MISC_STATUS_LEVEL_CRITICAL, MISC_STATUS_LEVEL_WARNING as MISC_STATUS_LEVEL_WARNING
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicles.mechanics.mechanic_commands import IMechanicCommandsListenerLogic as IMechanicCommandsListenerLogic
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from PillboxSiegeComponent import PillboxSiegeModeState as PillboxSiegeModeState
from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater as IViewUpdater
from gui.veh_mechanics.battle.updaters.vehicle_misc_status_view_updater import _ObservableMiscStatuses as _ObservableMiscStatuses
_HotKeyInfo: Any

class PillboxSiegeMechanicWidget(PillboxSiegeWidgetMeta, ContainersListener, IMechanicStatesListenerLogic, IMechanicCommandsListenerLogic, IVehicleMiscStatusView, IVehicleDeviceStatusView):
    __sessionProvider: Any
    _PILLBOX_SIEGE_UI_STATES: dict
    _PILLBOX_CONDITIONS: dict
    _HOT_KEY_MAP: dict
    _HOT_KEY_UI_MAP: dict
    _VEHICLE_MISC_OBSERVE: dict
    _VEHICLE_DEVICES_OBSERVE: dict
    __miscStatuses: Any
    __devicesStatuses: Any
    def __init__(self):
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
    def vehicleMiscStatusChanged(self, miscStatuses):
        ...
    def vehicleDeviceStatusChanged(self, devicesStatuses):
        ...
    def _dispose(self):
        ...
    def _getViewUpdaters(self):
        ...
    def __getDisplayState(self, state):
        ...
    def __getCondition(self):
        ...
    def __invalidateState(self, state, isInstantly=False):
        ...
    def __invalidateProgress(self, state):
        ...
    def __invalidateCondition(self):
        ...
