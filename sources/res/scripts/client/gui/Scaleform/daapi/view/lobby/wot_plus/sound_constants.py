# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/wot_plus/sound_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/wot_plus/sound_constants.py
from __future__ import absolute_import
from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class SOUNDS(CONST_CONTAINER):
    INFO_PAGE_NAME = 'wot_plus_info_page'
    VEHICLE_RENTAL_PAGE_NAME = 'vehicle_rental_page'
    OVERLAY_HANGAR_GENERAL = 'STATE_overlay_hangar_general'
    OVERLAY_HANGAR_GENERAL_ON = 'STATE_overlay_hangar_general_on'
    OVERLAY_HANGAR_GENERAL_OFF = 'STATE_overlay_hangar_general_off'


WOT_PLUS_INFO_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.INFO_PAGE_NAME, entranceStates={(SOUNDS.OVERLAY_HANGAR_GENERAL): (SOUNDS.OVERLAY_HANGAR_GENERAL_ON)}, exitStates={(SOUNDS.OVERLAY_HANGAR_GENERAL): (SOUNDS.OVERLAY_HANGAR_GENERAL_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent='', exitEvent='')
VEHICLE_RENTAL_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.VEHICLE_RENTAL_PAGE_NAME, entranceStates={(SOUNDS.OVERLAY_HANGAR_GENERAL): (SOUNDS.OVERLAY_HANGAR_GENERAL_ON)}, exitStates={(SOUNDS.OVERLAY_HANGAR_GENERAL): (SOUNDS.OVERLAY_HANGAR_GENERAL_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent='', exitEvent='')
