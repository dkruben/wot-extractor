# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/personal_reserves/reserves_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/personal_reserves/reserves_constants.py
from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class SOUNDS(CONST_CONTAINER):
    COMMON_SOUND_SPACE = 'personalReserves'
    STATE_PLACE = 'STATE_personal_reserves'
    STATE_PERSONAL_RESERVES_ON = 'STATE_personal_reserves_on'
    STATE_PERSONAL_RESERVES_OFF = 'STATE_personal_reserves_off'
    ENTER_EVENT = 'personal_reserves'


PERSONAL_RESERVES_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.COMMON_SOUND_SPACE, entranceStates={(SOUNDS.STATE_PLACE): (SOUNDS.STATE_PERSONAL_RESERVES_ON)}, exitStates={(SOUNDS.STATE_PLACE): (SOUNDS.STATE_PERSONAL_RESERVES_OFF)}, persistentSounds=(
 SOUNDS.ENTER_EVENT,), stoppableSounds=(), priorities=(), autoStart=True, enterEvent='', exitEvent='')
