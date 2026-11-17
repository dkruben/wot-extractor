# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/ChinaController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_process as adisp_process
from gui.Scaleform.locale.MENU import MENU as MENU
from helpers import dependency as dependency
from skeletons.gui.game_control import IBrowserController as IBrowserController, IChinaController as IChinaController, IGameSessionController as IGameSessionController

class NoChinaController(IChinaController):
    def showBrowser(self):
        ...

class ChinaController(IChinaController):
    gameSession: Any
    browser: Any
    __browserID: Any
    def __init__(self):
        ...
    def onDisconnected(self):
        ...
    # decorador original: @adisp_process
    def showBrowser(self):
        ...
    def __browserClosed(self, browserId):
        ...
