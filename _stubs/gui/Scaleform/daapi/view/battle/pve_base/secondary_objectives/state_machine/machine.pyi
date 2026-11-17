# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/secondary_objectives/state_machine/machine.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.daapi.view.battle.pve_base.base.state_machine.machine import BaseTimerStateMachine as BaseTimerStateMachine
from gui.Scaleform.daapi.view.battle.pve_base.base.state_machine.transitions import PostponedTransition as PostponedTransition, CountdownTimerCondition as CountdownTimerCondition, RegularTimerCondition as RegularTimerCondition
from gui.Scaleform.daapi.view.battle.pve_base.secondary_objectives.state_machine import states as states
from gui.Scaleform.daapi.view.battle.pve_base.secondary_objectives.state_machine.transitions import ToAppearanceTransition as ToAppearanceTransition, ToRegularTransition as ToRegularTransition, ToCountdownTransition as ToCountdownTransition, ToHiddenTransition as ToHiddenTransition, ToSuccessTransition as ToSuccessTransition, ToFailureTransition as ToFailureTransition, ToDisappearanceTransition as ToDisappearanceTransition, ToRestoredTransition as ToRestoredTransition

class SecondaryObjectiveStateMachine(BaseTimerStateMachine):
    def configure(self, view, widgetType, widgetId):
        ...
