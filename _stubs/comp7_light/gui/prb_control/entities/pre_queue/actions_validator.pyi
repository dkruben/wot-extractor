# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/prb_control/entities/pre_queue/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator as BaseActionsValidator, ActionsValidatorComposite as ActionsValidatorComposite
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator as PreQueueActionsValidator
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.settings import PRE_QUEUE_RESTRICTION as PRE_QUEUE_RESTRICTION
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7LightController as IComp7LightController

class Comp7LightPrimeTimeValidator(BaseActionsValidator):
    __comp7LightController: Any
    def _validate(self):
        ...

class Comp7LightPlayerValidator(BaseActionsValidator):
    __comp7LightController: Any
    def _validate(self):
        ...

class Comp7LightVehicleValidator(BaseActionsValidator):
    __comp7LightController: Any
    def _validate(self):
        ...

class Comp7LightActionsValidator(PreQueueActionsValidator):
    def _createStateValidator(self, entity):
        ...
    def _createVehiclesValidator(self, entity):
        ...
