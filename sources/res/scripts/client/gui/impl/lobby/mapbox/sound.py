# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/mapbox/sound.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/mapbox/sound.py
from enum import Enum
from sound_gui_manager import CommonSoundSpaceSettings
import WWISE

class Sounds(Enum):
    OVERLAY_HANGAR_GENERAL = 'STATE_overlay_hangar_general'
    OVERLAY_HANGAR_GENERAL_ON = 'STATE_overlay_hangar_general_on'
    OVERLAY_HANGAR_GENERAL_OFF = 'STATE_overlay_hangar_general_off'


class MapBoxSounds(Enum):
    REWARD_SCREEN = 'bp_reward_screen'


def getMapboxViewSoundSpace(enterEvent='', exitEvent=''):
    return CommonSoundSpaceSettings(name='mapbox_view', entranceStates={(Sounds.OVERLAY_HANGAR_GENERAL.value): (Sounds.OVERLAY_HANGAR_GENERAL_ON.value)}, exitStates={(Sounds.OVERLAY_HANGAR_GENERAL.value): (Sounds.OVERLAY_HANGAR_GENERAL_OFF.value)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=enterEvent, exitEvent=exitEvent)


def playSound(eventName):
    WWISE.WW_eventGlobal(eventName)
