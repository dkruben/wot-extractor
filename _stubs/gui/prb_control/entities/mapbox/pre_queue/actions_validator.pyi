# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/mapbox/pre_queue/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator as BaseActionsValidator, ActionsValidatorComposite as ActionsValidatorComposite, CurrentVehicleActionsValidator as CurrentVehicleActionsValidator
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator as PreQueueActionsValidator
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.settings import PRE_QUEUE_RESTRICTION as PRE_QUEUE_RESTRICTION, PREBATTLE_RESTRICTION as PREBATTLE_RESTRICTION
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.game_control import IMapboxController as IMapboxController

class MapboxVehicleValidator(CurrentVehicleActionsValidator):
    def _validate(self):
        ...
    @staticmethod
    def validateForMapbox(vehicle):
        ...

class MapboxStateValidator(BaseActionsValidator):
    def _validate(self):
        ...

class MapboxActionsValidator(PreQueueActionsValidator):
    def _createVehiclesValidator(self, entity):
        ...
    def _createStateValidator(self, entity):
        ...
