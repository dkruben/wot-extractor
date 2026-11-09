# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/client_web_api/api.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import time as time
import typing as typing
import weakref as weakref
from typing import Callable as Callable, Dict as Dict, Optional as Optional, Tuple as Tuple, Union as Union
from web.client_web_api.common import WebEventSender as WebEventSender
WebEvent: Any
HashedEvent: Any
_TYPE = 'type'
_DATA = 'data'
_TIME = 'time'

class C2WHandler(object):
    __sender: Any
    __previous: Any
    def __init__(self, sender):
        ...
    @property
    def preventIdentical(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def _sendWebEvent(self, webEvent):
        ...
    def __isDuplicate(self, eTime, eType, eData):
        ...
    def __cachePrevious(self, eTime, eType, eData):
        ...
    @staticmethod
    def __hashedEvent(webEvent):
        ...

def c2w(name, preventIdentical=True):
    ...
