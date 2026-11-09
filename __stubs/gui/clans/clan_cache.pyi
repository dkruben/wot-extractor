# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/clans/clan_cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import typing as typing
import BigWorld as BigWorld
from Event import Event as Event
from account_helpers import getAccountDatabaseID as getAccountDatabaseID
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from constants import CLAN_MEMBER_FLAGS as CLAN_MEMBER_FLAGS
from debug_utils import LOG_ERROR as LOG_ERROR
from helpers import dependency as dependency
from helpers import html as html
from gui.clans.formatters import getClanRoleString as getClanRoleString
from gui.shared.utils import code2str as code2str
from messenger.ext import passCensor as passCensor
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.clans.cache_providers.base_provider import IBaseProvider as IBaseProvider
g_clanCache: Any

class ProviderNames(CONST_CONTAINER):
    STRONGHOLD = 'STRONGHOLD'
    MISSIONS = 'MISSIONS'
    STRONGHOLD_EVENT = 'STRONGHOLD_EVENT'
    CLAN_SUPPLY = 'CLAN_SUPPLY'

# base nao representavel no stub: namedtuple(...)
class ClanInfo:
    def getClanName(self):
        ...
    def getClanAbbrev(self):
        ...
    def getMembersFlags(self):
        ...
    def getJoiningTime(self):
        ...

class _ClanCache(object):
    itemsCache: Any
    usersStorage: Any
    __waitForSync: Any
    __clanMembersLen: Any
    __clanMotto: Any
    __clanDescription: Any
    __providers: Any
    onSyncStarted: Any
    onSyncCompleted: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def onAccountShowGUI(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onDisconnected(self):
        ...
    def clear(self):
        ...
    @property
    def clanDBID(self):
        ...
    @property
    def isInClan(self):
        ...
    @property
    def clanMembers(self):
        ...
    @property
    def clanInfo(self):
        ...
    @property
    def clanName(self):
        ...
    @property
    def clanAbbrev(self):
        ...
    @property
    def clanMotto(self):
        ...
    @property
    def clanDescription(self):
        ...
    @property
    def clanTag(self):
        ...
    @property
    def clanCommanderName(self):
        ...
    @property
    def clanRole(self):
        ...
    @property
    def isClanLeader(self):
        ...
    @property
    def strongholdProvider(self):
        ...
    @property
    def strongholdEventProvider(self):
        ...
    @property
    def clanSupplyProvider(self):
        ...
    # decorador original: @adisp_async
    def getFileFromServer(self, clanId, fileType, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def getClanEmblemTextureID(self, clanDBID, isBig, textureID, callback):
        ...
    def getClanRoleUserString(self):
        ...
    def onClanInfoReceived(self, clanDBID, clanName, clanAbbrev, clanMotto, clanDescription):
        ...
    def _valueResponse(self, resID, value, callback):
        ...
    def __registerProvider(self, providerName, providerClazz, args):
        ...
    def __startProviders(self):
        ...
    def __stopProviders(self, withClear=False):
        ...
    def __me_onClanMembersListChanged(self):
        ...
