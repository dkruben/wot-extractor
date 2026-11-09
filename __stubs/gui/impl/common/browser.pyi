# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/common/browser.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import Event as Event
from frameworks.wulf import ViewSettings as ViewSettings, ViewFlags as ViewFlags
from gui.browser import BrowserViewWebHandlers as BrowserViewWebHandlers
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.gen.view_models.common.browser_model import BrowserModel as BrowserModel, BrowserState as BrowserState, PageState as PageState, TetxureState as TetxureState
from gui.impl.gen import R as R
from helpers import dependency as dependency
from adisp import adisp_process as adisp_process
from skeletons.gui.game_control import IBrowserController as IBrowserController
from typing import Optional as Optional
from WebBrowser import WebBrowser as WebBrowser
from web.web_client_api import webApiCollection as webApiCollection
_logger: Any
TViewModel: Any

class BrowserSettings(ViewSettings):
    def __init__(self, layoutID=..., flags=..., model=None, args=...):
        ...

# base nao representavel no stub: ViewImpl[...]
class Browser:
    __slots__: tuple
    __browserCtrl: Any
    __url: Any
    __browserId: Any
    __webHandlersMap: Any
    __browser: Any
    __webCommandHandler: Any
    __backUrl: Any
    __eventManager: Any
    onBrowserObtained: Any
    def __init__(self, url='', settings=None, webHandlersMap=None, preload=False, *args, **kwargs):
        ...
    @property
    def browser(self):
        ...
    @property
    def url(self):
        ...
    @property
    def backUrl(self):
        ...
    def setBackUrl(self, url):
        ...
    def setWaitingMessage(self, message):
        ...
    def showLoading(self, show):
        ...
    def _getEvents(self):
        ...
    def _finalize(self):
        ...
    # decorador original: @adisp_process
    def __loadBrowser(self):
        ...
    def __initBrowser(self):
        ...
    def __onBrowserAddedHandler(self, browserId):
        ...
    def __onCreateVebView(self):
        ...
    def __onFocus(self):
        ...
    def __onUnfocus(self):
        ...
    def __onReload(self):
        ...
    def __onLoadStart(self, url):
        ...
    def __onLoadEnd(self, _, isLoaded=True, httpStatusCode=None):
        ...
    def __onLoadingStateChange(self, isLoading, allowAutoLoadingScreenChange):
        ...
    def __onTitleChange(self, title):
        ...
    def __onJsHostQuery(self, command):
        ...
    def __onTextureStateChanged(self, isOk):
        ...
