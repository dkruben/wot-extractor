# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/state_machine/states/player_loading.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
import game_loading_bindings as game_loading_bindings
from frameworks_common.state_machine import StateFlags as StateFlags
from gui.game_loading.preferences import GameLoadingPreferences as GameLoadingPreferences
from gui.game_loading.state_machine.const import GameLoadingStates as GameLoadingStates, MINIMUM_PLAYER_LOADING_PROGRESS_BAR_MAX_VALUE as MINIMUM_PLAYER_LOADING_PROGRESS_BAR_MAX_VALUE
from gui.game_loading.state_machine.const import TickingMode as TickingMode
from gui.game_loading.state_machine.models import ImageViewSettingsModel as ImageViewSettingsModel
from gui.game_loading.state_machine.states.base import BaseGroupTickingStates as BaseGroupTickingStates
from gui.game_loading.state_machine.states.components.progress_bar import MilestoneProgressBarStateComponent as MilestoneProgressBarStateComponent
from gui.game_loading.state_machine.states.components.status_text import MilestoneStatusTextStateComponent as MilestoneStatusTextStateComponent
from gui.game_loading.state_machine.states.slide import SlideState as SlideState
from gui.game_loading.resources.cdn.images import CdnImagesResources as CdnImagesResources
from gui.game_loading.state_machine.models import ProgressSettingsModel as PSM

class PlayerLoadingSlideState(SlideState):
    __slots__: tuple
    def __init__(self, images, viewSettings):
        ...

class PlayerLoadingMilestoneProgressStateComponent(MilestoneProgressBarStateComponent):
    __slots__: tuple
    def __init__(self, preferences, settings, milestonesSettings):
        ...
    def _saveProgressMax(self, progressMax):
        ...

class PlayerLoadingStatusTextStateComponent(MilestoneStatusTextStateComponent):
    __slots__: tuple
    def __init__(self, milestonesSettings):
        ...

class PlayerLoadingState(BaseGroupTickingStates):
    __slots__: tuple
    def __init__(self):
        ...
    @property
    def mainState(self):
        ...
    @property
    def progressState(self):
        ...
    @property
    def statusTextState(self):
        ...
    def configure(self, preferences, images, progressSetting, milestonesSettings, viewSettings):
        ...
    def setRetainMilestones(self, value):
        ...
    def _onEntered(self, event):
        ...
