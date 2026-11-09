# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/stronghold/unit/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import BATTLE_MODE_VEH_TAGS_EXCEPT_CLAN as BATTLE_MODE_VEH_TAGS_EXCEPT_CLAN
from gui.prb_control import prb_getters as prb_getters
from gui.prb_control.entities.base.squad.actions_validator import UnitActionsValidator as UnitActionsValidator
from gui.prb_control.entities.base.unit.actions_validator import UnitVehiclesValidator as UnitVehiclesValidator, CommanderValidator as CommanderValidator, UnitStateValidator as UnitStateValidator, UnitPlayerValidator as UnitPlayerValidator
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.settings import UNIT_RESTRICTION as UNIT_RESTRICTION

class StrongholdVehiclesValidator(UnitVehiclesValidator):
    _BATTLE_MODE_VEHICLE_TAGS = BATTLE_MODE_VEH_TAGS_EXCEPT_CLAN

class StrongholdUnitSlotsValidator(CommanderValidator):
    def _validate(self):
        ...

class StrongholdUnitStateValidator(UnitStateValidator):
    def _validate(self):
        ...

class StrongholdUnitPlayerValidator(UnitPlayerValidator):
    def _validate(self):
        ...

class StrongholdActionsValidator(UnitActionsValidator):
    def _createVehiclesValidator(self, entity):
        ...
    def _createSlotsValidator(self, entity):
        ...
    def _createStateValidator(self, entity):
        ...
    def _createPlayerValidator(self, entity):
        ...
