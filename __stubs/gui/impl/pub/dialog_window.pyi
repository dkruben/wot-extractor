# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/pub/dialog_window.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
from wg_async import wg_async as wg_async, wg_await as wg_await, AsyncEvent as AsyncEvent, AsyncReturn as AsyncReturn, AsyncScope as AsyncScope, BrokenPromiseError as BrokenPromiseError
from frameworks.wulf import ViewFlags as ViewFlags, WindowSettings as WindowSettings, ViewSettings as ViewSettings
from frameworks.wulf import WindowFlags as WindowFlags, Window as Window
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from gui.impl.gen import R as R
from gui.impl.gen.view_models.ui_kit.dialog_button_model import DialogButtonModel as DialogButtonModel
from gui.impl.gen.view_models.windows.dialog_window_model import DialogWindowModel as DialogWindowModel
from gui.impl.pub.view_impl import ViewImpl as ViewImpl
from helpers import dependency as dependency
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.gui.impl import IGuiLoader as IGuiLoader
_logger: Any
DialogResult: Any
SingleDialogResult: Any

class DialogButtons(CONST_CONTAINER):
    SUBMIT = DialogButtonModel.BTN_SUBMIT
    CANCEL = DialogButtonModel.BTN_CANCEL
    PURCHASE = DialogButtonModel.BTN_PURCHASE
    RESEARCH = DialogButtonModel.BTN_RESEARCH
    ALL: tuple
    ACCEPT_BUTTONS: tuple

class DialogFlags(CONST_CONTAINER):
    WINDOW = WindowFlags.WINDOW
    TOP_WINDOW = WindowFlags.DIALOG
    TOP_FULLSCREEN_WINDOW: Any

class DialogContent(ViewImpl):
    __slots__: tuple

class DialogDecorator(ViewImpl):
    __slots__: tuple
    def __init__(self, balanceContent=None, bottomContent=None):
        ...
    @property
    def balanceContent(self):
        ...
    @property
    def bottomContent(self):
        ...
    def _onLoading(self, balanceContent, bottomContent):
        ...

class DialogWindow(Window):
    gui: Any
    __slots__: tuple
    __scope: Any
    __event: Any
    __result: Any
    __blur: Any
    __buttonToFocus: Any
    __focusInited: Any
    def __init__(self, content=None, bottomContent=None, parent=None, balanceContent=None, enableBlur=True, flags=...):
        ...
    # decorador original: @wg_async
    def wait(self):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def contentViewModel(self):
        ...
    @property
    def bottomContentViewModel(self):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...
    def _onClosed(self, _=None):
        ...
    def _removeAllButtons(self):
        ...
    def _addButton(self, name, label=..., isFocused=False, invalidateAll=False, isEnabled=True, soundDown=None, rawLabel='', tooltipHeader=..., tooltipBody=...):
        ...
    def _getButton(self, name):
        ...
    def _onButtonClick(self, item):
        ...
    def _setBackgroundImage(self, value):
        ...
    def _setIconHighlight(self, value):
        ...
    def _setAnimationHighlight(self, value):
        ...
    def _setPreset(self, value):
        ...
    def _setShowSoundId(self, value):
        ...
    def _setButtonEnabled(self, buttonName, value):
        ...
    def _getResultData(self):
        ...
    def _onFocus(self, focused):
        ...

class DialogViewMixin(object):
    __slots__: tuple
    __scope: Any
    __event: Any
    __result: Any
    def __init__(self, *args, **kwargs):
        ...
    # decorador original: @wg_async
    def wait(self):
        ...
    def _sendDialogResult(self, result):
        ...
    def _getAdditionalData(self):
        ...
    def _dispose(self):
        ...
