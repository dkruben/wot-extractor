# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/xmpp_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from constants import IS_CLIENT as IS_CLIENT, IS_CHINA as IS_CHINA
from debug_utils import LOG_WARNING as LOG_WARNING
_COOLDOWN_OFFSET: Any
_DEFAULT_COOLDOWN = 0.5
_CHINA_USER_MESSAGE_COOLDOWN = 3.0
CONTACT_ERROR_NAMES: dict
LIMIT_ERROR_NAMES: dict
CHANNEL_ERROR_NAMES: dict
ANY_ITEM_LITERAL = 'all'
MUC_CREATION_ERROR_NAMES: dict
XMPP_MUC_USER_TYPE_PRIORITY: dict
XMPP_MUC_USER_TEMPLATE_GROUPS: dict
XMPP_MUC_USER_GUI_TYPE_OVERRIDE_TRIGGER = 5

class MESSAGE_LIMIT(object):
    COOLDOWN: Any
    MESSAGE_MAX_SIZE = 512
    HISTORY_MAX_LEN = 100

class CONTACT_LIMIT(object):
    ROSTER_MAX_COUNT = 300
    BLOCK_MAX_COUNT = 1000
    GROUPS_MAX_COUNT = 100
    GROUP_MIN_LENGTH = 1
    GROUP_MAX_LENGTH = 15
    NOTE_MIN_CHARS_COUNT = 1
    NOTE_MAX_CHARS_COUNT = 140
    NOTES_PER_PAGE = 100

class CHANNEL_LIMIT(object):
    MAX_SEARCH_RESULTS = 50
    NAME_MIN_CHARS_COUNT = 3
    NAME_MAX_CHARS_COUNT = 100
    PWD_MIN_CHARS_COUNT = 3
    PWD_MAX_CHARS_COUNT = 32

class USER_SEARCH_LIMITS(object):
    FIND_USERS_BY_NAME_MAX_RESULT_SIZE = 50
    FIND_USERS_BY_NAME_REQUEST_COOLDOWN_SEC: Any

class CONTACT_ERROR_ID(object):
    CONTACT_ITEM_NOT_FOUND: Any
    ROSTER_ITEM_EXISTS: Any
    ROSTER_ITEM_NOT_FOUND: Any
    FRIENDSHIP_APPROVED: Any
    FRIENDSHIP_CANCELED: Any
    FRIENDSHIP_RQ_PROCESS: Any
    BLOCK_ITEM_EXISTS: Any
    BLOCK_ITEM_NOT_FOUND: Any
    MUTED_ITEM_NOT_FOUND: Any
    GROUP_EMPTY: Any
    GROUP_EXISTS: Any
    GROUP_NOT_FOUND: Any
    GROUP_INVALID_NAME: Any
    NOTE_EMPTY: Any
    NOTE_NOT_FOUND: Any

class LIMIT_ERROR_ID(object):
    MAX_ROSTER_ITEMS: Any
    MAX_GROUP: Any
    MAX_BLOCK_ITEMS: Any
    GROUP_INVALID_LENGTH: Any
    NOTE_INVALID_LENGTH: Any
    CHANNEL_INVALID_LENGTH: Any
    PWD_INVALID_LENGTH: Any

class CHANNEL_ERROR_ID(object):
    NAME_EMPTY: Any
    NAME_INVALID: Any
    PASSWORD_EMPTY: Any
    PASSWORD_INVALID: Any
    RETYPE_EMPTY: Any
    RETYPE_INVALID: Any
    PASSWORDS_NOT_EQUALS: Any
    NAME_ALREADY_EXISTS: Any

class XMPP_ITEM_TYPE(object):
    EMPTY_ITEM = 0
    ROSTER_ITEM = 1
    BLOCK_ITEM = 2
    SUB_PENDING = 3
    ROSTER_BLOCK_ITEM = 4
    BLOCK_ITEMS: tuple
    SUB_PENDING_ITEMS: tuple
    ROSTER_ITEMS: tuple
    ROSTER_BLOCK_ITEMS: tuple
    ROSTER_LIST: tuple
    PERSISTENT_BLOCKING_LIST: tuple

class XMPP_BAN_COMPONENT(object):
    BATTLE = 1
    PREBATTLE = 2
    PRIVATE = 4
    STANDARD = 8
    USER = 16
    CLAN = 32
    ALL: Any
    _STRING_TO_BITMASK: dict
    @classmethod
    def fromString(cls, value):
        ...

class MUC_STATUS(object):
    SELF_PRESENCE = 110
    CREATE_ROOM = 201
    INCLUDE_PRESENCE_STANZA: tuple

class SERVICE_DISCO_FEATURE(object):
    MUC_PASSWORD_PROTECTED = 'muc_passwordprotected'

class FORM_TYPE(object):
    UNDEFINED = ''
    FORM = 'form'
    SUBMIT = 'submit'
    CANCEL = 'cancel'
    RESULT = 'result'
    RANGE: tuple

class MUC_CREATION_ERROR(object):
    UNDEFINED = 0
    NAME_EXISTS = 201
    LIMIT_COUNT = 202
    LIMIT_PASS = 203
    LIMIT_NAME = 204
    WRONG_SYMBOL = 205
    WRONG_WORD = 206

class XMPP_MUC_CHANNEL_TYPE(object):
    UNKNOWN = 0
    STANDARD = 1
    USERS = 2
    CLANS = 3

class XMPP_MUC_USER_TYPE(object):
    NONE = 'none'
    OUTCAST = 'outcast'
    VISITOR = 'visitor'
    PARTICIPANT = 'participant'
    MEMBER = 'member'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    OWNER = 'owner'
