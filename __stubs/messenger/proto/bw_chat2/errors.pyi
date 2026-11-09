# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/bw_chat2/errors.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.locale.MESSENGER import MESSENGER as I18N_MESSENGER
from gui.Scaleform.locale.INGAME_GUI import INGAME_GUI as I18N_INGAME_GUI
from helpers import i18n as i18n, html as html
from helpers.time_utils import makeLocalServerTime as makeLocalServerTime
from messenger.proto.interfaces import IChatError as IChatError
from messenger.proto.shared_errors import ChatCoolDownError as ChatCoolDownError, ClientActionError as ClientActionError, I18nActionID as I18nActionID, I18nErrorID as I18nErrorID, ChatBanError as ChatBanError
from messenger_common_chat2 import MESSENGER_ACTION_IDS as _ACTIONS
from messenger_common_chat2 import MESSENGER_ERRORS as _ERRORS
from messenger_common_chat2 import MESSENGER_LIMITS as _LIMITS

class _BWChat2I18nError(I18nErrorID):
    def getName(self):
        ...
    def getI18nKey(self):
        ...

class _BWChat2I18nAction(I18nActionID):
    def getName(self):
        ...
    def getI18nName(self):
        ...

class _ActionCoolDownError(ChatCoolDownError):
    def createAction(self, actionID):
        ...

class _BattleCommandError(IChatError):
    __slots__: tuple
    _coolDown: Any
    def __init__(self, command):
        ...

class _BattleCommandCoolDownError(_BattleCommandError):
    _coolDown: Any
    def __init__(self, command, remainingTime=0.0):
        ...
    def getMessage(self):
        ...

class _BattleCommandGenericError(_BattleCommandError):
    __slots__: tuple
    _commandMessageKey: Any
    def __init__(self, command):
        ...
    def getMessage(self):
        ...
    def __getBattleCommandExample(self):
        ...

class _BattleCommandTeamCooldownError(_BattleCommandError):
    _coolDown: Any
    def __init__(self, command, remainingTime):
        ...
    def getMessage(self):
        ...

class _SimpleActionError(ClientActionError):
    def createError(self, errorID):
        ...
    def createAction(self, actionID):
        ...

class _AdminCommandError(IChatError):
    __slots__: tuple
    _error: Any
    def __init__(self, error):
        ...
    def getMessage(self):
        ...

class _SimpleAdminCommandError(_AdminCommandError):
    def __init__(self, errorID, kwargs=None):
        ...

class _AdminCommandI18nError(_AdminCommandError):
    def __init__(self, keys, kwargs):
        ...

class _AdminCommandCoolDownError(_AdminCommandError):
    def __init__(self):
        ...

def getChatActionName(actionID):
    ...
def getChatErrorMessage(errorID, kwargs):
    ...
def createCoolDownError(actionID, remainingTime=0.0):
    ...
def createBroadcastError(args, broadcastID):
    ...
def createAdminCommandError(args):
    ...
def createBattleCommandError(args, command):
    ...
def createVOIPError(args, actionID):
    ...
def createSearchUserError(args):
    ...
