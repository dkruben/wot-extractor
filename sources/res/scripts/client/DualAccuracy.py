# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/DualAccuracy.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/DualAccuracy.py
from __future__ import absolute_import, division
import Event
from constants import DUAL_ACCURACY_STATE
from gui.shared.utils.decorators import ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey, VehicleMechanicKeys
from vehicles.components.vehicle_component import VehicleDynamicComponent
from vehicles.mechanics.gun_mechanics.common import IGunMechanicComponent
_DEFAULT_ACCURACY_FACTOR = 1.0

@ReprInjector.withParent()
class DualAccuracy(VehicleDynamicComponent, IGunMechanicComponent):

    def __init__(self):
        super(DualAccuracy, self).__init__()
        self.__dualAccuracyFactor = _DEFAULT_ACCURACY_FACTOR
        self.__eManager = Event.EventManager()
        self.onSetDualAccState = Event.Event(self.__eManager)
        self._initComponent()

    @property
    def vehicleMechanicKey(self):
        return VehicleMechanicKeys.DUAL_ACCURACY

    def isActive(self):
        return self.state == DUAL_ACCURACY_STATE.ACTIVE

    def getComponentParams(self):
        return self.getDualAccuracyFactor()

    def getCurrentDualAccuracyFactor(self):
        if self.isActive():
            return self.__dualAccuracyFactor
        return _DEFAULT_ACCURACY_FACTOR

    def getDualAccuracyFactor(self):
        return self.__dualAccuracyFactor

    def set_state(self, _=None):
        self._updateComponentAvatar()
        self._updateComponentAppearance()

    def onDestroy(self):
        self.__eManager.clear()
        super(DualAccuracy, self).onDestroy()

    def _onComponentAvatarUpdate(self, player):
        super(DualAccuracy, self)._onComponentAvatarUpdate(player)
        player.getOwnVehicleShotDispersionAngle(player.gunRotator.turretRotationSpeed)

    def _onComponentAppearanceUpdate(self, **kwargs):
        super(DualAccuracy, self)._onComponentAppearanceUpdate(**kwargs)
        self.onSetDualAccState(self.isActive())

    def _collectComponentParams(self, typeDescriptor):
        super(DualAccuracy, self)._collectComponentParams(typeDescriptor)
        params = typeDescriptor.gun
        self.__dualAccuracyFactor = params.dualAccuracy.afterShotDispersionAngle / params.shotDispersionAngle
