# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/browser_in_view_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from helpers import dependency as dependency
from gui.Scaleform.daapi.view.meta.BrowserInViewComponentMeta import BrowserInViewComponentMeta as BrowserInViewComponentMeta
from skeletons.gui.game_control import IBrowserController as IBrowserController

class BrowserInViewComponent(BrowserInViewComponentMeta):
    browserCtrl: Any
    __browserId: Any
    __url: Any
    __size: Any
    __browserViewCreated: Any
    def __init__(self):
        ...
    def viewSize(self, width, height):
        ...
    def setUrl(self, url):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    # decorador original: @adisp_process
    def __loadBrowser(self):
        ...
    def __showBrowser(self):
        ...
