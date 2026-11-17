# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/prb_control/entities/squad/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewvalues as viewvalues
from comp7_light_constants import BATTLE_MODE_VEH_TAGS_EXCEPT_COMP7_LIGHT as BATTLE_MODE_VEH_TAGS_EXCEPT_COMP7_LIGHT
from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite as ActionsValidatorComposite, BaseActionsValidator as BaseActionsValidator
from gui.prb_control.entities.base.squad.actions_validator import SquadActionsValidator as SquadActionsValidator, SquadVehiclesValidator as SquadVehiclesValidator
from gui.prb_control.entities.base.unit.actions_validator import UnitSlotsValidator as UnitSlotsValidator, CommanderValidator as CommanderValidator, UnitPlayerValidator as UnitPlayerValidator
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.settings import UNIT_RESTRICTION as UNIT_RESTRICTION
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7LightController as IComp7LightController, IPlatoonController as IPlatoonController
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from gui.prb_control.items import PlayerUnitInfo as PlayerUnitInfo

class _Comp7LightVehiclesValidator(SquadVehiclesValidator):
    _BATTLE_MODE_VEHICLE_TAGS = BATTLE_MODE_VEH_TAGS_EXCEPT_COMP7_LIGHT

class _UnitSlotsValidator(UnitSlotsValidator):
    def _validate(self):
        ...

class _PrimeTimeValidator(CommanderValidator):
    def _validate(self):
        ...

class _Comp7LightPlayerValidator(UnitPlayerValidator):
    __comp7LightController: Any
    __platoonController: Any
    def _validate(self):
        ...

class _Comp7LightModeStatusValidator(BaseActionsValidator):
    def _validate(self):
        ...
    @staticmethod
    def __isModeOfflineForPlayer(pInfo):
        ...

class _Comp7LightSlotValidator(CommanderValidator):
    def _validate(self):
        ...

class Comp7LightSquadActionsValidator(SquadActionsValidator):
    def _createVehiclesValidator(self, entity):
        ...
    def _createSlotsValidator(self, entity):
        ...
    def _createPlayerValidator(self, entity):
        ...
