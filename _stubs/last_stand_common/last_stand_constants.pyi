# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/common/last_stand_common/last_stand_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import enum as enum
import constants as constants
import UnitBase as UnitBase
import arena_bonus_type_caps as arena_bonus_type_caps
from chat_commands_consts import MarkerType as MarkerType, BattleChatCommandExtProcessorType as BattleChatCommandExtProcessorType
from constants_utils import ConstInjector as ConstInjector, AbstractBattleMode as AbstractBattleMode
from last_stand_common.battle_results import ls_results as ls_results
from BattleFeedbackCommon import BATTLE_EVENT_TYPE as BET
from messenger_common_chat2 import ExtBattleChatCommand as ExtBattleChatCommand
LAST_STAND_ARENA_BONUS_TYPES: tuple
LAST_STAND_QUEUE_TYPES: tuple
UNIT_ASSEMBLER_CONFIG_NAME = 'last_stand'
UNIT_ASSEMBLER_IMPL_TO_CONFIG: dict
PREBATTLE_TYPE_TO_UNIT_ASSEMBLER: dict
UNIT_LS_EXTRA_DATA_KEY = 'LS_Data'
UNIT_DIFFICULTY_LEVELS_KEY = 'LS_difficultyLevels'
UNIT_INFO_BOOSTERS_KEY = 'LS_boostersInfo'
DEFAULT_UNIT_DIFFICULTY_LEVELS: list
LS_PLAYER_INFO_BOOSTERS_KEY = UNIT_INFO_BOOSTERS_KEY
LS_EXTRA_DATA_BOOSTERS_KEY = 'LS_ArenaBoosters'
LS_ADD_PARAM_BOOSTERS_KEY = 'LS_ArenaBoosters'
REQUIRED_VEHICLE_TAGS: dict
FORBIDDEN_VEHICLE_TAGS: Any
DAMAGE_INFO_CODES_PER_ATTACK_REASON: dict
LAST_STAND_GAME_PARAMS_KEY = 'last_stand_config'
LAST_STAND_BATTLE_PARAMS_KEY = 'last_stand_battle_config'
ENEMY_ROLE_TAG_PREFIX = 'lsrole_'
OBELISK_ROLE_TAG = 'lsrole_obelisk'
LS_BOSS_ROLE_TAG = 'lsrole_boss'
CONTINUOUS_TURRET_ROTATION_TAG = 'ls_continuous_turret_rotation'
LS_ROLE_PREFIX = 'ls_'
LS_BOMBER_ACTIVATE_REASON: tuple
PLAYERS_TEAM = 1
INVALID_BATTLE_PLACE = -1
CURRENT_QUEUE_TYPE_KEY = 'currentQueueType'
TOKEN_DIFFICULTY_LEVEL_TO_QUEUE_TYPE: dict
QUEUE_TYPE_TO_TOKEN_DIFFICULTY_LEVEL: dict
ARENA_BONUS_TYPE_TO_LEVEL: dict
ARTEFACT_ID_MASK = 'ls_artefact:{index}:'
SOULS_CHANGE_REASON_TO_BOOSTER_FACTOR_NAMES: dict
LS_INVENTORY_PDATA_KEY = 'LS_inventory'
LS_INFO_PDATA_KEY = 'LS_info'
LS_EMPTY_SLOTS_EQ: tuple
LS_BUILT_IN_EQUIPMENT: list
LS_DEFAULT_AUTO_MAINTENANCE = True
LS_VEHILCE_DAILY_QUEST = 'ls_vehicle_daily_quest:points'
INVALID_PHASE = 0
LS_QUESTS_PREFIX = 'ls_'
LS_TOKENS_PREFIX = 'ls_'
DEFAULT_DIFFICULTY_MODIFIER = 1
LS_OBELISK_ACTIVE_TIME = 10.0
LS_OBELISK_VEH_MARKER = 'lsObelisk'
LS_BATTLE_CHAT_COMMAND_SETTINGS: tuple

class ARENA_GUI_TYPE(constants.ARENA_GUI_TYPE, ConstInjector):
    LAST_STAND = 102

class ARENA_BONUS_TYPE(constants.ARENA_BONUS_TYPE, ConstInjector):
    LAST_STAND = 107
    LAST_STAND_MEDIUM = 108
    LAST_STAND_HARD = 109

class QUEUE_TYPE(constants.QUEUE_TYPE, ConstInjector):
    LAST_STAND = 107
    LAST_STAND_MEDIUM = 108
    LAST_STAND_HARD = 109

class PREBATTLE_TYPE(constants.PREBATTLE_TYPE, ConstInjector):
    LAST_STAND = 102

class UNIT_MGR_FLAGS(UnitBase.UNIT_MGR_FLAGS, ConstInjector):
    LAST_STAND = 8388608

class ROSTER_TYPE(UnitBase.ROSTER_TYPE, ConstInjector):
    LAST_STAND: Any

class INVITATION_TYPE(constants.INVITATION_TYPE, ConstInjector):
    LAST_STAND = PREBATTLE_TYPE.LAST_STAND

class CLIENT_UNIT_CMD(UnitBase.CLIENT_UNIT_CMD, ConstInjector):
    SET_LS_UNIT_DIFFICULTY_LEVEL = 2002

class UnitAssemblerImplType(UnitBase.UnitAssemblerImplType, ConstInjector):
    LAST_STAND = 107
    LAST_STAND_MEDIUM = 108
    LAST_STAND_HARD = 109

class ATTACK_REASON(constants.ATTACK_REASON, ConstInjector):
    _const_type: Any
    LS_BOMBER_EXPLOSION = 'ls_bomber_explosion'
    LS_ABILITY_VAMPIRE = 'ls_ability_vampire'
    LS_ABILITY_AOE_DAMAGE = 'ls_ability_aoe_damage'
    LS_ABILITY_IGNITE = 'ls_ability_ignite'
    LS_PHASE_TIMER = 'ls_phase_timer'
    LS_LEAVER = 'ls_leaver'
    LS_PASSIVE_IGNITE = 'ls_passive_ignite'
    LS_PASSIVE_VAMPIRE = 'ls_passive_vampire'
    LS_DEATH_PIT = 'ls_death_pit'
    LS_SHOT_AOE_DAMAGE = 'ls_shot_aoe_damage'
    LS_SHOT_AOE_DRAIN_ENEMY_HP = 'ls_shot_aoe_drain_enemy_hp'
    LS_SHOT_AOE_STUN = 'ls_shot_aoe_stun'
    LS_EXTRA_DAMAGE_SITUATIONAL = 'ls_extra_damage_situational'
    LS_OBELISK_DAMAGE_TRANSFER = 'ls_obelisk_damage_transfer'

class ARENA_BONUS_TYPE_CAPS(arena_bonus_type_caps.ARENA_BONUS_TYPE_CAPS, ConstInjector):
    _const_type: Any
    LAST_STAND = 'LAST_STAND'

class LastStandBattleMode(AbstractBattleMode):
    _PREBATTLE_TYPE = PREBATTLE_TYPE.LAST_STAND
    _QUEUE_TYPE = QUEUE_TYPE.LAST_STAND
    _ARENA_BONUS_TYPE = ARENA_BONUS_TYPE.LAST_STAND
    _ARENA_GUI_TYPE = ARENA_GUI_TYPE.LAST_STAND
    _INVITATION_TYPE = INVITATION_TYPE.LAST_STAND
    _BATTLE_MGR_NAME = 'LSBattlesMgr'
    _UNIT_MGR_NAME = 'LSUnitMgr'
    _UNIT_MGR_FLAGS = UNIT_MGR_FLAGS.LAST_STAND
    _ROSTER_TYPE = ROSTER_TYPE.LAST_STAND
    _GAME_PARAMS_KEY = LAST_STAND_GAME_PARAMS_KEY
    _BATTLE_PARAMS_KEY = LAST_STAND_BATTLE_PARAMS_KEY
    _BATTLE_RESULTS_CONFIG = ls_results
    _REQUIRED_VEHICLE_TAGS = REQUIRED_VEHICLE_TAGS
    _FORBIDDEN_VEHICLE_TAGS = FORBIDDEN_VEHICLE_TAGS
    _SM_TYPE_REWARD_CONGRATS = 'lsRewardCongrats'
    _SM_TYPE_DIFFICULTY_OPEN_MESSAGE = 'lsDifficultyOpenMessage'
    _SM_TYPE_PROGRESS_POINTS_MESSAGE = 'lsProgressPointsMessage'
    _SM_TYPE_PURCHASE_BUNDLE_FOR_GOLD_MESSAGE = 'lsPurchaseBundleForGold'
    _SM_TYPE_BATTLE_RESULT = 'lsBattleResults'
    _SM_TYPE_BATTLE_PASS_POINTS_MESSAGE = 'lsBattlePassPointsMessage'
    _SM_TYPE_AUTO_MAINTENANCE = 'lsAutoMaintenance'
    _SM_TYPE_LS_INVOICE_RECEIVED = 'lsInvoiceReceived'
    _FAIRPLAY_VEHICLE_BATTLE_STATS_COMPONENT = 'LSFairplayVehicleBattleStatsComponent'
    _SM_TYPES: list
    _CLIENT_SM_TYPES: list
    @property
    def _rosterClass(self):
        ...
    @property
    def _client_attackReasonToCode(self):
        ...

class DifficultyLevelToken(object):
    EASY = 'ls_difficulty_level:easy'
    MEDIUM = 'ls_difficulty_level:medium'
    HARD = 'ls_difficulty_level:hard'
    ALWAYS_AVIABLED: tuple
    ACCESS_REQUIRED: tuple
    ALL_LEVELS: tuple

class ShopSettings(object):
    SHOP_BUNDLE_PREFFIX = 'ls_bundle'
    PURCHASED_SUFFIX = ':purchased'
    WG_MONEY_CALLBACK = 'lsPurchaseEventShopBundleWGMoney'
    TOKEN_TTL = 720

class ArtefactsSettings(object):
    ARTEFACT = 'ls_artefact'
    QUEST_PREFIX = 'ls_artefact:'
    TOKEN_PREFIX = 'ls_artefact:'
    TOKEN_TTL = 720

class ProgressPointsSettings(object):
    TOKEN = 'ls_progress:point'
    TOKEN_TTL = 720
    TOKEN_LIMIT = 10000
    NOTIFY_TOKEN = 'ls_progress:notifyPoint'
    BONUS_NAME = 'ls_progress_point'

class StoryPointsSettings(object):
    TOKEN_PREFIX = 'ls_story_point:'
    TOKEN_TTL = 720
    TOKEN_LIMIT = 10000

class BoostersSettings(object):
    BONUS_NAME = 'boosterToken'
    TOKEN_PREFIX = 'ls_booster:'
    TOKEN_TTL = 720

class DifficultyMissionsSettings(object):
    DIFFICULTY_MISSISONS_QUEST_PREFFIX = 'ls_difficulty_missions:'
    DIFFICULTY_MISSISONS_QUEST_TPL = 'ls_difficulty_missions:{difficulty}:{index}'

class ArtefactType(object):
    TEXT = 'text'
    SOUND = 'sound'
    FINAL = 'final'
    KING_REWARD = 'kingReward'

class ArtefactTypeOpen(object):
    AUTOMATICALLY = 'automatically'
    MANUALLY = 'manually'

class MsgDataCacheKeys(object):
    ARTEFACTS = 'artefacts'
    DIFFICULTIES = 'difficulties'
    DIFFICULTY_MISSISONS = 'difficultyMissions'
    NARRATIVE_STORY_POINTS = 'narrativeStoryPoints'
    ALL: tuple

class DailyMissionsSettings(object):
    DAILY_MISSION_QUEST_PREFIX = 'ls_daily_mission:'
    DAILY_MISSION_TOKEN_PREFIX = 'ls_daily_token:'
    DAILY_MISSION_TOKEN_FORMAT: Any
    DAILY_MISSION_TOKEN_TTL = 24
    TOKEN_LIMIT = 1
    BADGE_MISSION_QUEST = 'ls_badge:mission'

class LSSoulsChangeReason(object):
    CHEAT = 0
    COLLECTOR = 1
    PICK_UP = 3
    VEHICLE_DEATH = 5
    COLLECTOR_RESET = 6
    EQUIPMENT_USED = 7
    PHASE_PROGRESS = 8
    PHASE_START = 9
    RESPAWN = 10
    CAPACITY = 11
    INITIAL_GRANT = 12

class LSBuffSequenceVisibilityMode(enum.IntEnum):
    NONE = 0
    SELF = 1
    OTHERS = 2
    ALL = 3

class BATTLE_EVENT_TYPE(BET, ConstInjector):
    LS_GAMEPLAY_ACTION = 102

class LSMarkersType(object):
    CAMP = 'LS_CAMP'
    MAGNUS = 'LS_MAGNUS'

class LSMarkerComponentNames(object):
    CAMP = 'lsCampMarker'
    MAGNUS = 'lsMagnusMarker'
    ALL: tuple

class DamageResistanceReason(constants.DamageResistanceReason, ConstInjector):
    LS_NITRO = 105
    LS_DAMAGE_SHIELD = 106
    LS_MODULES_INVULNERABILITY_BUFF = 107
    LS_INVISIBILITY_BUFF = 108

class LSRepairReason(object):
    NONE = 0
    BASIC_REPAIR = 1
    REPAIR_BY_AOE_ABILITY_VAMPIRE = 2
    REPAIR_BY_PASSIVE_VAMPIRE = 3
    REPAIR_BY_INFINITE_REGENERATION = 4
    REPAIR_BY_AOE_TEAM_REPAIR_KIT = 5
    REPAIR_BY_SELF_SITUATIONAL = 6
    REPAIR_BY_OBELISK = 7

class BOOSTER_FACTOR_NAMES(object):
    HEAL = 'heal'
    RESTORE_SOULS_ON_RESPAWN = 'restore_souls_on_respawn'
    ABILITY_RADIUS = 'ability_radius'
    SOULS_CAPACITY = 'souls_capacity'
    RECEIVE_SOULS_AFTER_WAVE = 'receive_souls_after_wave'
    PICK_UP_SOULS = 'pick_up_souls'
    PICK_UP_RADIUS = 'pick_up_radius'
    ABILITY_COST = 'ability_cost'
    ABILITY_DURATION = 'ability_duration'
    OBELISK_TRANSLATED_DAMAGE = 'obelisk_translated_damage'
    ALL: tuple
    RETENTION_FACTORS: tuple

class BOOSTER_FACTOR_OPERATIONS(object):
    ADD = 'add'
    ADD_PERCENT = 'add_percent'
    ALL: tuple

class LS_CHAT_CHANNELS(object):
    LS_CHAT_CHANNEL = '#last_stand.last_stand_chat:channels/last_stand'
    LS_CHAT_CHANNEL_EASY = '#last_stand.last_stand_chat:channels/last_stand_easy'
    LS_CHAT_CHANNEL_MEDIUM = '#last_stand.last_stand_chat:channels/last_stand_medium'
    LS_CHAT_CHANNEL_HARD = '#last_stand.last_stand_chat:channels/last_stand_hard'

class LS_BATTLE_CHAT_COMMANDS(object):
    LS_OBELISK = 'lsObelisk'
    LS_OBELISK_HELP = 'lsObeliskHelp'

def registerLoggingParams(personality):
    ...
