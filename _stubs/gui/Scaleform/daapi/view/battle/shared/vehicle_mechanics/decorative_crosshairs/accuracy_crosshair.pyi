# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/decorative_crosshairs/accuracy_crosshair.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from events_containers.common.containers import ContainersListener as ContainersListener
from events_handler import eventHandler as eventHandler
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from gui.Scaleform.daapi.view.meta.AccuracyStackDecorativeCrosshairMeta import AccuracyStackDecorativeCrosshairMeta as AccuracyStackDecorativeCrosshairMeta
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater as VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater as VehicleMechanicStatesUpdater
from gui.veh_mechanics.battle.updaters.vehicle_state_updater import VehicleStateUpdater as VehicleStateUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from AccuracyStacksController import AccuracyStacksState as AccuracyStacksState

class AccuracyDecorativeCrosshair(AccuracyStackDecorativeCrosshairMeta, ContainersListener, IMechanicStatesListenerLogic):
    __level: Any
    __progress: Any
    __speedThreshold: Any
    __isGainingActive: Any
    __isSpeedLimitActive: Any
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
    def _getViewUpdaters(self):
        ...
    def updateSpeedLimit(self, value, forced=False):
        ...
    def onVehicleStateUpdated(self, stateID, value):
        ...
    def __update(self, state):
        ...
