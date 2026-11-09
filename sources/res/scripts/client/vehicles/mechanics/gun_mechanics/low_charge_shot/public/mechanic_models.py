# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/low_charge_shot/public/mechanic_models.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/gun_mechanics/low_charge_shot/public/mechanic_models.py
from __future__ import absolute_import
import typing
from constants import LowChargeShotVisualState
from gui.shared.utils.decorators import ReprInjector
from vehicles.mechanics.mechanic_states import IMechanicState

@ReprInjector.simple('visualState', 'fullShotChangeTime')
class LowChargeShotPublicMechanicState(typing.NamedTuple('LowChargeShotPublicMechanicState', (
 (
  'visualState', LowChargeShotVisualState),
 (
  'fullShotChangeTime', float),
 (
  'almostFinishedTime', float))), IMechanicState):

    @classmethod
    def fromComponentStatus(cls, state, params):
        return cls(state.visualState, state.fullShotChangeTime, params.almostFinishedTime)

    def isTransition(self, other):
        return self.visualState != other.visualState
