# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/temperature/temperature_gun/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/gun_mechanics/temperature/temperature_gun/__init__.py
from __future__ import absolute_import
from constants import TEMPERATURE_GUN_STATE
from vehicles.mechanics.gun_mechanics.temperature.temperature_gun.mechanic_interfaces import ITemperatureGunComponentParams, ITemperatureGunMechanicState
from vehicles.mechanics.gun_mechanics.temperature.temperature_gun.mechanic_models import TemperatureGunComponentParams, TemperatureGunMechanicState, TemperatureGunAmmoState
__all__ = ('ITemperatureGunComponentParams', 'ITemperatureGunMechanicState', 'TemperatureGunComponentParams',
           'TemperatureGunMechanicState', 'TemperatureGunAmmoState', 'DEFAULT_TEMPERATURE_COMPONENT_PARAMS',
           'DEFAULT_TEMPERATURE_MECHANIC_STATE')
DEFAULT_TEMPERATURE_COMPONENT_PARAMS = TemperatureGunComponentParams(100.0, 1.0, 1.0)
DEFAULT_TEMPERATURE_MECHANIC_STATE = TemperatureGunMechanicState(TEMPERATURE_GUN_STATE.IDLE, 0, 0.0, 0.0, 0.0, 1.0, True, DEFAULT_TEMPERATURE_COMPONENT_PARAMS)
