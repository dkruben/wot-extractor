# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/parts/guns/twin_shoot/guns_interfaces.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/parts/guns/twin_shoot/guns_interfaces.py
from __future__ import absolute_import
import typing
from vehicles.parts.guns.common import IGunComponent, IGunShootingEvents, IGunShootingListener

class ITwinShootGunComponent(IGunComponent):

    def isDoubleBarrelMode(self):
        raise NotImplementedError

    def getActiveGunIndexes(self):
        raise NotImplementedError

    def getAfterShotDelay(self):
        raise NotImplementedError

    def getNextGunIndexes(self):
        raise NotImplementedError


class ITwinShootingEventsLogic(object):
    onActiveGunsUpdate = None
    onAnimatedGunsUpdate = None

    def processNextGunsUpdate(self, nextGunIndexes):
        raise NotImplementedError


class ITwinShootingEvents(IGunShootingEvents, ITwinShootingEventsLogic):
    pass


class ITwinShootingListenerLogic(object):

    def onActiveGunsUpdate(self, gunIndexes):
        pass

    def onAnimatedGunsUpdate(self, gunIndexes):
        pass


class ITwinShootingListener(IGunShootingListener, ITwinShootingListenerLogic):
    pass
