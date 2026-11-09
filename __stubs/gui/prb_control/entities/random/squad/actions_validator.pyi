# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/random/squad/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator as BaseActionsValidator, ActionsValidatorComposite as ActionsValidatorComposite
from gui.prb_control.entities.base.squad.actions_validator import SquadActionsValidator as SquadActionsValidator
from gui.prb_control.entities.base.unit.actions_validator import CommanderValidator as CommanderValidator
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.settings import UNIT_RESTRICTION as UNIT_RESTRICTION

class BalancedSquadVehiclesValidator(BaseActionsValidator):
    def _validate(self):
        ...

class BalancedSquadSlotsValidator(CommanderValidator):
    def _validate(self):
        ...

class SquadRestrictionsVehiclesValidator(BaseActionsValidator):
    def _validate(self):
        ...

class RandomSquadActionsValidator(SquadActionsValidator):
    ...

class BalancedSquadActionsValidator(RandomSquadActionsValidator):
    def _createVehiclesValidator(self, entity):
        ...
    def _createSlotsValidator(self, entity):
        ...

class VehTypeForbiddenSquadActionsValidator(RandomSquadActionsValidator):
    def _createVehiclesValidator(self, entity):
        ...

class VehTypeForbiddenBalancedSquadActionsValidator(BalancedSquadActionsValidator):
    def _createVehiclesValidator(self, entity):
        ...
