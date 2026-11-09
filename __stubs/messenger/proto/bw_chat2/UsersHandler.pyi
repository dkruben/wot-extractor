# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/bw_chat2/UsersHandler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from messenger.m_constants import GAME_ONLINE_STATUS as GAME_ONLINE_STATUS, USER_TAG as USER_TAG
from messenger.proto.bw_chat2 import provider as bw2_provider, limits as limits
from messenger.proto.bw_chat2.wrappers import SearchResultIterator as SearchResultIterator
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage
from messenger_common_chat2 import MESSENGER_ACTION_IDS as _ACTIONS, messageArgs as messageArgs
from debug_utils import LOG_WARNING as LOG_WARNING

class UsersHandler(bw2_provider.ResponseDictHandler):
    usersStorage: Any
    __limits: Any
    def __init__(self, provider):
        ...
    def findUsers(self, namePattern, searchOnlineOnly=None):
        ...
    def clear(self):
        ...
    def _onResponseSuccess(self, ids, args):
        ...
    def _onResponseFailure(self, ids, args):
        ...
