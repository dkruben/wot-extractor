# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/control_modes.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/control_modes.py
from __future__ import absolute_import
import CommandMapping
from AvatarInputHandler import control_modes

class HWArcadeControlMode(control_modes.ArcadeControlMode):

    def handleKeyEvent(self, isDown, key, mods, event=None):
        cmdMap = CommandMapping.g_instance
        if cmdMap.isFired(CommandMapping.CMD_CM_VEHICLE_SWITCH_AUTOROTATION, key) and isDown:
            return False
        return super(HWArcadeControlMode, self).handleKeyEvent(isDown, key, mods, event)


class HWSniperControlMode(control_modes.SniperControlMode):

    def handleKeyEvent(self, isDown, key, mods, event=None):
        cmdMap = CommandMapping.g_instance
        if cmdMap.isFired(CommandMapping.CMD_CM_VEHICLE_SWITCH_AUTOROTATION, key) and isDown:
            return False
        return super(HWSniperControlMode, self).handleKeyEvent(isDown, key, mods, event)


class HWPostMortemControlMode(control_modes.PostMortemControlMode):

    def _isPostmortemDelayEnabled(self):
        return False
