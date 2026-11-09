# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/uilogging/story_mode/loggers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import typing as typing
from gui.game_loading import loading as gameLoading
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from story_mode.uilogging.story_mode.consts import Features as Features, LogActions as LogActions, LogWindows as LogWindows, LogButtons as LogButtons, LogBattleResultStats as LogBattleResultStats, TOOLTIP_MIN_VIEW_TIME as TOOLTIP_MIN_VIEW_TIME
from uilogging.base.logger import MetricsLogger as MetricsLogger
from wotdecorators import noexcept as noexcept
from uilogging.types import ItemType as ItemType, ItemStateType as ItemStateType, InfoType as InfoType

class BaseMetricsLogger(MetricsLogger):
    __slots__: tuple
    _storyModeCtrl: Any
    _item: Any
    def __init__(self, item):
        ...

class WindowLogger(BaseMetricsLogger):
    __slots__: tuple
    _isOpened: Any
    def __init__(self, item):
        ...
    def logOpen(self, state=None, info=None):
        ...
    def logClose(self, state=None):
        ...
    def logButtonShown(self, button, once=False, state=None):
        ...
    def logClick(self, button, state=None):
        ...

class WindowBehindGameLoadingLogger(WindowLogger):
    __slots__: tuple
    # decorador original: @noexcept
    def logGameLoadingClose(self):
        ...

class MissionWindowLogger(WindowLogger):
    __slots__: tuple
    # decorador original: @noexcept
    def logOpen(self, missionId=None, info=None):
        ...

class PostBattleWindowLogger(MissionWindowLogger):
    __slots__: tuple
    def __init__(self):
        ...
    # decorador original: @noexcept
    def logOpen(self, missionId=None, win=False):
        ...

class SelectMissionWindow(MissionWindowLogger):
    __slots__: tuple
    def __init__(self):
        ...
    # decorador original: @noexcept
    def logMissionSelectClick(self, missionId):
        ...
    # decorador original: @noexcept
    def logAutoSelect(self, missionId):
        ...
    # decorador original: @noexcept
    def logTabChanged(self, missionId):
        ...

class SelectorCardLogger(BaseMetricsLogger):
    __slots__: tuple
    def __init__(self):
        ...
    # decorador original: @noexcept
    def logSelfClick(self):
        ...
    # decorador original: @noexcept
    def logInfoClick(self):
        ...

class BaseVideoLogger(WindowLogger):
    __slots__: tuple
    def logVideoStarted(self, missionId):
        ...

class IntroVideoLogger(BaseVideoLogger):
    __slots__: tuple
    def __init__(self):
        ...

class OutroVideoLogger(BaseVideoLogger):
    __slots__: tuple
    def __init__(self):
        ...

class EntryPointLogger(MetricsLogger):
    __slots__: tuple
    def __init__(self):
        ...
    # decorador original: @noexcept
    def logClick(self):
        ...

class NewbieEntryPointLogger(MetricsLogger):
    __slots__: tuple
    def __init__(self):
        ...
    # decorador original: @noexcept
    def logClick(self):
        ...

class EventEntryPointTooltipLogger(BaseMetricsLogger):
    __slots__: tuple
    def __init__(self):
        ...
    def start(self):
        ...
    # decorador original: @noexcept
    def stop(self):
        ...

class NewbieEntryPointTooltipLogger(BaseMetricsLogger):
    __slots__: tuple
    def __init__(self):
        ...
    def start(self):
        ...
    # decorador original: @noexcept
    def stop(self):
        ...

class NewbieAdvertisingViewLogger(WindowLogger):
    __slots__: tuple
    def __init__(self):
        ...

class EventWelcomeViewLogger(WindowLogger):
    __slots__: tuple
    def __init__(self):
        ...

class TasksCompletedWarningLogger(WindowLogger):
    __slots__: tuple
    def __init__(self):
        ...

def _getBattlesInfo():
    ...
