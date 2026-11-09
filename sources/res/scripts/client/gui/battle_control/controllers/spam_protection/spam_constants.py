# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/spam_protection/spam_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/spam_protection/spam_constants.py
from __future__ import absolute_import
from enum import IntEnum
DEFAULT_COOLDOWN = 1.0

class SpamEvents(IntEnum):
    FULLSCREEN_EFFECT = 1
    ALLY_HIT_MESSAGE = 2
    MARKERS_HIT_STATE = 3
    AUTO_SHOOT_TRACER_SOUND = 4


SPAM_COOLDOWNS = {(SpamEvents.FULLSCREEN_EFFECT): 1.0, 
   (SpamEvents.ALLY_HIT_MESSAGE): 3.0, 
   (SpamEvents.MARKERS_HIT_STATE): 1.0, 
   (SpamEvents.AUTO_SHOOT_TRACER_SOUND): 0.25}
