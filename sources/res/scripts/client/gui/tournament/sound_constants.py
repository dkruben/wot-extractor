# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/tournament/sound_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/tournament/sound_constants.py
from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class SOUNDS(CONST_CONTAINER):
    TOURNAMENTS_SOUND_SPACE = 'tournaments'
    STATE_HANGAR_PLACE = 'STATE_hangar_place'
    STATE_HANGAR_PLACE_TOURNAMENTS = 'STATE_hangar_place_tournaments'
    ENTER = 'tournaments_enter'
    EXIT = 'tournaments_exit'


TOURNAMENTS_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.TOURNAMENTS_SOUND_SPACE, entranceStates={(SOUNDS.STATE_HANGAR_PLACE): (SOUNDS.STATE_HANGAR_PLACE_TOURNAMENTS)}, exitStates={}, enterEvent=SOUNDS.ENTER, exitEvent=SOUNDS.EXIT, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True)
