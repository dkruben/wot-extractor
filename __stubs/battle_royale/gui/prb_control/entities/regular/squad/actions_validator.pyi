# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/prb_control/entities/regular/squad/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite as ActionsValidatorComposite
from gui.prb_control.entities.base.squad.actions_validator import SquadActionsValidator as SquadActionsValidator, SquadVehiclesValidator as SquadVehiclesValidator
from gui.prb_control.entities.base.unit.actions_validator import UnitSlotsValidator as UnitSlotsValidator, CommanderValidator as CommanderValidator
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.settings import UNIT_RESTRICTION as UNIT_RESTRICTION
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT

class _BattleRoyaleVehiclesValidator(SquadVehiclesValidator):
    def _isValidMode(self, vehicle):
        ...
    def _isVehicleSuitableForMode(self, vehicle):
        ...

class _UnitSlotsValidator(UnitSlotsValidator):
    def _validate(self):
        ...

class _BattleRoyaleValidator(CommanderValidator):
    def _validate(self):
        ...

class BattleRoyaleSquadActionsValidator(SquadActionsValidator):
    def _createVehiclesValidator(self, entity):
        ...
    def _createSlotsValidator(self, entity):
        ...

class BattleRoyalSquadSlotsValidator(CommanderValidator):
    def _validate(self):
        ...
