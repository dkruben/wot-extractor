# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/pub/window_impl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from frameworks.wulf import PositionAnchor as PositionAnchor, WindowLayer as WindowLayer
from frameworks.wulf import Window as Window, WindowSettings as WindowSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.windows.window_model import WindowModel as WindowModel
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from frameworks.wulf import WindowsArea as WindowsArea
_logger: Any

class WindowImpl(Window):
    __slots__: tuple
    gui: Any
    def __init__(self, wndFlags, *args, **kwargs):
        ...
    @property
    def windowModel(self):
        ...
    @property
    def area(self):
        ...
    def move(self, x, y, xAnchor=..., yAnchor=...):
        ...
    def center(self):
        ...
    def cascade(self):
        ...
    def _onDecoratorReady(self):
        ...
    def _onDecoratorReleased(self):
        ...
    def _onClosed(self, _=None):
        ...
    def _onMinimize(self, _=None):
        ...
