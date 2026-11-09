# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/SyncController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import zlib as zlib
from functools import partial as partial
from future.moves import pickle as pickle
import BigWorld as BigWorld
import AccountCommands as AccountCommands
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION, LOG_CODEPOINT_WARNING as LOG_CODEPOINT_WARNING, LOG_ERROR as LOG_ERROR

class SyncController(object):
    __STREAM_ERRORS_LIMIT = 3
    __account: Any
    __sendSyncRequest: Any
    __onOwnerSyncResponse: Any
    __onOwnerSyncComplete: Any
    __syncRequests: Any
    __streamErrors: Any
    def __init__(self, account, sendSyncRequest, onSyncResponse, onSyncComplete):
        ...
    def destroy(self):
        ...
    def request(self, syncID, callback):
        ...
    def __onSyncResponse(self, syncID, requestID, resultID, errorStr, ext=None):
        ...
    def __onSyncStreamComplete(self, syncID, isSuccess, data):
        ...
