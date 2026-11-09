# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/prb_control/entities/squad/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from fun_random_common.fun_constants import BATTLE_MODE_VEH_TAGS_EXCEPT_FUN as BATTLE_MODE_VEH_TAGS_EXCEPT_FUN
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode as hasDesiredSubMode
from gui.periodic_battles.prb_control.actions_validator import SquadPrimeTimeValidator as SquadPrimeTimeValidator
from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite as ActionsValidatorComposite
from gui.prb_control.entities.base.squad.actions_validator import SquadActionsValidator as SquadActionsValidator, SquadVehiclesValidator as SquadVehiclesValidator
from gui.prb_control.entities.random.squad.actions_validator import BalancedSquadVehiclesValidator as BalancedSquadVehiclesValidator, BalancedSquadSlotsValidator as BalancedSquadSlotsValidator, SquadRestrictionsVehiclesValidator as SquadRestrictionsVehiclesValidator

class _FunRandomSquadStateValidator(SquadPrimeTimeValidator, FunSubModesWatcher):
    def _getController(self):
        ...

class _FunRandomSquadVehicleValidator(SquadVehiclesValidator, FunSubModesWatcher):
    _BATTLE_MODE_VEHICLE_TAGS = BATTLE_MODE_VEH_TAGS_EXCEPT_FUN
    # decorador original: @hasDesiredSubMode(...)
    def _isVehicleSuitableForMode(self, vehicle):
        ...

class FunRandomActionsValidator(SquadActionsValidator):
    def _createStateValidator(self, entity):
        ...
    def _createSlotsValidator(self, entity):
        ...
    def _createVehiclesValidator(self, entity):
        ...
