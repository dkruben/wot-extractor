# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/prb_control/entities/tournament/pre_queue/action_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite as ActionsValidatorComposite
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator as PreQueueActionsValidator, InQueueValidator as InQueueValidator
from gui.prb_control.items import ValidationResult as ValidationResult

class _BattleRoyaleTournamentInQueueValidator(InQueueValidator):
    def _validate(self):
        ...

class BattleRoyaleTournamentActionsValidator(PreQueueActionsValidator):
    def _createStateValidator(self, entity):
        ...
