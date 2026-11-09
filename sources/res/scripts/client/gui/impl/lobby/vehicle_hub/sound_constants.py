# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/sound_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/vehicle_hub/sound_constants.py
from __future__ import absolute_import
from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER

class SOUNDS(CONST_CONTAINER):
    COMMON_SOUND_SPACE = 'vehicle_hub'
    ABOUT_VEHICLE_ENTER = 'ev_about_vehicle_enter'
    ABOUT_VEHICLE_EXIT = 'ev_about_vehicle_exit'
    STATE_PLACE_ABOUT_VEHICLE = 'STATE_hangar_place_about_vehicle'
    STATE_PLACE = 'STATE_hangar_place'


VH_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.COMMON_SOUND_SPACE, entranceStates={(SOUNDS.STATE_PLACE): (SOUNDS.STATE_PLACE_ABOUT_VEHICLE)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=SOUNDS.ABOUT_VEHICLE_ENTER, exitEvent=SOUNDS.ABOUT_VEHICLE_EXIT)
