# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/common/browser_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewFlags as ViewFlags
from gui.impl import backport as backport
from gui.impl.common.browser import Browser as Browser, BrowserSettings as BrowserSettings
from gui.impl.gen.view_models.views.browser_view_model import BrowserViewModel as BrowserViewModel
from gui.impl.gen import R as R
from gui.impl.lobby.common.sound_constants import BROWSER_VIEW_SOUND_SPACES as BROWSER_VIEW_SOUND_SPACES
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from web.web_client_api import webApiCollection as webApiCollection
BrowserViewSettings: Any

# base nao representavel no stub: Browser[...]
class BrowserView:
    __slots__: tuple
    __background_alpha__ = 1.0
    __appLoader: Any
    __settings: Any
    __closedByUser: Any
    __forceClosed: Any
    __savedBackAlpha: Any
    onBrowserObtained: Any
    def __init__(self, layoutID, settings):
        ...
    def onCloseView(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    @classmethod
    def __initSoundSpace(cls, soundSpaceID):
        ...
    def __onClose(self):
        ...
    def __setupBrowser(self):
        ...
    def __onBrowserObtained(self, _):
        ...

def makeSettings(url, webHandlers=None, isClosable=False, useSpecialKeys=False, allowRightClick=False, viewFlags=..., restoreBackground=False, waitingMessageID=..., disabledKeys=..., soundSpaceID=None, returnClb=None):
    ...
