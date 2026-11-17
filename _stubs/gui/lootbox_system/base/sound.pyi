# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/lootbox_system/base/sound.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from enum import Enum as Enum
import typing as typing
from typing import TYPE_CHECKING as TYPE_CHECKING
import SoundGroups as SoundGroups
import WWISE as WWISE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from typing import Tuple as Tuple
_logger: Any

class _LootBoxesSounds(str, Enum):
    STATE_GROUP = 'STATE_hangar_place'
    STATE_LOOTBOXES = 'STATE_hangar_place_lootboxes'
    STATE_GARAGE = 'STATE_hangar_place_garage'
    STATE_OVERLAY_GROUP = 'STATE_overlay_hangar_general'
    STATE_REWARDS_ENTER = 'STATE_overlay_hangar_general_on'
    STATE_REWARDS_EXIT = 'STATE_overlay_hangar_general_off'
    AMBIENT_ON = 'gui_lb_amb_on'
    AMBIENT_OFF = 'gui_lb_amb_off'
    VIDEO_PAUSE = 'gui_lb_video_pause'
    VIDEO_RESUME = 'gui_lb_video_resume'
    INFOPAGE_ENTER = 'gui_lb_infopage_enter'
    INFOPAGE_EXIT = 'gui_lb_infopage_exit'

def enterLootBoxesSoundState(eventName):
    ...
def exitLootBoxesSoundState(eventName):
    ...
def enterLootBoxesMultipleRewardState():
    ...
def exitLootBoxesMultipleRewardState():
    ...
def playInfopageEnterSound(eventName):
    ...
def playInfopageExitSound(eventName):
    ...
def playVideoPauseSound(eventName):
    ...
def playVideoResumeSound(eventName):
    ...
def _playAmbientOn(eventName):
    ...
def _playAmbientOff(eventName):
    ...
def _playSounds(soundNames, eventName):
    ...
def _getSound(soundName, eventName):
    ...
