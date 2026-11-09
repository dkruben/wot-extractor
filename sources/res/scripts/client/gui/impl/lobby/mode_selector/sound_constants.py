# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/mode_selector/sound_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/mode_selector/sound_constants.py
from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER

class ModeSelectorSound(CONST_CONTAINER):
    COMMON_SOUND_SPACE = 'mode_selector'
    STATE_PLACE = 'STATE_mode_selector'
    STATE_MODE_SELECTOR_ON = 'STATE_mode_selector_on'
    STATE_MODE_SELECTOR_OFF = 'STATE_mode_selector_off'
    ENTER_EVENT = 'ev_mode_selector_enter'
    EXIT_EVENT = 'ev_mode_selector_exit'


MODE_SELECTOR_SOUND_SPACE = CommonSoundSpaceSettings(name=ModeSelectorSound.COMMON_SOUND_SPACE, entranceStates={(ModeSelectorSound.STATE_PLACE): (ModeSelectorSound.STATE_MODE_SELECTOR_ON)}, exitStates={(ModeSelectorSound.STATE_PLACE): (ModeSelectorSound.STATE_MODE_SELECTOR_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=ModeSelectorSound.ENTER_EVENT, exitEvent=ModeSelectorSound.EXIT_EVENT)
