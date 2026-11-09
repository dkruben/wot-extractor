# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/formatters/chat_message.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import unicode as unicode
from helpers import dependency as dependency
from messenger import g_settings as g_settings
from messenger.ext.player_helpers import isCurrentPlayer as isCurrentPlayer
from messenger.formatters import TimeFormatter as TimeFormatter
from messenger.m_constants import USER_GUI_TYPE as USER_GUI_TYPE
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class _BattleMessageBuilder(object):
    sessionProvider: Any
    _ctx: Any
    def __init__(self):
        ...
    def setColors(self, avatarSessionID):
        ...
    def setName(self, avatarSessionID, pName=None, suffix='', vehID=None):
        ...
    def setText(self, text):
        ...
    def build(self):
        ...

class TeamMessageBuilder(_BattleMessageBuilder):
    def setColors(self, avatarSessionID):
        ...

class CommonMessageBuilder(_BattleMessageBuilder):
    def setColors(self, avatarSessionID):
        ...

class SquadMessageBuilder(_BattleMessageBuilder):
    def setColors(self, avatarSessionID):
        ...

class LobbyMessageBuilder(object):
    lobbyContext: Any
    usersStorage: Any
    __templateKey: Any
    __guiType: Any
    __name: Any
    __time: Any
    __text: Any
    def __init__(self):
        ...
    def setTime(self, time_):
        ...
    def getGroup(self):
        ...
    def setGroup(self, group):
        ...
    def getGuiType(self):
        ...
    def setGuiType(self, dbID):
        ...
    def setName(self, dbID, nickName, clanAbbrev=None):
        ...
    def setText(self, text):
        ...
    def build(self):
        ...
