# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/pub/tooltip_window.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from past.builtins import basestring as basestring
from frameworks.wulf import WindowFlags as WindowFlags, View as View, ViewSettings as ViewSettings, PositionAnchor as PositionAnchor
from gui.impl.gen import R as R
from gui.impl.gen.view_models.windows.advanced_animated_tooltip_content_model import AdvancedAnimatedTooltipContentModel as AdvancedAnimatedTooltipContentModel
from gui.impl.gen.view_models.windows.advanced_tooltip_content_model import AdvancedTooltipContentModel as AdvancedTooltipContentModel
from gui.impl.gen.view_models.windows.simple_tooltip_content_model import SimpleTooltipContentModel as SimpleTooltipContentModel
from gui.impl.pub.window_impl import WindowImpl as WindowImpl
from gui.impl.pub.window_view import WindowView as WindowView
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from typing import Optional as Optional
from frameworks.wulf import ViewEvent as ViewEvent, Window as Window

class ToolTipWindow(WindowImpl):
    __slots__: tuple
    _posX: Any
    _posY: Any
    def __init__(self, event, content, parent):
        ...
    def move(self, x, y, xAnchor=..., yAnchor=...):
        ...
    def _onReady(self):
        ...

class SimpleToolTipWindow(ToolTipWindow):
    __slots__: tuple
    __gui: Any
    def __init__(self, event, parent):
        ...
    @classmethod
    def makeString(cls, value):
        ...

class SimpleTooltipContent(View):
    __slots__: tuple
    def __init__(self, contentID, header='', body='', note='', alert=''):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, header, body, note, alert):
        ...

class AdvancedToolTipWindow(ToolTipWindow):
    __slots__: tuple
    def __init__(self, event, parent, normalContent, advancedContent):
        ...

class AdvancedTooltipContent(View):
    __settingsCore: Any
    __slots__: tuple
    def __init__(self, normalContent, advancedContent):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, normalContent, advancedContent):
        ...
    def _getDisableAnimFlag(self):
        ...
    def _setDisableAnimFlag(self):
        ...

class AdvancedAnimatedTooltipContent(View):
    __slots__: tuple
    def __init__(self, header='', body='', animation=''):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, header, body, animation):
        ...
