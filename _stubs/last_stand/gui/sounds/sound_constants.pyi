# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/sounds/sound_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from last_stand.gui.ls_gui_constants import DifficultyLevel as DifficultyLevel
from gui.impl.lobby.hangar.base.sound_constants import HangarSoundStates as HangarSoundStates
from gui.sounds.filters import States as States, StatesGroup as StatesGroup
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings
from last_stand_common.last_stand_constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from last_stand.gui.sounds.voiceovers import Voiceover as Voiceover
LS_ENTER_EVENT = 'ev_last_stand_main_enter'
LS_EXIT_EVENT = 'ev_last_stand_main_exit'
LS_SOUND_REMAPPING = 'last_stand_remapping'
ABOUT_GAME_MODE_ENTER = 'ev_last_stand_about_event_enter'
ABOUT_GAME_MODE_EXIT = 'ev_last_stand_about_event_exit'
REWARD_PATH_ENTER = 'ev_last_stand_reward_path_enter'
REWARD_PATH_EXIT = 'ev_last_stand_reward_path_exit'
META_INTRO_ENTER = 'ev_last_stand_info_objectives_enter'
META_INTRO_EXIT = 'ev_last_stand_info_objectives_exit'
CONSUMABLES_VIEW_ENTER = 'ev_last_stand_consumables_enter'
CONSUMABLES_VIEW_EXIT = 'ev_last_stand_consumables_exit'
PRE_QUEUE_ENTER = 'ev_last_stand_matchmaker_enter'
PRE_QUEUE_EXIT = 'ev_last_stand_matchmaker_exit'
LS_PREVIEW_ENTER = 'ev_hw_hangar_tank_preview_enter'
LS_PREVIEW_EXIT = 'ev_hw_hangar_tank_preview_exit'
META_STORY_POINT_OPEN_SOUND = 'ev_last_stand_quantum{}_enter'
META_STORY_POINT_CLOSE_SOUND = 'ev_last_stand_quantum{}_exit'
META_VOICEOVER_UNMUTE = 'ev_last_stand_quantum_sound_on'
META_VOICEOVER_MUTE = 'ev_last_stand_quantum_sound_off'
META_VOICEOVER_BUTTON_CLICK_UNMUTE = 'ev_last_stand_quantum_button_sound_on'
META_VOICEOVER_BUTTON_CLICK_MUTE = 'ev_last_stand_quantum_button_sound_off'
PBS_ENTER = 'ev_last_stand_pbs_screen_enter'
PBS_EXIT = 'ev_last_stand_pbs_screen_exit'
BUNDLE_VIEW_ENTER = 'ev_last_stand_exchange_screen_enter'
BUNDLE_VIEW_EXIT = 'ev_last_stand_exchange_screen_exit'
REWARD_WINDOW_ENTER = 'ev_last_stand_reward_screen_enter'
REWARD_WINDOW_EXIT = 'ev_last_stand_reward_screen_exit'
DIFFICULTY_SCREEN: dict
BOTS_SPAWN: dict
BOTS_ENGINE: dict
BOTS_EXPLOSION: dict
BATTLE_START = 'ev_last_stand_gameplay_start'
BATTLE_FINISH = 'ev_last_stand_gameplay_stop'
CONVOY_PROGRESS_RTPC = 'RTPC_ext_ls_boss_bomber'
VEHICLE_OBJ_NAME_PATTERN = 'lsVehicleSound_{}'
HANGAR_SOUND_SETTINGS: Any

class SoundLanguage(CONST_CONTAINER):
    RU_VOICEOVER_REALM_CODES: tuple
    VOICEOVER_LOCALIZATION_SWITCH = 'SWITCH_ext_ev_hw_vo'
    VOICEOVER_CN = 'SWITCH_ext_ev_hw_vo_CN'
    VOICEOVER_RU = 'SWITCH_ext_ev_hw_vo_RU'
    VOICEOVER_UA = 'SWITCH_ext_ev_hw_vo_UA'
    VOICEOVER_EN = 'SWITCH_ext_ev_hw_vo_EN'
    LANGUAGE_UA = 'uk'
    LANGUAGE_RU = 'ru'

class DifficultyWindowState(CONST_CONTAINER):
    GROUP = 'STATE_hangar_filtered'
    OPEN = 'STATE_hangar_filtered_on'
    CLOSE = 'STATE_hangar_filtered_off'

class RewardState(CONST_CONTAINER):
    GROUP = 'STATE_overlay_hangar_general'
    GENERAL_ON = 'STATE_overlay_hangar_general_on'
    GENERAL_OFF = 'STATE_overlay_hangar_general_off'

class PersonalDeathZoneAbilityBossState(CONST_CONTAINER):
    GROUP = 'STATE_ev_gp_deathzone_aoe'
    ENTER = 'STATE_ev_gp_deathzone_aoe_enter'
    EXIT = 'STATE_ev_gp_deathzone_aoe_exit'

class DeathZoneSounds(CONST_CONTAINER):
    ENTER = 'ev_gp_red_death_zone_enter'
    LEAVE = 'ev_gp_red_death_zone_exit'
    DAMAGE = 'ev_gp_red_death_zone_damage'

class PersonalDeathZoneSounds(CONST_CONTAINER):
    ACTIVATION = 'ev_gp_deathzone_aoe_activation'
    DEACTIVATION = 'ev_gp_deathzone_aoe_deactivation'

class PostMortemSounds(CONST_CONTAINER):
    ON = 'ev_last_stand_postmortem_on'
    OFF = 'ev_last_stand_postmortem_off'

class Difficulty(CONST_CONTAINER):
    EASY = '01'
    MEDIUM = '02'
    HARD = '03'
    DEFAULT = EASY
    _DIFFICULTY_BY_ARENA_BONUS_TYPE: dict
    @classmethod
    def getDifficultyByArenaBonusType(cls, arenaBonusType):
        ...

class DifficultyFormatter(object):
    _str: Any
    def __init__(self, str_):
        ...
    def __call__(self, arenaBonusType):
        ...

class DifficultyState(CONST_CONTAINER):
    GROUP = 'STATE_ev_last_stand_chapter'
    VALUE: Any

class BattleEquipmentPanelSounds(CONST_CONTAINER):
    ACTIVATE = 'ev_last_stand_gp_ui_ability_button'
    READY = 'ev_last_stand_gp_ui_ability_button_ready'
    NOT_READY = 'ev_last_stand_gp_ui_ability_button_not_ready'

class LootSounds(CONST_CONTAINER):
    class Player(CONST_CONTAINER):
        PICKUP_SUCCEED: dict
    class Ally(CONST_CONTAINER):
        PICKUP_SUCCEED = 'ev_last_stand_collect_all_players'

class LastStandVO(CONST_CONTAINER):
    PLAYER_DEAD = 'ev_last_stand_vo_player_dead'
    ALLY_4_TANKS_LEFT: Any
    ALLY_3_TANKS_LEFT: Any
    ALLY_2_TANKS_LEFT: Any
    ALLY_1_TANKS_LEFT: Any
    BATTLE_STARTED: Any
    WAVE_2_STARTED = 'ev_last_stand_vo_bots_spawn_02'
    WAVE_3_STARTED = 'ev_last_stand_vo_bots_spawn_03'
    WAVE_4_STARTED = 'ev_last_stand_vo_bots_spawn_04'
    WAVE_5_STARTED = 'ev_last_stand_vo_final_bots_spawn'
    WAVE_FINISHED: Any
    ONE_MINUTE_LEFT = 'ev_last_stand_vo_1min'
    WIN = 'ev_last_stand_vo_win'
    LOSE = 'ev_last_stand_vo_defeat'
    @classmethod
    def getWaveStartedVO(cls, phase):
        ...
    @classmethod
    def getAllyTanksLeftVO(cls, alliesAliveCount):
        ...

class BattleMusic(CONST_CONTAINER):
    WAVE_STARTED = 'ev_last_stand_music_battle'
    BOTS_DESTROYED = 'ev_last_stand_music_exploration'
    WIN = 'ev_last_stand_music_end'

class ObeliskBattleSound(CONST_CONTAINER):
    HIT_2D = 'ev_gp_bot_obelisk_weak_zone_hit_2d'
    HIT_3D = 'ev_gp_bot_obelisk_weak_zone_hit_3d'
