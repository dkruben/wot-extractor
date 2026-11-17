# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/progress_counter/state_machine/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks_common.state_machine import StateFlags as StateFlags
from gui.Scaleform.daapi.view.battle.pve_base.base.state_machine.states import BaseState as BaseState
from pve_battle_hud import ProgressCounterState as ProgressCounterState

class InitialState(BaseState):
    __slots__: tuple
    def __init__(self):
        ...

class BaseProgressCounterState(BaseState):
    def _showProgress(self, isAnimated):
        ...
    def _updateView(self):
        ...

class AppearanceState(BaseProgressCounterState):
    __slots__: tuple
    def __init__(self):
        ...
    def _showView(self):
        ...

class RegularState(BaseProgressCounterState):
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
