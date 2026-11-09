# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/components_states/ammo/constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/components_states/ammo/constants.py
from __future__ import absolute_import
from enum import Enum, IntEnum
from items.vehicle_mechanics_types import VehicleMechanicKeys

class AmmoShootPossibility(IntEnum):
    NOT_DEFINED = 0
    ALLOWED = 1
    DENIED = 2


class ActiveAmmoMode(IntEnum):
    NOT_DEFINED = 0
    DEFAULT_SHELLS = 1
    MODIFIED_SHELLS = 2


class ShellMode(Enum):
    NOT_DEFINED = ''
    LOW_CHARGE_SHOT = VehicleMechanicKeys.LOW_CHARGE_SHOT.uniqueName
    BUSTLE_FEED = VehicleMechanicKeys.BUSTLE_FEED.uniqueName
    SHELL_PARAMS_SWITCHER = VehicleMechanicKeys.SHELL_PARAMS_SWITCHER.uniqueName
    AUXILIARY_ROCKET_LAUNCHER = VehicleMechanicKeys.AUXILIARY_ROCKET_LAUNCHER.uniqueName
    SHELL_CALIBRATION = VehicleMechanicKeys.SHELL_CALIBRATION.uniqueName
