# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/challenges/sounds.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/challenges/sounds.py
from __future__ import absolute_import
from enum import Enum
from gui.sounds.filters import States, StatesGroup
from sound_gui_manager import CommonSoundSpaceSettings

class ChallengesSounds(str, Enum):
    REWARD_SCREEN = 'bp_reward_screen'


CHALLENGE_AWARDS_SOUND_SPACE = CommonSoundSpaceSettings(name=StatesGroup.OVERLAY_HANGAR_GENERAL, entranceStates={(StatesGroup.OVERLAY_HANGAR_GENERAL): (States.OVERLAY_HANGAR_GENERAL_ON)}, exitStates={(StatesGroup.OVERLAY_HANGAR_GENERAL): (States.OVERLAY_HANGAR_GENERAL_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=ChallengesSounds.REWARD_SCREEN, exitEvent='')
