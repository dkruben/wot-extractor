# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgnc/common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from web.web_client_api import CommandHandler as CommandHandler
_logger: Any

class WebHandlersContainer(object):
    _webHandlers: dict
    @classmethod
    def addWebHandler(cls, name, handler):
        ...
    @classmethod
    def removeWebHandler(cls, name):
        ...
    @classmethod
    def getWebHandler(cls, name):
        ...
