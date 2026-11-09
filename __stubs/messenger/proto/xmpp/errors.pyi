# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/errors.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.locale.MESSENGER import MESSENGER as I18N_MESSENGER
from helpers import i18n as i18n, time_utils as time_utils
from messenger.m_constants import CLIENT_ACTION_ID as CLIENT_ACTION_ID, CLIENT_ERROR_ID as CLIENT_ERROR_ID
from messenger.proto.interfaces import IChatError as IChatError
from messenger.proto import shared_errors as shared_errors
from messenger.proto.shared_errors import ClientActionError as ClientActionError
from messenger.proto.xmpp.extensions.error import StanzaErrorExtension as StanzaErrorExtension, WgErrorExtension as WgErrorExtension, DEF_STANZA_ERROR_CONDITION as DEF_STANZA_ERROR_CONDITION
from messenger.proto.xmpp.extensions.shared_handlers import IQHandler as IQHandler, ProxyHandler as ProxyHandler
from messenger.proto.xmpp import xmpp_constants as xmpp_constants

class _ContactErrorID(shared_errors.I18nErrorID):
    def getName(self):
        ...
    def getI18nKey(self):
        ...

class _LimitErrorID(shared_errors.I18nErrorID):
    def getName(self):
        ...
    def getI18nKey(self):
        ...

class _ChannelErrorID(shared_errors.I18nErrorID):
    def getName(self):
        ...
    def getI18nKey(self):
        ...

class _UserRoomCreationErrorID(shared_errors.I18nErrorID):
    def getName(self):
        ...
    def getI18nKey(self):
        ...

class ClientContactError(shared_errors.ClientError):
    def __init__(self, errorID, name=None):
        ...
    def createError(self, errorID):
        ...

class ClientIntLimitError(shared_errors.ClientError):
    def __init__(self, errorID, maxLimit, minLimit=0):
        ...
    def createError(self, errorID):
        ...

class ClientChannelError(shared_errors.ClientError):
    def __init__(self, errorID, name=None):
        ...
    def createError(self, errorID):
        ...

class StanzaConditionError(IChatError):
    __slots__: tuple
    _errorType: Any
    _condition: Any
    def __init__(self, errorType, condition):
        ...
    def getErrorType(self):
        ...
    def getCondition(self):
        ...
    def getMessage(self):
        ...

class ServerActionError(StanzaConditionError):
    __slots__: tuple
    _actionID: Any
    def __init__(self, actionID, errorType, condition):
        ...
    def getActionID(self):
        ...
    def getMessage(self):
        ...

class ServerUserRoomCreationError(IChatError):
    __slots__: tuple
    _error: Any
    _kwargs: Any
    def __init__(self, errorID, roomName):
        ...
    def getMessage(self):
        ...

def createServerIQError(pyGlooxTag):
    ...
def createServerActionIQError(actionID, pyGlooxTag):
    ...
def createServerUserRoomCreationIQError(pyGlooxTag, roomName):
    ...
def createServerPresenceError(pyGlooxTag):
    ...
def createServerActionPresenceError(actionID, pyGlooxTag):
    ...
def createServerMessageError(pyGlooxTag):
    ...
def createServerActionMessageError(actionID, pyGlooxTag):
    ...
def createChatBanError(banInfo):
    ...
