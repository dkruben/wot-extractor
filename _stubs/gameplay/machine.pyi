# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gameplay/machine.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BattleReplay as BattleReplay
from constants import HAS_DEV_RESOURCES as HAS_DEV_RESOURCES
from frameworks_common.state_machine import StateMachine as StateMachine
from gameplay import states as states
from gameplay.observers import BlockingStateClearObserver as BlockingStateClearObserver
_logger: Any

class GameplayStateMachine(StateMachine):
    __slots__: tuple
    def start(self, doValidate=True):
        ...
    @property
    def offline(self):
        ...
    @property
    def online(self):
        ...
    def configure(self):
        ...

class BattleReplayMachine(StateMachine):
    __slots__: tuple
    def configure(self):
        ...

def create():
    ...
