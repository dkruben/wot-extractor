# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/chat.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import basestring as basestring
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE
from messenger.proto import proto_getter as proto_getter
from messenger.storage import UsersStorage as UsersStorage, MessengerStorageDescriptor as MessengerStorageDescriptor
from web.web_client_api import W2CSchema as W2CSchema, Field as Field, w2c as w2c
from web.web_client_api.common import SPA_ID_TYPES as SPA_ID_TYPES

class _OpenChatSchema(W2CSchema):
    user_id: Any
    user_name: Any

class ChatWebApiMixin(object):
    usersStorage: Any
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    # decorador original: @w2c(...)
    def openChat(self, cmd):
        ...
