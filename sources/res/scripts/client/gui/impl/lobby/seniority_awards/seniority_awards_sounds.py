# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/seniority_awards/seniority_awards_sounds.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/seniority_awards/seniority_awards_sounds.py
from __future__ import absolute_import
import WWISE
from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings
from gui.sounds.filters import StatesGroup, States
SENIORITY_REWARD_SOUND_SPACE = CommonSoundSpaceSettings(name='seniority_award', entranceStates={(StatesGroup.OVERLAY_HANGAR_GENERAL): (States.OVERLAY_HANGAR_GENERAL_ON)}, exitStates={(StatesGroup.OVERLAY_HANGAR_GENERAL): (States.OVERLAY_HANGAR_GENERAL_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent='', exitEvent='')

class LootBoxViewEvents(CONST_CONTAINER):
    ENTRY_VIEW_ENTER = 'gui_lootbox_logistic_center_ambience_on'
    ENTRY_VIEW_EXIT = 'gui_lootbox_logistic_center_ambience_off'
    BENGAL_FIRE_OFF = 'gui_lootbox_logistic_center_bengal_fire_off'


def playSound(eventName):
    if eventName:
        WWISE.WW_eventGlobal(eventName)
