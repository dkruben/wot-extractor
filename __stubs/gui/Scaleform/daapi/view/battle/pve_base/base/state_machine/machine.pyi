# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/base/state_machine/machine.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from frameworks_common.state_machine import StateMachine as StateMachine
from gui.Scaleform.daapi.view.battle.pve_base.base.state_machine.events import OneSecondEvent as OneSecondEvent, ToStateEvent as ToStateEvent
from gui.Scaleform.daapi.view.battle.pve_base.base.state_machine.states import BaseTimerState as BaseTimerState
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from frameworks_common.state_machine import StateEvent as StateEvent
STATE_TICK_INTERVAL = 1

class BaseStateMachine(StateMachine):
    def post(self, event):
        ...
    def postFinalState(self):
        ...
    def update(self):
        ...

class BaseTimerStateMachine(BaseStateMachine):
    __slots__: tuple
    _callbackDelayer: Any
    _lastTime: Any
    def __init__(self):
        ...
    def start(self, doValidate=True):
        ...
    def stop(self):
        ...
    def _tick(self):
        ...
