# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/common/browser_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class BrowserState(Enum):
    INITIALIZATION = 'initialization'
    LOADING = 'loading'
    FORCELOADING = 'forceLoading'
    LOADED = 'loaded'

class PageState(Enum):
    INITIALIZATION = 'initialization'
    LOADING = 'loading'
    LOADED = 'loaded'
    FAILED = 'failed'

class TetxureState(Enum):
    INITIALIZATION = 'initialization'
    LOADED = 'loaded'
    FAILED = 'failed'

class BrowserModel(ViewModel):
    __slots__: tuple
    createWebView: Any
    focus: Any
    unfocus: Any
    reload: Any
    def __init__(self, properties=7, commands=4):
        ...
    def getId(self):
        ...
    def setId(self, value):
        ...
    def getBrowserState(self):
        ...
    def setBrowserState(self, value):
        ...
    def getPageState(self):
        ...
    def setPageState(self, value):
        ...
    def getTexState(self):
        ...
    def setTexState(self, value):
        ...
    def getHttpStatusCode(self):
        ...
    def setHttpStatusCode(self, value):
        ...
    def getTitle(self):
        ...
    def setTitle(self, value):
        ...
    def getWaitingMessage(self):
        ...
    def setWaitingMessage(self, value):
        ...
    def _initialize(self):
        ...
