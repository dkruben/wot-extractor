# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/components_states/ammo/shells.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/components_states/ammo/shells.py
from __future__ import absolute_import
import typing
from gui.battle_control.components_states.ammo.constants import ActiveAmmoMode, ShellMode
from gui.battle_control.components_states.ammo.interfaces import IAmmoMode

class DefaultAmmoMode(IAmmoMode):

    def getActiveMode(self):
        return ActiveAmmoMode.NOT_DEFINED

    def getModifiedShells(self):
        return ()

    def getShellMode(self, shellIntCD):
        return ShellMode.NOT_DEFINED
