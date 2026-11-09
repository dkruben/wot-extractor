# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/propellant_gun/mechanic_interfaces.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/gun_mechanics/propellant_gun/mechanic_interfaces.py
from __future__ import absolute_import
import typing
from vehicles.mechanics.mechanic_states import IMechanicState
if typing.TYPE_CHECKING:
    from items.components.shared_components import PropellantGunParams

class IPropellantGunComponentParams(object):

    @classmethod
    def fromMechanicParams(cls, params):
        raise NotImplementedError

    @property
    def chargePerSec(self):
        raise NotImplementedError

    @property
    def dischargePerSec(self):
        raise NotImplementedError

    @property
    def maxCharge(self):
        raise NotImplementedError

    @property
    def maxOvercharge(self):
        raise NotImplementedError

    @property
    def stages(self):
        raise NotImplementedError

    @property
    def forbiddenShells(self):
        raise NotImplementedError


class IPropellantGunMechanicState(IMechanicState):

    @classmethod
    def fromComponentStatus(cls, status, params):
        raise NotImplementedError

    @property
    def state(self):
        raise NotImplementedError

    @property
    def currentStage(self):
        raise NotImplementedError

    @property
    def currentCharge(self):
        raise NotImplementedError

    @property
    def currentThreshold(self):
        raise NotImplementedError

    @property
    def isOvercharge(self):
        raise NotImplementedError

    @property
    def isAvailable(self):
        raise NotImplementedError

    @property
    def timeLeft(self):
        raise NotImplementedError

    @property
    def isLastStage(self):
        raise NotImplementedError

    @property
    def isUsableShell(self):
        raise NotImplementedError

    @property
    def lastShotTimestamp(self):
        raise NotImplementedError

    @property
    def lastShotCharge(self):
        raise NotImplementedError

    def getCurrentDamageFactor(self, progress=None):
        raise NotImplementedError
