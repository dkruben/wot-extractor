# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/techtree/sound_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/techtree/sound_constants.py
from __future__ import absolute_import
from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER

class Sounds(CONST_CONTAINER):
    COMMON_SOUND_SPACE = 'techtree'
    STATE_PLACE = 'STATE_hangar_place'
    STATE_PLACE_TECHTREE = 'STATE_hangar_place_research'
    AMBIENT = 'researches_ambience'
    MUSIC = 'researches_music'
    RESET = 'researches_music_reset'


TECHTREE_SOUND_SPACE = CommonSoundSpaceSettings(name=Sounds.COMMON_SOUND_SPACE, entranceStates={(Sounds.STATE_PLACE): (Sounds.STATE_PLACE_TECHTREE)}, exitStates={}, persistentSounds=(
 Sounds.MUSIC, Sounds.AMBIENT), stoppableSounds=(), priorities=(), autoStart=True, exitEvent=Sounds.RESET)
