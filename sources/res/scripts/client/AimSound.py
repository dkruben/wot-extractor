# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/AimSound.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/AimSound.py
from __future__ import absolute_import
import SoundGroups

class AimSound(object):
    TARGET_UNLOCKED = 0
    TARGET_LOCKED = 1
    TARGET_LOST = 2
    aimSounds = (
     ('ui_target_unlocked', 'target_unlocked'),
     ('ui_target_locked', 'target_captured'),
     ('ui_target_lost', 'target_lost'))

    @staticmethod
    def play(state, playerNotifications=None):
        sounds = AimSound.aimSounds[state]
        SoundGroups.g_instance.playSound2D(sounds[0])
        if playerNotifications is not None:
            playerNotifications.play(sounds[1])
        return
