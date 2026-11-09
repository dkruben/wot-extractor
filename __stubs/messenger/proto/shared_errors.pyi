# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/shared_errors.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.locale.MESSENGER import MESSENGER as I18N_MESSENGER
from gui.impl import backport as backport
from helpers import i18n as i18n
from messenger.m_constants import CLIENT_ERROR_NAMES as CLIENT_ERROR_NAMES, CLIENT_ACTION_NAMES as CLIENT_ACTION_NAMES, CLIENT_ERROR_ID as CLIENT_ERROR_ID
from messenger.proto.interfaces import IChatError as IChatError

class I18nErrorID(object):
    __slots__: tuple
    errorID: Any
    def __init__(self, errorID):
        ...
    def __repr__(self):
        ...
    def getName(self):
        ...
    def getI18nKey(self):
        ...

class I18nActionID(object):
    __slots__: tuple
    actionID: Any
    def __init__(self, actionID):
        ...
    def __repr__(self):
        ...
    def getName(self):
        ...
    def getI18nName(self):
        ...

class ClientError(IChatError):
    __slots__: tuple
    _error: Any
    _kwargs: Any
    def __init__(self, errorID, **kwargs):
        ...
    def __repr__(self):
        ...
    def createError(self, errorID):
        ...
    def getErrorID(self):
        ...
    def getErrorName(self):
        ...
    def getMessage(self):
        ...

class ClientActionError(ClientError):
    __slots__: tuple
    _action: Any
    def __init__(self, actionID, errorID=None, **kwargs):
        ...
    def __repr__(self):
        ...
    def createAction(self, actionID):
        ...
    def getActionID(self):
        ...
    def getMessage(self):
        ...

class ChatCoolDownError(ClientActionError):
    def __init__(self, actionID, coolDown=None):
        ...
    def getMessage(self):
        ...

class ChatBanError(IChatError):
    __slots__: tuple
    _endTime: Any
    _reason: Any
    def __init__(self, endTime, reason):
        ...
    def getTitle(self):
        ...
    def getMessage(self):
        ...
    def isModal(self):
        ...
