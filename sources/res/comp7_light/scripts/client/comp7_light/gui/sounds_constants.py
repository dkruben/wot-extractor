# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/sounds_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/sounds_constants.py
from __future__ import absolute_import
from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class SOUNDS(CONST_CONTAINER):
    GENERAL_STATE = 'STATE_overlay_hangar_general'
    GENERAL_STATE_ON = 'STATE_overlay_hangar_general_on'
    GENERAL_STATE_OFF = 'STATE_overlay_hangar_general_off'


GENERAL_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.GENERAL_STATE, entranceStates={(SOUNDS.GENERAL_STATE): (SOUNDS.GENERAL_STATE_ON)}, exitStates={(SOUNDS.GENERAL_STATE): (SOUNDS.GENERAL_STATE_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent='', exitEvent='')
