# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/base/state_machine/transitions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from frameworks_common.state_machine import StringEventTransition as StringEventTransition, ConditionTransition as ConditionTransition, StateEvent as StateEvent
from gui.Scaleform.daapi.view.battle.pve_base.base.state_machine.events import OneSecondEvent as OneSecondEvent
from math_common import round_py2_style as round_py2_style
from enum import IntEnum as IntEnum
DEFAULT_STATE_DURATION = 4

class ToStateTransition(StringEventTransition):
    __slots__: tuple
    def __init__(self, widgetState, priority=3):
        ...

class PostponedTransition(ConditionTransition):
    __slots__: tuple
    _transitionDelay: Any
    _startCheckTransition: Any
    def __init__(self, delay=..., invert=False, priority=5):
        ...
    def execute(self, event):
        ...
    def _timerCondition(self, event):
        ...

class BaseTimerCondition(ConditionTransition):
    def __init__(self, invert=False, priority=4):
        ...
    def _condition(self, event, timerValue=0):
        ...

class CountdownTimerCondition(BaseTimerCondition):
    def _condition(self, event, timerValue=0):
        ...

class RegularTimerCondition(ConditionTransition):
    def __init__(self, invert=False, priority=4):
        ...
    def _condition(self, event, *_):
        ...
