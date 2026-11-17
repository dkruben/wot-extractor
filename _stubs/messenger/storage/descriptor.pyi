# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/storage/descriptor.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from gui.shared.utils import getPlayerDatabaseID as getPlayerDatabaseID, getPlayerName as getPlayerName
from messenger import error as error
from py2to3.patched_typing import Generic as Generic
from .ChannelsStorage import ChannelsStorage as ChannelsStorage
from .local_cache import StorageLocalCache as StorageLocalCache
from .PlayerCtxStorage import PlayerCtxStorage as PlayerCtxStorage
from .shown_messages_storage import ShownMessagesStorage as ShownMessagesStorage
from .UsersStorage import UsersStorage as UsersStorage
_STORAGE: dict
_StorageType: Any

# base nao representavel no stub: Generic[...]
class MessengerStorageDescriptor:
    __class: Any
    def __init__(self, class_):
        ...
    def __get__(self, obj, objType):
        ...
    def get(self):
        ...

class StorageDecorator(object):
    __storageCache: Any
    def __repr__(self):
        ...
    def __init__(self):
        ...
    def restoreFromCache(self):
        ...
    def init(self):
        ...
    def switch(self, scope):
        ...
    def clear(self):
        ...
    def __onRead(self):
        ...
