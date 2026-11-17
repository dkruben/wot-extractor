# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/prebattle_highlights/sub_systems/pbh_window_handler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import Windowing as Windowing
from frameworks.wulf import WindowLayer as WindowLayer
from gui.battle_control.controllers.prebattle_highlights.sub_systems.base_sub_system import BasePbhSubSystem as BasePbhSubSystem
from gui.impl.battle.prebattle_highlights.utils import getPrebattleHighlightsWindow as getPrebattleHighlightsWindow
from gui.impl.common.fade_manager import FadeManager as FadeManager, FadingCoverWindow as FadingCoverWindow, DefaultFadingCover as DefaultFadingCover
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent
from uilogging.prebattle_highlights.loggers import PrebattleHighlightsEventLogger as PrebattleHighlightsEventLogger
from wg_async import await_callback as await_callback, wg_async as wg_async
from typing import Optional as Optional, Callable as Callable
from gui.impl.common.fade_manager import ICover as ICover
_logger: Any

class _PreloadedFadeManager(FadeManager):
    _preloaded: Any
    _currentWindow: Any
    def __init__(self, layer, coverFactory=None):
        ...
    def preload(self):
        ...
    def hideImmediately(self):
        ...
    # decorador original: @wg_async
    def _doShow(self):
        ...

class PbhWindowHandler(BasePbhSubSystem):
    __window: Any
    __windowReady: Any
    __inFade: Any
    __fadeManager: Any
    __uiLogger: Any
    def __init__(self, readyCallback):
        ...
    def subscribe(self):
        ...
    def unsubscribe(self):
        ...
    def isReady(self):
        ...
    @property
    def inFade(self):
        ...
    def startFlow(self):
        ...
    def stopFlow(self):
        ...
    def clear(self):
        ...
    def preload(self):
        ...
    def forceStopFlow(self):
        ...
    # decorador original: @wg_async
    def toggleFadeManager(self, value):
        ...
    def __handleBattleLoading(self, event):
        ...
    def __preload(self):
        ...
    def __onPBHWindowReady(self):
        ...
    def __onWindowAccessibilityChanged(self, isAccessible):
        ...
