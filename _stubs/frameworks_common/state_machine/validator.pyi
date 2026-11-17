# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/frameworks_common/state_machine/validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from . import states as _states
from . import visitor as visitor
from .exceptions import StateMachineError as StateMachineError
from .transitions import BaseTransition as BaseTransition
from . import StateMachine as StateMachine

def _validateTransition(transition, upper=None):
    ...
def _validateInitialState(state):
    ...
def _validateState(state, machine):
    ...
def validate(machine):
    ...
