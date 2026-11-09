# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/primary_objective/state_machine/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import enum as enum
from frameworks_common.state_machine import StateFlags as StateFlags
from gui.Scaleform.daapi.view.battle.pve_base.base.state_machine.states import BaseTimerState as BaseTimerState, BaseState as BaseState
from math_common import round_py2_style as round_py2_style
from pve_battle_hud import PrimaryObjectiveState as PrimaryObjectiveState, getPveHudLogger as getPveHudLogger
_logger: Any

class TimerState(enum.IntEnum):
    SMALL = 0
    BIG = 1
    NO_TIMER = 2

class InitialState(BaseState):
    __slots__: tuple
    def __init__(self):
        ...

class BaseViewTimerState(BaseTimerState):
    __slots__: tuple
    def tick(self, currentTime):
        ...
    @property
    def _subheader(self):
        ...

class AppearanceState(BaseViewTimerState):
    __slots__: tuple
    def __init__(self):
        ...
    def _showView(self):
        ...
    def _updateView(self):
        ...

class RegularState(BaseViewTimerState):
    __slots__: tuple
    def __init__(self):
        ...
    def _showView(self):
        ...
    def _updateView(self):
        ...

class RemindState(BaseViewTimerState):
    __slots__: tuple
    def __init__(self, stateID=..., flags=...):
        ...
    def _showView(self):
        ...
    def _updateView(self):
        ...

class LastRemindState(RemindState):
    __slots__: tuple
    def __init__(self):
        ...

class LargeTimerState(BaseViewTimerState):
    __slots__: tuple
    def __init__(self):
        ...
    def _showView(self):
        ...
    def _updateView(self):
        ...

class CountdownState(BaseViewTimerState):
    __slots__: tuple
    def __init__(self):
        ...
    def tick(self, currentTime):
        ...
    def _showView(self):
        ...
    def _updateView(self):
        ...
    def _onExited(self):
        ...

class SuccessState(BaseState):
    __slots__: tuple
    def __init__(self):
        ...
    def _showView(self):
        ...

class FailureState(BaseState):
    __slots__: tuple
    def __init__(self):
        ...
    def _showView(self):
        ...

class HiddenState(BaseState):
    __slots__: tuple
    def __init__(self):
        ...
    def _showView(self):
        ...
