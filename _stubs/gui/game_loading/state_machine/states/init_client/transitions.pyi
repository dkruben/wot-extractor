# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/state_machine/states/init_client/transitions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from frameworks_common.state_machine.transitions import StringEventTransition as StringEventTransition
from gui.game_loading.state_machine.const import GameLoadingStatesEvents as GameLoadingStatesEvents
from gui.game_loading.state_machine.states.transitions import SourceToSingleTargetTransition as SourceToSingleTargetTransition
from frameworks_common.state_machine.events import StringEvent as StringEvent
from gui.game_loading.state_machine.machine import GameLoadingStateMachine as GameLoadingStateMachine
from gui.game_loading.state_machine.states.init_client.logos_loading import LogosLoadingState as LogosLoadingState
from gui.game_loading.state_machine.states.init_client.client_loading_stub import ClientLoadingStubState as ClientLoadingStubState

class LogosShownToClientLoadingStubTransition(SourceToSingleTargetTransition):
    __slots__: tuple
    def __init__(self, priority=0):
        ...
    def _apply(self, event, source, target):
        ...
    def _condition(self, machine):
        ...

class LogosShownToClientLoadingTransition(LogosShownToClientLoadingStubTransition):
    __slots__: tuple
    def _condition(self, machine):
        ...

class ClientLoadingTransition(StringEventTransition):
    __slots__: tuple
    def __init__(self, priority=0):
        ...
