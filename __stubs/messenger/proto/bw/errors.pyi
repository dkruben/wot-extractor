# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/bw/errors.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import basestring as basestring
import messenger as messenger
from chat_shared import CHAT_RESPONSES as CHAT_RESPONSES
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_WARNING as LOG_WARNING
from gui.Scaleform.locale.MESSENGER import MESSENGER as MESSENGER
from gui.impl import backport as backport
from helpers import i18n as i18n
from helpers.time_utils import makeLocalServerTime as makeLocalServerTime
from messenger.m_constants import MESSENGER_I18N_FILE as MESSENGER_I18N_FILE
from messenger.proto.bw.cooldown import getOperationInCooldownMsg as getOperationInCooldownMsg
from messenger.proto.interfaces import IChatError as IChatError

class ChannelNotFound(messenger.error):
    cid: Any
    def __init__(self, cid, *args, **kwargs):
        ...
    def __str__(self):
        ...

class ChatActionError(IChatError):
    _title: Any
    _message: Any
    _isModal: Any
    def __init__(self, title, message, isModal=False):
        ...
    def getTitle(self):
        ...
    def getMessage(self):
        ...
    def isModal(self):
        ...
    @classmethod
    def _makeTitle(cls, name):
        ...
    @classmethod
    def _makeMessage(cls, name):
        ...
    @classmethod
    def create(cls, chatAction):
        ...

class MemberBannedError(ChatActionError):
    @classmethod
    def create(cls, chatAction):
        ...

class ChatBannedError(ChatActionError):
    @classmethod
    def create(cls, chatAction):
        ...

class CommandInCooldownError(ChatActionError):
    @classmethod
    def create(cls, chatAction):
        ...

class I18nError(IChatError):
    __slots__: tuple
    __message: Any
    def __init__(self, key, **kwargs):
        ...
    def getMessage(self):
        ...

class ChannelLimitReachedError(I18nError):
    def __init__(self):
        ...
