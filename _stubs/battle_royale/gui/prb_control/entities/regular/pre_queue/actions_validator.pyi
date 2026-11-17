# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/prb_control/entities/regular/pre_queue/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator as BaseActionsValidator, ActionsValidatorComposite as ActionsValidatorComposite
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator as PreQueueActionsValidator
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.settings import PRE_QUEUE_RESTRICTION as PRE_QUEUE_RESTRICTION
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController

class BattleRoyaleValidator(BaseActionsValidator):
    def _validate(self):
        ...

class BattleRoyaleActionsValidator(PreQueueActionsValidator):
    def _createStateValidator(self, entity):
        ...
