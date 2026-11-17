# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/gui/Scaleform/view/lobby/ContactsTreeComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers.i18n import makeString as makeString
from gui.Scaleform.daapi.view.meta.ContactsTreeComponentMeta import ContactsTreeComponentMeta as ContactsTreeComponentMeta
from gui.Scaleform.locale.MESSENGER import MESSENGER as MESSENGER
from messenger.gui.Scaleform.data.contacts_data_provider import ContactsDataProvider as ContactsDataProvider
from messenger.gui.Scaleform.view.lobby import ACCOUNT_NAME_MIN_CHARS_LENGTH as ACCOUNT_NAME_MIN_CHARS_LENGTH, ACCOUNT_NAME_MAX_CHARS_LENGTH as ACCOUNT_NAME_MAX_CHARS_LENGTH
from messenger import normalizeGroupId as normalizeGroupId
import Event as Event

class ContactsTreeComponent(ContactsTreeComponentMeta):
    LIST_EMPTY_STATE = 'listEmptyState'
    _mainDP: Any
    onListStateChanged: Any
    onGroupToggled: Any
    def __init__(self):
        ...
    def getMainDP(self):
        ...
    def onGroupSelected(self, mainGroup, groupData):
        ...
    def searchLocalContact(self, flt):
        ...
    def showContacts(self, onlineMode=True, showVisibleOthers=None, showFriends=True, showEmptyGroups=True, showGroupMenu=True):
        ...
    def hasDisplayingContacts(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _updateListState(self):
        ...
    def _setSearchInfo(self):
        ...
    def __onTotalStatusChanged(self):
        ...
