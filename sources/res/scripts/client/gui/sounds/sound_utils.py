# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/sounds/sound_utils.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/sounds/sound_utils.py
from debug_utils import LOG_DEBUG
from gui.sounds.sound_constants import IS_ADVANCED_LOGGING
if IS_ADVANCED_LOGGING:

    def SOUND_DEBUG(msg, *kargs):
        LOG_DEBUG('[SOUND]', msg, kargs)


else:

    def SOUND_DEBUG(msg, *kargs):
        pass
