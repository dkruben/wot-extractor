# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/common/halloween_common/halloween_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import enum as enum
import constants as constants
import UnitBase as UnitBase
import arena_bonus_type_caps as arena_bonus_type_caps
from constants_utils import ConstInjector as ConstInjector, AbstractBattleMode as AbstractBattleMode
from halloween_common.battle_results import halloween_results as halloween_results
from BattleFeedbackCommon import BATTLE_EVENT_TYPE as BET
UNIT_HALLOWEEN_EXTRA_DATA_KEY = 'halloweenData'
UNIT_DIFFICULTY_LEVELS_KEY = 'difficultyLevels'
UNIT_BLOCKED_RENT_VEHICLES_KEY = 'blockedRentVehicles'
DAMAGE_INFO_CODES_PER_ATTACK_REASON: dict
HALLOWEEN_GAME_PARAMS_KEY = 'halloween_config'
HALLOWEEN_BESTIARY_PARAMS_KEY = 'halloween_bestiary_config'
HALLOWEEN_GSW_PARAMS_KEY = 'halloween_gsw_config'
HALLOWEEN_LOOT_PARAMS_KEY = 'halloween_loot_config'
HALLOWEEN_ANOMALIES_PARAMS_KEY = 'halloween_anomalies_config'
NITRO_BUILTIN_EXTRA_PATTERN = 'nitroRamDamage'
BOSS_ROLE_TAG = 'hwrole_boss'
ENEMY_ROLE_TAG_PREFIX = 'hwrole_'
PLAYERS_TEAM = 1
INVALID_BATTLE_PLACE = -1
INVALID_PHASE = 0
HALLOWEEN_BOMBER_ACTIVATE_REASON: tuple
TOKEN_DIFFICULTY_LEVEL_TO_QUEUE_TYPE: dict
QUEUE_TYPE_TO_TOKEN_DIFFICULTY_LEVEL: dict
ARENA_BONUS_TYPE_TO_LEVEL: dict
MIN_REWARD_PHASE = 2
ALL_LOOT_ANOMALY_TYPES: tuple
TOKEN_LIFETIME_HOURS = 2160
HALLOWEEN_CHAT_CHANNEL = '#halloween.halloween_chat:channels/halloween'
HW_EMPTY_SLOTS_EQ: tuple
HW_BUILT_IN_EQUIPMENT: tuple
CURRENT_QUEUE_TYPE_KEY = 'currentQueueType'
HALLOWEEN_QUESTS_PREFFIX = 'hw_'
RENT_VEHICLE_PREFIX = 'hw_rent_vehicle'
KEY_DAILY_QUEST_TPL = 'hw_key_daily_quest:{intCD}'
ARTEFACT_ID_MASK = 'hw_artefact:{index}:'
ANOMALIES_SYSTEM_UNLOCKED = 'hw_unlock_recipes'
HW_UPGRADE_OPTIONS_REASON_UNLOCKED = -1
HALLOWEEN_SCOPE_ID = 'halloween'

class ARENA_GUI_TYPE(constants.ARENA_GUI_TYPE, ConstInjector):
    HALLOWEEN = 101

class ARENA_BONUS_TYPE(constants.ARENA_BONUS_TYPE, ConstInjector):
    HALLOWEEN = 101
    HALLOWEEN_MEDIUM = 102
    HALLOWEEN_HARD = 103

class QUEUE_TYPE(constants.QUEUE_TYPE, ConstInjector):
    HALLOWEEN = 101
    HALLOWEEN_MEDIUM = 102
    HALLOWEEN_HARD = 103

class PREBATTLE_TYPE(constants.PREBATTLE_TYPE, ConstInjector):
    HALLOWEEN = 101

class UNIT_MGR_FLAGS(UnitBase.UNIT_MGR_FLAGS, ConstInjector):
    HALLOWEEN = 2097152

class ROSTER_TYPE(UnitBase.ROSTER_TYPE, ConstInjector):
    HALLOWEEN: Any

class INVITATION_TYPE(constants.INVITATION_TYPE, ConstInjector):
    HALLOWEEN = PREBATTLE_TYPE.HALLOWEEN

class CLIENT_UNIT_CMD(UnitBase.CLIENT_UNIT_CMD, ConstInjector):
    SET_UNIT_DIFFICULTY_LEVEL = 2001

class ATTACK_REASON(constants.ATTACK_REASON, ConstInjector):
    _const_type: Any
    HALLOWEEN_BOMBER_EXPLOSION = 'halloween_bomber_explosion'
    HALLOWEEN_ABILITY_VAMPIRE = 'halloween_ability_vampire'
    HALLOWEEN_ABILITY_AOE_DAMAGE = 'halloween_ability_aoe_damage'
    HALLOWEEN_ABILITY_IGNITE = 'halloween_ability_ignite'
    HALLOWEEN_PHASE_TIMER = 'halloween_phase_timer'
    HALLOWEEN_LEAVER = 'halloween_leaver'
    HALLOWEEN_PASSIVE_IGNITE = 'halloween_passive_ignite'
    HALLOWEEN_PASSIVE_VAMPIRE = 'halloween_passive_vampire'
    HALLOWEEN_BOSS_AURA = 'halloween_boss_aura'
    HALLOWEEN_DEATH_PIT = 'halloween_death_pit'
    HALLOWEEN_SHOT_AOE_DAMAGE = 'halloween_shot_aoe_damage'
    HALLOWEEN_SHOT_AOE_DRAIN_ENEMY_HP = 'halloween_shot_aoe_drain_enemy_hp'
    HALLOWEEN_SHOT_AOE_STUN = 'halloween_shot_aoe_stun'
    HALLOWEEN_DEATH_ZONE_IGNITE = 'halloween_death_zone_ignite'
    HALLOWEEN_DEATH_ZONE_STUN = 'halloween_death_zone_stun'
    HALLOWEEN_DEATH_ZONE_INTERVAL = 'halloween_death_zone_interval'
    HALLOWEEN_INSTANT_KILL = 'halloween_instance_kill'
    HALLOWEEN_CORROSION = 'halloween_corrosion'
    HALLOWEEN_STOMPING = 'halloween_stomping'
    HALLOWEEN_DEATH_ZONE = 'halloween_deathzone'

class ARENA_BONUS_TYPE_CAPS(arena_bonus_type_caps.ARENA_BONUS_TYPE_CAPS, ConstInjector):
    _const_type: Any
    HALLOWEEN = 'HALLOWEEN'

class HalloweenBattleMode(AbstractBattleMode):
    _PREBATTLE_TYPE = PREBATTLE_TYPE.HALLOWEEN
    _QUEUE_TYPE = QUEUE_TYPE.HALLOWEEN
    _ARENA_BONUS_TYPE = ARENA_BONUS_TYPE.HALLOWEEN
    _ARENA_GUI_TYPE = ARENA_GUI_TYPE.HALLOWEEN
    _INVITATION_TYPE = INVITATION_TYPE.HALLOWEEN
    _BATTLE_MGR_NAME = 'HalloweenBattlesMgr'
    _UNIT_MGR_NAME = 'HalloweenUnitMgr'
    _UNIT_MGR_FLAGS = UNIT_MGR_FLAGS.HALLOWEEN
    _ROSTER_TYPE = ROSTER_TYPE.HALLOWEEN
    _GAME_PARAMS_KEY = HALLOWEEN_GAME_PARAMS_KEY
    _BATTLE_RESULTS_CONFIG = halloween_results
    _REQUIRED_VEHICLE_TAGS: tuple
    _FORBIDDEN_VEHICLE_TAGS: Any
    _SM_TYPE_ARTEFACT_REWARD_CONGRATS = 'hwArtefactRewardCongrats'
    _SM_TYPE_DIFFICULTY_REWARD_CONGRATS = 'hwDifficultyRewardCongrats'
    _SM_TYPE_DIFFICULTY_OPEN_MESSAGE = 'hwDifficultyOpenMessage'
    _SM_TYPE_VEHICLE_RENT_MESSAGE = 'hwVehicleRentMessage'
    _SM_TYPE_ARTEFACT_KEYS_MESSAGE = 'hwArtefactKeysMessage'
    _SM_TYPE_PURCHASE_BUNDLE_FOR_GOLD_MESSAGE = 'hwPurchaseBundleForGold'
    _SM_TYPE_BATTLE_RESULT = 'hwBattleResults'
    _SM_TYPE_BATTLE_PASS_POINTS_MESSAGE = 'hwBattlePassPointsMessage'
    _SM_TYPE_AUTO_MAINTENANCE = 'hwAutoMaintenance'
    _SM_TYPE_INVOICE_RECEIVED = 'hwInvoiceReceived'
    _SM_TYPE_INVOICE_RECEIVED_LOW_PRIORITY = 'hwInvoiceReceivedLowPriority'
    _FAIRPLAY_VEHICLE_BATTLE_STATS_COMPONENT = 'HWFairplayVehicleBattleStatsComponent'
    _SM_TYPES: list
    _CLIENT_SM_TYPES: list
    @property
    def _rosterClass(self):
        ...
    @property
    def _client_attackReasonToCode(self):
        ...

class DifficultyLevelToken(object):
    EASY = 'hw_difficulty_level:easy'
    MEDIUM = 'hw_difficulty_level:medium'
    HARD = 'hw_difficulty_level:hard'
    ALWAYS_AVIABLED: tuple
    ACCESS_REQUIRED: tuple
    ALL_LEVELS: tuple

class ShopSettings(object):
    SHOP_BUNDLE_PREFFIX = 'hw26bundle'
    PURCHASED_SUFFIX = ':purchased'
    WG_MONEY_CALLBACK = 'purchaseEventShopBundleWGMoney'

class ArtefactsSettings(object):
    ARTEFACT = 'hw_artefact'
    QUEST_PREFIX = 'hw_artefact:'
    TOKEN_PREFIX = 'hw_artefact:'
    KEY_TOKEN = 'hw_artefact:key'
    KEY_NOTIFY_TOKEN = 'hw_artefact:notifyKey'
    MEMORY = 'img:hw_artefact:memory'
    CREW_100 = 'hw_bonus_crew:100'
    KEY_TOKEN_TTL = 2160
    KEY_TOKEN_LIMIT = 10000

class ArtefactType(object):
    TEXT = 'text'
    SOUND = 'sound'
    FINAL = 'final'

class HWModifierColors(enum.IntEnum):
    blue = 0
    green = 1
    red = 2
    violet = 3
    orange = 4

class HalloweenSoulsChangeReason(object):
    CHEAT = 0
    COLLECTOR = 1
    BOSS_AURA = 2
    PICK_UP = 3
    VEHICLE_DEATH = 5
    COLLECTOR_RESET = 6
    EQUIPMENT_USED = 7
    PHASE_PROGRESS = 8
    PHASE_START = 9
    PHASE_MIRIUMIZATION = 10

class HWBuffSequenceVisibilityMode(enum.IntEnum):
    NONE = 0
    SELF = 1
    OTHERS = 2
    ALL = 3

class AnomalySettings(object):
    TOKEN_PREFIX = 'hw_anomaly:'

class LootAnomalyType(object):
    INDIVIDUAL = 'individual'
    SECRET = 'secret'

class AnomalyType(LootAnomalyType):
    EPIC = 'epic'
    REGULAR = 'regular'

class BATTLE_EVENT_TYPE(BET, ConstInjector):
    HW_GAMEPLAY_ACTION = 101

class HalloweenMarkersType(object):
    SOULS_COLLECTOR = 'SOULS_COLLECTOR'
    CAMP = 'HW_CAMP_1'

class HalloweenMarkerComponentNames(object):
    CAMP = 'hwCampMarker'
    SOULS_COLLECTOR = 'hwSoulsCollectorMarker'

class DamageResistanceReason(constants.DamageResistanceReason, ConstInjector):
    DAMAGE_SHIELD = 102
    MODULES_INVULNERABILITY_BUFF = 103
    BOSS_DAMAGE_SHIELD = 104
    BOMBER_EXPLOSION_RESIST = 109

class HWRepairReason(object):
    NONE = 0
    BASIC_REPAIR = 1
    REPAIR_BY_AOE_ABILITY_VAMPIRE = 2
    REPAIR_BY_PASSIVE_VAMPIRE = 3
    REPAIR_BY_INFINITE_REGENERATION = 4
    REPAIR_BY_AOE_TEAM_REPAIR_KIT = 5

class HWDeathZoneShapes(enum.IntEnum):
    RECT = 1
    CIRCLE = 2

class HWStoryChoiceSettings(object):
    STORY_CHOICE_TOKEN_LIFETIME_HOURS = 9360
    FAKE_MEDAL = 'hw_fake_choice_medal:hw2026Medal'
    MEDAL_BONUS_NAME: Any
    _medalSuffix: Any
    MEDAL_FORMAT: Any
    OPTION_1 = 'hw26_ending:1'
    OPTION_2 = 'hw26_ending:2'
    OPTION_SKIP = 'option_skip'
    ALL_OPTIONS: tuple

class HWVehicleModifiers(object):
    EQUIPMENT_COOLDOWN = 'equipment/cooldown'
    EQUIPMENT_DURATION = 'equipment/duration'
    EQUIPMENT_USAGE_COST = 'equipment/usageCost'
    SHELLS_DEATH_KEEPER = 'shells/deathKeeper'
    SOULS_EXTRA_DROP_FROM_BOTS = 'souls/extraDropFromBots'
    SOULS_CAPACITY = 'souls/capacity'
    SOULS_REFUND_AMOUNT = 'souls/refundAmount'
    SOULS_REFUND_CHANCE = 'souls/refundChance'
    SOULS_DEATH_KEEPER = 'souls/deathKeeper'
    SOULS_DEATH_DROP_RATE = 'souls/deathDropRate'

class HWSoundEventType(enum.IntEnum):
    OVERRIDING = 0
    INITIAL = 1
    FINAL = 2

def registerLoggingParams(personality):
    ...
