# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/state_machine/states/components/progress_bar.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks_common.state_machine import StateFlags as StateFlags
import game_loading_bindings as game_loading_bindings
from gui.game_loading import loggers as loggers
from gui.game_loading.state_machine.const import TickingMode as TickingMode
from gui.game_loading.state_machine.states.base import BaseTickingState as BaseTickingState
from gui.game_loading.state_machine.states.handlers.milestones import ProgressBarMilestonesHandler as ProgressBarMilestonesHandler
from frameworks_common.state_machine import StateEvent as StateEvent
from gui.game_loading.preferences import GameLoadingPreferences as GameLoadingPreferences
from gui.game_loading.state_machine.models import ProgressSettingsModel as ProgressSettingsModel, LoadingMilestoneModel as LoadingMilestoneModel
_logger: Any

class ProgressBarStateComponent(BaseTickingState):
    __slots__: tuple
    _settings: Any
    _preferences: Any
    _progressMax: Any
    _progress: Any
    _progressLimit: Any
    _ticks: Any
    def __init__(self, stateID, settings, preferences=None, flags=..., tickingMode=..., onCompleteEvent=None):
        ...
    def _onExited(self):
        ...
    def _saveProgressMax(self, progressMax):
        ...
    def _setInitialProgress(self):
        ...
    def _task(self):
        ...
    def _increaseTicks(self):
        ...
    def _increaseProgress(self):
        ...
    def _isLimitReached(self):
        ...
    def _setProgress(self, progress):
        ...
    def _calcProgress(self, percent):
        ...
    def _calcProgressMax(self, ticks):
        ...

class MilestoneProgressBarStateComponent(ProgressBarStateComponent):
    __slots__: tuple
    _milestone: Any
    _milestonesHandler: Any
    _retainMilestones: Any
    def __init__(self, settings, preferences, milestonesSettings, stateID, flags=..., tickingMode=..., onCompleteEvent=None):
        ...
    def setRetainMilestones(self, value):
        ...
    def _start(self):
        ...
    def _stop(self):
        ...
    def _onMilestoneReached(self, newMilestone):
        ...
    def _onMilestoneTypeChanged(self, newMilestone):
        ...
    def _getMilestoneLimit(self):
        ...
    def _isLimitReached(self):
        ...
