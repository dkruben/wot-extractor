# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/temp_heating_zones_widget.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/temp_heating_zones_widget.py
from __future__ import absolute_import, division
import typing
from cache import last_cached_method
from events_containers.common.containers import ContainersListener
from events_containers.components.life_cycle import IComponentLifeCycleListenerLogic
from events_handler import eventHandler
from gui.Scaleform.daapi.view.meta.TemperatureGunHeatZonesWidgetMeta import TemperatureGunHeatZonesWidgetMeta
from gui.Scaleform.genConsts.MECHANICS_WIDGET_CONST import MECHANICS_WIDGET_CONST
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_life_cycle_updater import VehicleMechanicLifeCycleUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic
if typing.TYPE_CHECKING:
    from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater
    from vehicles.mechanics.gun_mechanics.temperature.heating_zones_gun import IHeatingZonesGunComponentParams
    from vehicles.mechanics.gun_mechanics.temperature.temperature_gun import ITemperatureGunMechanicState

class TemperatureHeatingZonesGunWidget(TemperatureGunHeatZonesWidgetMeta, ContainersListener, IComponentLifeCycleListenerLogic, IMechanicStatesListenerLogic):

    @eventHandler
    def onComponentParamsCollected(self, params):
        self.as_setHeatZonesValuesS(params.lowZonePercent, params.mediumZonePercent)

    @eventHandler
    def onStatePrepared(self, state):
        self.__invalidateAll(state, isInstantly=True)

    @eventHandler
    def onStateObservation(self, state):
        self.__invalidateAll(state)

    @eventHandler
    def onStateTick(self, state):
        self.__invalidateProgresses(state.temperatureProgress)

    def _getViewUpdaters(self):
        return [
         VehicleMechanicLifeCycleUpdater(VehicleMechanicKeys.HEATING_ZONES_GUN, self),
         VehicleMechanicPassengerUpdater(VehicleMechanicKeys.HEATING_ZONES_GUN, self),
         VehicleMechanicStatesUpdater(VehicleMechanicKeys.TEMPERATURE_GUN, self)]

    def __invalidateAll(self, state, isInstantly=False):
        self.as_setStateS(MECHANICS_WIDGET_CONST.ACTIVE, isInstantly)
        self.__invalidateProgresses.reset()
        self.__invalidateProgresses(state.temperatureProgress)

    @last_cached_method()
    def __invalidateProgresses(self, temperatureProgress):
        self.as_setTemperatureS(temperatureProgress)
