# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/common/fade_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import Window as Window, View as View, WindowSettings as WindowSettings, ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowStatus as WindowStatus, PyResAccessor as PyResAccessor
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.fading_cover_view_model import FadingCoverViewModel as FadingCoverViewModel
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import IFadingController as IFadingController
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from wg_async import AsyncSemaphore as AsyncSemaphore, AsyncEvent as AsyncEvent
import logging as logging
import time as time
from functools import wraps as wraps
import BattleReplay as BattleReplay
import BigWorld as BigWorld
import adisp as adisp
from frameworks.wulf import WindowLayer as WindowLayer
from gui.shared import g_eventBus as g_eventBus, events as events
from helpers import dependency as dependency
from wg_async import wg_await as wg_await, wg_async as wg_async, BrokenPromiseError as BrokenPromiseError, await_callback as await_callback, forwardAsFuture as forwardAsFuture
from typing import Callable as Callable, Optional as Optional, Union as Union
_logger: Any
FADE_IN_DURATION = 0.15
FADE_OUT_DURATION = 0.4
BRING_TO_FRONT_FRAMES_COUNT = 2
WAIT_FOR_EVENT_TIMEOUT = 10.0

class ICover(object):
    __slots__: tuple
    def fadeOut(self, onComplete):
        ...
    def fadeIn(self, onComplete):
        ...

class DefaultFadingCover(View, ICover):
    __slots__: tuple
    _onComplete: Any
    def __init__(self, background=None, fadeInDuration=..., fadeOutDuration=...):
        ...
    @property
    def viewModel(self):
        ...
    def fadeOut(self, onComplete):
        ...
    def fadeIn(self, onComplete):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _fadingCompleteHandler(self):
        ...

class FadingCoverWindow(Window):
    __slots__: tuple
    _preloaded: Any
    def __init__(self, content, layer):
        ...
    def preload(self):
        ...
    @property
    def _cover(self):
        ...
    def fadeOut(self, callback):
        ...
    def fadeIn(self, callback):
        ...

class FadeManager(object):
    __slots__: tuple
    _gui: Any
    _appLoader: Any
    _layer: Any
    _coverFactory: Any
    _currentWindow: Any
    _isDestroyed: Any
    _semaphore: Any
    def __init__(self, layer, coverFactory=None):
        ...
    def __enter__(self):
        ...
    def __exit__(self, exceptionType, exceptionValue, exceptionTraceBack):
        ...
    def destroy(self):
        ...
    @property
    def isAnimating(self):
        ...
    # decorador original: @wg_async
    def show(self):
        ...
    # decorador original: @wg_async
    def hide(self):
        ...
    def hideImmediately(self):
        ...
    # decorador original: @wg_async
    def _doShow(self):
        ...
    # decorador original: @wg_async
    def _doHide(self):
        ...
    # decorador original: @wg_async
    def _transit(self, transition):
        ...
    def _windowStatusChanged(self, uniqueID, newStatus):
        ...
    def _bringToFront(self, framesLeft):
        ...

class AsyncEventWithTimout(AsyncEvent):
    _warning: Any
    _expireTime: Any
    _updateTimeoutID: Any
    def __init__(self, warning, state=False, scope=None):
        ...
    def wait(self):
        ...
    def set(self):
        ...
    def update(self):
        ...

class UseFading(object):
    __slots__: tuple
    _fadeManager: Any
    _hide: Any
    _show: Any
    _layer: Any
    _waitForLayoutReady: Any
    _currentFunctions: Any
    _callback: Any
    def __init__(self, show=True, hide=True, layer=..., waitForLayoutReady=None, callback=None):
        ...
    def __call__(self, func):
        ...

def dispatcherFadeWrapper(func, fadeCtx, *args, **kwargs):
    ...
