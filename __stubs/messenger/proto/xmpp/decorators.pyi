# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/decorators.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_WARNING as LOG_WARNING
from messenger.ext import validateAccountName as validateAccountName
from messenger.m_constants import CLIENT_ERROR_ID as CLIENT_ERROR_ID
from messenger.proto.shared_errors import ClientError as ClientError
from messenger.proto.xmpp import xmpp_string_utils as xmpp_string_utils
from messenger.proto.xmpp.gloox_wrapper import ClientHolder as ClientHolder
_QUERY_SIGN_VALIDATORS: dict
_QUERY_OPT_SIGNS: tuple

class QUERY_SIGN(object):
    DATABASE_ID = 1
    ACCOUNT_NAME = 2
    GROUP_NAME = 3
    OPT_GROUP_NAME = 4
    NOTE_TEXT = 5
    SHADOW_MODE = 6

class local_query(ClientHolder):
    __slots__: tuple
    _sign: Any
    def __init__(self, *args):
        ...
    def __call__(self, func):
        ...
    def _validate(self, *args):
        ...

class xmpp_query(local_query):
    __slots__: tuple
    def _validate(self, *args):
        ...

def _validateDatabaseID(dbID):
    ...
def _validateAccountName(name):
    ...
def _validateGroupName(name):
    ...
def _validateOptionalGroupName(name):
    ...
def _validateNoteText(note):
    ...
def _validateShadowMode(_):
    ...
