# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/mechanics/tracked_mechanics_updater.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from events_containers.common.containers import ContainersListener as ContainersListener
from events_handler import eventHandler as eventHandler
from gui.battle_control.controllers.vehicles_tracking import VehiclesTrackingWatcher as VehiclesTrackingWatcher
from gui.veh_mechanics.battle.updaters.updaters_common import ViewUpdater as ViewUpdater
from vehicles.mechanics.mechanic_trackers import IVehicleMechanicsTrackerListenerLogic as IVehicleMechanicsTrackerListenerLogic
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey

class IVehicleTrackedMechanicsView(object):
    def onTrackedMechanicsUpdate(self, mechanics):
        ...

class VehicleTrackedMechanicsUpdater(ViewUpdater, ContainersListener, VehiclesTrackingWatcher, IVehicleMechanicsTrackerListenerLogic):
    def initialize(self):
        ...
    def finalize(self):
        ...
    # decorador original: @eventHandler
    def onMechanicComponentsUpdate(self, components):
        ...
