# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/gui/Scaleform/view/lobby/ContactsSettingsView.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.locale.MESSENGER import MESSENGER as MESSENGER
from account_helpers.AccountSettings import AccountSettings as AccountSettings, CONTACTS as CONTACTS
from helpers import dependency as dependency
from messenger.gui.Scaleform.meta.ContactsSettingsViewMeta import ContactsSettingsViewMeta as ContactsSettingsViewMeta
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore

class ContactsSettingsView(ContactsSettingsViewMeta):
    settingsCore: Any
    __startData: Any
    __currentData: Any
    __isOperationAvailable: Any
    def __init__(self):
        ...
    def onOk(self, data):
        ...
    def showOfflineUsers(self, value):
        ...
    def showOthers(self, value):
        ...
    def messagesNotFromContacts(self, value):
        ...
    def _populate(self):
        ...
    def _getInitDataObject(self):
        ...
    def __checkIsDataChanged(self):
        ...
