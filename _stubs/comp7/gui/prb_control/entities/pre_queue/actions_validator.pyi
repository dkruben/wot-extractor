# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/prb_control/entities/pre_queue/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName as SeasonName
from comp7_core.gui.impl.lobby.comp7_core_helpers.comp7_core_model_helpers import getSeasonNameEnum as getSeasonNameEnum
from gui.periodic_battles.models import PeriodType as PeriodType
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator as BaseActionsValidator, ActionsValidatorComposite as ActionsValidatorComposite
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator as PreQueueActionsValidator
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.settings import PRE_QUEUE_RESTRICTION as PRE_QUEUE_RESTRICTION
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from gui.prb_control.entities.base.entity import BasePrbEntity as BasePrbEntity

class Comp7TournamentValidator(BaseActionsValidator):
    __comp7Controller: Any
    def _validate(self):
        ...

class Comp7Validator(BaseActionsValidator):
    __comp7Ctrl: Any
    def _validate(self):
        ...

class Comp7VehicleValidator(BaseActionsValidator):
    __comp7Ctrl: Any
    def _validate(self):
        ...

class Comp7ActionsValidator(PreQueueActionsValidator):
    def _createStateValidator(self, entity):
        ...
    def _createVehiclesValidator(self, entity):
        ...
