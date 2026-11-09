# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/low_charge_shot/private/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/gun_mechanics/low_charge_shot/private/__init__.py
from __future__ import absolute_import
from constants import LowChargeShotReloadingState
from vehicles.mechanics.gun_mechanics.low_charge_shot.private.mechanic_models import LowChargeShotMechanicState, LowChargeShotAmmoState
from vehicles.mechanics.gun_mechanics.low_charge_shot.private.mechanic_logging import LowChargeShotUILogging
__all__ = ('LowChargeShotMechanicState', 'LowChargeShotAmmoState', 'LowChargeShotUILogging')
DEFAULT_MECHANIC_STATE = LowChargeShotMechanicState(LowChargeShotReloadingState.EMPTY, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
