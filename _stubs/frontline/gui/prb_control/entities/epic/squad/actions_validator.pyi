# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/prb_control/entities/epic/squad/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import BATTLE_MODE_VEH_TAGS_EXCEPT_EPIC as BATTLE_MODE_VEH_TAGS_EXCEPT_EPIC
from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite as ActionsValidatorComposite
from gui.prb_control.entities.base.squad.actions_validator import SquadActionsValidator as SquadActionsValidator, SquadVehiclesValidator as SquadVehiclesValidator
from gui.prb_control.entities.base.unit.actions_validator import CommanderValidator as CommanderValidator
from gui.prb_control.entities.base.unit.actions_validator import UnitStateValidator as UnitStateValidator
from gui.prb_control.entities.random.squad.actions_validator import BalancedSquadVehiclesValidator as BalancedSquadVehiclesValidator, SquadRestrictionsVehiclesValidator as SquadRestrictionsVehiclesValidator
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.settings import UNIT_RESTRICTION as UNIT_RESTRICTION
from helpers import time_utils as time_utils, dependency as dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController

class _EpicVehiclesValidator(SquadVehiclesValidator):
    _BATTLE_MODE_VEHICLE_TAGS = BATTLE_MODE_VEH_TAGS_EXCEPT_EPIC

class _EpicBalancedSquadVehiclesValidator(BalancedSquadVehiclesValidator):
    __epicCtrl: Any
    def _validate(self):
        ...

class _EpicStateValidator(UnitStateValidator):
    __epicCtrl: Any
    def _validate(self):
        ...

class EpicSquadActionsValidator(SquadActionsValidator):
    def _createVehiclesValidator(self, entity):
        ...
    def _createStateValidator(self, entity):
        ...
    def _createSlotsValidator(self, entity):
        ...

class EpicSquadSlotsValidator(CommanderValidator):
    def _validate(self):
        ...
