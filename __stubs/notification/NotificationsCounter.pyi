# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/notification/NotificationsCounter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.prb_control import prbInvitesProperty as prbInvitesProperty
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE
from messenger.proto import proto_getter as proto_getter
from gui.shared.notifications import NotificationGroup as NotificationGroup
_COUNT_ONLY_ONCE_INDEX = 2

class _GroupCounter(object):
    __notifications: Any
    __seenNotifications: Any
    def __init__(self):
        ...
    def addNotification(self, typeID, entityID, countOnlyOnce):
        ...
    def removeNotification(self, typeID, entityID, countOnlyOnce):
        ...
    def count(self):
        ...
    def reset(self):
        ...
    def resetUnreadCount(self):
        ...
    @classmethod
    def getGroupID(cls):
        ...

class _InfoGroupCounter(_GroupCounter):
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    def resetUnreadCount(self):
        ...
    @classmethod
    def getGroupID(cls):
        ...

class _InviteGroupCounter(_GroupCounter):
    # decorador original: @prbInvitesProperty
    def prbInvites(self):
        ...
    def resetUnreadCount(self):
        ...
    @classmethod
    def getGroupID(cls):
        ...

class _OfferGroupCounter(_GroupCounter):
    @classmethod
    def getGroupID(cls):
        ...

class _CounterCollection(object):
    __counters: Any
    def __init__(self, seq):
        ...
    def clear(self):
        ...
    def addNotification(self, group, typeID, entityID, countOnlyOnce):
        ...
    def removeNotification(self, group, typeID, entityID, countOnlyOnce):
        ...
    def count(self, group=None):
        ...
    def reset(self, group=None):
        ...
    def resetUnreadCount(self, group=None):
        ...

class NotificationsCounter(_CounterCollection):
    def __init__(self):
        ...
