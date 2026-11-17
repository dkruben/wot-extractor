# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/training/legacy/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite as ActionsValidatorComposite, BaseActionsValidator as BaseActionsValidator, CurrentVehicleActionsValidator as CurrentVehicleActionsValidator
from gui.prb_control.entities.base.legacy.actions_validator import LegacyVehicleValid as LegacyVehicleValid
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.items import ValidationResult as ValidationResult

class TrainingIsLoaded(BaseActionsValidator):
    def _validate(self):
        ...

class TrainingIntroActionsValidator(ActionsValidatorComposite):
    def __init__(self, entity):
        ...

class TrainingActionsValidator(TrainingIntroActionsValidator):
    def __init__(self, entity):
        ...
