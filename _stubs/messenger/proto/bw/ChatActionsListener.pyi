# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/bw/ChatActionsListener.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from ChatManager import chatManager as chatManager
from debug_utils import LOG_ERROR as LOG_ERROR

class ChatActionsListener(object):
    _responseHandlers: Any
    def __init__(self, responseHandlers=None):
        ...
    def addListener(self, callback, action, cid=None):
        ...
    def removeListener(self, callback, action, cid=None):
        ...
    def removeAllListeners(self):
        ...
    def handleChatActionFailureEvent(self, actionResponse, chatAction):
        ...
