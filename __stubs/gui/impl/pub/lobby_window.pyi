# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/pub/lobby_window.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from frameworks.wulf import Window as Window, WindowSettings as WindowSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer, WindowStatus as WindowStatus
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from frameworks.wulf import View as View
from typing import Optional as Optional
_logger: Any

class LobbyWindow(Window):
    __slots__: tuple
    __appLoader: Any
    __gui: Any
    def __init__(self, wndFlags, decorator=None, content=None, parent=None, layer=...):
        ...
    @classmethod
    def getInstances(cls):
        ...
    def _getParent(self, parent, content):
        ...
    @classmethod
    def __loadedWindowPredicate(cls, window):
        ...

class LobbyNotificationWindow(LobbyWindow):
    __slots__: tuple
    __appLoader: Any
    __initialParent: Any
    def __init__(self, wndFlags=None, decorator=None, content=None, parent=None, layer=...):
        ...
    def load(self):
        ...
    def _getParent(self, parent, content):
        ...
