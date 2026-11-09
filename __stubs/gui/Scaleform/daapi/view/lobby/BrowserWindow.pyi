# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/BrowserWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.meta.BrowserWindowMeta import BrowserWindowMeta as BrowserWindowMeta
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from skeletons.gui.game_control import IBrowserController as IBrowserController

class BrowserWindow(BrowserWindowMeta):
    browserCtrl: Any
    __size: Any
    __browserID: Any
    __customTitle: Any
    __showActionBtn: Any
    __showWaiting: Any
    __showCloseBtn: Any
    __isSolidBorder: Any
    __alias: Any
    __handlers: Any
    def __init__(self, ctx=None):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def onWindowClose(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __handleBrowserClose(self, event):
        ...
