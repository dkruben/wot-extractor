# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/prb_control/entities/pre_queue/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator as PreQueueActionsValidator
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator as BaseActionsValidator, ActionsValidatorComposite as ActionsValidatorComposite
from gui.prb_control.settings import PRE_QUEUE_RESTRICTION as PRE_QUEUE_RESTRICTION
from helpers import dependency as dependency

class FortRushBattleVehicleValidator(BaseActionsValidator):
    _battleController: Any
    def _validate(self):
        ...

class FortRushBattleActionsValidator(PreQueueActionsValidator):
    _vehicleValidatorExt: Any
    def __init__(self, entity):
        ...
    def _createVehiclesValidator(self, entity):
        ...
