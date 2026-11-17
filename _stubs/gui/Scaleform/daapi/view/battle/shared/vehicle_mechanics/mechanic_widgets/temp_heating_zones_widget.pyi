# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/temp_heating_zones_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from cache import last_cached_method as last_cached_method
from events_containers.common.containers import ContainersListener as ContainersListener
from events_containers.components.life_cycle import IComponentLifeCycleListenerLogic as IComponentLifeCycleListenerLogic
from events_handler import eventHandler as eventHandler
from gui.Scaleform.daapi.view.meta.TemperatureGunHeatZonesWidgetMeta import TemperatureGunHeatZonesWidgetMeta as TemperatureGunHeatZonesWidgetMeta
from gui.Scaleform.genConsts.MECHANICS_WIDGET_CONST import MECHANICS_WIDGET_CONST as MECHANICS_WIDGET_CONST
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_life_cycle_updater import VehicleMechanicLifeCycleUpdater as VehicleMechanicLifeCycleUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater as VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater as VehicleMechanicStatesUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater as IViewUpdater
from vehicles.mechanics.gun_mechanics.temperature.heating_zones_gun import IHeatingZonesGunComponentParams as IHeatingZonesGunComponentParams
from vehicles.mechanics.gun_mechanics.temperature.temperature_gun import ITemperatureGunMechanicState as ITemperatureGunMechanicState

class TemperatureHeatingZonesGunWidget(TemperatureGunHeatZonesWidgetMeta, ContainersListener, IComponentLifeCycleListenerLogic, IMechanicStatesListenerLogic):
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
    def _getViewUpdaters(self):
        ...
    def __invalidateAll(self, state, isInstantly=False):
        ...
    # decorador original: @last_cached_method(...)
    def __invalidateProgresses(self, temperatureProgress):
        ...
