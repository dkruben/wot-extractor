# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/generic_mechanics/shell_calibration/mechanic_models.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/generic_mechanics/shell_calibration/mechanic_models.py
from __future__ import absolute_import, division
from gui.battle_control.components_states.ammo import DefaultComponentAmmoState
from gui.battle_control.components_states.ammo.constants import ShellMode
from gui.battle_control.components_states.ammo.shells import DefaultAmmoMode

class ShellCalibrationAmmoMode(DefaultAmmoMode):

    def __init__(self, calibrationShells):
        self.__calibrationShells = frozenset(calibrationShells)

    def getShellMode(self, shellIntCD):
        if shellIntCD in self.__calibrationShells:
            return ShellMode.SHELL_CALIBRATION
        return ShellMode.NOT_DEFINED


class ShellCalibrationAmmoState(DefaultComponentAmmoState):

    def __init__(self, calibrationShells):
        super(ShellCalibrationAmmoState, self).__init__()
        self.__ammoMode = ShellCalibrationAmmoMode(calibrationShells)

    def getAmmoMode(self):
        return self.__ammoMode
