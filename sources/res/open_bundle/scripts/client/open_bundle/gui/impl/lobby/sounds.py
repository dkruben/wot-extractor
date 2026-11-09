# wot-extractor: codigo DESCOMPILADO de sources/res/open_bundle/scripts/client/open_bundle/gui/impl/lobby/sounds.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: open_bundle/scripts/client/open_bundle/gui/impl/lobby/sounds.py
from __future__ import absolute_import
from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class SOUNDS(CONST_CONTAINER):
    SPACE = 'open_bundle_space'
    STATE_PLACE = 'STATE_hangar_place'
    STATE_PLACE_BUNDLE = 'STATE_hangar_place_open_bundle'
    BUNDLE_ENTER = 'openbundle_enter'
    BUNDLE_EXIT = 'openbundle_exit'


OPEN_BUNDLE_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.SPACE, entranceStates={(SOUNDS.STATE_PLACE): (SOUNDS.STATE_PLACE_BUNDLE)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=SOUNDS.BUNDLE_ENTER, exitEvent=SOUNDS.BUNDLE_EXIT)
