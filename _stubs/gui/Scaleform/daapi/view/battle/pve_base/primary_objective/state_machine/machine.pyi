# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/primary_objective/state_machine/machine.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.daapi.view.battle.pve_base.base.state_machine.machine import BaseTimerStateMachine as BaseTimerStateMachine
from gui.Scaleform.daapi.view.battle.pve_base.base.state_machine.transitions import PostponedTransition as PostponedTransition, CountdownTimerCondition as CountdownTimerCondition, RegularTimerCondition as RegularTimerCondition
from gui.Scaleform.daapi.view.battle.pve_base.primary_objective.state_machine import states as states
from gui.Scaleform.daapi.view.battle.pve_base.primary_objective.state_machine.transitions import ToAppearanceTransition as ToAppearanceTransition, ToRegularTransition as ToRegularTransition, ToLargeTimerTransition as ToLargeTimerTransition, ToCountdownTransition as ToCountdownTransition, ToRemindTransition as ToRemindTransition, ToLastRemindTransition as ToLastRemindTransition, ToSuccessTransition as ToSuccessTransition, ToFailureTransition as ToFailureTransition, ToHiddenTransition as ToHiddenTransition, RemindTimerCondition as RemindTimerCondition, LastRemindTimerCondition as LastRemindTimerCondition

class PrimaryObjectiveStateMachine(BaseTimerStateMachine):
    def configure(self, view, widgetType, widgetId):
        ...
