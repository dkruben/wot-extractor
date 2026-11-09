# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/state_machine/states/transitions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks_common.state_machine.transitions import StringEventTransition as StringEventTransition
from gui.game_loading import loggers as loggers
from gui.game_loading.resources.cdn.models import LocalSlideModel as LocalSlideModel
from gui.game_loading.state_machine.const import GameLoadingStatesEvents as GameLoadingStatesEvents
from frameworks_common.state_machine.events import StringEvent as StringEvent
from gui.game_loading.state_machine.states.base import BaseState as BaseState
from gui.game_loading.state_machine.states.login_screen import LoginScreenState as LoginScreenState
from gui.game_loading.state_machine.states.player_loading import PlayerLoadingState as PlayerLoadingState
from gui.game_loading.state_machine.states.init_client.logos_loading import LogosLoadingState as LogosLoadingState
from gui.game_loading.state_machine.states.init_client.client_loading import ClientLoadingSlideState as ClientLoadingSlideState
from gui.game_loading.state_machine.states.init_client.client_loading_stub import ClientLoadingStubState as ClientLoadingStubState
_ClientInitStates: Any
_logger: Any

class SourceToSingleTargetTransition(StringEventTransition):
    __slots__: tuple
    def execute(self, event):
        ...
    def _apply(self, event, source, target):
        ...

class LoginScreenTransition(SourceToSingleTargetTransition):
    __slots__: tuple
    def __init__(self, priority=0):
        ...

class LoginScreenTransitionWithLastShownImage(LoginScreenTransition):
    __slots__: tuple
    def _apply(self, event, source, target):
        ...

class PlayerLoadingTransition(SourceToSingleTargetTransition):
    __slots__: tuple
    def __init__(self, priority=0):
        ...

class PlayerLoadingTransitionWithLastShownImage(PlayerLoadingTransition):
    __slots__: tuple
    def _apply(self, event, source, target):
        ...
    def _getMinShowTime(self, source, image):
        ...

class ClientInitToPlayerLoadingTransition(PlayerLoadingTransitionWithLastShownImage):
    __slots__: tuple
    def _getMinShowTime(self, source, image):
        ...

class LoginScreenToPlayerLoadingTransition(PlayerLoadingTransitionWithLastShownImage):
    __slots__: tuple
    def _getMinShowTime(self, source, image):
        ...

class IdleTransition(StringEventTransition):
    __slots__: tuple
    def __init__(self, priority=0):
        ...
