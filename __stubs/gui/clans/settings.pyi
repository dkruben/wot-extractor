# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/clans/settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import re as re
from collections import namedtuple as namedtuple
from constants import CLAN_MEMBER_FLAGS as CLAN_MEMBER_FLAGS
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
DEFAULT_COOLDOWN = 1.0
REQUEST_TIMEOUT = 60.0
SEND_INVITES_COOLDOWN = 5.0
ACCEPT_INVITES_COOLDOWN = 2.0
DECLINE_INVITES_COOLDOWN = 2.0
MAX_ACCOUNT_APPLICATIONS_COUNT = 100
MAX_CLAN_INVITES_COUNT = 100
MAX_CLAN_MEMBERS_COUNT = 100
COUNT_THRESHOLD = 2000
PERSONAL_INVITES_COUNT_THRESHOLD = 500
DATA_UNAVAILABLE_PLACEHOLDER = '--'
ACTIVE_INVITE_LIFE_TIME = 259200
INVITE_LIMITS_LIFE_TIME = 300
CLAN_DOSSIER_LIFE_TIME = 3600
DEFAULT_EMBLEM_PATH = 'gui/maps/icons/clans'
DEFAULT_EMBLEM_NAME_PREFIX = 'default_clan_icon'
NO_EMBLEM_NAME_PREFIX = 'no_clan_icon'
CLAN_MEMBERS: dict
_RE_SEARCH_CLANS: Any
CLAN_INVITE_STATES_SORT_RULES: dict
_RestrResult: Any
AccessTokenData: Any

class LOGIN_STATE(CONST_CONTAINER):
    LOGGED_OFF = 0
    LOGGING_IN = 1
    LOGGED_ON = 2
    @classmethod
    def canDoLogin(cls, state):
        ...

class CLAN_INVITE_STATES(CONST_CONTAINER):
    ACTIVE = 'active'
    DECLINED = 'declined'
    DECLINED_RESENT = 'declined_resent'
    ACCEPTED = 'accepted'
    EXPIRED = 'expired'
    ERROR = 'error'
    DELETED = 'deleted'
    EXPIRED_RESENT = 'expired_resent'
    PROCESSED: tuple
    ALL: tuple
    @classmethod
    def isActive(cls, status):
        ...

class CLAN_APPLICATION_STATES(CONST_CONTAINER):
    ACTIVE = 'active'
    DECLINED = 'declined'
    ACCEPTED = 'accepted'
    ALL: tuple

class CLIENT_CLAN_RESTRICTIONS(CONST_CONTAINER):
    NO_RESTRICTIONS = 'NO_RESTRICTIONS'
    DEFAULT = 'HAVE_NO_RIGHTS'
    OWN_CLAN = 'OWN_CLAN'
    RESYNCHRONIZE = 'RESYNCHRONIZE'
    ALREADY_IN_CLAN = 'ALREADY_IN_CLAN'
    FORBIDDEN_ACCOUNT_TYPE = 'FORBIDDEN_ACCOUNT_TYPE'
    CLAN_APPLICATION_ALREADY_SENT = 'CLAN_APPLICATION_ALREADY_SENT'
    CLAN_INVITE_ALREADY_RECEIVED = 'CLAN_INVITE_ALREADY_RECEIVED'
    SENT_INVITES_LIMIT_REACHED = 'SENT_INVITES_LIMIT_REACHED'
    CLAN_SEND_INVITES_LIMIT_REACHED = 'CLAN_SEND_INVITES_LIMIT_REACHED'
    CLAN_CONSCRIPTION_CLOSED = 'CLAN_CONSCRIPTION_CLOSED'
    CANT_SEE_TREASURY = 'HAVE_NO_RIGHTS_TO_SEE_TREASURY'
    CANT_HANDLE_INVITES = 'CANT_HANDLE_INVITES'
    CANT_SEND_INVITES = 'HAVE_NO_RIGHTS_TO_SEND_INVITES'
    SEARCH_PATTERN_INVALID = 'SEARCH_PATTERN_INVALID'
    CLAN_IS_FULL = 'CLAN_IS_FULL'
    CLAN_ENTER_COOLDOWN = 'CLAN_ENTER_COOLDOWN'

def isValidPattern(pattern):
    ...
def error(reason):
    ...
def success():
    ...
def getDefaultEmblem16x16():
    ...
def getDefaultEmblem32x32():
    ...
def getDefaultEmblem64x64():
    ...
def getDefaultEmblem128x128():
    ...
def getDefaultEmblem256x256():
    ...
def getNoClanEmblem32x32():
    ...
def getClanRoleName(role):
    ...
def _getDefaultEmblemPath(size):
    ...
def _getNoClanEmblemPath(size):
    ...
