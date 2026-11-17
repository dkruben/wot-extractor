# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from UnitBase import UNIT_ERROR as UNIT_ERROR, UNIT_BROWSER_ERROR as UNIT_BROWSER_ERROR, LEADER_SLOT as LEADER_SLOT
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE, PREBATTLE_INVITE_STATE as PREBATTLE_INVITE_STATE, QUEUE_TYPE as QUEUE_TYPE, MIN_VEHICLE_LEVEL as MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL
from prebattle_shared import SETTING_DEFAULTS as SETTING_DEFAULTS, PrebattleSettings as PrebattleSettings
from shared_utils import CONST_CONTAINER as CONST_CONTAINER, BitmaskHelper as BitmaskHelper
from gui.shared.system_factory import registerIgnoredModeForAutoSelectVehicle as registerIgnoredModeForAutoSelectVehicle
VEHICLE_DEF_LEVEL_RANGE: tuple
VEHICLE_LEVELS: Any
TEAM_MAX_LIMIT = 150
INVITE_COMMENT_MAX_LENGTH = 400
UNIT_COMMENT_MAX_LENGTH = 240
CREATOR_SLOT_INDEX = LEADER_SLOT
CREATOR_ROSTER_SLOT_INDEXES: tuple
UNIT_CLOSED_SLOTS_MASK: Any
UNIT_CLOSED_SLOT_COST = 1
AUTO_SEARCH_UNITS_ARG_TIME = 5
UNIT_MIN_RECOMMENDED_LEVEL = 40
CTRL_ENTITY_TYPE_NAMES: Any
_FUNCTIONAL_FLAG_NAMES: Any
IGNORED_UNIT_MGR_ERRORS: tuple
ENTER_UNIT_MGR_RESTORE_ERRORS: tuple
ENTER_UNIT_MGR_RESET_ERRORS: list
IGNORED_UNIT_BROWSER_ERRORS: tuple
UNIT_ERRORS_TRANSLATE_AS_WARNINGS: tuple
UNIT_NOTIFICATION_TO_DISPLAY: tuple
UNIT_ERROR_NAMES: Any
UNIT_BROWSER_ERROR_NAMES: Any
QUEUE_TYPE_TO_PREBATTLE_TYPE: dict
PREBATTLE_TYPE_TO_QUEUE_TYPE: dict
REQUEST_TYPE_NAMES: Any
_PREBATTLE_DEFAULT_SETTINGS = SETTING_DEFAULTS

class CTRL_ENTITY_TYPE(object):
    UNKNOWN = 0
    LEGACY = 1
    UNIT = 2
    PREQUEUE = 3

class FUNCTIONAL_FLAG(BitmaskHelper):
    UNDEFINED = 0
    SWITCH = 1
    EXIT = 2
    LOAD_PAGE = 4
    LOAD_WINDOW = 8
    LEGACY_INTRO = 16
    LEGACY_INIT = 32
    LEGACY = 64
    UNIT_INTRO = 128
    UNIT_BROWSER = 256
    UNIT = 512
    PRE_QUEUE_INTRO = 1024
    PRE_QUEUE = 2048
    E_SPORT = 4096
    TRAINING = 8192
    BATTLE_SESSION = 16384
    RANDOM = 32768
    EVENT = 65536
    STRONGHOLD = 524288
    RANKED = 1048576
    EPIC_TRAINING = 4194304
    TOURNAMENT = 8388608
    EPIC = 16777216
    BATTLE_ROYALE = 33554432
    MAPBOX = 67108864
    MAPS_TRAINING = 134217728
    DEFAULT = 68719476736
    LEGACY_BITMASK: Any
    UNIT_BITMASK: Any
    PRE_QUEUE_BITMASK: Any
    MODES_BITMASK: Any
    SET_GLOBAL_LISTENERS: Any
    RANGE: tuple

class UNIT_NOTIFICATION_KEY(object):
    PLAYER_OFFLINE = 'playerOffline'
    PLAYER_ONLINE = 'playerOnline'
    PLAYER_ADDED = 'playerAdded'
    PLAYER_ADDED_WITH_FILTER = 'playerAddedWithFilter'
    PLAYER_REMOVED = 'playerRemoved'
    GIVE_LEADERSHIP = 'giveLeadership'

class PREBATTLE_ACTION_NAME(object):
    UNDEFINED = ''
    RANDOM = 'random'
    TRAININGS_LIST = 'trainingsList'
    SPEC_BATTLES_LIST = 'specBattlesList'
    SQUAD = 'squad'
    EVENT_SQUAD = 'eventSquad'
    BATTLE_ROYALE_SQUAD = 'battleRoyaleSquad'
    MAPBOX_SQUAD = 'mapboxSquad'
    TOURNAMENT = 'tournament'
    CLAN = 'clan'
    E_SPORT = 'eSport'
    PUBLICS_LIST = 'publicsList'
    STRONGHOLD = 'stronghold'
    STRONGHOLDS_BATTLES_LIST = 'strongholdsBattlesList'
    RANKED = 'ranked'
    EPIC_TRAINING_LIST = 'epicTrainingsList'
    EPIC = 'epicQueue'
    BATTLE_ROYALE = 'battleRoyaleQueue'
    BATTLE_ROYALE_TOURNAMENT = 'battleRoyaleTournamentQueue'
    MAPS_TRAINING = 'mapsTraining'
    EVENT_BATTLE = 'event'
    MAPBOX = 'mapbox'
    WINBACK = 'winback'

class PREBATTLE_INIT_STEP(object):
    SETTING_RECEIVED = 1
    ROSTERS_RECEIVED = 2
    INITED: Any

class SELECTOR_BATTLE_TYPES(object):
    UNIT = 'unit'
    HISTORICAL = 'historical'
    SORTIE = 'sortie'
    RANKED = 'ranked'
    EPIC = 'epic'
    BATTLE_ROYALE = 'battleRoyale'
    MAPBOX = 'mapbox'
    MAPS_TRAINING = 'mapsTraining'
    EVENT = 'event'
    WINBACK = 'winback'

class REQUEST_TYPE(object):
    CREATE = 1
    ASSIGN = 2
    JOIN = 3
    LEAVE = 4
    SET_TEAM_STATE = 5
    SET_PLAYER_STATE = 6
    SWAP_TEAMS = 7
    CHANGE_SETTINGS = 8
    CHANGE_OPENED = 9
    CHANGE_COMMENT = 10
    CHANGE_DIVISION = 11
    CHANGE_ARENA_VOIP = 12
    KICK = 13
    SEND_INVITE = 14
    PREBATTLES_LIST = 15
    LOCK = 16
    CLOSE_SLOT = 17
    SET_VEHICLE = 18
    SET_ROSTERS_SLOTS = 19
    SET_SLOT_VEHICLE_TYPE_FILTER = 20
    SET_SLOT_VEHICLES_FILTER = 21
    STOP_PLAYERS_MATCHING = 22
    AUTO_SEARCH = 23
    ACCEPT_SEARCH = 24
    DECLINE_SEARCH = 25
    BATTLE_QUEUE = 26
    CHANGE_UNIT_STATE = 27
    UNITS_LIST = 28
    UNITS_RECENTER = 29
    UNITS_REFRESH = 30
    UNITS_NAV_LEFT = 31
    UNITS_NAV_RIGHT = 32
    CHANGE_USER_STATUS = 33
    GIVE_LEADERSHIP = 34
    GET_ROSTER = 35
    SET_VEHICLE_LIST = 36
    QUEUE = 37
    DEQUEUE = 38
    SET_RESERVE = 39
    UPDATE_STRONGHOLD = 40
    UNASSIGN = 41
    UNSET_RESERVE = 42
    SET_EQUIPMENT_COMMANDER = 43
    MATCHMAKING_INFO = 44
    EPIC_SWAP_IN_TEAM = 45
    EPIC_SWAP_BETWEEN_TEAM = 46
    CHANGE_ARENA_GUI = 48

class PREQUEUE_SETTING_NAME(CONST_CONTAINER):
    BATTLE_ID = 'battleID'
    SELECTED_VEHICLE_ID = 'selectedVehicleID'
    PRICE_INDEX = 'priceIndex'

class PREBATTLE_SETTING_NAME(object):
    CREATOR = 'creator'
    IS_OPENED = 'isOpened'
    COMMENT = 'comment'
    ARENA_TYPE_ID = 'arenaTypeID'
    ROUND_LENGTH = 'roundLength'
    ARENA_VOIP_CHANNELS = 'arenaVoipChannels'
    CURRENT_USER_STATUS = 'currentUserStatus'
    DEFAULT_ROSTER = 'defaultRoster'
    VEHICLE_LOCK_MODE = 'vehicleLockMode'
    DIVISION = 'division'
    START_TIME = 'startTime'
    BATTLES_LIMIT = 'battlesLimit'
    WINS_LIMIT = 'winsLimit'
    EXTRA_DATA = 'extraData'
    LIMITS = 'limits'
    DESTROY_IF_CREATOR_OUT = 'destroyIfCreatorOut'
    BATTLE_TYPE = 'type'
    WINNER_IF_DRAW = 'winnerIfDraw'
    SWITCH_TEAMS = 'switchBattleTeams'
    ARENA_GUI_TYPE = 'arenaGuiType'

class PREBATTLE_PROPERTY_NAME(object):
    TEAMS_POSITIONS = 'teamsPositions'

class PREBATTLE_RESTRICTION(object):
    UNDEFINED = ''
    LIMIT_MIN_COUNT = 'limit/minCount'
    LIMIT_MAX_COUNT = 'limit/maxCount'
    LIMIT_LEVEL = 'limits/level'
    LIMIT_TOTAL_LEVEL = 'limit/totalLevel'
    LIMIT_CLASSES = 'limits/classes'
    LIMIT_CLASS_LEVEL = 'limits/classLevel'
    LIMIT_VEHICLES = 'limits/vehicles'
    LIMIT_NATIONS = 'limits/nations'
    LIMIT_COMPONENTS = 'limits/components'
    LIMIT_AMMO = 'limits/ammo'
    LIMIT_NOT_ENOUGH_SUITABLE_VEHICLES = 'limits/notEnoughSuitableVehicles'
    LIMIT_SHELLS = 'limits/shells'
    LIMIT_TAGS = 'limits/tags'
    LIMIT_MAX_OBSERVERS = 'limits/maxObservers'
    LIMIT_LIGHT_TANK = 'limits/classes/lightTank'
    LIMIT_MEDIUM_TANK = 'limits/classes/mediumTank'
    LIMIT_HEAVY_TANK = 'limits/classes/heavyTank'
    LIMIT_SPG = 'limits/classes/SPG'
    LIMIT_AT_SPG = 'limits/classes/AT-SPG'
    HAS_PLAYER_IN_BATTLE = 'player/inBattle'
    TEAM_IS_IN_QUEUE = 'team/inQueue'
    PREVIEW_VEHICLE_IS_PRESENT = 'previewVehicle/isPresent'
    VEHICLE_NOT_READY = 'vehicle/notReady'
    VEHICLE_NOT_PRESENT = 'vehicle/notPresent'
    VEHICLE_IN_BATTLE = 'vehicle/inBattle'
    VEHICLE_BROKEN = 'vehicle/broken'
    VEHICLE_GROUP_IS_NOT_READY = 'vehicle/group_is_not_ready'
    VEHICLE_GROUP_MIN = 'vehicle/group_min'
    VEHICLE_GROUP_REQUIRED = 'vehicle/group_required'
    VEHICLE_ROAMING = 'vehicle/roaming'
    VEHICLE_RENTALS_IS_OVER = 'vehicle/rentalsIsOver'
    VEHICLE_IGR_RENTALS_IS_OVER = 'vehicle/igrRentalsIsOver'
    VEHICLE_TELECOM_RENTALS_IS_OVER = 'vehicle/telecomRentalsIsOver'
    VEHICLE_IN_PREMIUM_IGR_ONLY = 'vehicle/inPremiumIgrOnly'
    VEHICLE_NOT_SUPPORTED = 'vehicle/not_supported'
    VEHICLE_EPIC_ONLY = 'vehicle/epic_only'
    VEHICLE_ROTATION_GROUP_LOCKED = 'vehicle/rotationGroupLocked'
    UNSUITABLE_VEHICLE_FOR_BATTLE_ROYALE = 'vehicle/notForBattleRoyaleMode'
    VEHICLE_WILL_BE_UNLOCKED = 'vehicle/willBeUnlocked'
    VEHICLE_WOT_PLUS_EXCLUSIVE_UNAVAILABLE = 'vehicle/wotPlusExclusiveUnavailable'
    CREW_NOT_FULL = 'crew/notFull'
    UNIT_NOT_FULL = 'squad/notFull'
    TUTORIAL_NOT_FINISHED = 'tutorial/notFinished'
    SERVER_LIMITS: tuple
    VEHICLE_CLASS_LIMITS: tuple
    VEHICLE_INVALID_STATES: tuple
    @classmethod
    def getVehClassRestrictions(cls):
        ...
    @classmethod
    def getVehClassTags(cls):
        ...
    @classmethod
    def inVehClassLimit(cls, search):
        ...

class UNIT_RESTRICTION(object):
    UNDEFINED = 0
    NOT_READY_IN_SLOTS = 1
    MIN_SLOTS = 2
    ZERO_TOTAL_LEVEL = 3
    MIN_TOTAL_LEVEL = 4
    MAX_TOTAL_LEVEL = 5
    INVALID_TOTAL_LEVEL = 6
    NEED_PLAYERS_SEARCH = 7
    IS_IN_IDLE = 8
    IS_IN_ARENA = 9
    UNIT_IS_FULL = 10
    UNIT_IS_LOCKED = 11
    VEHICLE_NOT_SELECTED = 12
    VEHICLE_NOT_VALID = 13
    IS_IN_PRE_ARENA = 15
    NOT_IN_SLOT = 16
    VEHICLE_BROKEN = 17
    VEHICLE_CREW_NOT_FULL = 18
    VEHICLE_RENT_IS_OVER = 19
    VEHICLE_IS_IN_BATTLE = 20
    VEHICLE_NOT_VALID_FOR_EVENT = 21
    CURFEW = 22
    VEHICLE_WRONG_MODE = 23
    FORT_DISABLED = 29
    VEHICLE_INVALID_LEVEL = 30
    XP_PENALTY_VEHICLE_LEVELS = 31
    ROTATION_GROUP_LOCKED = 32
    COMMANDER_VEHICLE_NOT_SELECTED = 33
    UNIT_MAINTENANCE = 33
    UNIT_INACTIVE_PERIPHERY_UNDEF = 34
    UNIT_INACTIVE_PERIPHERY_SORTIE = 35
    UNIT_INACTIVE_PERIPHERY_BATTLE = 36
    VEHICLES_GROUP_IS_FULL = 37
    UNIT_WAITINGFORDATA = 38
    UNIT_MIN_CLAN_MEMBERS = 40
    UNIT_WILL_SEARCH_PLAYERS = 41
    UNIT_IS_IN_PLAYERS_MATCHING = 42
    UNIT_NOT_FULL = 43
    UNSUITABLE_VEHICLE = 44
    UNIT_WRONG_DATA = 46
    LIMIT_LEVEL = 50
    LIMIT_VEHICLE_TYPE = 51
    LIMIT_VEHICLE_CLASS = 52
    MODE_NO_BATTLES = 53
    MODE_NOT_SET = 54
    MODE_NOT_AVAILABLE = 55
    BAN_IS_SET = 56
    RANK_RESTRICTION = 57
    MODE_OFFLINE = 58
    PLAY_LIMITS_IS_ACTIVE = 59
    HAS_FROZEN_VEHICLES = 60
    LIMIT_NOT_ENOUGH_SUITABLE_VEHICLES = 69
    VEHICLE_LIMITS: tuple

class PRE_QUEUE_RESTRICTION(object):
    UNDEFINED = 'undefined'
    LIMIT_LEVEL = 'limits/level'
    LIMIT_VEHICLE_TYPE = 'limits/vehicleType'
    LIMIT_VEHICLE_CLASS = 'limits/vehicleClass'
    LIMIT_NO_SUITABLE_VEHICLES = 'limits/noSuitableVehicles'
    LIMIT_NOT_ENOUGH_SUITABLE_VEHICLES = 'limits/notEnoughSuitableVehicles'
    MODE_NO_BATTLES = 'mode/noBattles'
    MODE_NOT_SET = 'mode/notSet'
    MODE_NOT_AVAILABLE = 'mode/notAvailable'
    MODE_OFFLINE = 'mode/offline'
    MODE_IS_IN_PREANNOUNCE = 'mode/preannounce'
    MODE_SEASON_ENDED = 'mode/seasonEnded'
    VEHICLE_WILL_BE_UNLOCKED = 'vehicle/willBeUnlocked'
    BAN_IS_SET = 'ban/isSet'
    QUALIFICATION_RESULTS_PROCESSING = 'qualification/resultsProcessing'
    VEHICLE_LIMITS: tuple

class PRE_QUEUE_JOIN_ERRORS(object):
    DISABLED = 0
    NOT_AVAILABLE = 1

class PREBATTLE_ROSTER(object):
    UNKNOWN = -1
    ASSIGNED = 0
    UNASSIGNED = 16
    ASSIGNED_IN_TEAM1: Any
    UNASSIGNED_IN_TEAM1: Any
    ASSIGNED_IN_TEAM2: Any
    UNASSIGNED_IN_TEAM2: Any
    ALL: tuple
    PREBATTLE_RANGES: dict
    @classmethod
    def getRange(cls, pbType, team=None):
        ...

class FUNCTIONAL_ORDER(object):
    ENTRY: tuple
    ACTION: tuple
    EXIT_FROM_QUEUE: tuple
    BEFORE_GENERAL_CHECKING: tuple
    AFTER_GENERAL_CHECKING: tuple

class PRB_INVITE_STATE(CONST_CONTAINER):
    ERROR = -1
    PENDING = 0
    ACCEPTED = 1
    DECLINED = 2
    REVOKED = 3
    EXPIRED = 4
    POSTPONED = 5
    OLD_MAPPING: dict
    @classmethod
    def getFromOldState(cls, invite):
        ...
    @classmethod
    def getFromNewState(cls, invite):
        ...

class PREBATTLE_PLAYERS_SORT_TYPES(object):
    REGULAR = 1
    OBSERVERS_TO_BOTTOM = 2
    BY_VEHICLE = 3
    BY_STATE = 4
    BY_PLAYER_NAME = 5

def convertFlagsToNames(flags):
    ...
def makePrebattleSettings(settings=None):
    ...
