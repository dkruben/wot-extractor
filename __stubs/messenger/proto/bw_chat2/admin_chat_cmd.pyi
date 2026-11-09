# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/bw_chat2/admin_chat_cmd.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import basestring as basestring, long as long, unicode as unicode
from debug_utils import LOG_WARNING as LOG_WARNING
from external_strings_utils import isAccountNameValid as isAccountNameValid, normalizedAccountName as normalizedAccountName
from gui.Scaleform.locale.MESSENGER import MESSENGER as I18N_MESSENGER
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from helpers import i18n as i18n
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE, MESSENGER_COMMAND_TYPE as MESSENGER_COMMAND_TYPE
from messenger.proto.bw_chat2.errors import _SimpleAdminCommandError as _SimpleAdminCommandError, _AdminCommandI18nError as _AdminCommandI18nError
from messenger.proto.entities import _ChatCommand as _ChatCommand
from messenger_common_chat2 import MESSENGER_ACTION_IDS as _ACTIONS
from messenger_common_chat2 import ADMIN_CHAT_COMMANDS_BY_NAMES as _COMMANDS_BY_NAMES
from messenger_common_chat2 import messageArgs as messageArgs
from messenger_common_chat2 import MESSENGER_ERRORS as _ERRORS
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, PlayerCtxStorage as PlayerCtxStorage
from soft_exception import SoftException as SoftException
_MAX_BAN_TIME = 5256000
_TIME_LETTER_TO_MULTIPLIER: dict
_AVAILABLE_PARSERS: dict

# decorador original: @ReprInjector.simple(...)
class _ParsingResult(object):
    __slots__: tuple
    id: Any
    args: Any
    tail: Any
    def __init__(self, args=None, tail=None):
        ...
    def hasError(self):
        ...
    def getError(self):
        ...
    def _next(self):
        ...

class _ParsingError(_ParsingResult):
    __slots__: tuple
    id: Any
    i18nKey: Any
    def __init__(self, errorID, args=None, i18nKey=None):
        ...
    def hasError(self):
        ...
    def getError(self):
        ...

class _ArgsParser(object):
    playerCtx: Any
    nargs: Any
    def __init__(self, nargs):
        ...
    def parse_args(self, argsLine):
        ...

class _UserBanUnBanArgsParser(_ArgsParser):
    def parse_args(self, argsLine):
        ...

class _UserBanArgsParser(_UserBanUnBanArgsParser):
    def __init__(self):
        ...
    def parse_args(self, argsLine):
        ...

class _UserUnBanArgsParser(_UserBanUnBanArgsParser):
    def __init__(self):
        ...

class _AdminChatCommandDecorator(_ChatCommand):
    __slots__: tuple
    _actionID: Any
    def __init__(self, actionID, protoData, clientID=0):
        ...
    def getID(self):
        ...
    def getProtoType(self):
        ...
    def getCommandType(self):
        ...
    def getCommandText(self):
        ...

def getCommandFromLine(text):
    ...
def parseCommandLine(text):
    ...
def makeDecorator(result, clientID):
    ...
