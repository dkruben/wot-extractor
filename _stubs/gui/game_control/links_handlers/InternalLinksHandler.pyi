# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/links_handlers/InternalLinksHandler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import iteritems as iteritems
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from debug_utils import LOG_ERROR as LOG_ERROR
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.game_control.links import URLMacros as URLMacros
from gui.shared import g_eventBus as g_eventBus
from helpers import dependency as dependency
from skeletons.gui.game_control import IInternalLinksController as IInternalLinksController, IBrowserController as IBrowserController
_LISTENERS: dict

class InternalLinksHandler(IInternalLinksController):
    browserCtrl: Any
    __urlMacros: Any
    _browserID: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def getURL(self, name, callback):
        ...
    # decorador original: @adisp_process
    def __openInternalBrowse(self, urlName, title='', browserSize=None, showActionBtn=True, showCloseBtn=False):
        ...
