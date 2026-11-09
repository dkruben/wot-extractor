# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/xmpp_clan_listener.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_DEBUG as LOG_DEBUG
from gui.shared.utils import getPlayerDatabaseID as getPlayerDatabaseID
from messenger import g_settings as g_settings
from messenger.m_constants import GAME_ONLINE_STATUS as GAME_ONLINE_STATUS, USER_TAG as USER_TAG, PROTO_TYPE as PROTO_TYPE
from messenger.proto.entities import ClanInfo as ClanInfo
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto.xmpp import entities as entities
from messenger.proto.xmpp.entities import XMPPUserEntity as XMPPUserEntity
from messenger.proto.xmpp.find_criteria import XmppClanChannelCriteria as XmppClanChannelCriteria
from messenger.proto.xmpp.gloox_wrapper import ClientHolder as ClientHolder
from messenger.proto.xmpp.xmpp_constants import XMPP_MUC_CHANNEL_TYPE as XMPP_MUC_CHANNEL_TYPE
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, ChannelsStorage as ChannelsStorage, PlayerCtxStorage as PlayerCtxStorage, UsersStorage as UsersStorage

class XmppClanListener(ClientHolder):
    usersStorage: Any
    channelsStorage: Any
    playerCtx: Any
    __slots__: tuple
    __channelCriteria: Any
    __clanChannel: Any
    __clanDBID: Any
    __clanAbbrev: Any
    def __init__(self):
        ...
    def registerHandlers(self):
        ...
    def unregisterHandlers(self):
        ...
    def clear(self):
        ...
    def __addClanChannelToStorage(self):
        ...
    def __removeClanChannel(self):
        ...
    def __initClanChannel(self, channel):
        ...
    def __refreshClanMembers(self):
        ...
    def __ce_onChannelInited(self, channel):
        ...
    def __ce_onChannelDestroyed(self, channel):
        ...
    def __ce_onMembersListChanged(self):
        ...
    def __pe_onClanMembersListChanged(self):
        ...
    def __pc_onClanInfoChanged(self):
        ...
    def __onPluginConnected(self, proto):
        ...
    def __checkForJoin(self):
        ...
    def __checkForLeave(self):
        ...
