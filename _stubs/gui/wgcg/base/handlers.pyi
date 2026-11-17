# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgcg/base/handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.wgcg.settings import WebRequestDataType as WebRequestDataType

class RequestHandlers(object):
    _requester: Any
    def __init__(self, requester):
        ...

class BaseRequestHandlers(RequestHandlers):
    def get(self):
        ...
    def __login(self, ctx, callback=None):
        ...
    def __logout(self, ctx, callback=None):
        ...
    def __ping(self, ctx, callback=None):
        ...
