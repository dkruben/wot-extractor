# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/browser.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from web.client_web_api.common import WebEventSender as WebEventSender
from web.web_client_api import WebCommandHandler as WebCommandHandler
from WebBrowser import WebBrowser as WebBrowser
_logger: Any

class BrowserViewWebHandlers(object):
    __slots__: tuple
    __browser: Any
    __webCommandHandler: Any
    __webEventSender: Any
    def __init__(self, browser, browserID, view, webHandlersMap=None, alias=''):
        ...
    def fini(self):
        ...
    def handleCommand(self, command):
        ...
    def __onWebCommandCallback(self, callbackData):
        ...
    def __onWebEventCallback(self, callbackData):
        ...
