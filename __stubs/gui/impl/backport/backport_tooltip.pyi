# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/backport/backport_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from collections import namedtuple as namedtuple
from typing import TYPE_CHECKING as TYPE_CHECKING
from frameworks.wulf import ViewModel as ViewModel, Window as Window, WindowFlags as WindowFlags, ViewSettings as ViewSettings, PositionAnchor as PositionAnchor
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.impl.pub.window_view import WindowView as WindowView
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from typing import Optional as Optional, Iterable as Iterable, Any as Any
from frameworks.wulf import ViewEvent as ViewEvent
_STATE_TYPE_INFO = 'INFO'
TooltipData: _Any

class _BackportTooltipContent(ViewImpl):
    appLoader: _Any
    __slots__: tuple
    __tooltipData: _Any
    __mousePosX: _Any
    __mousePosY: _Any
    def __init__(self, tooltipData, event=None):
        ...
    def _onShown(self):
        ...
    def _onHidden(self):
        ...

class BackportTooltipWindow(WindowImpl):
    __slots__: tuple
    def __init__(self, tooltipData, parent, event=None):
        ...

class DecoratedTooltipWindow(WindowImpl):
    __slots__: tuple
    _posX: _Any
    _posY: _Any
    def __init__(self, content, parent=None, useDecorator=True, ownerViewID=None):
        ...
    def move(self, x, y, xAnchor=..., yAnchor=...):
        ...
    def _onReady(self):
        ...

def createTooltipData(tooltip=None, isSpecial=False, specialAlias=None, specialArgs=None, isWulfTooltip=False):
    ...
def createAndLoadBackportTooltipWindow(parentWindow, tooltip=None, isSpecial=False, tooltipId=None, specialArgs=None, isWulfTooltip=False):
    ...
def createBackportTooltipContent(specialAlias=None, specialArgs=None, isSpecial=True, tooltip=None, tooltipData=None, isWulfTooltip=False):
    ...
