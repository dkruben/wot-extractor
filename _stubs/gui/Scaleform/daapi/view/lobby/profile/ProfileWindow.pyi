# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from PlayerEvents import g_playerEvents as g_playerEvents
from adisp import adisp_process as adisp_process
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.profile.ProfileUtils import getProfileCommonInfo as getProfileCommonInfo
from gui.Scaleform.daapi.view.meta.ProfileWindowMeta import ProfileWindowMeta as ProfileWindowMeta
from gui.Scaleform.locale.PROFILE import PROFILE as PROFILE
from gui.clans.clan_helpers import ClanListener as ClanListener, showClanInviteSystemMsg as showClanInviteSystemMsg
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from gui.wgcg.clan.contexts import CreateInviteCtx as CreateInviteCtx
from helpers import dependency as dependency
from helpers.i18n import makeString as makeString
from messenger import g_settings as g_settings
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE
from messenger.proto import proto_getter as proto_getter
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache

class ProfileWindow(ProfileWindowMeta, ClanListener):
    itemsCache: Any
    lobbyContext: Any
    usersStorage: Any
    __userName: Any
    __databaseID: Any
    __selectedAlias: Any
    __eventOwner: Any
    def __init__(self, ctx=None):
        ...
    def onClanEnableChanged(self, enabled):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __checkUserRosterInfo(self):
        ...
    def __updateAddToClanBtn(self):
        ...
    def __isEnabledInRoaming(self, dbID):
        ...
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    def _onUserActionReceived(self, _, user, shadowMode):
        ...
    def __dossierResyncHandler(self, *args):
        ...
    def __updateUserInfo(self):
        ...
    def registerFlashComponent(self, component, alias, *args):
        ...
    def __getSectionDataObject(self, label, tooltip, alias, linkage, uiId):
        ...
    def userAddFriend(self):
        ...
    # decorador original: @adisp_process
    def userAddToClan(self):
        ...
    def userSetIgnored(self):
        ...
    def userCreatePrivateChannel(self):
        ...
    def onWindowClose(self):
        ...
    def onWindowCloseByIndex(self, *args):
        ...
