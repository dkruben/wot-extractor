# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/external_strings_utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import re as re
import unicodedata as unicodedata
from builtins import chr as chr
from future.utils import lrange as lrange
from past.builtins import unicode as unicode, xrange as xrange
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from constants import CREDENTIALS_RESTRICTION as CREDENTIALS_RESTRICTION, CREDENTIALS_RESTRICTION_SET as CREDENTIALS_RESTRICTION_SET
from soft_exception import SoftException as SoftException
from struct_helpers import unpackByte as unpackByte
_MAX_NORMALIZED_NAME_BYTES = 96
textRestrictions: Any
_ACCOUNT_NAME_RE = textRestrictions.ACCOUNT_NAME_RE
_ACCOUNT_NAME_MIN_LENGTH = textRestrictions.ACCOUNT_NAME_MIN_LENGTH
_ACCOUNT_NAME_MAX_LENGTH = textRestrictions.ACCOUNT_NAME_MAX_LENGTH
_ACCOUNT_NAME_MIN_LENGTH_REG = textRestrictions.ACCOUNT_NAME_MIN_LENGTH_REG
_LOGIN_NAME_RE = textRestrictions.LOGIN_NAME_RE
_LOGIN_NAME_MIN_LENGTH = textRestrictions.LOGIN_NAME_MIN_LENGTH
_LOGIN_NAME_MAX_LENGTH = textRestrictions.LOGIN_NAME_MAX_LENGTH
_CLAN_ABBREV_RE = textRestrictions.CLAN_ABBREV_RE
_CLAN_NAME_MAX_LENGTH = textRestrictions.CLAN_NAME_MAX_LENGTH
_CLAN_ABBREV_MAX_LENGTH = textRestrictions.CLAN_ABBREV_MAX_LENGTH
_UPPERCASE_CLAN_ABBREV = textRestrictions.UPPERCASE_CLAN_ABBREV
_REQUIRE_NORMALIZED_CLAN_ABBREV = textRestrictions.REQUIRE_NORMALIZED_CLAN_ABBREV
CLAN_DESCR_MAX_LENGTH = textRestrictions.CLAN_DESCR_MAX_LENGTH
CLAN_MOTTO_MAX_LENGTH = textRestrictions.CLAN_MOTTO_MAX_LENGTH
CLAN_DESCR_MAX_BYTES: Any
CLAN_MOTTO_MAX_BYTES: Any

class TextRestrictionsBasic(object):
    __slots__: tuple
    ACCOUNT_NAME_RE: Any
    ACCOUNT_NAME_MIN_LENGTH: Any
    ACCOUNT_NAME_MAX_LENGTH: Any
    ACCOUNT_NAME_MIN_LENGTH_REG: Any
    LOGIN_NAME_RE: Any
    LOGIN_NAME_MIN_LENGTH: Any
    LOGIN_NAME_MAX_LENGTH: Any
    UPPERCASE_CLAN_ABBREV: Any
    REQUIRE_NORMALIZED_CLAN_ABBREV: Any
    CLAN_ABBREV_RE: Any
    CLAN_NAME_MAX_LENGTH: Any
    CLAN_ABBREV_MAX_LENGTH: Any
    CLAN_DESCR_MAX_LENGTH: Any
    CLAN_MOTTO_MAX_LENGTH: Any
    def __init__(self):
        ...

class TextRestrictionsChinese(TextRestrictionsBasic):
    __slots__ = TextRestrictionsBasic.__slots__
    ACCOUNT_NAME_RE: Any
    ACCOUNT_NAME_MIN_LENGTH_REG: Any
    LOGIN_NAME_RE: Any
    LOGIN_NAME_MIN_LENGTH: Any
    LOGIN_NAME_MAX_LENGTH: Any
    CLAN_ABBREV_RE: Any
    UPPERCASE_CLAN_ABBREV: Any
    REQUIRE_NORMALIZED_CLAN_ABBREV: Any
    def __init__(self):
        ...

class TextRestrictionsKorea(TextRestrictionsChinese):
    __slots__ = TextRestrictionsChinese.__slots__
    LOGIN_NAME_MIN_LENGTH: Any
    LOGIN_NAME_MAX_LENGTH: Any
    LOGIN_NAME_RE: Any
    ACCOUNT_NAME_RE: Any
    def __init__(self):
        ...

class TextRestrictionsSandbox(TextRestrictionsBasic):
    __slots__ = TextRestrictionsBasic.__slots__
    SANDBOX_POSTFIX_LENGTH = 5
    ACCOUNT_NAME_MAX_LENGTH: Any
    def __init__(self):
        ...

class TextRestrictionsCT(TextRestrictionsBasic):
    __slots__ = TextRestrictionsBasic.__slots__
    CT_POSTFIX_LENGTH = 5
    ACCOUNT_NAME_MAX_LENGTH: Any
    def __init__(self):
        ...

class InvalidStringValueException(SoftException):
    ...

def getClanAbbrevMaxLength():
    ...
def unicode_from_utf8(utf8str, unicodeNormalForm='NFKC'):
    ...
def utf8_accepted(utf8str, regExp, minLen, maxLen, unicodeNormalForm='NFKC', checkBeforeNormalisation=True):
    ...
def normalized_unicode_trim(utf8str, length, unicodeNormalForm='NFKC'):
    ...
def normalized_unicode_trim_u(unicodeStr, length, unicodeNormalForm='NFKC'):
    ...
def normalized_unicode_trim_and_lowercase(utf8str, length, unicodeNormalForm='NFKC'):
    ...
def isAccountNameValid(text, minLength=...):
    ...
def normalizedAccountName(text):
    ...
def isAccountLoginValid(text):
    ...
def normalizedAccountLogin(text):
    ...
def forgeAccountNormalizedName(origNormalizedName, centerID):
    ...
def isClanNameValid(text):
    ...
def normalizedClanName(text):
    ...
def isClanAbbrevValid(abbrev):
    ...
def normalizedClanAbbrev(abbrev):
    ...
def isChannelNameValid(channelName):
    ...
def escapeSQL(text, default='\\0'):
    ...
def normalize_utf8(utf8str):
    ...
def truncate_utf8(utf8str, maxbytes):
    ...
def _is_utf8_one_byte(byte):
    ...
def _is_utf8_first_byte(byte):
    ...
def _decode_utf8_len_byte(byte):
    ...
def strtobool(val):
    ...
