# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/SimpleStreamResponseHandler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import zlib as zlib
from future.moves import pickle as pickle
import AccountCommands as AccountCommands
from debug_utils import LOG_CODEPOINT_WARNING as LOG_CODEPOINT_WARNING, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION

class SimpleStreamResponseHandler(object):
    __accountRef: Any
    __callback: Any
    __default: Any
    def __init__(self, account, callback, default=None):
        ...
    def __call__(self, requestID, resultID, errorStr, ext=None):
        ...
    def __onStreamComplete(self, isSuccess, data):
        ...
