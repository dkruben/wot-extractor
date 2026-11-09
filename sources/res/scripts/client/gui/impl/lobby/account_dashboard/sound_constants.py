# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/account_dashboard/sound_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/account_dashboard/sound_constants.py
from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER

class SOUNDS(CONST_CONTAINER):
    STATE_PLACE = 'STATE_hangar_place'
    STATE_PLACE_AD = 'STATE_hangar_place_acc_dashboard'
    EVENT_ENTER = 'ev_acc_dashboard_enter'
    EVENT_EXIT = 'ev_acc_dashboard_exit'


ACC_DASHBOARD_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.STATE_PLACE, entranceStates={(SOUNDS.STATE_PLACE): (SOUNDS.STATE_PLACE_AD)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=SOUNDS.EVENT_ENTER, exitEvent=SOUNDS.EVENT_EXIT)
