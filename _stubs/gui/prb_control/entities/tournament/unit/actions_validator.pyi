# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/tournament/unit/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.prb_control.entities.base.squad.actions_validator import UnitActionsValidator as UnitActionsValidator
from gui.prb_control.entities.base.unit.actions_validator import UnitVehiclesValidator as UnitVehiclesValidator, CommanderValidator as CommanderValidator, UnitStateValidator as UnitStateValidator
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.settings import UNIT_RESTRICTION as UNIT_RESTRICTION

class TournamentUnitSlotsValidator(CommanderValidator):
    def _validate(self):
        ...

class TournamentUnitStateValidator(UnitStateValidator):
    def _validate(self):
        ...

class TournamentActionsValidator(UnitActionsValidator):
    def _createVehiclesValidator(self, entity):
        ...
    def _createSlotsValidator(self, entity):
        ...
    def _createStateValidator(self, entity):
        ...
