# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/prb_control/entities/squad/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite as ActionsValidatorComposite
from gui.prb_control.entities.base.squad.actions_validator import SquadActionsValidator as SquadActionsValidator, SquadVehiclesValidator as SquadVehiclesValidator
from gui.prb_control.entities.random.squad.actions_validator import SquadRestrictionsVehiclesValidator as SquadRestrictionsVehiclesValidator
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.settings import UNIT_RESTRICTION as UNIT_RESTRICTION
from helpers import dependency as dependency
from gui.prb_control.entities.base.entity import BasePrbEntity as BasePrbEntity
from Vehicle import Vehicle as Vehicle

class FortRushSquadVehiclesValidator(SquadVehiclesValidator):
    battleController: Any
    def _isVehicleSuitableForMode(self, vehicle):
        ...
    def _isValidMode(self, vehicle):
        ...

class FortRushSquadActionsValidator(SquadActionsValidator):
    def _createVehiclesValidator(self, entity):
        ...
