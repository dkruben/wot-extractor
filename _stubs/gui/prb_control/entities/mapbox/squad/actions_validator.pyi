# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/mapbox/squad/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite as ActionsValidatorComposite
from gui.prb_control.entities.base.squad.actions_validator import SquadActionsValidator as SquadActionsValidator, SquadVehiclesValidator as SquadVehiclesValidator
from gui.prb_control.entities.base.unit.actions_validator import CommanderValidator as CommanderValidator
from gui.prb_control.entities.base.unit.actions_validator import UnitStateValidator as UnitStateValidator
from gui.prb_control.entities.random.squad.actions_validator import BalancedSquadVehiclesValidator as BalancedSquadVehiclesValidator, SquadRestrictionsVehiclesValidator as SquadRestrictionsVehiclesValidator
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.settings import UNIT_RESTRICTION as UNIT_RESTRICTION
from helpers import dependency as dependency
from skeletons.gui.game_control import IMapboxController as IMapboxController

class _MapboxStateValidator(UnitStateValidator):
    def _validate(self):
        ...

class _UnitSlotsValidator(CommanderValidator):
    def _validate(self):
        ...

class MapboxSquadActionsValidator(SquadActionsValidator):
    def _createVehiclesValidator(self, entity):
        ...
    def _createStateValidator(self, entity):
        ...
    def _createSlotsValidator(self, entity):
        ...
