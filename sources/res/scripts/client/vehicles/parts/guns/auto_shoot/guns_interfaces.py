# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/parts/guns/auto_shoot/guns_interfaces.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/parts/guns/auto_shoot/guns_interfaces.py
from __future__ import absolute_import
from vehicles.parts.guns.common import IGunComponent, IGunShootingEvents, IGunShootingListener

class IAutoShootDispersionState(object):

    def getCurrentDispersionFactor(self):
        raise NotImplementedError


class IAutoShootGunComponentState(object):

    def isShooting(self):
        raise NotImplementedError

    def isContinuousShooting(self):
        raise NotImplementedError

    def getDefaultShotRatePerSecond(self):
        raise NotImplementedError

    def getGroupShotInterval(self):
        raise NotImplementedError

    def getShotRatePerSecond(self):
        raise NotImplementedError


class IAutoShootGunComponent(IGunComponent):

    def getComponentState(self):
        raise NotImplementedError

    def getDispersionState(self):
        raise NotImplementedError


class IAutoShootingEventsLogic(object):
    onBurstActivation = None
    onBurstDeactivation = None
    onContinuousBurstActivation = None
    onContinuousBurstDeactivation = None
    onContinuousBurstUpdate = None
    onShotRateUpdate = None

    def updateAutoShootingState(self, componentState):
        raise NotImplementedError


class IAutoShootingEvents(IGunShootingEvents, IAutoShootingEventsLogic):
    pass


class IAutoShootingListenerLogic(object):

    def onBurstActivation(self):
        pass

    def onBurstDeactivation(self):
        pass

    def onContinuousBurstActivation(self):
        pass

    def onContinuousBurstDeactivation(self):
        pass

    def onContinuousBurstUpdate(self):
        pass

    def onShotRateUpdate(self, rate):
        pass


class IAutoShootingListener(IGunShootingListener, IAutoShootingListenerLogic):
    pass
