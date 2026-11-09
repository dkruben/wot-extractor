# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/storage/shown_messages_storage.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import listitems as listitems
from messenger.storage.local_cache import SimpleCachedStorage as SimpleCachedStorage

class ShownMessagesStorage(SimpleCachedStorage):
    __slots__: tuple
    __channelShownMessageIDs: Any
    def __init__(self):
        ...
    def __repr__(self):
        ...
    def clear(self):
        ...
    def getMessages(self, channelID):
        ...
    def setMessages(self, channelID, messageIDs):
        ...
    def _getCachedData(self):
        ...
    def _setCachedData(self, data):
        ...
