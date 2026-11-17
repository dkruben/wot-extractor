# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/primary_objective/state_machine/transitions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks_common.state_machine import StateEvent as StateEvent
from gui.Scaleform.daapi.view.battle.pve_base.base.state_machine.events import OneSecondEvent as OneSecondEvent
from gui.Scaleform.daapi.view.battle.pve_base.base.state_machine.transitions import ToStateTransition as ToStateTransition, BaseTimerCondition as BaseTimerCondition
from pve_battle_hud import PrimaryObjectiveState as PrimaryObjectiveState

class ToAppearanceTransition(ToStateTransition):
    __slots__: tuple
    def __init__(self):
        ...

class ToRegularTransition(ToStateTransition):
    __slots__: tuple
    def __init__(self):
        ...

class ToRemindTransition(ToStateTransition):
    __slots__: tuple
    def __init__(self):
        ...

class ToLastRemindTransition(ToStateTransition):
    __slots__: tuple
    def __init__(self):
        ...

class ToLargeTimerTransition(ToStateTransition):
    __slots__: tuple
    def __init__(self):
        ...

class ToCountdownTransition(ToStateTransition):
    __slots__: tuple
    def __init__(self):
        ...

class ToSuccessTransition(ToStateTransition):
    __slots__: tuple
    def __init__(self):
        ...

class ToFailureTransition(ToStateTransition):
    __slots__: tuple
    def __init__(self):
        ...

class ToHiddenTransition(ToStateTransition):
    __slots__: tuple
    def __init__(self):
        ...

class RemindTimerCondition(BaseTimerCondition):
    def _condition(self, event, timerValue=0):
        ...

class LastRemindTimerCondition(BaseTimerCondition):
    def _condition(self, event, timerValue=0):
        ...
