# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/extensions/shared_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from messenger.proto.xmpp.extensions import PyHandler as PyHandler

class IQHandler(PyHandler):
    def getFilterString(self):
        ...

class IQChildHandler(PyHandler):
    __slots__: tuple
    _index: Any
    def __init__(self, ext, index=0):
        ...
    def getFilterString(self):
        ...
    def handleTag(self, pyGlooxTag):
        ...

class ProxyHandler(PyHandler):
    def getFilterString(self):
        ...
