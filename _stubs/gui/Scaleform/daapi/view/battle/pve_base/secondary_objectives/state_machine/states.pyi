# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/secondary_objectives/state_machine/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
import BigWorld as BigWorld
from frameworks_common.state_machine import StateFlags as StateFlags
from gui.Scaleform.daapi.view.battle.pve_base.base.state_machine.states import BaseState as BaseState, BaseTimerState as BaseTimerState
from math_common import round_py2_style as round_py2_style
from pve_battle_hud import SecondaryObjectiveState as SecondaryObjectiveState

class HideType(Enum):
    SUCCESS = 'hideGreen'
    FAILURE = 'hideRed'
    DISAPPEARANCE = 'hide'

class InitialState(BaseState):
    __slots__: tuple
    def __init__(self):
        ...

class BaseViewTimerState(BaseTimerState):
    def tick(self, currentTime):
        ...
    @property
    def _isWarning(self):
        ...
    def _updateView(self):
        ...

class AppearanceState(BaseViewTimerState):
    def __init__(self):
        ...
    def _showView(self):
        ...

class RestoredState(BaseViewTimerState):
    def __init__(self):
        ...
    @property
    def _isWarning(self):
        ...
    def _showView(self):
        ...

class RegularState(BaseViewTimerState):
    def __init__(self):
        ...

class CountdownState(BaseViewTimerState):
    def __init__(self):
        ...
    @property
    def _isWarning(self):
        ...
    def tick(self, currentTime):
        ...

class SuccessState(BaseState):
    def __init__(self):
        ...
    def _showView(self):
        ...

class FailureState(BaseState):
    def __init__(self):
        ...
    def _showView(self):
        ...

class DisappearingState(BaseState):
    def __init__(self):
        ...
    def _showView(self):
        ...

class HiddenState(BaseState):
    def __init__(self):
        ...
    def _showView(self):
        ...
