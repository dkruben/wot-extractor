# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/state_machine/states/init_client/client_loading.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import game_loading_bindings as game_loading_bindings
from frameworks_common.state_machine import StateFlags as StateFlags
from gui.game_loading import loggers as loggers
from gui.game_loading.state_machine.const import GameLoadingStates as GameLoadingStates, TickingMode as TickingMode
from gui.game_loading.state_machine.models import ImageViewSettingsModel as ImageViewSettingsModel
from gui.game_loading.state_machine.states.base import BaseGroupTickingStates as BaseGroupTickingStates
from gui.game_loading.state_machine.states.components.progress_bar import ProgressBarStateComponent as ProgressBarStateComponent
from gui.game_loading.state_machine.states.components.status_text import MilestoneStatusTextStateComponent as MilestoneStatusTextStateComponent
from gui.game_loading.state_machine.states.slide import SlideState as SlideState
from gui.game_loading.resources.cdn.images import CdnImagesResources as CdnImagesResources
from gui.game_loading.preferences import GameLoadingPreferences as GameLoadingPreferences
from gui.game_loading.state_machine.models import ProgressSettingsModel as PSM
_logger: Any

class ClientLoadingSlideState(SlideState):
    __slots__: tuple
    def __init__(self, images, viewSettings):
        ...

class ClientLoadingProgressStateComponent(ProgressBarStateComponent):
    __slots__: tuple
    _stepsBegin: Any
    _ticks: Any
    def __init__(self, preferences, progressSettings):
        ...
    def _increaseTicks(self):
        ...
    def _increaseProgress(self):
        ...

class ClientLoadingStatusTextStateComponent(MilestoneStatusTextStateComponent):
    __slots__: tuple
    def __init__(self, milestonesSettings):
        ...

class ClientLoadingState(BaseGroupTickingStates):
    __slots__: tuple
    def __init__(self):
        ...
    @property
    def mainState(self):
        ...
    def configure(self, preferences, images, milestonesSettings, progressSetting, viewSettings):
        ...
    def _onEntered(self, event):
        ...
