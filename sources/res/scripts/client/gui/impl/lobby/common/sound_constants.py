# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/common/sound_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/common/sound_constants.py
from sound_gui_manager import CommonSoundSpaceSettings
from gui.sounds.filters import States, StatesGroup
FIELD_POST_SOUND_SETTINGS = CommonSoundSpaceSettings(name='field_post', entranceStates={'STATE_hangar_place': 'STATE_hangar_place_garage', 
   (StatesGroup.HANGAR_FILTERED): (States.HANGAR_FILTERED_ON)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent='', exitEvent='')
SUBVIEW_SOUND_SPACE = CommonSoundSpaceSettings(name='sub_view', entranceStates={'STATE_hangar_place': 'STATE_hangar_place_garage', 
   (StatesGroup.HANGAR_FILTERED): (States.HANGAR_FILTERED_ON)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent='', exitEvent='')
BROWSER_VIEW_SOUND_SPACES = {(FIELD_POST_SOUND_SETTINGS.name): FIELD_POST_SOUND_SETTINGS, 
   (SUBVIEW_SOUND_SPACE.name): SUBVIEW_SOUND_SPACE}
HANGAR_FILTERED_SOUND_SPACE = CommonSoundSpaceSettings(name='filterHangar', entranceStates={(StatesGroup.HANGAR_FILTERED): (States.HANGAR_FILTERED_ON)}, exitStates={(StatesGroup.HANGAR_FILTERED): (States.HANGAR_FILTERED_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent='', exitEvent='')
