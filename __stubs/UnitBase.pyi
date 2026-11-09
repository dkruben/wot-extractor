# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/UnitBase.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import copy as copy
import struct as struct
import weakref as weakref
from collections import namedtuple as namedtuple
from future.moves import pickle as pickle
from future.utils import listvalues as listvalues, viewitems as viewitems, viewvalues as viewvalues
from past.builtins import xrange as xrange
from typing import TYPE_CHECKING as TYPE_CHECKING
from constants import VEHICLE_CLASS_INDICES as VEHICLE_CLASS_INDICES, PREBATTLE_TYPE as PREBATTLE_TYPE, QUEUE_TYPE as QUEUE_TYPE, INVITATION_TYPE as INVITATION_TYPE, BATTLE_MODE_VEHICLE_TAGS as BATTLE_MODE_VEHICLE_TAGS
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_DEBUG_DEV as LOG_DEBUG_DEV
from items import vehicles as vehicles
from items.badges_common import BadgesCommon as BadgesCommon
from UnitRoster import BaseUnitRosterSlot as BaseUnitRosterSlot, _BAD_CLASS_INDEX as _BAD_CLASS_INDEX, buildNamesDict as buildNamesDict, reprBitMaskFromDict as reprBitMaskFromDict
from ops_pack import OpsUnpacker as OpsUnpacker, packPascalString as packPascalString, unpackPascalString as unpackPascalString, initOpsFormatDef as initOpsFormatDef
from unit_helpers.ExtrasHandler import EmptyExtrasHandler as EmptyExtrasHandler, ClanBattleExtrasHandler as ClanBattleExtrasHandler
from unit_helpers.ExtrasHandler import SquadExtrasHandler as SquadExtrasHandler, ExternalExtrasHandler as ExternalExtrasHandler
from unit_roster_config import SquadRoster as SquadRoster, UnitRoster as UnitRoster, SpecRoster as SpecRoster, EventRoster as EventRoster, EpicRoster as EpicRoster, BattleRoyaleRoster as BattleRoyaleRoster, MapBoxRoster as MapBoxRoster
from typing import List as TList, Tuple as TTuple, Dict as TDict
UnitVehicle: Any
ProfileVehicle: Any
UNIT_STATE_NAMES: Any
UNIT_BROWSER_TYPE_NAMES: Any
OK = UNIT_ERROR.OK
UNIT_ERROR_NAMES: Any
INV_ID_CLEAR_VEHICLE = 0
LEADER_SLOT = 0
UNIT_CONFIRMATION_WAIT_TIME = 5.0
MAX_UNIT_ROSTER_ELEMENTS = 14
UNDEFINED_ESTIMATED_TIME = -1
INFINITY_ESTIMATED_TIME = 0
UNIT_ROLE_NAMES: Any
VEHICLE_CLASS_SPG: Any
CMD_NAMES: dict
FORCED_CLIENT_UNIT_CMDS: tuple
UNIT_ASSEMBLER_IMPL_NAMES: dict
UNIT_ASSEMBLER_IMPL_IDS: dict
UNIT_ASSEMBLER_IMPL_TO_CONFIG: dict
PREBATTLE_TYPE_TO_UNIT_ASSEMBLER: dict
VEHICLE_TAGS_GROUP_BY_UNIT_MGR_FLAGS: dict
UNIT_MGR_FLAGS_TO_PREBATTLE_TYPE: dict
UNIT_MGR_FLAGS_TO_UNIT_MGR_ENTITY_NAME: dict
UNIT_MGR_FLAGS_TO_INVITATION_TYPE: dict
PREBATTLE_TYPE_BY_UNIT_MGR_ROSTER: dict
PREBATTLE_TYPE_BY_UNIT_MGR_ROSTER_EXT: dict
QUEUE_TYPE_BY_UNIT_MGR_ROSTER: dict
ROSTER_TYPE_TO_CLASS: dict
EXTRAS_HANDLER_TYPE_TO_HANDLER: dict

class UNIT_MGR_STATE:
    IDLE = 0
    IN_QUEUE = 1
    IN_PRE_ARENA = 2
    IN_AUTO_SEARCH = 3
    REQUEUE_ASSEMBLER = 4
    FINISH_ASSEMBLING_ACCOUNTS = 5

class UNIT_FLAGS:
    LOCKED = 1
    INVITE_ONLY = 2
    IN_QUEUE = 4
    IN_SEARCH = 8
    DEV_MODE = 16
    IN_ARENA = 32
    SORTIES_FORBIDDEN = 64
    RATED_BATTLE_FORBIDDEN = 128
    IN_PRE_ARENA = 256
    IS_EXTERNAL_LOCK = 512
    IS_DYNAMIC = 1024
    ARENA_FINISHED = 2048
    KEEP_OFFLINE_ROSTER = 4096
    EXTERNAL_LEGIONARIES_MATCHING = 8192
    FINISH_ASSEMBLING = 16384
    DEFAULT = 0
    PRE_QUEUE = 0
    PRE_SEARCH = 0
    IN_ROSTER_WAIT = 0
    MODAL_STATES: Any
    CHANGED_STATE_ASQ: Any

class UNIT_BROWSER_TYPE:
    NOT_RATED_UNITS = 1
    ALL = NOT_RATED_UNITS

class UNIT_CREATE_TYPE:
    DEFAULT = 0
    FALLOUT = 1
    SQUAD = 2
    EVENT = 3
    EXPOSED_TYPES: tuple

class UNIT_ERROR:
    OK = 0
    ALREADY_JOINED_UNIT = 1
    UNIT_MGR_ENTITY_CREATION_FAIL = 2
    UNIT_ADD_FAIL = 3
    CANT_FIND_UNIT_MGR = 4
    ADD_PLAYER_FAIL = 5
    NO_UNIT_MGR = 6
    WRONG_UNIT_REQUISITES = 7
    REMOVE_PLAYER_FAIL = 8
    GET_VEHICLE_FAIL = 9
    ADD_MEMBER_FAIL = 10
    SET_MEMBER_READY_FAIL = 11
    ASSIGN_MEMBER_FAIL = 12
    FAIL_UNIT_METHOD = 13
    BAD_SLOT_IDX = 14
    INSUFFICIENT_ROLE = 15
    NO_UNIT = 16
    BAD_ROSTER_PACK = 17
    TOO_MANY_ROSTERS = 18
    JOIN_CTX_LOCK = 19
    CANT_INVITE = 20
    TIMEOUT = 21
    NOT_READY = 22
    NOT_IN_QUEUE = 23
    NOT_IDLE = 24
    NOT_IN_SEARCH = 25
    BAD_JOINING_ACC = 26
    PLAYER_IGNORED = 27
    NOT_INVITED = 28
    REMOVED_PLAYER = 29
    OFFLINE_PLAYER = 30
    KICKED_PLAYER = 31
    UNIT_RESTORED = 32
    ACCOUNT_RESTORED = 33
    GET_READY_VEHICLE_FAIL = 34
    COOLDOWN = 35
    ALREADY_INVITED = 37
    HAS_IN_ARENA_MEMBERS = 38
    KICKED_CANDIDATE = 39
    INVITE_REMOVED = 40
    BAD_ACCOUNT_TYPE = 41
    BAD_POINTS_SUM = 42
    WAITING_FOR_JOIN = 43
    BAD_VEHICLE_LEVEL = 44
    CLAN_CHANGED = 45
    NO_CLAN_MEMBERS = 46
    BAD_CLAN = 47
    NO_PLAYER = 48
    SLOT_RESERVED = 49
    SLOT_OCCUPIED = 50
    TOO_MANY_CLOSED_SLOTS = 51
    SLOT_NOT_CLOSED = 52
    CANT_PICK_LEADER = 53
    RESTRICT_LEGIONARIES = 54
    RESTRICT_INVITED = 55
    VEHICLE_MISMATCH = 56
    NO_VEHICLES = 57
    TOO_MANY_LEGIONARIES = 58
    VEHICLE_NOT_CHOSEN = 59
    ALREADY_IN_SLOT = 60
    FORT_BATTLE_END = 61
    NO_AVAILABLE_SLOTS = 62
    TOO_FEW_POINTS = 63
    BAD_DIVISION = 64
    CANT_CHANGE_DIVISION = 65
    CANNOT_LEAD = 66
    WRONG_UNITMGR = 68
    LEGIONARIES_FORBIDDEN = 69
    PREV_RATED_BATTLE_IN_PROGRESS = 70
    OFF_SEASON = 71
    BAD_PARAMS = 72
    PLAYER_READY = 73
    SORTIES_FORBIDDEN = 74
    NO_UNIT_ASSEMBLER = 75
    SPEC_BATTLE_END = 77
    BAD_VEHICLE_TYPE = 78
    TOO_FEW_VEHICLE_TYPE = 79
    TOO_MANY_VEHICLE_TYPE = 80
    TOO_FEW_VEHICLES = 81
    TOO_MANY_VEHICLES = 82
    BAD_FALLOUT_TYPE = 83
    BAD_VEHICLES_SET = 84
    WRONG_UNIT_API = 85
    NO_ACCOUNT = 86
    ASYNC_CALL_FAILED = 87
    BAD_WGSH_CMD = 88
    FAIL_EXT_BATTLE_MGR_CALL = 89
    FAIL_EXT_ACCOUNT_CALL = 90
    FAIL_EXT_UNIT_MGR_CALL = 91
    FAIL_EXT_UNIT_QUEUE_CALL = 92
    UNIT_DESTROYED = 93
    UNIT_NOT_IN_QUEUE = 94
    UNIT_LOCKED_IN_QUEUE = 95
    UNIT_KICKED_FROM_QUEUE = 96
    UNIT_BACK_TO_QUEUE = 97
    EXTERNAL_UNIT_NOT_ENABLED = 98
    BAD_ARENA_BONUS_TYPE = 99
    UNIT_CHANGED_LEADER = 100
    FAIL_EXT_UNIT_QUEUE_START = 101
    WRONG_VEHICLE = 102
    KICKED_PLAYER_TO_JOIN_ASSEMBLED_UNIT = 103
    UNIT_ASSEMBLER_NO_MATCH_POSSIBLE = 104
    UNIT_ASSEMBLER_UNIT_NOT_SUPPORTED = 105
    UNIT_ASSEMBLER_NO_DATE_RECEIVED = 106
    UNIT_ASSEMBLER_DISABLED = 107
    UNIT_ASSEMBLER_TIMEOUT = 108
    KICKED_SEARCH_ONLY_PLAYER = 109
    INVALID_ACCOUNT = 110
    ACCOUNT_BANNED = 111
    MODE_OFFLINE = 112
    NO_ARENA_VEHICLES = 113
    EXPIRED_PLAY_LIMITS = 114
    EXPIRED_PLAY_LIMITS_TO_COMMANDER = 115
    COMP7_QUALIFICATION = 116

class UNIT_SLOT:
    ANY = -1
    REMOVE = -2

class UNIT_OP:
    SET_VEHICLE = 1
    SET_MEMBER = 2
    DEL_MEMBER = 3
    ADD_PLAYER = 4
    REMOVE_PLAYER = 5
    READY_MASK = 6
    SET_SLOT = 7
    CLEAR_VEHICLE = 8
    VEHICLE_DICT = 9
    UNIT_FLAGS = 10
    CLOSE_SLOT = 11
    OPEN_SLOT = 12
    SET_COMMENT = 13
    CHANGE_ROLE = 14
    MODAL_TIMESTAMP = 15
    GIVE_LEADERSHIP = 16
    EXTRAS_UPDATE = 18
    EXTRAS_RESET = 19
    GAMEPLAYS_MASK = 20
    SET_VEHICLE_LIST = 21
    ARENA_TYPE = 23
    SET_PLAYER_PROFILE = 24
    DEL_PLAYER_PROFILE = 25
    ESTIMATED_TIME_IN_QUEUE = 26
    CLEAR_SEARCH_FLAGS = 28
    REMOVE_SEARCH_FLAGS = 29
    SET_SEARCH_FLAGS = 30
    SQUAD_SIZE = 31

class UNIT_ROLE:
    DEFAULT = 0
    INVITED = 1
    COMMANDER_UPDATES = 2
    CHANGE_ROSTER = 4
    LEGIONARY = 16
    MANAGER = 32
    IN_ARENA = 64
    OFFLINE = 128
    CAN_LEAD = 256
    AUTO_SEARCH = 512
    CAN_USE_EXTRA_EQUIPMENTS = 1024
    CAN_USE_BOOST_EQUIPMENTS = 2048
    START_STOP_BATTLE = CHANGE_ROSTER
    ADD_REMOVE_MEMBERS = CHANGE_ROSTER
    INVITE_KICK_PLAYERS = CHANGE_ROSTER
    CREATOR: Any
    CHANGE_LEADERSHIP: Any
    SOCIAL_ROLES: Any
    SELF_ONLY = 65536
    SELF_UNLOCKED = 131072
    NON_IDLE = 262144
    NO_LEGIONARY_CANDIDATES = 524288
    PRE_ARENA = 1048576
    IN_AUTO_SEARCH = 2097152

class UNIT_BROWSER_CMD:
    REFRESH = 0
    LEFT = 1
    RIGHT = 2

class UNIT_BROWSER_ERROR:
    OK = 0
    UNSUBSCRIBED = 1
    PAGING_ERROR = 2
    ACCEPT_TIMEOUT = 3
    BAD_ACCEPT_CONTEXT = 4
    SEARCH_CANCELED = 5
    ACCEPT_CANCELED = 6
    ALREADY_SUBSCRIBED = 7
    NOT_SUBSCRIBED = 8
    SERVICE_UNAVAILABLE = 9
    BAD_ACCOUNT_TYPE = 10
    COOLDOWN = 11

class UNIT_PUBLISHER_ERROR:
    OK = 0
    ALREADY_PUBLISHED = 1
    NOT_PUBLISHED = 2

class UNIT_NOTIFY_CMD:
    SET_VEHICLE_LIST = 1
    PLAYER_ONLINE = 2
    TRANSFER_LEADERSHIP = 3
    PUBLISH_STATE_CHANGE = 4
    SET_MEMBER_READY = 5
    KICK_ALL = 6
    EXTRAS_UPDATED = 7
    AUTO_ASSEMBLED_MEMBER_ADDED = 11
    APPROVED_VEHICLE_LIST = 12
    REMOVED_VEHICLE = 13
    UPD_VEHICLE_DESCRS = 14
    REMOVED_VEHICLE_MAX_SPG_EXCEED = 15
    REMOVED_VEHICLE_FROM_FILTER = 16
    INCORRECT_EVENT_ENQUEUE_DATA = 17
    REMOVED_VEHICLE_MAX_SCOUT_EXCEED = 18
    CHANGE_SQUAD_SIZE = 19
    PLAYER_LIMITS_EXPIRED = 20
    REMOVED_VEHICLE_FROM_SQUAD = 21

class CLIENT_UNIT_CMD:
    NONE = 0
    LEAVE_UNIT = 1
    START_UNIT_BATTLE = 2
    STOP_UNIT_BATTLE = 3
    START_AUTO_SEARCH = 4
    STOP_AUTO_SEARCH = 5
    SET_UNIT_MEMBER = 6
    SET_UNIT_VEHICLE = 7
    FIT_UNIT_MEMBER = 8
    ASSIGN_UNIT_MEMBER = 9
    REASSIGN_UNIT_MEMBER = 10
    SET_UNIT_MEMBER_READY = 11
    KICK_UNIT_PLAYER = 12
    LOCK_UNIT = 13
    OPEN_UNIT = 14
    CLOSE_UNIT_SLOT = 15
    SET_ROSTER_SLOT = 16
    SET_UNIT_COMMENT = 17
    SET_UNIT_DEV_MODE = 18
    GIVE_LEADERSHIP = 19
    SET_GAMEPLAYS_MASK = 22
    SET_VEHICLE_LIST = 23
    SET_UNIT_VEHICLE_TYPE = 25
    SET_ARENA_TYPE = 26

class UNIT_NOTIFY_ID:
    PARENT_UNIT_MGR = -1

class UNIT_MGR_FLAGS:
    DEFAULT = 0
    SQUAD = 64
    SPEC_BATTLE = 128
    FALLOUT_CLASSIC = 256
    FALLOUT_MULTITEAM = 512
    EVENT = 1024
    STRONGHOLD = 2048
    EPIC = 4096
    TOURNAMENT = 8192
    BATTLE_ROYALE = 16384
    MAPBOX = 32768
    RTS = 65536

class UnitAssemblerSearchFlags(object):
    NO_FILTER = 0
    USE_VOICE = 1
    VEH_TIER_1 = 2
    VEH_TIER_2 = 4
    VEH_TIER_3 = 8
    VEH_TIER_4 = 16
    VEH_TIER_5 = 32
    VEH_TIER_6 = 64
    VEH_TIER_7 = 128
    VEH_TIER_8 = 256
    VEH_TIER_9 = 512
    VEH_TIER_10 = 1024
    VEH_TIER_11 = 2048
    DESTROY_UNIT_ON_ABORT = 4096
    ALL_VEH_TIERS: Any

class UnitAssemblerImplType(object):
    SQUAD = 1
    EPIC = 2

class BitfieldHelper:
    _value: Any
    def __init__(self, value):
        ...
    @property
    def value(self):
        ...
    @staticmethod
    def bitToFlag(bit):
        ...
    def setFlag(self, flag):
        ...
    def setBit(self, bit):
        ...
    def unsetFlag(self, flag):
        ...
    def unsetBit(self, bit):
        ...
    def isSetFlag(self, flag):
        ...
    def isSetBit(self, bit):
        ...
    def toggleFlag(self, flag):
        ...
    def toggleBit(self, bit):
        ...
    def compare(self, value):
        ...

class ROSTER_TYPE:
    UNIT_ROSTER = 0
    FALLOUT_CLASSIC_ROSTER: Any
    FALLOUT_MULTITEAM_ROSTER: Any
    SQUAD_ROSTER = UNIT_MGR_FLAGS.SQUAD
    SPEC_ROSTER = UNIT_MGR_FLAGS.SPEC_BATTLE
    EVENT_ROSTER: Any
    STRONGHOLD_ROSTER = UNIT_MGR_FLAGS.STRONGHOLD
    TOURNAMENT_ROSTER = UNIT_MGR_FLAGS.TOURNAMENT
    EPIC_ROSTER: Any
    BATTLE_ROYALE_ROSTER: Any
    MAPBOX_ROSTER: Any
    _MASK: Any

class EXTRAS_HANDLER_TYPE:
    EMPTY = 0
    SQUAD = 4
    SPEC_BATTLE = 5
    EXTERNAL = 6

class UnitPlayerDataKey(object):
    ACCOUNT_ID = 'accountID'
    ACCOUNT = 'account'
    NICKNAME = 'nickName'
    BADGES = 'badges'
    ROLE = 'role'
    OFFLINE = 'offline'
    IGRTYPE = 'igrType'
    PERIPHERY_ID = 'peripheryID'
    TIME_JOIN = 'timeJoin'
    RATING = 'rating'
    BATTLES_COUNT = 'battlesCount'
    MATCHMAKER_STATS = 'matchmakerStats'
    MAP_BLACKLIST = 'mapBlackList'
    ACCOUNT_WTR = 'accountWTR'
    ACCOUNT_NEW_WTR = 'accountNewWTR'
    HAS_WINBACK_TOKEN = 'hasWinbackToken'
    CLAN_DBID = 'clanDBID'
    CLAN_ABBREV = 'clanAbbrev'
    CLAN_NAME = 'clanName'
    CLAN_ROLE = 'clanRole'
    IS_PREMIUM = 'isPremium'
    VEH_DICT = 'vehDict'
    VEH_BATTLES_COUNT = 'vehBattlesCount'
    EXTRA_DATA = 'extraData'

class UnitBase(OpsUnpacker):
    _opsFormatDefs: Any
    MAX_PLAYERS = 250
    _HEADER = '<HHHHHHHHBiiiii'
    _PLAYER_DATA = '<qiIHBHHHq?'
    _PLAYER_VEHICLES_LIST = '<qH'
    _PLAYER_VEHICLE_TUPLE = '<iI'
    _SLOT_PLAYERS = '<Bq'
    _IDS = '<IBB'
    _VEHICLE_DICT_HEADER = '<Hq'
    _VEHICLE_DICT_ITEM = '<Ii'
    _VEHICLE_PROFILE_HEADER = '<qBBII'
    _PLAYER_SEARCH_FLAGS_TUPLE = '<qH'
    _HEADER_SIZE: Any
    _SLOT_PLAYERS_SIZE: Any
    _PLAYER_DATA_SIZE: Any
    _PLAYER_VEHICLES_LIST_SIZE: Any
    _PLAYER_VEHICLE_TUPLE_SIZE: Any
    _IDS_SIZE: Any
    _VEHICLE_DICT_HEADER_SIZE: Any
    _VEHICLE_DICT_ITEM_SIZE: Any
    _VEHICLE_PROFILE_HEADER_SIZE: Any
    _PLAYER_SEARCH_FLAGS_TUPLE_SIZE: Any
    _members: Any
    _vehicles: Any
    _players: Any
    _playerSlots: Any
    _playerProfileVehicles: Any
    _readyMask: Any
    _gameplaysMask: Any
    _arenaType: Any
    _fullReadyMask: Any
    _strComment: Any
    _packedOps: Any
    _packedCmdrOps: Any
    _closedSlotMask: Any
    _notifications: Any
    _reservedSlots: Any
    _modalTimestamp: Any
    _estimatedTimeInQueue: Any
    _squadSize: Any
    _unitAssemblerSearchFlags: Any
    __extrasHandler: Any
    _dirty: Any
    _packed: Any
    _rosterTypeID: Any
    _extrasHandlerID: Any
    _prebattleTypeID: Any
    _roster: Any
    _freeSlots: Any
    _flags: Any
    _extras: Any
    def __init__(self, limitsDefs=None, slotDefs=None, slotCount=0, packedRoster='', extrasInit=None, packedUnit='', rosterTypeID=..., extrasHandlerID=..., prebattleTypeID=...):
        ...
    def _initClean(self):
        ...
    def _initExtrasHandler(self):
        ...
    @property
    def _extrasHandler(self):
        ...
    def _setVehicle(self, accountDBID, vehTypeCompDescr, vehInvID):
        ...
    def _setVehicleList(self, accountDBID, vehShortList):
        ...
    def _clearVehicle(self, accountDBID):
        ...
    def _setMember(self, accountDBID, slotChosenIdx):
        ...
    def __updateReadyMask(self, accountDBID, newSlotIdx):
        ...
    def _delMemberBySlot(self, slotIdx):
        ...
    def _autoSelectProfileVehicle(self, accountDBID, unitVehicles):
        ...
    def _setProfileVehicle(self, accountDBID, vehCompDescr, vehOutfitCD, seasonType, marksOnGun, prestigeLevel, stFrags):
        ...
    def _delProfileVehicle(self, accountDBID):
        ...
    def _setProfileVehicleByData(self, packedOps):
        ...
    def _setEstimatedTimeInQueue(self, estimatedTimeInQueue):
        ...
    def _addPlayer(self, accountDBID, **kwargs):
        ...
    def _removePlayer(self, accountDBID):
        ...
    def _changePlayerRole(self, accountDBID, roleFlags):
        ...
    def _setRosterSlot(self, rosterSlotIdx, packedSlot):
        ...
    def isEmpty(self):
        ...
    def pack(self):
        ...
    def unpack(self, packed):
        ...
    def isDirty(self):
        ...
    def getCommanderDBID(self):
        ...
    def getAccountsStates(self):
        ...
    def updateUnitExtras(self, updateStr):
        ...
    def getPacked(self):
        ...
    def isReady(self):
        ...
    def anyReady(self):
        ...
    def isLocked(self):
        ...
    def isInviteOnly(self):
        ...
    def isIdle(self):
        ...
    def isDevMode(self):
        ...
    def isInQueue(self):
        ...
    def isInSearch(self):
        ...
    def isFinishAssembling(self):
        ...
    def isInArena(self):
        ...
    def isSortiesForbidden(self):
        ...
    def isDynamic(self):
        ...
    def isSquad(self):
        ...
    def shouldPublish(self):
        ...
    def __repr__(self):
        ...
    def dump(self):
        ...
    def setMemberReady(self, accountDBID, isReady=True):
        ...
    def setAutoSearchFlags(self, accountDBID, flags):
        ...
    def removeAutoSearchFlags(self, flags):
        ...
    def clearAutoSearchFlags(self):
        ...
    def getAutoSearchFlags(self):
        ...
    def hasAutoSearchFlags(self, flags):
        ...
    def getAutoSearchFlagsOfAccount(self, accountDBID):
        ...
    def _canUseVehicles(self, vehiclesList, isSet=False, isCommanderSet=False, accountDBID=0):
        ...
    def _setGameplaysMask(self, newGameplaysMask):
        ...
    def _setSquadSize(self, newSquadSize):
        ...
    def _setArenaType(self, newArenaType):
        ...
    def isMemberReady(self, accountDBID):
        ...
    def _setModalTimestamp(self, timestamp):
        ...
    def _setReadyMask(self, mask):
        ...
    def _setUnitFlags(self, flags):
        ...
    def _closeSlot(self, slotIdx):
        ...
    def getMaxSlotCount(self):
        ...
    def getClosedSlotsCount(self):
        ...
    def getPointsSum(self):
        ...
    def checkVehicleLevelsRange(self, lvlsByClass, commonLvls):
        ...
    def checkVehicleTypesRange(self, vehicleTypes):
        ...
    def hasInArenaMembers(self):
        ...
    def getLegionaryCount(self):
        ...
    def getLegionaryMaxCount(self):
        ...
    def resetExtras(self):
        ...
    def _openSlot(self, slotIdx):
        ...
    def _reserveUnitSlot(self, unitSlotIdx):
        ...
    def setComment(self, strComment):
        ...
    def _appendCmdrOp(self, op, packedArgs):
        ...
    def _storeNotification(self, accountDBID, notifyCmd, argList=None):
        ...
    def _unpackRosterSlot(self, packedOps):
        ...
    def _packVehicleDict(self, accountDBID, vehDict=None):
        ...
    def _packFullVehDictUpdates(self):
        ...
    def _unpackVehicleDict(self, packedOps):
        ...
    def _unpackPlayer(self, packedOps):
        ...
    def _giveLeadership(self, newLeaderDBID):
        ...
    def _refreshFreeSlots(self, prevMax, newMax):
        ...
    def _getLeaderDBID(self):
        ...
    def isMultiVehicle(self):
        ...
    def getRosterType(self):
        ...
    def getSquadSize(self):
        ...
    def _isValidMember(self, accountDBID):
        ...
    def _checkAllVehiclesMatchSlot(self, accountDBID, unitSlotIdx):
        ...
    def _makePlayerExtraDataForClient(self, extraData):
        ...
    def __packPlayerData(self, accountDBID, **kwargs):
        ...
    def __unpackPlayerData(self, packedData):
        ...
    @staticmethod
    def __packPlayerExtraData(packedData):
        ...
    @staticmethod
    def __unpackPlayerExtraData(packedData, initialOffset):
        ...
    def __packProfileVehicle(self, accountDBID, profileVehicle):
        ...
    def __unpackProfileVehicle(self, packedData):
        ...

def _prebattleTypeFromFlags(flags):
    ...
def _entityNameFromFlags(flags):
    ...
def _invitationTypeFromFlags(flags):
    ...
def _unitAssemblerTypeFromFlags(flags):
    ...
def extendTiersFilter(filterFlags):
    ...
