# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/ext/filters/collection.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import re as re
import sre_compile as sre_compile
import BigWorld as BigWorld
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from constants import IS_CHINA as IS_CHINA
from external_strings_utils import normalized_unicode_trim as normalized_unicode_trim
from gui import GUI_SETTINGS as GUI_SETTINGS
from helpers import html as html
from messenger import g_settings as g_settings
from messenger.ext import g_olDictionary as g_olDictionary, g_dnDictionary as g_dnDictionary
from messenger.ext.filters.chain import IIncomingMessageFilter as IIncomingMessageFilter
from messenger.ext.filters.chain import IOutgoingMessageFilter as IOutgoingMessageFilter
from messenger.ext.player_helpers import isCurrentPlayer as isCurrentPlayer
from messenger.m_constants import MESSAGE_FLOOD_COOLDOWN as MESSAGE_FLOOD_COOLDOWN
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage

class ObsceneLanguageFilter(IIncomingMessageFilter):
    def __init__(self):
        ...
    def filter(self, senderID, text):
        ...

class ChinaMessageFilter(ObsceneLanguageFilter):
    def filter(self, senderID, text):
        ...

class ColoringObsceneLanguageFilter(IIncomingMessageFilter):
    usersStorage: Any
    __currentID: Any
    def __init__(self):
        ...
    def __del__(self):
        ...
    def __processBadWord(self, word):
        ...
    def filter(self, senderID, text):
        ...

class SpamFilter(IIncomingMessageFilter):
    _filter: Any
    def __init__(self):
        ...
    def filter(self, senderID, text):
        ...

class FloodFilter(IIncomingMessageFilter):
    __history: Any
    def __init__(self):
        ...
    def filter(self, senderID, text):
        ...
    def resetHistory(self, contactId):
        ...

class DomainNameFilter(IIncomingMessageFilter):
    def __init__(self):
        ...
    def filter(self, senderID, text):
        ...

class HtmlEscapeFilter(IIncomingMessageFilter):
    def filter(self, senderID, text):
        ...

class PostBattleLinksFilter(IIncomingMessageFilter):
    __pattern: Any
    def __init__(self):
        ...
    def filter(self, senderID, text):
        ...
    @classmethod
    def __reSubHandler(cls, match):
        ...
    @classmethod
    def __getUrl(cls):
        ...

class NormalizeMessageFilter(IOutgoingMessageFilter):
    def filter(self, text, limits):
        ...

def getObsceneLanguageFilter():
    ...
