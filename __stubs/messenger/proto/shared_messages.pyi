# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/shared_messages.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from messenger.proto.interfaces import IChatMessage as IChatMessage

class ACTION_MESSAGE_TYPE(object):
    PLAYER = 0
    WARNING = 1
    ERROR = 2
    FAIRPLAY_WARNING = 3
    DYN_SQUAD = 4
    COMMENDATIONS = 5

class ClientActionMessage(IChatMessage):
    __message: Any
    __type: Any
    def __init__(self, msg=None, type_=...):
        ...
    def setMessage(self, msg):
        ...
    def getMessage(self):
        ...
    def getType(self):
        ...

class ClientActionTemplateMessage(ClientActionMessage):
    _tempalteKey: Any
    def __init__(self, tempalteKey, type_=...):
        ...
    def getTemplateKey(self):
        ...
