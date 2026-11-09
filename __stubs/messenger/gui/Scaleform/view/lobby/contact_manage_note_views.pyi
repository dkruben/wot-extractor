# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/gui/Scaleform/view/lobby/contact_manage_note_views.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import long as long
from gui.Scaleform.locale.MESSENGER import MESSENGER as MESSENGER
from messenger.gui.Scaleform.data.contacts_vo_converter import ContactConverter as ContactConverter
from messenger.gui.Scaleform.meta.ContactNoteManageViewMeta import ContactNoteManageViewMeta as ContactNoteManageViewMeta
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE
from messenger.proto import proto_getter as proto_getter
from messenger.proto.xmpp.xmpp_string_utils import validateContactNote as validateContactNote
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage
from messenger.proto.xmpp.xmpp_constants import CONTACT_LIMIT as CONTACT_LIMIT
from helpers import i18n as i18n
from messenger import g_settings as g_settings

class ContactManageNoteView(ContactNoteManageViewMeta):
    usersStorage: Any
    _dbID: Any
    _note: Any
    def __init__(self):
        ...
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    def sendData(self, data):
        ...
    def checkText(self, txt):
        ...
    def onOk(self, data):
        ...
    def _isTextValid(self, text):
        ...
    def _extendInitData(self, defData):
        ...

class ContactEditNoteView(ContactManageNoteView):
    def sendData(self, data):
        ...
    def _isTextValid(self, text):
        ...
    def _getInitDataObject(self):
        ...

class ContactCreateNoteView(ContactManageNoteView):
    def _populate(self):
        ...
    def _getInitDataObject(self):
        ...
