# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/gf_notifications/cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from wotdecorators import singleton as singleton

class IGFNotificationsCache(object):
    __slots__: tuple
    def setPayload(self, id, payload):
        ...
    def getPayload(self, id):
        ...
    def clear(self):
        ...

# decorador original: @singleton
class GFNotificationsCache(IGFNotificationsCache):
    __data: Any
    def __init__(self):
        ...
    def setPayload(self, id, payload):
        ...
    def getPayload(self, id):
        ...
    def clear(self):
        ...

def getCache():
    ...
