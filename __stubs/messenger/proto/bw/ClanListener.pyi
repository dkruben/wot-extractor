# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/bw/ClanListener.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR
from gui.shared.utils import getPlayerDatabaseID as getPlayerDatabaseID
from messenger.m_constants import USER_TAG as USER_TAG, GAME_ONLINE_STATUS as GAME_ONLINE_STATUS
from messenger.proto.bw.find_criteria import BWClanChannelFindCriteria as BWClanChannelFindCriteria
from messenger.proto.entities import CurrentLobbyUserEntity as CurrentLobbyUserEntity, SharedUserEntity as SharedUserEntity, ClanInfo as ClanInfo
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, ChannelsStorage as ChannelsStorage, PlayerCtxStorage as PlayerCtxStorage, UsersStorage as UsersStorage

class _INIT_STEPS(object):
    CLAN_INFO_RECEIVED = 1
    MEMBERS_LIST_RECEIVED = 2
    LIST_INITED: Any

class ClanListener(object):
    usersStorage: Any
    channelsStorage: Any
    playerCtx: Any
    __initSteps: Any
    __clanChannel: Any
    __channelCriteria: Any
    def __init__(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def __findClanChannel(self):
        ...
    def __initClanChannel(self, channel):
        ...
    def __clearClanChannel(self):
        ...
    def __refreshClanMembers(self):
        ...
    def __pe_onClanMembersListChanged(self):
        ...
    def __pc_onClanInfoChanged(self):
        ...
    def __ce_onChannelInited(self, channel):
        ...
    def __ce_onChannelDestroyed(self, channel):
        ...
    def __ce_onMembersListChanged(self):
        ...
