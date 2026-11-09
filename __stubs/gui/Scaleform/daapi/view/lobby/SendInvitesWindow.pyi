# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/SendInvitesWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_ERROR as LOG_ERROR
from gui import SystemMessages as SystemMessages
from gui.Scaleform.daapi.view.meta.SendInvitesWindowMeta import SendInvitesWindowMeta as SendInvitesWindowMeta
from gui.Scaleform.genConsts.CONTACTS_ALIASES import CONTACTS_ALIASES as CONTACTS_ALIASES
from gui.Scaleform.locale.DIALOGS import DIALOGS as DIALOGS
from gui.prb_control import prbDispatcherProperty as prbDispatcherProperty, prbEntityProperty as prbEntityProperty
from gui.prb_control.entities.base.ctx import SendInvitesCtx as SendInvitesCtx
from gui.prb_control.settings import REQUEST_TYPE as REQUEST_TYPE, CTRL_ENTITY_TYPE as CTRL_ENTITY_TYPE
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from helpers import i18n as i18n
from messenger.gui.Scaleform.data.contacts_vo_converter import ContactConverter as ContactConverter
from messenger.gui.Scaleform.view.lobby.ContactsTreeComponent import ContactsTreeComponent as ContactsTreeComponent
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto.interfaces import ISearchHandler as ISearchHandler
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage

class SendInvitesWindow(SendInvitesWindowMeta, ISearchHandler):
    usersStorage: Any
    _onlineMode: Any
    _ctx: Any
    _converter: Any
    _ctrlType: Any
    _prbName: Any
    _showClanOnly: Any
    _invites: Any
    def __init__(self, ctx=None):
        ...
    def getAllAvailableContacts(self):
        ...
    # decorador original: @prbDispatcherProperty
    def prbDispatcher(self):
        ...
    # decorador original: @prbEntityProperty
    def prbEntity(self):
        ...
    @property
    def pyTree(self):
        ...
    def showError(self, value):
        ...
    def setOnlineFlag(self, value):
        ...
    def _getTitle(self):
        ...
    def sendInvites(self, accountsToInvite, comment):
        ...
    def onWindowClose(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _initCooldown(self):
        ...
    def _finiCooldown(self):
        ...
    def _handleSetCoolDown(self, event):
        ...
    def __onUserDataChanged(self, _, user, shadowMode):
        ...
    def __onUserStatusUpdated(self, user):
        ...
    def __onTreeListStateChanged(self, state, isEmpty):
        ...
