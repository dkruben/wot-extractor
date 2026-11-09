# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/event/squad/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import BATTLE_MODE_VEH_TAGS_EXCEPT_EVENT as BATTLE_MODE_VEH_TAGS_EXCEPT_EVENT
from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite as ActionsValidatorComposite
from gui.prb_control.entities.base.squad.actions_validator import SquadActionsValidator as SquadActionsValidator, SquadVehiclesValidator as SquadVehiclesValidator
from gui.prb_control.entities.base.unit.actions_validator import CommanderValidator as CommanderValidator
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.settings import UNIT_RESTRICTION as UNIT_RESTRICTION

class _EventBattleVehiclesValidator(SquadVehiclesValidator):
    def _validate(self):
        ...
    def _isValidMode(self, vehicle):
        ...

class EventSquadSlotsValidator(CommanderValidator):
    def _validate(self):
        ...

class EventBattleSquadActionsValidator(SquadActionsValidator):
    def _createVehiclesValidator(self, entity):
        ...
    def _createSlotsValidator(self, entity):
        ...
