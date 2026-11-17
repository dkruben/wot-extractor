# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/base/pre_queue/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator as BaseActionsValidator, ActionsValidatorComposite as ActionsValidatorComposite, CurrentVehicleActionsValidator as CurrentVehicleActionsValidator, TutorialActionsValidator as TutorialActionsValidator, CurrentPreviewVehicleActionsValidator as CurrentPreviewVehicleActionsValidator
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.entities.base.entity import BasePrbEntity as BasePrbEntity

class InQueueValidator(BaseActionsValidator):
    def _validate(self):
        ...

class PreQueueActionsValidator(ActionsValidatorComposite):
    _stateValidator: Any
    _vehiclesValidator: Any
    _tutorialValidator: Any
    _previewVehiclesValidator: Any
    def __init__(self, entity):
        ...
    def _createStateValidator(self, entity):
        ...
    def _createVehiclesValidator(self, entity):
        ...
    def _createTutorialValidator(self, entity):
        ...
    def _createPreviewVehiclesValidator(self, entity):
        ...
