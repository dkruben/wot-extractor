# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/periodic_battles/prb_control/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.prb_control.entities.base.actions_validator import BaseActionsValidator as BaseActionsValidator
from gui.prb_control.entities.base.unit.actions_validator import UnitStateValidator as UnitStateValidator
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.settings import PRE_QUEUE_RESTRICTION as PRE_QUEUE_RESTRICTION, UNIT_RESTRICTION as UNIT_RESTRICTION
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus

class PrimeTimeValidator(BaseActionsValidator):
    def _getController(self):
        ...
    def _validate(self):
        ...

class SquadPrimeTimeValidator(UnitStateValidator):
    def _getController(self):
        ...
    def _validate(self):
        ...

def _validateModeState(controller, restrictions):
    ...
