# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/social/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from gui.clans.clan_cache import g_clanCache as g_clanCache
from gui.shared.view_helpers import UsersInfoHelper as UsersInfoHelper
from helpers import isPlayerAccount as isPlayerAccount
from messenger.m_constants import USER_TAG as USER_TAG
from messenger.proto.shared_find_criteria import MutualFriendsFindCriteria as MutualFriendsFindCriteria
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage
from web.web_client_api import w2capi as w2capi, w2c as w2c, W2CSchema as W2CSchema, Field as Field
from web.web_client_api.common import SPA_ID_TYPES as SPA_ID_TYPES
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class _OnlineStatus(object):
    OFFLINE = 0
    ONLINE = 1
    BUSY = 2

class _PlayerStatusSchema(W2CSchema):
    player_id: Any

# decorador original: @w2capi(...)
class SocialWebApi(object):
    lobbyContext: Any
    usersStorage: Any
    __usersInfoHelper: Any
    def __init__(self):
        ...
    # decorador original: @w2c(...)
    def friendsStatus(self, cmd):
        ...
    # decorador original: @w2c(...)
    def isPlayerOnline(self, cmd, ctx):
        ...
    # decorador original: @w2c(...)
    def getPlayerInfo(self, _):
        ...

def getStatuses(users):
    ...
