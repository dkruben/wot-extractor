# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/prb_control/entities/pre_queue/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from CurrentVehicle import g_currentVehicle as g_currentVehicle
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode as hasDesiredSubMode
from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite as ActionsValidatorComposite
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator as PreQueueActionsValidator
from gui.periodic_battles.prb_control.actions_validator import PrimeTimeValidator as PrimeTimeValidator, BaseActionsValidator as BaseActionsValidator

class FunRandomPrimeTimeValidator(PrimeTimeValidator, FunSubModesWatcher):
    def _getController(self):
        ...

class FunRandomVehicleValidator(BaseActionsValidator, FunSubModesWatcher):
    def _validate(self):
        ...
    # decorador original: @hasDesiredSubMode(...)
    def __validate(self, vehicle):
        ...

class FunRandomActionsValidator(PreQueueActionsValidator):
    def _createStateValidator(self, entity):
        ...
    def _createVehiclesValidator(self, entity):
        ...
