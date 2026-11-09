# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/auxiliary_rocket_launcher_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import CommandMapping as CommandMapping
from BattleReplay import g_replayCtrl as g_replayCtrl
from cache import last_cached_method as last_cached_method
from constants import SECONDARY_GUN_STATE as SECONDARY_GUN_STATE, UNKNOWN_GUN_INSTALLATION_INDEX as UNKNOWN_GUN_INSTALLATION_INDEX
from events_containers.common.containers import ContainersListener as ContainersListener
from events_handler import eventHandler as eventHandler
from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import HotKeyData as HotKeyData
from gui.Scaleform.daapi.view.meta.AuxiliaryRocketLauncherWidgetMeta import AuxiliaryRocketLauncherWidgetMeta as AuxiliaryRocketLauncherWidgetMeta
from gui.Scaleform.genConsts.MECHANICS_WIDGET_CONST import MECHANICS_WIDGET_CONST as MECHANICS_WIDGET_CONST
from gui.veh_mechanics.battle.updaters.hotkey_updaters import HotKeysViewUpdater as HotKeysViewUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater as VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater as VehicleMechanicStatesUpdater
from gui.veh_mechanics.battle.updaters.shooting_updaters import IShootingReactionsView as IShootingReactionsView, ShootingReactionsUpdater as ShootingReactionsUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater as IViewUpdater
from items.components.gun_installation_components import GunInstallationSlot as GunInstallationSlot
from vehicles.mechanics.gun_mechanics.auxiliary_rocket_launcher import AuxiliaryRocketLauncherState as AuxiliaryRocketLauncherState

class AuxiliaryRocketLauncherWidget(AuxiliaryRocketLauncherWidgetMeta, ContainersListener, IMechanicStatesListenerLogic, IShootingReactionsView):
    _AUXILIARY_ROCKET_LAUNCHER_UI_STATES: dict
    _HOT_KEY_MAP: dict
    __installationIndex: Any
    __progressUpdaters: Any
    def __init__(self):
        ...
    def onDiscreteShotsDone(self, gunInstallationSlot, isCurrentVehicle):
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
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _getViewUpdaters(self):
        ...
    def __getDisplayState(self, state):
        ...
    def __invalidateAll(self, state, isInstantly=False):
        ...
    # decorador original: @last_cached_method(...)
    def __invalidateProgress(self, uiState, progress, timeLeft):
        ...
