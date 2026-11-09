# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/SecondaryGunComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/SecondaryGunComponent.py
from __future__ import absolute_import
import typing
from gui.shared.utils.decorators import ReprInjector
from vehicles.components.vehicle_component import VehicleDynamicComponent
from vehicles.parts.guns.common import IGunComponent, createGunShootingEvents
if typing.TYPE_CHECKING:
    from vehicles.parts.guns.common import IGunShootingEvents

@ReprInjector.withParent()
class SecondaryGunComponent(VehicleDynamicComponent, IGunComponent):

    def __init__(self):
        super(SecondaryGunComponent, self).__init__()
        self.__shootingEvents = createGunShootingEvents(self.entity, self)
        self._initComponent()

    @property
    def shootingEvents(self):
        return self.__shootingEvents

    def getGunInstallationIndex(self):
        return self.gunInstallationIndex

    def onDestroy(self):
        self.__shootingEvents.destroy()
        super(SecondaryGunComponent, self).onDestroy()

    def onDiscreteShot(self, gunIndex):
        self.__shootingEvents.processDiscreteShot(gunIndex)

    def onMultiShot(self, gunIndexes):
        self.__shootingEvents.processMultiShot(gunIndexes)

    def _onAppearanceReady(self):
        super(SecondaryGunComponent, self)._onAppearanceReady()
        self.__shootingEvents.processAppearanceReady()

    def _onAppearanceReset(self):
        super(SecondaryGunComponent, self)._onAppearanceReset()
        self.__shootingEvents.processAppearanceReset()
