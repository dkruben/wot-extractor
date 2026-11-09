# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/sound_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/profile/sound_constants.py
from __future__ import absolute_import
from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER

class SOUNDS(CONST_CONTAINER):
    COMMON_SOUND_SPACE = 'achievements'
    ACHIEVEMENTS_ENTER = 'achievements_enter'
    ACHIEVEMENTS_EXIT = 'achievements_exit'
    STATE_PLACE_ACHIEVEMENTS = 'STATE_hangar_place_achievements'
    STATE_PLACE = 'STATE_hangar_place'


ACHIEVEMENTS_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.COMMON_SOUND_SPACE, entranceStates={(SOUNDS.STATE_PLACE): (SOUNDS.STATE_PLACE_ACHIEVEMENTS)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=SOUNDS.ACHIEVEMENTS_ENTER, exitEvent=SOUNDS.ACHIEVEMENTS_EXIT)
ACHIEVEMENTS_REWARD_SCREEN_EXIT_EVENT = 'ach_reward_screen_exit'
