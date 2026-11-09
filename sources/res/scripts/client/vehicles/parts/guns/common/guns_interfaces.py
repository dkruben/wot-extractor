# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/parts/guns/common/guns_interfaces.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/parts/guns/common/guns_interfaces.py
from __future__ import absolute_import
import typing
from events_containers.common.containers import IClientEventsContainer, IClientEventsContainerListener
from vehicles.components.component_interfaces import IVehicleGunSlotComponent

class IGunComponent(IVehicleGunSlotComponent):

    @property
    def shootingEvents(self):
        raise NotImplementedError


class IGunShootingEventsLogic(object):
    onAppearanceReady = None
    onDiscreteShot = None
    onMultiShot = None

    def processAppearanceReady(self):
        raise NotImplementedError

    def processAppearanceReset(self):
        raise NotImplementedError

    def processDiscreteShot(self, gunIndex):
        raise NotImplementedError

    def processMultiShot(self, gunIndexes):
        raise NotImplementedError


class IGunShootingEvents(IClientEventsContainer, IGunShootingEventsLogic):
    pass


class IGunShootingListenerLogic(object):

    def onAppearanceReady(self):
        pass

    def onDiscreteShot(self, gunIndex):
        pass

    def onMultiShot(self, gunIndexes):
        pass


class IGunShootingListener(IClientEventsContainerListener, IGunShootingListenerLogic):
    pass
