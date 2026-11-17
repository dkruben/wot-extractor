# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/bw/search_processors.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import chat_shared as chat_shared
from constants import CHANNEL_SEARCH_RESULTS_LIMIT as CHANNEL_SEARCH_RESULTS_LIMIT
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE
from messenger.proto import proto_getter as proto_getter
from messenger.proto.bw import cooldown as cooldown
from messenger.proto.search_processor import SearchProcessor as SearchProcessor
from soft_exception import SoftException as SoftException

class SearchChannelsProcessor(SearchProcessor):
    _lastRequestID: Any
    def init(self):
        ...
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    def fini(self):
        ...
    def isInCooldown(self):
        ...
    def find(self, token, **kwargs):
        ...
    def getChatCommand(self):
        ...
    def getSearchResultLimit(self):
        ...
    def getSearchCoolDown(self):
        ...
    def __cm_onSearchTokenComplete(self, requestID, result):
        ...
    def __cm_onSearchTokenFailed(self, requestID, actionResponse, data):
        ...
    def __cm_onChannelExcludeFromSearch(self, channel):
        ...
