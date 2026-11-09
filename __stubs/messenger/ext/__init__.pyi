# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/ext/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import types as types
from past.builtins import unicode as unicode
import BigWorld as BigWorld
import BattleReplay as BattleReplay
import constants as constants
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from helpers import i18n as i18n
from gui.Scaleform.locale.MESSENGER import MESSENGER as MESSENGER
from external_strings_utils import isAccountNameValid as isAccountNameValid
from external_strings_utils import _ACCOUNT_NAME_MIN_LENGTH as _ACCOUNT_NAME_MIN_LENGTH, _ACCOUNT_NAME_MAX_LENGTH as _ACCOUNT_NAME_MAX_LENGTH
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_DEBUG as LOG_DEBUG
from messenger import g_settings as g_settings
from messenger.ext import dictionaries as dictionaries
from messenger.m_constants import CLIENT_ERROR_ID as CLIENT_ERROR_ID
MESSENGER_OLDICT_FILE_PATH = 'text/messenger_oldictionary.xml'
MESSENGER_DOMAIN_FILE_PATH = 'text/messenger_dndictionary.xml'
g_dnDictionary: Any
g_olDictionary: Any

def passCensor(text):
    ...
def isBattleChatEnabled(common=False):
    ...
def validateAccountName(name):
    ...
def checkAccountName(token):
    ...
def isSenderIgnored(user):
    ...
def isNotFriendSenderIgnored(user, areFriendsOnly):
    ...
