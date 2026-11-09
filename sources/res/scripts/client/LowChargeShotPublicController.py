# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/LowChargeShotPublicController.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/LowChargeShotPublicController.py
from __future__ import absolute_import
import typing
from gui.shared.utils.decorators import ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKeys
from vehicles.components.component_interfaces import IVehicleGunSlotComponent
from vehicles.components.vehicle_component import VehicleDynamicComponent
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams
from vehicles.mechanics.mechanic_states import IMechanicStatesComponent
from vehicles.mechanics.gun_mechanics.low_charge_shot.public import LowChargeShotPublicMechanicState, DEFAULT_MECHANIC_STATE, createLowChargeShotPublicStatesEvents
if typing.TYPE_CHECKING:
    from items.components.shared_components import LowChargeShotParams

@ReprInjector.withParent()
class LowChargeShotPublicController(VehicleDynamicComponent, IVehicleGunSlotComponent, IMechanicStatesComponent):

    def __init__(self):
        super(LowChargeShotPublicController, self).__init__()
        self.__mechanicState = DEFAULT_MECHANIC_STATE
        self.__params = None
        self.__statesEvents = createLowChargeShotPublicStatesEvents(self)
        self._initComponent()
        return

    @property
    def statesEvents(self):
        return self.__statesEvents

    def getComponentParams(self):
        return self.__params

    def getMechanicState(self):
        return self.__mechanicState

    def set_stateStatus(self, _=None):
        self._updateComponentAppearance()

    def onDestroy(self):
        self.__statesEvents.destroy()
        super(LowChargeShotPublicController, self).onDestroy()

    def _onAppearanceReady(self):
        super(LowChargeShotPublicController, self)._onAppearanceReady()
        self.__updateMechanicState()
        self.__statesEvents.processStatePrepared()

    def _onComponentAppearanceUpdate(self, **kwargs):
        super(LowChargeShotPublicController, self)._onComponentAppearanceUpdate(**kwargs)
        self.__updateMechanicState()
        self.__statesEvents.updateMechanicState(self.getMechanicState())

    def _collectComponentParams(self, typeDescriptor):
        super(LowChargeShotPublicController, self)._collectComponentParams(typeDescriptor)
        self.__params = getVehicleDescrMechanicParams(typeDescriptor, VehicleMechanicKeys.LOW_CHARGE_SHOT)

    def __updateMechanicState(self):
        self.__mechanicState = LowChargeShotPublicMechanicState.fromComponentStatus(self.stateStatus, self.__params) if self.stateStatus is not None else DEFAULT_MECHANIC_STATE
        return
