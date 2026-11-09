# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/spa_requesters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_async as adisp_async
from messenger.m_constants import CLIENT_ERROR_ID as CLIENT_ERROR_ID
from messenger.proto.entities import SharedUserEntity as SharedUserEntity
from messenger.proto.shared_errors import ClientError as ClientError
from messenger.proto.xmpp.errors import createServerIQError as createServerIQError
from messenger.proto.xmpp.extensions import spa_resolver as spa_resolver
from messenger.proto.xmpp.gloox_constants import GLOOX_EVENT as _EVENT, IQ_TYPE as IQ_TYPE
from messenger.proto.xmpp.gloox_wrapper import ClientEventsHandler as ClientEventsHandler
from messenger.proto.xmpp.log_output import g_logOutput as g_logOutput, CLIENT_LOG_AREA as CLIENT_LOG_AREA
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage

class NicknameResolver(ClientEventsHandler):
    usersStorage: Any
    __cached: Any
    __callback: Any
    __iqID: Any
    __isRegistered: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def registerHandlers(self):
        ...
    def unregisterHandlers(self):
        ...
    def resolve(self, dbIDs, callback=None):
        ...
    def __doCallback(self, result=None, error=None):
        ...
    def __handleIQ(self, iqID, iqType, pyGlooxTag):
        ...
    def __handleDisconnected(self, reason, description):
        ...

class AsyncNicknameResolver(NicknameResolver):
    # decorador original: @adisp_async
    def resolve(self, dbIDs, callback=None):
        ...
