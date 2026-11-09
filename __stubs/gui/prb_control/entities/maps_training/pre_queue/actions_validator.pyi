# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/maps_training/pre_queue/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator as BaseActionsValidator, ActionsValidatorComposite as ActionsValidatorComposite
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator as PreQueueActionsValidator
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.settings import PRE_QUEUE_RESTRICTION as PRE_QUEUE_RESTRICTION, PREBATTLE_RESTRICTION as PREBATTLE_RESTRICTION
from helpers import dependency as dependency
from skeletons.gui.game_control import IMapsTrainingController as IMapsTrainingController

class MapsTrainingValidator(BaseActionsValidator):
    mapsTrainingController: Any
    def _validate(self):
        ...

class MapsTrainingActionsValidator(PreQueueActionsValidator):
    def _createStateValidator(self, entity):
        ...
    def _createVehiclesValidator(self, entity):
        ...
    def _createPreviewVehiclesValidator(self, entity):
        ...
    def _createTutorialValidator(self, entity):
        ...
