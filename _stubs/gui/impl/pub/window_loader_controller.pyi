# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/pub/window_loader_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from frameworks.wulf import WindowStatus as WindowStatus, WindowFlags as WindowFlags
from gui.Scaleform.Waiting import Waiting as Waiting
from helpers import dependency as dependency
from skeletons.gui.impl import IWindowLoaderController as IWindowLoaderController, IGuiLoader as IGuiLoader
_logger: Any

class WindowLoaderController(IWindowLoaderController):
    __slots__: tuple
    __gui: Any
    __loadingWindows: Any
    __isWaitingShown: Any
    __callbackID: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def __windowStatusChanged(self, uniqueID, newStatus):
        ...
    def __triggerWaiting(self):
        ...
    def __onDAAPIContentLoaded(self, window):
        ...
