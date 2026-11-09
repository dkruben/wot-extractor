# wot-extractor: codigo DESCOMPILADO de sources/res/server_side_replay/scripts/client/server_side_replay/gui/impl/lobby/replays_lobby_sounds.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: server_side_replay/scripts/client/server_side_replay/gui/impl/lobby/replays_lobby_sounds.py
from __future__ import absolute_import
from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class SOUNDS(CONST_CONTAINER):
    COMMON_SOUND_SPACE = 'crew'
    STATE_PLACE = 'STATE_hangar_place'
    STATE_PLACE_BARRAKS = 'STATE_hangar_place_barracks'
    STATE_PLACE_HANGAR = 'STATE_hangar_place_garage'
    OVERLAY_SOUND_SPACE = 'crew_overlay'
    OVERLAY_HANGAR_GENERAL = 'STATE_overlay_hangar_general'
    OVERLAY_HANGAR_GENERAL_ON = 'STATE_overlay_hangar_general_on'
    OVERLAY_HANGAR_GENERAL_OFF = 'STATE_overlay_hangar_general_off'


REPLAYS_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.COMMON_SOUND_SPACE, entranceStates={(SOUNDS.STATE_PLACE): (SOUNDS.STATE_PLACE_BARRAKS)}, exitStates={(SOUNDS.STATE_PLACE): (SOUNDS.STATE_PLACE_HANGAR)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent='hangar_crew_enter', exitEvent='hangar_crew_exit')
REPLAYS_SOUND_OVERLAY_SPACE = CommonSoundSpaceSettings(name=SOUNDS.OVERLAY_SOUND_SPACE, entranceStates={(SOUNDS.OVERLAY_HANGAR_GENERAL): (SOUNDS.OVERLAY_HANGAR_GENERAL_ON)}, exitStates={(SOUNDS.OVERLAY_HANGAR_GENERAL): (SOUNDS.OVERLAY_HANGAR_GENERAL_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent='', exitEvent='', parentSpace=SOUNDS.COMMON_SOUND_SPACE)
