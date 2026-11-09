# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/bw_chat2/search_processor.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_WARNING as LOG_WARNING
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE
from messenger.proto import proto_getter as proto_getter
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto.search_processor import SearchProcessor as SearchProcessor
from messenger.proto.bw_chat2 import limits as limits
from messenger.ext import checkAccountName as checkAccountName
from messenger.proto.bw_chat2 import errors as errors

class SearchUsersProcessor(SearchProcessor):
    __limits: Any
    _lastRequestID: Any
    def __init__(self):
        ...
    def init(self):
        ...
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    def getSearchResultLimit(self):
        ...
    def getSearchCoolDown(self):
        ...
    def find(self, token, onlineMode=None):
        ...
    def fini(self):
        ...
    def __um_onSearchTokenComplete(self, requestID, result):
        ...
    def __um_onSearchTokenFailed(self, requestID, args):
        ...
