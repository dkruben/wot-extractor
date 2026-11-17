# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/browser.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import basestring as basestring, long as long
from adisp import adisp_process as adisp_process
from frameworks import wulf as wulf
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA as POP_UP_CRITERIA
from gui.game_control.links import URLMacros as URLMacros
from gui.shared.event_dispatcher import showBrowserOverlayView as showBrowserOverlayView
from gui.shared.utils.functions import getViewName as getViewName
from gui.shop import showBuyGoldWebOverlay as showBuyGoldWebOverlay
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import IBrowserController as IBrowserController, IExternalLinksController as IExternalLinksController
from web.web_client_api import Field as Field, W2CSchema as W2CSchema, WebCommandException as WebCommandException, w2c as w2c

class _OpenBrowserWindowSchema(W2CSchema):
    url: Any
    title: Any
    width: Any
    height: Any
    is_modal: Any
    show_refresh: Any
    show_create_waiting: Any
    is_solid_border: Any

class _OpenExternalBrowserSchema(W2CSchema):
    url: Any

class _OpenBrowserOverlaySchema(W2CSchema):
    url: Any
    blur_bg: Any
    is_client_close_control: Any

class _OpenBuyGoldOverlaySchema(W2CSchema):
    params: Any

class OpenBrowserWindowWebApiMixin(object):
    # decorador original: @w2c(...)
    def browser(self, cmd):
        ...
    def _onBrowserOpen(self, alias):
        ...
    def _createHandlers(self):
        ...
    # decorador original: @adisp_process
    def __loadBrowser(self, url, title, width, height, isModal, showRefresh, showCreateWaiting):
        ...

class CloseBrowserWindowWebApiMixin(object):
    # decorador original: @w2c(...)
    def browser(self, cmd, ctx):
        ...
    def _onBrowserClose(self):
        ...

class CloseBrowserViewWebApiMixin(object):
    # decorador original: @w2c(...)
    def browser(self, cmd, ctx):
        ...

class OpenExternalBrowserWebApiMixin(object):
    # decorador original: @w2c(...)
    def externalBrowser(self, cmd):
        ...

class OpenBrowserOverlayWebApiMixin(object):
    # decorador original: @w2c(...)
    def openBrowserOverlay(self, cmd):
        ...

class OpenBuyGoldWebApiMixin(object):
    # decorador original: @w2c(...)
    def openBuyGoldWebOverlay(self, cmd):
        ...

def _tryToCloseWulfView(view):
    ...
