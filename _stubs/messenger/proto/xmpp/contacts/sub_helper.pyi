# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/contacts/sub_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from messenger import g_settings as g_settings
from messenger.m_constants import USER_TAG as USER_TAG, PROTO_TYPE as PROTO_TYPE
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto.xmpp import entities as entities
from messenger.proto.xmpp.contacts.sub_tasks import CancelSubscriptionTask as CancelSubscriptionTask, ApproveSubscriptionTask as ApproveSubscriptionTask, AskSubscriptionTask as AskSubscriptionTask
from messenger.proto.xmpp.errors import ClientContactError as ClientContactError, ClientIntLimitError as ClientIntLimitError
from messenger.proto.xmpp.find_criteria import ItemsFindCriteria as ItemsFindCriteria
from messenger.proto.xmpp.gloox_constants import SUBSCRIPTION as _SUB
from messenger.proto.xmpp.log_output import g_logOutput as g_logOutput, CLIENT_LOG_AREA as _LOG
from messenger.proto.xmpp.xmpp_constants import XMPP_ITEM_TYPE as XMPP_ITEM_TYPE, CONTACT_ERROR_ID as CONTACT_ERROR_ID, LIMIT_ERROR_ID as LIMIT_ERROR_ID, CONTACT_LIMIT as CONTACT_LIMIT
from messenger.proto.xmpp.xmpp_items import SubPendingItem as SubPendingItem
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage
_INBOUND_SUB_REMOVE_TAGS: set

class InboundSubscriptionsBatch(object):
    usersStorage: Any
    __slots__: tuple
    _subs: Any
    _cancelTasks: Any
    _approveTasks: Any
    _newRqs: Any
    _oldRqs: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def addSubs(self, subs):
        ...
    def process(self, taskQueue):
        ...
    def _reset(self):
        ...
    def _cancel(self, jid, _):
        ...
    def _approve(self, jid, contact):
        ...
    def _ignore(self, contact):
        ...
    def _validate(self):
        ...
    def _populate(self, taskQueue):
        ...

class SubscriptionsRestrictions(object):
    usersStorage: Any
    __slots__: tuple
    _useCachedCounts: Any
    _cachedRosterCount: Any
    def __init__(self):
        ...
    def setToUseCachedCounts(self, flag):
        ...
    def canAddFriends(self):
        ...
    def canApproveFriendship(self, contact):
        ...
    def canCancelFriendship(self, contact):
        ...
    def _getRosterCount(self):
        ...
