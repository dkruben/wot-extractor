# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/mechanics/mechanic_passenger_updater.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from events_handler import eventHandler as eventHandler
from gui.battle_control.controllers.vehicle_passenger import VehiclePassengerInfoWatcher as VehiclePassengerInfoWatcher, hasVehiclePassengerCtrl as hasVehiclePassengerCtrl
from gui.veh_mechanics.battle.updaters.mechanics.mechanics_common import VehicleMechanicUpdater as VehicleMechanicUpdater
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey

class IMechanicPassengerView(object):
    def setVisibleForPassenger(self, visibleForPassenger):
        ...

class VehicleMechanicPassengerUpdater(VehicleMechanicUpdater, VehiclePassengerInfoWatcher):
    __isVisibleForPassenger: Any
    __hasMechanicComponent: Any
    def __init__(self, mechanicTracker, view):
        ...
    # decorador original: @eventHandler
    def onMechanicComponentCatching(self, component):
        ...
    # decorador original: @eventHandler
    def onMechanicComponentReleasing(self, component):
        ...
    def initialize(self):
        ...
    def finalize(self):
        ...
    def __onVehiclePassengerUpdate(self, *_, **__):
        ...
    # decorador original: @hasVehiclePassengerCtrl(...)
    def __getVisibleByPassenger(self, passengerCtrl=None):
        ...
    def __updateMechanicView(self):
        ...
