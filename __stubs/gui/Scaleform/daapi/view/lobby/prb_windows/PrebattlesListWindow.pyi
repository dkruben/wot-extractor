# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/prb_windows/PrebattlesListWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView as AbstractWindowView
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from messenger.gui import events_dispatcher as events_dispatcher
from messenger.gui.Scaleform.view.lobby import MESSENGER_VIEW_ALIAS as MESSENGER_VIEW_ALIAS

class PrebattlesListWindow(AbstractWindowView, IGlobalListener):
    _name: Any
    isMinimising: Any
    def __init__(self, name):
        ...
    @property
    def chat(self):
        ...
    def onWindowClose(self):
        ...
    def onWindowMinimize(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _onUnregisterFlashComponent(self, viewPy, alias):
        ...
