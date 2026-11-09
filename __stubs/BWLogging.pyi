# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/BWLogging.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
import sys as sys
import BigWorld as BigWorld
logLevelToBigWorldFunction: dict
_bwRedirectionHandler = None

class BWLogger(logging.Logger):
    TRACE: Any
    NOTICE: Any
    HACK: Any
    def __init__(self, name, level=...):
        ...
    def trace(self, msg, *args, **kw):
        ...
    def notice(self, msg, *args, **kw):
        ...
    def hack(self, msg, *args, **kw):
        ...

class BWLogRedirectionHandler(logging.Handler):
    def __init__(self):
        ...
    def emit(self, record):
        ...

def getBwHandler():
    ...
def init():
    ...
