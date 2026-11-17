# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/shared/web_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
import logging as logging
from adisp import adisp_process as adisp_process
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.hangar.BrowserView import makeBrowserParams as makeBrowserParams
from gui.Scaleform.daapi.view.meta.BrowserScreenMeta import BrowserScreenMeta as BrowserScreenMeta
from gui.Scaleform.framework.entities.DisposableEntity import EntityState as EntityState
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from gui.sounds.ambients import HangarOverlayEnv as HangarOverlayEnv
from helpers import dependency as dependency
from skeletons.gui.game_control import IBrowserController as IBrowserController
from gui.Scaleform.framework.managers import ContainerManager as ContainerManager
_logger: Any
BROWSER_LOAD_CALLBACK_DELAY = 0.01

class WebView(BrowserScreenMeta):
    __browserCtrl: Any
    __browser: Any
    __hasFocus: Any
    __browserId: Any
    __loadBrowserCbID: Any
    __ctx: Any
    __browserView: Any
    _url: Any
    _forcedSkipEscape: Any
    _browserParams: Any
    __callbackOnLoad: Any
    __callbackOnClose: Any
    def __init__(self, ctx=None):
        ...
    @property
    def webHandlersReplacements(self):
        ...
    def getBackUrl(self):
        ...
    def onEscapePress(self):
        ...
    def onCloseBtnClick(self):
        ...
    def onFocusChange(self, hasFocus):
        ...
    def viewSize(self, width, height):
        ...
    def getBrowser(self):
        ...
    def webHandlers(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _onUnregisterFlashComponent(self, viewPy, alias):
        ...
    def _getUrl(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _refresh(self):
        ...
    def _onError(self):
        ...
    # decorador original: @adisp_process
    def __loadBrowser(self, width, height):
        ...
    def __updateSkipEscape(self, skipEscape):
        ...
    def __showBrowser(self):
        ...
    def __loadBrowserAS(self):
        ...
    def __handleBrowserClose(self, _):
        ...

class WebViewTransparent(WebView):
    __sound_env__ = HangarOverlayEnv
    _browserParams: Any
    __blur: Any
    __hiddenLayers: Any
    def __init__(self, ctx=None):
        ...
    def _populate(self):
        ...
    def setParentWindow(self, window):
        ...
    def onEscapePress(self):
        ...
    def _needToBeDisposed(self):
        ...
    def _dispose(self):
        ...
