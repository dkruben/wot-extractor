# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/framework/entities/sf_window.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import weakref as weakref
import Event as Event
from frameworks.wulf import Window as Window, WindowFlags as WindowFlags, WindowSettings as WindowSettings, WindowStatus as WindowStatus
from frameworks.wulf.gui_constants import ShowingStatus as ShowingStatus
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events, g_eventBus as g_eventBus
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from soft_exception import SoftException as SoftException
from wg_async import AsyncReturn as AsyncReturn, wg_async as wg_async, wg_await as wg_await
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.framework.entities.View import View as View
_logger: Any

class SFWindow(Window):
    __guiLoader: Any
    __slots__: tuple
    args: Any
    kwargs: Any
    onContentLoaded: Any
    __loadParams: Any
    __view: Any
    __scope: Any
    __fireEvent: Any
    isReady: Any
    def __init__(self, loadParams, scope=..., fireEvent=True, *args, **kwargs):
        ...
    def __repr__(self):
        ...
    def getName(self):
        ...
    @property
    def loadParams(self):
        ...
    @property
    def content(self):
        ...
    @property
    def windowStatus(self):
        ...
    @property
    def showingStatus(self):
        ...
    def isParamsEqual(self, loadParams, scope=..., fireEvent=True, *args, **kwargs):
        ...
    def load(self):
        ...
    def setContent(self, view):
        ...
    def setViewLoaded(self):
        ...
    # decorador original: @wg_async
    def wait(self):
        ...
    def _finalize(self):
        ...
    def __onViewDispose(self, _):
        ...
