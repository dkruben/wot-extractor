# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/currency_reserves/sounds.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/currency_reserves/sounds.py
from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class SOUNDS(CONST_CONTAINER):
    STATE = 'STATE_overlay_hangar_general'
    ENTER = 'STATE_overlay_hangar_general_on'
    EXIT = 'STATE_overlay_hangar_general_off'


RESERVES_AWARD_SOUND_SPACE = CommonSoundSpaceSettings(name='reserves_award_view', entranceStates={(SOUNDS.STATE): (SOUNDS.ENTER)}, exitStates={(SOUNDS.STATE): (SOUNDS.EXIT)}, enterEvent='', persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True)
