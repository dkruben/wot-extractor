# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/state_machine/states/init_client/client_loading_stub.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
import game_loading_bindings as game_loading_bindings
from shared_utils import safeCancelCallback as safeCancelCallback
from helpers.time_utils import MS_IN_SECOND as MS_IN_SECOND
from gui.game_loading import loggers as loggers
from gui.game_loading.state_machine.const import GameLoadingStates as GameLoadingStates
from gui.game_loading.state_machine.models import ImageViewSettingsModel as ImageViewSettingsModel
from gui.game_loading.state_machine.states.slide import StaticSlideState as StaticSlideState
from gui.game_loading.resources.cdn.images import CdnImagesResources as CdnImagesResources
_logger: Any

class ClientLoadingStubState(StaticSlideState):
    __slots__: tuple
    _minDurationTimerId: Any
    def __init__(self, images):
        ...
    def clear(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _fireMinimumDurationEvent(self):
        ...
    def _cancelMinDurationTimer(self):
        ...
