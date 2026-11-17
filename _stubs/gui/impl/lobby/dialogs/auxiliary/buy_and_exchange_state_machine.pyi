# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dialogs/auxiliary/buy_and_exchange_state_machine.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import weakref as weakref
import typing as typing
from enum import Enum as Enum
from frameworks_common.state_machine import State as State, StateFlags as StateFlags, StateMachine as StateMachine, StringEventTransition as StringEventTransition, StringEvent as StringEvent, StateIdsObserver as StateIdsObserver
_logger: Any

class BuyAndExchangeStateEnum(Enum):
    BUY_CONTENT = 'buyContent'
    NEED_EXCHANGE = 'needExchange'
    EXCHANGE_CONTENT = 'exchangeContent'
    EXCHANGE_IN_PROCESS = 'exchangeInProcess'
    BUY_NOT_REQUIRED = 'buyNotRequired'
    EXCHANGE_NOT_REQUIRED = 'exchangeNotRequired'
    CAN_NOT_BUY = 'canNotBuy'
    GOLD_NOT_ENOUGH = 'goldNotEnough'

class BuyAndExchangeEventEnum(Enum):
    ACCEPT_CLICKED = 'acceptClicked'
    NEED_EXCHANGE = 'needExchange'
    START_EXCHANGE = 'startExchange'
    EXCHANGE_COMPLETED = 'exchangeCompleted'
    EXCHANGE_VALIDATION_ERROR = 'exchangeValidationError'
    CAN_BUY = 'canBuy'
    CAN_NOT_BUY = 'canNotBuy'

class BuyAndExchangeStateObserver(StateIdsObserver):
    __slots__: tuple
    __proxy: Any
    __currentState: Any
    def __init__(self, handler, startState):
        ...
    def getCurrentState(self):
        ...
    def onStateChanged(self, state, stateEntered, event=None):
        ...

class BuyAndExchangeStateMachine(object):
    __stateMachine: Any
    __initState: Any
    __observer: Any
    __stateToContentMap: Any
    def __init__(self, handler, stateToContent, startState=None):
        ...
    def run(self):
        ...
    def stop(self):
        ...
    def getCurrentState(self):
        ...
    def isCurrentState(self, state):
        ...
    def getCurrentContentType(self):
        ...
    def transit(self, event, condition=...):
        ...
    def _configuredStates(self, startState):
        ...
