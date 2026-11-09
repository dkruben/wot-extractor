# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/components_states/ammo/interfaces.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/components_states/ammo/interfaces.py
from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from gui.battle_control.components_states.ammo.constants import AmmoShootPossibility, ActiveAmmoMode, ShellMode

class IComponentAmmoState(object):

    def isReloadingBlocked(self):
        raise NotImplementedError

    def canChangeVehicleSetting(self, code):
        raise NotImplementedError

    def canShootValidation(self):
        raise NotImplementedError

    def getShotsAmount(self):
        raise NotImplementedError

    def getShootPossibility(self, currentShells):
        raise NotImplementedError

    def getSpecialReloadMessage(self):
        raise NotImplementedError

    def getAmmoMode(self):
        raise NotImplementedError

    def getShellReloadTimes(self, currShell, shellChangeTime, shells):
        raise NotImplementedError


class IAmmoMode(object):

    def getActiveMode(self):
        raise NotImplementedError

    def getModifiedShells(self):
        raise NotImplementedError

    def getShellMode(self, shellIntCD):
        raise NotImplementedError
