# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/pub/view_impl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
import typing as typing
from frameworks.wulf import View as View, ViewEvent as ViewEvent, ViewModel as ViewModel, Window as Window, WindowLayer as WindowLayer, WindowStatus as WindowStatus
from gui.impl.gen import R as R
from gui.impl.pub import SimpleToolTipWindow as SimpleToolTipWindow, ToolTipWindow as ToolTipWindow, PopOverWindow as PopOverWindow, ContextMenuContent as ContextMenuContent, ContextMenuWindow as ContextMenuWindow, AdvancedToolTipWindow as AdvancedToolTipWindow
from gui.impl.pub.view_impl_helpers import createWulfTooltipWindow as createWulfTooltipWindow, createParamTooltipWindow as createParamTooltipWindow, createBackportContextMenuWindow as createBackportContextMenuWindow
from helpers import dependency as dependency
from helpers.events_handler import EventsHandler as EventsHandler
from py2to3 import patched_typing as patched_typing
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from soft_exception import SoftException as SoftException
TViewModel: Any
_logger: Any
_BACKPORT_POPOVER_DIRECTION_OVERRIDE: dict

# base nao representavel no stub: patched_typing.Generic[...]
class ViewImpl(View, EventsHandler):
    __slots__: tuple
    gui: Any
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def createPopOverContent(self, event):
        ...
    def createContextMenuContent(self, event):
        ...
    def prepareBackportTooltipArgs(self, args):
        ...
    def prepareBackportPopOverArgs(self, args):
        ...
    def createToolTip(self, event):
        ...
    def createPopOver(self, event):
        ...
    def createContextMenu(self, event):
        ...
    def _getPopOverLayer(self):
        ...
    def __createSpecialTooltipContentWindow(self, event, parentWindow):
        ...
    def __createAdvancedTooltipContentWindow(self, event, parentWindow):
        ...
    def __createBackportPopOverContent(self, event):
        ...

class PopOverViewImpl(ViewImpl):
    __slots__: tuple
    @property
    def isCloseBtnVisible(self):
        ...
