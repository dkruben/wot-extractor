# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/sounds/sound_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from halloween.gui.halloween_gui_constants import DifficultyLevel as DifficultyLevel
from gui.impl.lobby.hangar.base.sound_constants import HangarSoundStates as HangarSoundStates
from gui.sounds.filters import States as States, StatesGroup as StatesGroup
from halloween.gui.impl.gen.view_models.views.lobby.story_choice_view_model import StoryChoiceViewModel as StoryChoiceViewModel
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings
from halloween_common.halloween_constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from halloween.gui.sounds.voiceovers import Voiceover as Voiceover
HW_SOUND_REMAPPING = 'halloween_remapping'
BUNDLE_ENTER = 'ev_hw_hangar_bundle_screen_enter'
BUNDLE_EXIT = 'ev_hw_hangar_bundle_screen_exit'
HW_ENTER_EVENT = 'ev_hw_main_enter'
HW_EXIT_EVENT = 'ev_hw_main_exit'
HW_RESET_HANGAR_MUSIC_EVENT = 'ev_hw_main_reset'
ABOUT_GAME_MODE_ENTER = 'ev_hw_hangar_info_gamemode_enter'
ABOUT_GAME_MODE_EXIT = 'ev_hw_hangar_info_gamemode_exit'
REWARD_PATH_ENTER = 'ev_hw_hangar_reward_path_enter'
REWARD_PATH_EXIT = 'ev_hw_hangar_reward_path_exit'
META_INTRO_ENTER = 'ev_hw_hangar_info_missions_enter'
META_INTRO_EXIT = 'ev_hw_hangar_info_missions_exit'
CONSUMABLES_VIEW_ENTER = 'ev_hw_hangar_consumables_enter'
CONSUMABLES_VIEW_EXIT = 'ev_hw_hangar_consumables_exit'
COMPARISON_VIEW_ENTER = 'ev_hw_hangar_comparison_enter'
COMPARISON_VIEW_EXIT = 'ev_hw_hangar_comparison_exit'
PRE_QUEUE_ENTER = 'ev_hw_hangar_matchmaker_enter'
PRE_QUEUE_EXIT = 'ev_hw_hangar_matchmaker_exit'
HW_PREVIEW_ENTER = 'ev_hw_hangar_tank_preview_enter'
HW_PREVIEW_EXIT = 'ev_hw_hangar_tank_preview_exit'
META_QUANTUM_SCREEN_ENTER = 'ev_hw_meta_quantum{}_enter'
META_QUANTUM_SCREEN_EXIT = 'ev_hw_meta_quantum{}_exit'
META_QUANTUM_VO_ON = 'ev_hw_meta_quantum{}_vo_on'
META_QUANTUM_VO_OFF = 'ev_hw_meta_quantum{}_vo_off'
PBS_ENTER = 'ev_hw_pbs_screen_enter'
PBS_EXIT = 'ev_hw_pbs_screen_exit'
KING_REWARD_WINDOW_ENTER = 'ev_hw_hangar_king_reward_enter'
KING_REWARD_WINDOW_EXIT = 'ev_hw_hangar_king_reward_exit'
STORY_CHOICE_WINDOW_ENTER = 'ev_hw_meta_narrative_choice_enter'
STORY_CHOICE_WINDOW_EXIT = 'ev_hw_meta_narrative_choice_exit'
CREW_SHOWCASE_ENTER = 'ev_hw_hangar_reward_path_crew_members_enter'
CREW_SHOWCASE_EXIT = 'ev_hw_hangar_reward_path_crew_members_exit'
ABILITIES_INCOMPLETE_DIALOG_ENTER = 'ev_hw_hangar_abilities_incomplete_enter'
ABILITIES_INCOMPLETE_DIALOG_EXIT = 'ev_hw_hangar_abilities_incomplete_exit'
BESTIARY_ENTER = 'ev_hw_hangar_bestiary_enter'
BESTIARY_EXIT = 'ev_hw_hangar_bestiary_exit'
ARENA_PHASE_END_WARNING_EVENT_PREFIX = 'ev_hw_gp_music_1min_{phase:02d}'
DIFFICULTY_SCREEN: dict
BOTS_SPAWN: dict
DEFAULT_BOT_SPAWN = None
BOTS_ENGINE: dict
BOTS_EXPLOSION: dict
BATTLE_START = 'ev_hw_gp_start'
BATTLE_FINISH = 'ev_hw_gp_stop'
PHASE_CHANGED = 'ev_hw_gp_phase_teleportation'
ACTIVE_PHASE_RTPC = 'RTPC_ext_hw_gp_phase'
SOULS_COLLECTOR_OBJ_NAME = 'hwSoulsCollector'
VEHICLE_OBJ_NAME_PATTERN = 'hwVehicleSound_{}'
LOOT_OBJ_NAME_PATTERN = 'hwLootSound_{}'
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

class KingRewardState(CONST_CONTAINER):
    GROUP = 'STATE_overlay_hangar_general'
    GENERAL_ON = 'STATE_overlay_hangar_general_on'
    GENERAL_OFF = 'STATE_overlay_hangar_general_off'

class PersonalDeathZoneAbilityBossState(CONST_CONTAINER):
    GROUP = 'STATE_ev_gp_deathzone_aoe'
    ENTER = 'STATE_ev_gp_deathzone_aoe_enter'
    EXIT = 'STATE_ev_gp_deathzone_aoe_exit'

class VehicleSoulsContainerSounds(CONST_CONTAINER):
    class Player(CONST_CONTAINER):
        ON = 'ev_hw_gp_mini_collector_on'
        OFF = 'ev_hw_gp_mini_collector_off'
    class Ally(CONST_CONTAINER):
        ON = 'ev_hw_gp_mini_collector_on_npc'
        OFF = 'ev_hw_gp_mini_collector_off_npc'

class SoulsCollectorSounds(CONST_CONTAINER):
    RTPC = 'RTPC_ext_hw_gp_collector_capacity'
    LOOP = 'ev_hw_gp_phase_collector'
    COLLECT = 'ev_hw_gp_collecting_mirium_progress'
    FULL = 'ev_hw_gp_collecting_mirium_done'

class DeathZoneSounds(CONST_CONTAINER):
    ENTER = 'ev_hw_gp_red_death_zone_enter'
    LEAVE = 'ev_hw_gp_red_death_zone_exit'
    DAMAGE = 'ev_hw_gp_red_death_zone_damage'

class PersonalDeathZoneSounds(CONST_CONTAINER):
    ACTIVATION = 'ev_hw_gp_deathzone_aoe_activation'
    DEACTIVATION = 'ev_hw_gp_deathzone_aoe_deactivation'

class PostMortemSounds(CONST_CONTAINER):
    ON = 'ev_hw_gp_postmortem_on'
    OFF = 'ev_hw_gp_postmortem_off'

class VehicleDetectorSounds(CONST_CONTAINER):
    RTPC = 'RTPC_ext_hw_gp_immortal_detector'
    DETECTOR_ON = 'ev_hw_gp_immortal_detector_on'
    DETECTOR_OFF = 'ev_hw_gp_immortal_detector_off'

class AwardCongratsWindowSounds(CONST_CONTAINER):
    ON_ENTER: dict

class ActivePhaseState(CONST_CONTAINER):
    GROUP = 'STATE_ev_hw_gp_phase'
    PHASE_1 = 'STATE_ev_hw_gp_phase_01'
    PHASE_2 = 'STATE_ev_hw_gp_phase_02'
    PHASE_3 = 'STATE_ev_hw_gp_phase_03'
    PHASE_4 = 'STATE_ev_hw_gp_phase_04'
    DEFAULT = PHASE_1
    _STATE_PATTERN = 'PHASE_{}'
    @classmethod
    def getStateByPhase(cls, phaseID):
        ...

class Difficulty(CONST_CONTAINER):
    EASY = 'normal'
    MEDIUM = 'hard'
    HARD = 'nightmare'
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
    GROUP = 'STATE_ev_hw_difficulty'
    VALUE: Any

class BossBattleMusic(CONST_CONTAINER):
    BOSS_FIGHT_START = 'ev_hw_music_bf_normal_start'
    FIRST_DAMAGE_2_LIVES_LEFT = 'ev_hw_music_bf_normal_1_2'
    FIRST_DAMAGE_1_LIVES_LEFT = 'ev_hw_music_bf_normal_2_2'
    PHASE_1_FINISH = 'ev_hw_music_bf_normal_2_1'
    BOSS_KILLED = 'ev_hw_music_bf_normal_win'
    LOSE_2_LIVES_LEFT_BEFORE_1_SHOT = 'ev_hw_music_bf_normal_lose_1_1'
    LOSE_2_LIVES_LEFT_AFTER_1_SHOT = 'ev_hw_music_bf_normal_lose_1_2'
    LOSE_1_LIVES_LEFT_BEFORE_1_SHOT = 'ev_hw_music_bf_normal_lose_2_1'
    LOSE_1_LIVES_LEFT_AFTER_1_SHOT = 'ev_hw_music_bf_normal_lose_2_2'
    @classmethod
    def getFirstDamageEventByBossLives(cls, livesLeft):
        ...
    @classmethod
    def getLoseEvent(cls, isFirstShotPerformed, livesLeft):
        ...

class HexapodBossBattleMusic(CONST_CONTAINER):
    BOSS_HP_RTPC = 'RTPC_ext_hw_gp_boss_hp'

class AnomaliesSounds(CONST_CONTAINER):
    class Battle(CONST_CONTAINER):
        ITEM_HOVER = 'ev_hw_gp_ui_anomalies_highlight'
        UPGRADE_PANEL_APPEAR = 'ev_hw_gp_ui_anomalies_appear'
        ENTER = 'ev_hw_gp_ui_anomalies_enter'
        LEAVE = 'ev_hw_gp_ui_anomalies_exit'
    class Hangar(CONST_CONTAINER):
        ENTER = 'ev_hw_hangar_anomalies_enter'
        LEAVE = 'ev_hw_hangar_anomalies_exit'

class BattleEquipmentPanelSounds(CONST_CONTAINER):
    ACTIVATE = 'ev_hw_gp_ui_ability_button'
    READY = 'ev_hw_gp_ui_ability_button_ready'
    NOT_READY = 'ev_hw_gp_ui_ability_button_not_ready'

class BattleBuffsPanelSounds(CONST_CONTAINER):
    ACTIVATE = 'ev_hw_gp_random_buff_hud_on'
    DEACTIVATE = 'ev_hw_gp_random_buff_hud_off'
    SHOW_ICON = 'ev_hw_gp_random_buff_icon'

class PhaseStartSounds(CONST_CONTAINER):
    PHASE_1_STARTED = 'ev_hw_gp_phase_01_stinger'
    PHASE_2_STARTED = 'ev_hw_gp_phase_02_stinger'
    PHASE_3_STARTED = 'ev_hw_gp_phase_03_stinger'
    PHASE_4_STARTED = 'ev_hw_gp_phase_04_stinger'
    _PHASE_STARTED_PATTERN = 'PHASE_{}_STARTED'
    DEFAULT = PHASE_1_STARTED
    @classmethod
    def getPhaseStartedEvent(cls, phaseID):
        ...

class PhaseModifierSounds(CONST_CONTAINER):
    START: dict

class BossBattleSound(CONST_CONTAINER):
    PLAYER_ENTERED_AURA = 'ev_hw_gp_boss_aura_player_in'
    PLAYER_LEAVED_AURA = 'ev_hw_gp_boss_aura_player_out'
    AURA_ACTIVATION = 'ev_hw_gp_boss_aura'
    BOSS_TELEPORTATION = 'ev_hw_gp_bf_boss_teleportation'
    BOSS_HIT_MARKER = 'ev_hw_gp_boss_hit_marker'
    BOSS_HIT_MARKER_INVULNERABILITY = 'ev_hw_gp_boss_hit_marker_invulnerability'
    @classmethod
    def getAuraIntersectionEvent(cls, entered):
        ...

class HexapodBossBattleSound(CONST_CONTAINER):
    HEXAPOD_FIRE = 'ev_hw_gp_bot_hexapod_fire'

class PhaseStartedVoiceover(CONST_CONTAINER):
    PHASE_1: Any
    PHASE_2: Any
    PHASE_3: Any
    PHASE_4: Any
    @classmethod
    def get(cls, phaseIndex):
        ...

class VO(CONST_CONTAINER):
    BOSS_APPEARING: dict
    LOSE_BEFORE_BOSS_BATTLE = 'ev_hw_vo_phase_lose'
    FIRST_SHOT_AT_BOSS_BEFORE_BOSS_BATTLE: Any
    BOSSFIGHT_PHASE_2: Any
    BOSSFIGHT_PHASE_3: Any
    LOSE_BOSS_FIGHT = 'ev_hw_vo_bossfight_lose'
    PHASE_ONE_MINUTE_LEFT: Any
    COLLECTOR_HALF_FILLED: Any
    COLLECTOR_FULL_FILLED: Any
    SHOT_AT_INVULNERABLE_BOSS: Any
    PLAYER_DEAD_COMMON = 'ev_hw_gp_vo_player_dead'
    PLAYER_DEAD_BOSSFIGHT = 'ev_hw_gp_vo_player_bossfight_dead'
    ALLY_4_TANKS_LEFT: Any
    ALLY_3_TANKS_LEFT: Any
    ALLY_2_TANKS_LEFT: Any
    ALLY_1_TANKS_LEFT: Any
    BOTS_SPAWN_BY_ROLE: dict
    SUBTITLES_ENABLED_SETTING = False
    @classmethod
    def getAllyTanksLeftVO(cls, alliesAliveCount):
        ...

class VOObjects(CONST_CONTAINER):
    WIN: Any

class LootSounds(CONST_CONTAINER):
    class States(CONST_CONTAINER):
        DEFAULT: dict
        CAPTURED: dict
    class Player(CONST_CONTAINER):
        PICKUP_STARTED: dict
        PICKUP_CANCELED: dict
        PICKUP_SUCCEED: dict
    class Ally(CONST_CONTAINER):
        PICKUP_SUCCEED = 'ev_hw_gp_collect_mirium_npc'
