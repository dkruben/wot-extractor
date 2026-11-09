# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/m_settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple, defaultdict as defaultdict
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import Event as Event
from debug_utils import LOG_ERROR as LOG_ERROR
from helpers import dependency as dependency
from helpers.html.templates import XMLCollection as XMLCollection
from messenger import doc_loaders as doc_loaders
from messenger.doc_loaders.html_templates import MessageTemplates as MessageTemplates
from messenger.m_constants import BATTLE_CHANNEL as BATTLE_CHANNEL
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
_ServiceChannelSettings: Any
_BattleMessageLifeCycle: Any
_UserPrefs: Any

class _ColorScheme(defaultdict):
    __colorsNames: Any
    __current: Any
    def __init__(self, names, default_factory=None, **kwargs):
        ...
    def __missing__(self, key):
        ...
    def getColorsNames(self):
        ...
    def getDefColorName(self):
        ...
    def getColor(self, key):
        ...
    def getColors(self, key):
        ...
    def setCurrent(self, name):
        ...
    def getHexStr(self, key):
        ...
    def iterColors(self):
        ...
    def iterHexs(self):
        ...

class _LobbySettings(object):
    __slots__: tuple
    serviceChannel: Any
    messageRawFormat: Any
    badWordFormat: Any
    __messageFormats: Any
    def __init__(self):
        ...
    def getMessageFormat(self, key):
        ...
    def onSettingsLoaded(self, root):
        ...

class _BattleSettings(object):
    __slots__: tuple
    messageLifeCycle: Any
    messageFormat: Any
    targetFormat: Any
    inactiveStateAlpha: Any
    toolTipText: Any
    chatIsLockedToolTipText: Any
    chatIsLockedParentalControlToolTipText: Any
    chatIsLockedCountryControlToolTipText: Any
    chatIsLockedOtherControlToolTipText: Any
    toolTipTextWithMuteInfo: Any
    battleRoyaleTooltip: Any
    numberOfMessagesInHistory: Any
    receivers: Any
    alphaForLastMessages: Any
    recoveredLatestMessages: Any
    lifeTimeRecoveredMessages: Any
    lastReceiver: Any
    def __init__(self):
        ...

class MessengerSettings(object):
    __slots__: tuple
    settingsCore: Any
    __colorsSchemes: Any
    lobby: Any
    battle: Any
    userPrefs: Any
    __isUserPrefsInited: Any
    __defaultUserPrefsSnapshot: Any
    htmlTemplates: Any
    msgTemplates: Any
    __messageFormatters: Any
    server: Any
    __eManager: Any
    onUserPreferencesUpdated: Any
    onColorsSchemesUpdated: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def update(self):
        ...
    def getColorScheme(self, key):
        ...
    def resetUserPreferences(self):
        ...
    def saveUserPreferences(self, data):
        ...
    def resetBattleReceiverIfNeed(self):
        ...
    def __accs_onSettingsChanged(self, diff):
        ...

def _getAccountRepository():
    ...
def _makeDefUserPrefs():
    ...
