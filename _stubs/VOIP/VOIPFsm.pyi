# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/VOIP/VOIPFsm.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import viewitems as viewitems
import Event as Event
_logger: Any
_STATE = VOIP_FSM_STATE
_STATE_NAMES: dict

class VOIP_FSM_STATE(object):
    NONE = 0
    INITIALIZING = 1
    INITIALIZED = 2
    LOGGING_IN = 3
    LOGGED_IN = 4
    LOGGING_OUT = 5
    JOINING_CHANNEL = 6
    JOINED_CHANNEL = 7
    LEAVING_CHANNEL = 8

class VOIPFsm(object):
    __state: Any
    onStateChanged: Any
    def __init__(self):
        ...
    def getState(self):
        ...
    def __setState(self, newState):
        ...
    def inNoneState(self):
        ...
    def reset(self):
        ...
    def start(self):
        ...
    def update(self, voip):
        ...
