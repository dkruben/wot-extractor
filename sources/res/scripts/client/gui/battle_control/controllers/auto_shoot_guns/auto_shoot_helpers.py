# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/auto_shoot_guns/auto_shoot_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/auto_shoot_guns/auto_shoot_helpers.py
from __future__ import absolute_import
from enum import Enum
AUTO_SHOOT_DEV_KEYS = False
AUTO_SHOOT_DEV_BURST_CLAMP = 1.0

class AutoShootDevCommand(Enum):
    RATE_UP = 0
    RATE_DOWN = 1
    RATE_SPEED_UP = 2
    RATE_SPEED_DOWN = 3
    CLAMP_BURST = 4
    RESET = 5
