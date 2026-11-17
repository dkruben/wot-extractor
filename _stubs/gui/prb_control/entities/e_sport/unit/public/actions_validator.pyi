# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/e_sport/unit/public/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite as ActionsValidatorComposite
from gui.prb_control.entities.base.unit.actions_validator import UnitActionsValidator as UnitActionsValidator, UnitLevelsValidator as UnitLevelsValidator, CommanderValidator as CommanderValidator
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.settings import UNIT_RESTRICTION as UNIT_RESTRICTION

class ESportLevelsValidator(CommanderValidator):
    def _validate(self):
        ...
    def _getInvalidLevels(self, stats):
        ...

class ESportSearchValidator(UnitLevelsValidator):
    def _validate(self):
        ...
    def _isEnabled(self):
        ...

class ESportActionsValidator(UnitActionsValidator):
    def __init__(self, entity):
        ...
    def _createLevelsValidator(self, entity):
        ...
