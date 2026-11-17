# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/gui/Scaleform/data/contacts_cm_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.user_cm_handlers import BaseUserCMHandler as BaseUserCMHandler
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity as EventSystemEntity
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuCollectEventsHandler as AbstractContextMenuCollectEventsHandler
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.locale.MESSENGER import MESSENGER as MESSENGER
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.system_factory import registerLobbyContexMenuHandler as registerLobbyContexMenuHandler
from gui.shared.system_factory import collectLobbyContexMenuHandler as collectLobbyContexMenuHandler
from messenger import normalizeGroupId as normalizeGroupId
from messenger.m_constants import USER_TAG as USER_TAG

class CONTACTS_ACTION_ID(object):
    EDIT_GROUP = 'editGroup'
    REMOVE_GROUP = 'removeGroup'
    REMOVE_FROM_GROUP = 'removeFromGroup'
    CREATE_CONTACT_NOTE = 'createContactNote'
    EDIT_CONTACT_NOTE = 'editContactNote'
    REMOVE_CONTACT_NOTE = 'removeContactNote'
    REJECT_FRIENDSHIP = 'rejectFriendship'

class SimpleContactsCMHandler(AbstractContextMenuCollectEventsHandler, EventSystemEntity):
    targetGroupName: Any
    def _getContexMenuHandler(self):
        ...
    def _generateOptions(self, ctx=None):
        ...
    def _initFlashValues(self, ctx):
        ...
    def _clearFlashValues(self):
        ...

class PlayerContactsCMHandler(BaseUserCMHandler):
    targetGroupName: Any
    showUserNotes: Any
    def _initFlashValues(self, ctx):
        ...
    def _clearFlashValues(self):
        ...
    def _addRejectFriendshipInfo(self, options, userCMInfo):
        ...
    def _addContactsNoteInfo(self, options, userCMInfo):
        ...
    def _addRemoveFromGroupInfo(self, options, isIgnored):
        ...

def editGroup(cm):
    ...
def removeGroup(cm):
    ...
def createContactNote(cm):
    ...
def editContactNote(cm):
    ...
def removeContactNote(cm):
    ...
def removeFromGroup(cm):
    ...
def rejectFriendship(cm):
    ...
