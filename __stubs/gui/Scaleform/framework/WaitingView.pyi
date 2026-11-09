# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/framework/WaitingView.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Keys as Keys
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from gui import InputHandler as InputHandler
from gui.Scaleform.daapi.view.meta.WaitingViewMeta import WaitingViewMeta as WaitingViewMeta
from gui.impl import backport as backport
from skeletons.gui.app_loader import IWaitingWidget as IWaitingWidget

class WaitingView(WaitingViewMeta, IWaitingWidget):
    __callback: Any
    def __init__(self, **kwargs):
        ...
    def handleKeyUpEvent(self, event):
        ...
    def destroy(self):
        ...
    def setCallback(self, callback=None):
        ...
    def cancelCallback(self):
        ...
    def showWaiting(self, messageID, softStart=False, showBg=True):
        ...
    def hideWaiting(self):
        ...
    def setBackgroundImage(self, image):
        ...
