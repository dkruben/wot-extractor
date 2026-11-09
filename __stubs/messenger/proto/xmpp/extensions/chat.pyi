# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/extensions/chat.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import calendar as calendar
import json as json
import time as time
from datetime import datetime as datetime
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from messenger.proto.xmpp.extensions import PyExtension as PyExtension, PyHandler as PyHandler, PyQuery as PyQuery
from messenger.proto.xmpp.extensions.dataform import DataForm as DataForm, Field as Field
from messenger.proto.xmpp.extensions.ext_constants import XML_NAME_SPACE as _NS
from messenger.proto.xmpp.extensions.ext_constants import XML_TAG_NAME as _TAG
from messenger.proto.xmpp.extensions.shared_handlers import IQHandler as IQHandler
from messenger.proto.xmpp.extensions.shared_queries import MessageQuery as MessageQuery
from messenger.proto.xmpp.extensions.shared_queries import PresenceQuery as PresenceQuery
from messenger.proto.xmpp.extensions.wg_items import WgSharedExtension as WgSharedExtension
from messenger.proto.xmpp.gloox_constants import IQ_TYPE as IQ_TYPE, CHAT_STATE as CHAT_STATE, MESSAGE_TYPE_ATTR as MESSAGE_TYPE_ATTR, PRESENCE as PRESENCE
from messenger.proto.xmpp.wrappers import ChatMessage as ChatMessage

class ChatStateExtension(PyExtension):
    def __init__(self, state=...):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def getXPath(self, index=None, suffix='', name=None):
        ...
    def parseTag(self, pyGlooxTag):
        ...

class DelayExtension(PyExtension):
    def __init__(self):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def parseTag(self, pyGlooxTag):
        ...

class MessageIDExtension(PyExtension):
    def __init__(self):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def parseTag(self, pyGlooxTag):
        ...

class ChatHistoryQuery(PyExtension):
    def __init__(self, jid, limit):
        ...

class PrivateHistoryItem(PyExtension):
    def __init__(self):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def parseTag(self, pyGlooxTag):
        ...

class _MucPrivilegesExtension(PyExtension):
    def __init__(self, affiliation='', role=''):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def parseTag(self, pyGlooxTag):
        ...

class MessageWgSharedExtension(WgSharedExtension):
    def __init__(self, includeNS=True):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def parseTag(self, pyGlooxTag):
        ...

class _MessageCustomExtension(PyExtension):
    def __init__(self, msgType, state=...):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def parseTag(self, pyGlooxTag):
        ...

class ChatMessageHolder(MessageQuery):
    def __init__(self, msgType, to, msgBody='', state=...):
        ...

class MessageHandler(PyHandler):
    __slots__: tuple
    _typeAttr: Any
    def __init__(self, typeAttr):
        ...
    def getFilterString(self):
        ...

class ChatMessageHandler(MessageHandler):
    def __init__(self):
        ...

class GetChatHistoryQuery(PyQuery):
    def __init__(self, jid, limit):
        ...

class MUCEntryQuery(PresenceQuery):
    def __init__(self, to):
        ...

class MUCLeaveQuery(PresenceQuery):
    def __init__(self, to):
        ...

class OwnerConfigurationForm(PyExtension):
    def __init__(self, fields=None):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def parseTag(self, pyGlooxTag):
        ...

class OwnerConfigurationFormQuery(PyQuery):
    def __init__(self, to):
        ...

class OwnerConfigurationFormSet(PyQuery):
    def __init__(self, to, fields):
        ...

class OwnerConfigurationFormHandler(IQHandler):
    def __init__(self):
        ...

class UserRoomConfigurationFormSet(OwnerConfigurationFormSet):
    def __init__(self, to, room, password=''):
        ...
