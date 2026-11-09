# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/state_machine/states/init_client/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks_common.state_machine import StateFlags as StateFlags
from gui.game_loading import loggers as loggers
from gui.game_loading.state_machine.const import GameLoadingStates as GameLoadingStates
from gui.game_loading.state_machine.states.base import BaseGroupTickingStates as BaseGroupTickingStates
from gui.game_loading.state_machine.states.init_client.client_loading import ClientLoadingState as ClientLoadingState, ClientLoadingSlideState as ClientLoadingSlideState
from gui.game_loading.state_machine.states.init_client.client_loading_stub import ClientLoadingStubState as ClientLoadingStubState
from gui.game_loading.state_machine.states.init_client.logos_loading import LogosLoadingState as LogosLoadingState
from gui.game_loading.state_machine.states.init_client.transitions import LogosShownToClientLoadingStubTransition as LogosShownToClientLoadingStubTransition, LogosShownToClientLoadingTransition as LogosShownToClientLoadingTransition, ClientLoadingTransition as ClientLoadingTransition
from frameworks_common.state_machine.transitions import BaseTransition as BaseTransition
from gui.game_loading.resources.cdn.images import CdnImagesResources as CdnImagesResources
from gui.game_loading.preferences import GameLoadingPreferences as GameLoadingPreferences
from gui.game_loading.resources.local.base import LocalResources as LocalResources
from gui.game_loading.state_machine.states.base import BaseState as BaseState
from gui.game_loading.state_machine.models import ProgressSettingsModel as PSM, ImageViewSettingsModel as ImageViewSettingsModel
_logger: Any

class ClientInitState(BaseGroupTickingStates):
    __slots__: tuple
    def __init__(self):
        ...
    def configure(self, preferences, logos, clientLoadingImages, milestonesSettings, clientLoadingProgressSetting, clientLoadingViewSettings):
        ...
    def addTransitionToGroupState(self, transitionFactory, target=None):
        ...
    @property
    def _logosLoadingState(self):
        ...
    @property
    def _clientLoadingState(self):
        ...
    @property
    def _clientLoadingStubState(self):
        ...
