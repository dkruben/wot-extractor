# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/ranked/pre_queue/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator as BaseActionsValidator, ActionsValidatorComposite as ActionsValidatorComposite
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator as PreQueueActionsValidator
from gui.periodic_battles.prb_control.actions_validator import PrimeTimeValidator as PrimeTimeValidator
from helpers import dependency as dependency
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController

class RankedPrimeTimeValidator(PrimeTimeValidator):
    __rankedController: Any
    def _getController(self):
        ...

class RankedVehicleValidator(BaseActionsValidator):
    __rankedController: Any
    def _validate(self):
        ...

class RankedActionsValidator(PreQueueActionsValidator):
    def _createStateValidator(self, entity):
        ...
    def _createVehiclesValidator(self, entity):
        ...
