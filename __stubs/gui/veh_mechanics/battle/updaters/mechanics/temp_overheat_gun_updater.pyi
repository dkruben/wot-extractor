# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/mechanics/temp_overheat_gun_updater.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import weakref as weakref
from events_handler import eventHandler as eventHandler
from gui.veh_mechanics.battle.updaters.updaters_common import ViewUpdater as ViewUpdater, ViewUpdatersCollection as ViewUpdatersCollection
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater as VehicleMechanicStatesUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from Event import SafeEvent as SafeEvent
from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater as IViewUpdater
from vehicles.mechanics.gun_mechanics.temperature.overheat_gun import IOverheatGunMechanicState as IOverheatGunMechanicState
from vehicles.mechanics.gun_mechanics.temperature.temperature_gun import ITemperatureGunMechanicState as ITemperatureGunMechanicState

class ITemperatureOverheatGunStatesListenerLogic(object):
    def onOverheatStatePrepared(self, state):
        ...
    def onOverheatStateTransition(self, prevState, newState):
        ...
    def onTemperatureStatePrepared(self, state):
        ...
    def onTemperatureStateObservation(self, state):
        ...
    def onTemperatureStateTick(self, state):
        ...

class OverheatStatesBridge(VehicleMechanicStatesUpdater, IMechanicStatesListenerLogic):
    __onStatePrepared: Any
    __onStateTransition: Any
    def __init__(self, onStatePrepared, onStateTransition):
        ...
    # decorador original: @eventHandler
    def onStatePrepared(self, state):
        ...
    # decorador original: @eventHandler
    def onStateTransition(self, prevState, newState):
        ...

class TemperatureStatesBridge(VehicleMechanicStatesUpdater, IMechanicStatesListenerLogic):
    __onStatePrepared: Any
    __onStateObservation: Any
    __onStateTick: Any
    def __init__(self, onStatePrepared, onStateObservation, onStateTick):
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

class TemperatureOverheatGunStatesUpdater(ViewUpdater):
    onOverheatStatePrepared: Any
    onOverheatStateTransition: Any
    onTemperatureStatePrepared: Any
    onTemperatureStateObservation: Any
    onTemperatureStateTick: Any
    __updatersCollection: Any
    def __init__(self, view):
        ...
    def initialize(self):
        ...
    def finalize(self):
        ...
    def destroy(self):
        ...
    def _getViewUpdaters(self):
        ...
