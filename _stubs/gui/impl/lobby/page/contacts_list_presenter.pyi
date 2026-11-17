# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/page/contacts_list_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl.gen.view_models.views.lobby.page.footer.contacts_list_model import ContactsListModel as ContactsListModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from messenger.m_constants import USER_TAG as USER_TAG, USER_ACTION_ID as USER_ACTION_ID
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto.shared_find_criteria import FriendsFindCriteria as FriendsFindCriteria
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage
from messenger.proto.bw.entities import BWUserEntity as BWUserEntity

# base nao representavel no stub: ViewComponent[...]
class ContactsListPresenter:
    __usersStorage: Any
    def __init__(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __onUsersListReceived(self, tags):
        ...
    def __onUserStatusUpdated(self, user):
        ...
    def __onUserActionReceived(self, actionID, *args):
        ...
    def __updateContactsCount(self):
        ...
