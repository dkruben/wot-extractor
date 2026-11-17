# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/m_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from collections import namedtuple as namedtuple
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
MESSENGER_XML_FILE = 'messenger'
MESSENGER_I18N_FILE = 'messenger'
MESSENGER_XML_FILE_PATH: Any
MESSAGE_FLOOD_COOLDOWN = 20
BREAKERS_MAX_LENGTH = 1
MESSAGES_HISTORY_MAX_LEN = 50
BATTLE_SHARED_HISTORY_MAX_LEN = 250
SCH_MSGS_MAX_LENGTH = 250
GUI_FORCED_CLOSE_ON_LOGIN: tuple
PROTO_TYPE_NAMES: dict
USER_DEFAULT_NAME_PREFIX = '#settings:defaultNamePrefix'
USER_ACTION_ID_NAMES: dict
CLIENT_ERROR_NAMES: dict
CLIENT_ACTION_NAMES: dict

class MESSENGER_SCOPE(object):
    UNKNOWN = 0
    LOGIN = 1
    LOBBY = 2
    BATTLE = 3

class PROTO_TYPE(object):
    BW = 1
    XMPP = 2
    BW_CHAT2 = 3
    MIGRATION = 4

class UserEntityScope(CONST_CONTAINER):
    LOBBY = 1
    BATTLE = 2

class MESSENGER_COMMAND_TYPE(object):
    UNDEFINED = 0
    BATTLE = 1
    ADMIN = 2

class LAZY_CHANNEL(object):
    COMMON = '#chat:channels/common'
    SPECIAL_BATTLES = '#chat:channels/special_battles'
    XMPP_COMMON = '#chat:channels/xmpp_common'
    ALL: tuple

class BATTLE_CHANNEL(object):
    _ITEM: Any
    TEAM: Any
    COMMON: Any
    SQUAD: Any
    REQUIRED: tuple
    ALL: tuple
    NAMES: Any
    @classmethod
    def isInitialized(cls, mask):
        ...

class USER_TAG(object):
    CACHED = 'cached'
    WO_NOTIFICATION = 'woNotification'
    FRIEND = 'friend'
    IGNORED = 'ignored'
    IGNORED_TMP = 'tmp_ignored'
    MUTED = 'muted'
    CURRENT = 'himself'
    CLAN_MEMBER = 'ownClanMember'
    OTHER_CLAN_MEMBER = 'otherClanMember'
    IGR_BASE = 'igr/base'
    IGR_PREMIUM = 'igr/premium'
    INVALID_NAME = 'invalid/name'
    INVALID_RATING = 'invalid/rating'
    SEARCH = 'search'
    TEMP = 'temp'
    SUB_NONE = 'sub/none'
    SUB_PENDING_IN = 'sub/pendingIn'
    SUB_PENDING_OUT = 'sub/pendingOut'
    SUB_APPROVED = 'sub/approved'
    SUB_CANCELED = 'sub/canceled'
    SUB_IN_PROCESS = 'sub/inProcess'
    SUB_TO = 'sub/to'
    SUB_FROM = 'sub/from'
    PRESENCE_DND = 'presence/dnd'
    BAN_CHAT = 'ban/chat'
    _SHARED_TAGS: set
    _CLOSED_CONTACTS: set
    _ALL_CONTACTS: set
    @classmethod
    def filterAllContactsTags(cls, tags):
        ...
    @classmethod
    def filterClosedContactsTags(cls, tags):
        ...
    @classmethod
    def filterSharedTags(cls, tags):
        ...
    @classmethod
    def filterToRemoveTags(cls, tags):
        ...

class USER_ACTION_ID(object):
    UNDEFINED: Any
    FRIEND_ADDED: Any
    FRIEND_REMOVED: Any
    IGNORED_ADDED: Any
    IGNORED_REMOVED: Any
    TMP_IGNORED_ADDED: Any
    TMP_IGNORED_REMOVED: Any
    MUTE_SET: Any
    MUTE_UNSET: Any
    GROUPS_CHANGED: Any
    SUBSCRIPTION_CHANGED: Any
    NOTE_CHANGED: Any

class USER_GUI_TYPE(object):
    CURRENT_PLAYER = 'himself'
    FRIEND = 'friend'
    IGNORED = 'ignored'
    OTHER = 'other'
    BREAKER = 'breaker'
    RANGE: tuple

class CLIENT_ERROR_ID(object):
    GENERIC: Any
    LOCKED: Any
    WRONG_ARGS: Any
    NOT_CONNECTED: Any
    NOT_SUPPORTED: Any
    DBID_INVALID: Any
    NAME_EMPTY: Any
    NAME_INVALID: Any
    COOLDOWN: Any
    WAITING_BEFORE_START: Any

class CLIENT_ACTION_ID(object):
    ADD_FRIEND: Any
    REMOVE_FRIEND: Any
    ADD_IGNORED: Any
    REMOVE_IGNORED: Any
    SET_MUTE: Any
    UNSET_MUTE: Any
    ADD_GROUP: Any
    CHANGE_GROUP: Any
    RQ_FRIENDSHIP: Any
    APPROVE_FRIENDSHIP: Any
    CANCEL_FRIENDSHIP: Any
    SET_NOTE: Any
    REMOVE_NOTE: Any
    SEND_MESSAGE: Any
    RQ_HISTORY: Any
    CREATE_USER_ROOM: Any
    JOIN_USER_ROOM: Any
    LEAVE_USER_ROOM: Any
    SEARCH_USER_ROOM: Any
    FIND_USERS_BY_PREFIX: Any
    JOIN_CLAN_ROOM: Any

class GAME_ONLINE_STATUS(object):
    UNDEFINED = 0
    IN_CLAN_CHAT = 1
    IN_SEARCH = 2
    ONLINE = IN_CLAN_CHAT
    @classmethod
    def addBit(cls, status, bit):
        ...
    @classmethod
    def removeBit(cls, status, bit):
        ...
    @classmethod
    def update(cls, status, bit):
        ...

class PRIMARY_CHANNEL_ORDER(object):
    LAZY = 1
    CLAN = 2
    SYSTEM = 3
    OTHER = 4

class SCH_CLIENT_MSG_TYPE(object):
    SYS_MSG_TYPE = 0
    PREMIUM_ACCOUNT_EXPIRY_MSG = 1
    AOGAS_NOTIFY_TYPE = 2
    ACTION_NOTIFY_TYPE = 3
    KOREA_PARENTAL_CONTROL_TYPE = 5
    TECH_TREE_ACTION_DISCOUNT = 6
    BLUEPRINTS_CONVERT_SALE = 7
    MAPBOX_PROGRESSION_REWARD = 8
    MAPBOX_SURVEY_AVAILABLE = 9
    MAPBOX_EVENT_ENDED = 10
    MAPBOX_EVENT_STARTED = 11
    BATTLE_MATTERS_TOKEN_AWARD = 14
    BATTLE_MATTERS_BATTLE_AWARD = 15
    WOTPLUS_SWITCH = 16
    INTEGRATED_AUCTION_LOST_RATE = 17
    WOTPLUS_FEATURE_DISABLED = 18
    WINBACK_SELECTABLE_REWARD = 19
    WINBACK_BATTLERESULTS_REWARD = 20
    ACHIEVEMENTS20_SM_TYPE = 21
    WOTPLUS_SUBSCRIPTION_UNLOCKED = 23
    PERSONAL_RESERVES_FIRST_LOGIN = 35
    PERSONAL_RESERVES_SOON_EXPIRATION = 36
    ACHIEVEMENTS20_EARNING_SM_TYPE = 37
    GF_SM_TYPE = 39
    COLLECTOR20_REWARD_RECEIVED = 40
    PET_SYSTEM_EVENT_CREDITS_AWARD = 41
    PET_SYSYEM_EVENT_ITEMS_AWARD = 42
