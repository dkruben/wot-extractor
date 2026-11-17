# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/chargeable_burst_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from events_containers.common.containers import ContainersListener as ContainersListener
from gui.Scaleform.daapi.view.meta.ChargeableBurstWidgetMeta import ChargeableBurstWidgetMeta as ChargeableBurstWidgetMeta
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater as VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater as VehicleMechanicStatesUpdater
from helpers import dependency as dependency
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from events_handler import eventHandler as eventHandler
from ChargeableBurstComponent import ChargeableBurstModeState as ChargeableBurstModeState
from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater as IViewUpdater
from gui.battle_control.controllers.consumables.ammo_ctrl import ReloadingTimeSnapshot as ReloadingTimeSnapshot

class ChargeableBurstMechanicWidget(ChargeableBurstWidgetMeta, ContainersListener, IMechanicStatesListenerLogic):
    __sessionProvider: Any
    # decorador original: @eventHandler
    def onStatePrepared(self, state):
        ...
    # decorador original: @eventHandler
    def onStateTransition(self, prevState, newState):
        ...
    # decorador original: @eventHandler
    def onStateObservation(self, state):
        ...
    def _getViewUpdaters(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onShellsUpdated(self, intCD, quantity, quantityInClip, result):
        ...
    def __onCurrentShellChanged(self, intCD):
        ...
    def __onCurrentShellReset(self):
        ...
    def __onGunReloadTimeSet(self, currShellCD, state, skipAutoLoader):
        ...
    def __invalidateAll(self, state, isInstantly=False):
        ...
    def __invalidateMode(self, state, isInstantly=False):
        ...
    def __invalidateCharges(self, state, isInstantly=False):
        ...
    def __invalidateShells(self):
        ...
