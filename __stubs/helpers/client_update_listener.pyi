# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/client_update_listener.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import Event as Event
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers import AccountSyncData as AccountSyncData
from helpers import dependency as dependency
from shared_utils.account_helpers.diff_utils import synchronizeDicts as synchronizeDicts
from skeletons.connection_mgr import IConnectionManager as IConnectionManager

class ClientUpdateListener(object):
    __slots__: tuple
    __connectionMgr: Any
    __default: Any
    __data: Any
    __synced: Any
    __key: Any
    __resetOnDisconnect: Any
    onDataUpdated: Any
    def __init__(self, key, resetOnDisconnect=True, default=None):
        ...
    @property
    def data(self):
        ...
    @property
    def synced(self):
        ...
    def init(self):
        ...
    def destroy(self):
        ...
    def reset(self):
        ...
    def __onClientUpdated(self, diff, *_):
        ...
    def __onDisconnected(self):
        ...
