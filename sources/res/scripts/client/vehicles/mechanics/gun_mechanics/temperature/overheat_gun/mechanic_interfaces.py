# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/temperature/overheat_gun/mechanic_interfaces.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/gun_mechanics/temperature/overheat_gun/mechanic_interfaces.py
from __future__ import absolute_import
import typing
from vehicles.mechanics.mechanic_states import IMechanicState
if typing.TYPE_CHECKING:
    from items.components.shared_components import OverheatGunParams
    from vehicles.mechanics.gun_mechanics.temperature.temperature_gun import ITemperatureGunMechanicState

class IOverheatGunComponentParams(object):

    @classmethod
    def fromMechanicParams(cls, params):
        raise NotImplementedError

    @property
    def overheatWarnPercent(self):
        raise NotImplementedError

    @property
    def overheatOffPercent(self):
        raise NotImplementedError

    @property
    def overheatOffThreshold(self):
        raise NotImplementedError


class IOverheatGunMechanicState(IMechanicState):

    @classmethod
    def fromComponentStatus(cls, overheatState, params):
        raise NotImplementedError

    @property
    def isOverheated(self):
        raise NotImplementedError

    @property
    def overheatState(self):
        raise NotImplementedError

    def overheatTimeLeft(self, temperatureGunState):
        raise NotImplementedError
