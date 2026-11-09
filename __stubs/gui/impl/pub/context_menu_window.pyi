# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/pub/context_menu_window.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from frameworks.wulf import View as View, ViewFlags as ViewFlags, WindowFlags as WindowFlags, ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.ui_kit.context_menu_item_model import ContextMenuItemModel as ContextMenuItemModel
from gui.impl.gen.view_models.ui_kit.context_menu_sub_item_model import ContextMenuSubItemModel as ContextMenuSubItemModel
from gui.impl.gen.view_models.windows.context_menu_content_model import ContextMenuContentModel as ContextMenuContentModel
from gui.impl.pub.window_impl import WindowImpl as WindowImpl
from gui.impl.pub.window_view import WindowView as WindowView
_logger: Any

class ContextMenuContent(View):
    def __init__(self, layoutID=..., *args, **kwargs):
        ...
    @property
    def isGameface(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _addItem(self, actionID, label, icon=None, isEnabled=True):
        ...
    def _addSubItem(self, parentActionID, actionID, label, icon=None, isEnabled=True):
        ...
    def _updateItem(self, actionID, label=None, icon=None, isEnabled=True):
        ...
    def _addSeparator(self):
        ...
    def _initItems(self):
        ...
    def _onAction(self, actionID):
        ...
    def __onItemClicked(self, args=None):
        ...

class ContextMenuWindow(WindowImpl):
    __slots__: tuple
    def __init__(self, event, content, parent):
        ...
