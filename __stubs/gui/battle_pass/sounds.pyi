# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_pass/sounds.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import WWISE as WWISE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.sounds.filters import StatesGroup as StatesGroup, States as States
from helpers.dependency import replace_none_kwargs as replace_none_kwargs
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings
_logger: Any
BATTLE_PASS_SOUND_SPACE = 'tasks'
BATTLE_PASS_TASKS_SOUND_SPACE: Any
ACTIVATE_CHAPTER_SOUND_SPACE: Any

class BattlePassSounds(CONST_CONTAINER):
    CONFIRM_BUY = 'bp_overlay_pay'
    REWARD_SCREEN = 'bp_reward_screen'
    TANK_POINTS_CAP = 'bp_tank_point_done'
    VIDEO_PAUSE = 'bp_video_pause'
    VIDEO_RESUME = 'bp_video_resume'
    VIDEO_STOP = 'bp_video_stop'
    VOICEOVER_STOP = 'bp_voiceovers_stop'
    REGULAR_VOICEOVER_STOP = 'bp_regular_voiceovers_stop'
    HOLIDAY_VOICEOVER_STOP = 'bp_holiday_voiceovers_stop'
    HOLIDAY_REWARD_SCREEN = 'bp_holiday_reward_screen'
    TASKS_ENTER = 'tasks_enter'
    TASKS_EXIT = 'tasks_exit'
    SPECIAL_TASKS_ENTER = 'tasks_special_enter'
    SPECIAL_TASKS_EXIT = 'tasks_special_exit'
    HOLIDAY_TASKS_ENTER = 'tasks_holiday_enter'
    HOLIDAY_TASKS_EXIT = 'tasks_holiday_exit'

class BattlePassStates(CONST_CONTAINER):
    DIALOG_STATE = 'STATE_overlay_hangar_general'
    DIALOG_STATE_ON = 'STATE_overlay_hangar_general_on'
    DIALOG_STATE_OFF = 'STATE_overlay_hangar_general_off'
    HANGAR_PLACE_STATE = 'STATE_hangar_place'
    HANGAR_PLACE_STATE_TASKS = 'STATE_hangar_place_tasks'
    BATTLE_PASS_PLACE_STATE = 'STATE_hangar_place_battle_pass'
    BATTLE_PASS_PLACE_STATE_ON = 'STATE_hangar_place_battle_pass_on'
    BATTLE_PASS_PLACE_STATE_OFF = 'STATE_hangar_place_battle_pass_off'

def switchBattlePassSoundFilter(on=True):
    ...
def switchOverlaySoundFilter(on=True):
    ...
# decorador original: @replace_none_kwargs(...)
def getBattlePassEnterSound(battlePass=None):
    ...
# decorador original: @replace_none_kwargs(...)
def getBattlePassExitSound(battlePass=None):
    ...
def getBattlePassExtraEnterSound(chapterID):
    ...
def getBattlePassExtraExitSound(chapterID):
    ...
def _getSound(soundNameTemplate, soundID, defaultSound):
    ...
