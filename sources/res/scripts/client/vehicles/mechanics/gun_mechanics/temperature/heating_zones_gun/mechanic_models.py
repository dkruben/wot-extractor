# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/temperature/heating_zones_gun/mechanic_models.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/gun_mechanics/temperature/heating_zones_gun/mechanic_models.py
from __future__ import absolute_import, division
import typing
from constants import HEATING_ZONES_GUN_STATE
from gui.shared.utils.decorators import ReprInjector
from vehicles.mechanics.gun_mechanics.temperature.heating_zones_gun.mechanic_interfaces import IHeatingZonesGunComponentParams, IHeatingZonesGunMechanicState
if typing.TYPE_CHECKING:
    from items.components.shared_components import HeatingZonesGunParams

@ReprInjector.simple('lowZonePercent', 'mediumZonePercent')
class HeatingZonesGunComponentParams(IHeatingZonesGunComponentParams):

    def __init__(self, lowZonePercent, mediumZonePercent):
        self.__lowZonePercent = lowZonePercent
        self.__mediumZonePercent = mediumZonePercent

    @classmethod
    def fromMechanicParams(cls, params):
        maxBorderValue = params.zones[-1][1]
        return cls(*(borderValue / maxBorderValue for stateID, borderValue in params.zones[1:-1]))

    @property
    def lowZonePercent(self):
        return self.__lowZonePercent

    @property
    def mediumZonePercent(self):
        return self.__mediumZonePercent


@ReprInjector.simple('heatingZoneState')
class HeatingZonesGunMechanicState(IHeatingZonesGunMechanicState):

    def __init__(self, heatingZoneState, params):
        self.__heatingZoneState = heatingZoneState
        self.__params = params

    @classmethod
    def fromComponentStatus(cls, heatingZoneState, params):
        return cls(heatingZoneState, params)

    @property
    def isComfortZone(self):
        return self.__heatingZoneState in (HEATING_ZONES_GUN_STATE.IDLE, HEATING_ZONES_GUN_STATE.LOW)

    @property
    def heatingZoneState(self):
        return self.__heatingZoneState

    def isTransition(self, other):
        return self.heatingZoneState != other.heatingZoneState
