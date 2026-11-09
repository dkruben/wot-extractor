# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/prb_control/entities/pre_queue/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.prb_control.settings import PREBATTLE_RESTRICTION as PREBATTLE_RESTRICTION, PRE_QUEUE_RESTRICTION as PRE_QUEUE_RESTRICTION
from helpers import dependency as dependency
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator as PreQueueActionsValidator
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator as BaseActionsValidator, ActionsValidatorComposite as ActionsValidatorComposite
from last_stand.skeletons.ls_controller import ILSController as ILSController
from last_stand.skeletons.difficulty_level_controller import IDifficultyLevelController as IDifficultyLevelController

class LastStandStateValidator(BaseActionsValidator):
    lsCtrl: Any
    def _validate(self):
        ...

class LastStandVehiclesValidator(BaseActionsValidator):
    lsCtrl: Any
    __difficultyLevelCtrl: Any
    def _validate(self):
        ...

class LastStandActionsValidator(PreQueueActionsValidator):
    def _createVehiclesValidator(self, entity):
        ...
