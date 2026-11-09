# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/state_machine/states/idle.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks_common.state_machine import StateFlags as StateFlags
import game_loading_bindings as game_loading_bindings
from gui.game_loading import loggers as loggers
from gui.game_loading.state_machine.states.base import BaseState as BaseState
from gui.game_loading.state_machine.const import GameLoadingStates as GameLoadingStates, LOADING_VIEW_FADE_OUT_DURATION as LOADING_VIEW_FADE_OUT_DURATION
_logger: Any

class IdleState(BaseState):
    __slots__: tuple
    def __init__(self, flags=...):
        ...
    def _onEntered(self, event):
        ...
