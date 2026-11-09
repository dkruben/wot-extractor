# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/requesters/TokenResponse.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
TOKEN_EXPIRED_TIME = 3000

class TokenResponse(object):
    __slots__: tuple
    _receivedAt: Any
    _token: Any
    _databaseID: Any
    _error: Any
    def __init__(self, token=None, databaseID=0, error=None, **kwargs):
        ...
    def __repr__(self):
        ...
    def clear(self):
        ...
    def isValid(self):
        ...
    def getDatabaseID(self):
        ...
    def getToken(self):
        ...
    def hasError(self):
        ...
    def getError(self):
        ...
