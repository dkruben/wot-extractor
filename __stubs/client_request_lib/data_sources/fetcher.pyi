# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/client_request_lib/data_sources/fetcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from soft_exception import SoftException as SoftException

class FakeResponse(object):
    responseCode: Any
    body: Any
    _headers: Any
    def __init__(self, r):
        ...
    def headers(self):
        ...
    def __repr__(self):
        ...

def fetchURL(url, callback, headers=None, timeout=30, method='GET', postData=''):
    ...
