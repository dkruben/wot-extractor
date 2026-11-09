# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/temperature/heating_zones_gun/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/gun_mechanics/temperature/heating_zones_gun/__init__.py
from __future__ import absolute_import
from constants import HEATING_ZONES_GUN_STATE
from vehicles.mechanics.gun_mechanics.temperature.heating_zones_gun.mechanic_interfaces import IHeatingZonesGunComponentParams, IHeatingZonesGunMechanicState
from vehicles.mechanics.gun_mechanics.temperature.heating_zones_gun.mechanic_models import HeatingZonesGunComponentParams, HeatingZonesGunMechanicState
__all__ = ('IHeatingZonesGunComponentParams', 'IHeatingZonesGunMechanicState', 'HeatingZonesGunComponentParams',
           'HeatingZonesGunMechanicState', 'DEFAULT_HEATING_ZONES_COMPONENT_PARAMS',
           'DEFAULT_HEATING_ZONES_MECHANIC_STATE')
DEFAULT_HEATING_ZONES_COMPONENT_PARAMS = HeatingZonesGunComponentParams(1.0, 1.0)
DEFAULT_HEATING_ZONES_MECHANIC_STATE = HeatingZonesGunMechanicState(HEATING_ZONES_GUN_STATE.IDLE, DEFAULT_HEATING_ZONES_COMPONENT_PARAMS)
