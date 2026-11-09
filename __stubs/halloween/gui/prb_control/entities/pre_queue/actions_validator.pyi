# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/prb_control/entities/pre_queue/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.prb_control.settings import PRE_QUEUE_RESTRICTION as PRE_QUEUE_RESTRICTION
from helpers import dependency as dependency
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator as PreQueueActionsValidator
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator as BaseActionsValidator, ActionsValidatorComposite as ActionsValidatorComposite
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController

class HalloweenStateValidator(BaseActionsValidator):
    __halloweenBattleCtrl: Any
    def _validate(self):
        ...

class HalloweenVehicleValidator(BaseActionsValidator):
    def _validate(self):
        ...

class HalloweenActionsValidator(PreQueueActionsValidator):
    def _createVehiclesValidator(self, entity):
        ...
