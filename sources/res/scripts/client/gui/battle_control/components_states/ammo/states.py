# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/components_states/ammo/states.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/components_states/ammo/states.py
from __future__ import absolute_import
import typing
from gui.battle_control.battle_constants import CANT_SHOOT_ERROR
from gui.battle_control.components_states.ammo.constants import AmmoShootPossibility
from gui.battle_control.components_states.ammo.interfaces import IComponentAmmoState
if typing.TYPE_CHECKING:
    from gui.battle_control.components_states.ammo.interfaces import IAmmoMode

class DefaultComponentAmmoState(IComponentAmmoState):

    def isReloadingBlocked(self):
        return False

    def canChangeVehicleSetting(self, code):
        return True

    def canShootValidation(self):
        return (
         True, CANT_SHOOT_ERROR.UNDEFINED)

    def getShotsAmount(self):
        return -1

    def getShootPossibility(self, currentShells):
        return AmmoShootPossibility.NOT_DEFINED

    def getSpecialReloadMessage(self):
        return

    def getAmmoMode(self):
        return

    def getShellReloadTimes(self, currShell, shellChangeTime, shells):
        return
