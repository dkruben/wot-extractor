# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/components/browser_view_page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from gui.impl import backport as backport
from gui.impl.gen import R as R
from adisp import adisp_process as adisp_process
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.meta.BrowserViewStackExPaddingMeta import BrowserViewStackExPaddingMeta as BrowserViewStackExPaddingMeta
from helpers import dependency as dependency
from skeletons.gui.game_control import IBrowserController as IBrowserController
_logger: Any

class BrowserPageComponent(BrowserViewStackExPaddingMeta):
    browserCtrl: Any
    _wasError: Any
    __browserId: Any
    __url: Any
    __size: Any
    __browserViewCreated: Any
    def __init__(self):
        ...
    def setViewSize(self, width, height):
        ...
    def invalidateUrl(self):
        ...
    def refreshUrl(self):
        ...
    def _populate(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _onUnregisterFlashComponent(self, viewPy, alias):
        ...
    def _onError(self):
        ...
    @classmethod
    def _isRightClickAllowed(cls):
        ...
    def _getWebHandlers(self):
        ...
    def _getUrl(self):
        ...
    def __initializeBrowser(self):
        ...
    # decorador original: @adisp_process
    def __createBrowser(self):
        ...
    def __showBrowser(self):
        ...
