# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/ext/player_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from avatar_helpers import getAvatarSessionID as getAvatarSessionID
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.shared.utils import getPlayerDatabaseID as getPlayerDatabaseID, getPlayerName as getPlayerName
from helpers import dependency as dependency
from messenger.m_constants import USER_TAG as USER_TAG
from messenger.proto.entities import ClanInfo as ClanInfo, CurrentLobbyUserEntity as CurrentLobbyUserEntity
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, PlayerCtxStorage as PlayerCtxStorage, UsersStorage as UsersStorage
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any
_CLAN_INFO_ABBREV_INDEX = 1
_CLAN_INFO_ROLE_INDEX = 3

class CurrentPlayerHelper(object):
    itemsCache: Any
    usersStorage: Any
    playerCtx: Any
    def clear(self):
        ...
    def initPersonalAccount(self):
        ...
    def initCachedData(self):
        ...
    def onAvatarShowGUI(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onDisconnected(self):
        ...
    def __setAccountAttrs(self, accountAttrs):
        ...
    def __setClanInfo(self, info):
        ...

def _getInfo4AccountPlayer():
    ...
def _getInfo4AvatarPlayer():
    ...
def isCurrentPlayer(userID):
    ...
