# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/HeatingZonesGunComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/HeatingZonesGunComponent.py
from __future__ import absolute_import
import typing
from gui.shared.utils.decorators import ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey, VehicleMechanicKeys
from vehicles.components.vehicle_component import VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner
from vehicles.mechanics.gun_mechanics.common import IGunMechanicComponent
from vehicles.mechanics.gun_mechanics.temperature.heating_zones_gun import DEFAULT_HEATING_ZONES_MECHANIC_STATE, DEFAULT_HEATING_ZONES_COMPONENT_PARAMS, HeatingZonesGunComponentParams, HeatingZonesGunMechanicState
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams
from vehicles.mechanics.mechanic_states import createMechanicStatesEvents, IMechanicStatesComponent
if typing.TYPE_CHECKING:
    from vehicles.mechanics.gun_mechanics.temperature.heating_zones_gun import IHeatingZonesGunComponentParams, IHeatingZonesGunMechanicState
    from vehicles.mechanics.mechanic_states import IMechanicStatesEvents

@ReprInjector.withParent()
class HeatingZonesGunComponent(VehicleDynamicComponent, IGunMechanicComponent, IMechanicStatesComponent):

    def __init__(self):
        super(HeatingZonesGunComponent, self).__init__()
        self.__componentParams = DEFAULT_HEATING_ZONES_COMPONENT_PARAMS
        self.__mechanicState = DEFAULT_HEATING_ZONES_MECHANIC_STATE
        self.__statesEvents = createMechanicStatesEvents(self)
        self.__mechanicPrefabSpawner = createMechanicPrefabSpawner(self.entity, self)
        self._initComponent()

    @property
    def vehicleMechanicKey(self):
        return VehicleMechanicKeys.HEATING_ZONES_GUN

    @property
    def statesEvents(self):
        return self.__statesEvents

    def getComponentParams(self):
        return self.__componentParams

    def getMechanicState(self):
        return self.__mechanicState

    def set_state(self, _=None):
        self._updateComponentAppearance()

    def onDestroy(self):
        self.__statesEvents.destroy()
        super(HeatingZonesGunComponent, self).onDestroy()

    def _onAppearanceReady(self):
        super(HeatingZonesGunComponent, self)._onAppearanceReady()
        self.__updateMechanicState()
        self.__statesEvents.processStatePrepared()

    def _onComponentAppearanceUpdate(self, **kwargs):
        super(HeatingZonesGunComponent, self)._onComponentAppearanceUpdate(**kwargs)
        self.__updateMechanicState()
        self.__statesEvents.updateMechanicState(self.getMechanicState())

    def _collectComponentParams(self, typeDescriptor):
        super(HeatingZonesGunComponent, self)._collectComponentParams(typeDescriptor)
        mechanicParams = getVehicleDescrMechanicParams(typeDescriptor, self.vehicleMechanicKey)
        self.__componentParams = HeatingZonesGunComponentParams.fromMechanicParams(mechanicParams)

    def __updateMechanicState(self):
        self.__mechanicState = HeatingZonesGunMechanicState.fromComponentStatus(self.state, self.__componentParams)
