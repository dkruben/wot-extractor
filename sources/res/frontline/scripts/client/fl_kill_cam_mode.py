# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/fl_kill_cam_mode.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/fl_kill_cam_mode.py
from __future__ import absolute_import
from AvatarInputHandler.kill_cam_modes import LookAtKillerMode

class FLLookAtKillerMode(LookAtKillerMode):

    def _canSwitchToAllyVehicle(self):
        return False
