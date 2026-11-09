# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/auxiliary_rocket_launcher/mechanic_models.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/gun_mechanics/auxiliary_rocket_launcher/mechanic_models.py
from __future__ import absolute_import, division
import typing
from collections import namedtuple
import BigWorld
from constants import SECONDARY_GUN_STATE
from gui.battle_control.components_states.ammo import ActiveAmmoMode, DefaultAmmoMode, DefaultComponentAmmoState, ShellMode
from vehicles.mechanics.mechanic_states import IMechanicState
if typing.TYPE_CHECKING:
    from gui.battle_control.components_states.ammo.interfaces import IAmmoMode

class AuxiliaryRocketLauncherState(namedtuple('AuxiliaryRocketLauncherState', ('gunInstallationIndex', 'state', 'baseTime',
                                            'endTime', 'isReloaded', 'reloadStartTime',
                                            'isInAimingMode')), IMechanicState):

    @property
    def progress(self):
        if self.baseTime > 0:
            return 1.0 - self.timeLeft / self.baseTime
        return 1.0

    @property
    def timeLeft(self):
        return max(0.0, self.endTime - BigWorld.serverTime() if self.endTime >= 0 else self.baseTime)

    def isTransition(self, other):
        return self.state != other.state or self.isInAimingMode != other.isInAimingMode

    def isValidForAimingMode(self):
        return self.state in (
         SECONDARY_GUN_STATE.READY,
         SECONDARY_GUN_STATE.DISABLED)


class AuxiliaryRocketLauncherAmmoMode(DefaultAmmoMode):

    def __init__(self, isInAimingMode):
        self.__isInAimingMode = isInAimingMode

    def getActiveMode(self):
        if self.__isInAimingMode:
            return ActiveAmmoMode.MODIFIED_SHELLS
        return ActiveAmmoMode.DEFAULT_SHELLS

    def getShellMode(self, shellIntCD):
        return ShellMode.AUXILIARY_ROCKET_LAUNCHER


class AuxiliaryRocketLauncherAmmoState(DefaultComponentAmmoState):

    def __init__(self, isInAimingMode):
        super(AuxiliaryRocketLauncherAmmoState, self).__init__()
        self.__ammoMode = AuxiliaryRocketLauncherAmmoMode(isInAimingMode)

    def getAmmoMode(self):
        return self.__ammoMode
