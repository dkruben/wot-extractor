# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/base/unit/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import BATTLE_MODE_VEHICLE_TAGS as BATTLE_MODE_VEHICLE_TAGS
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator as BaseActionsValidator, ActionsValidatorComposite as ActionsValidatorComposite
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.settings import UNIT_RESTRICTION as UNIT_RESTRICTION
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from shared_utils import findFirst as findFirst

class UnitStateValidator(BaseActionsValidator):
    def _validate(self):
        ...

class UnitPlayerValidator(BaseActionsValidator):
    def _validate(self):
        ...

class UnitVehiclesValidator(BaseActionsValidator):
    _BATTLE_MODE_VEHICLE_TAGS = BATTLE_MODE_VEHICLE_TAGS
    def _validate(self):
        ...
    def _isValidMode(self, vehicle):
        ...
    def _isVehicleSuitableForMode(self, vehicle):
        ...
    def _isCheckForRent(self):
        ...
    def _getVehiclesInfo(self):
        ...

class ExceptDevModeValidator(BaseActionsValidator):
    def _isEnabled(self):
        ...

class CommanderValidator(ExceptDevModeValidator):
    def _isEnabled(self):
        ...

class UnitSlotsValidator(CommanderValidator):
    def _validate(self):
        ...

class UnitLevelsValidator(ExceptDevModeValidator):
    def _validate(self):
        ...
    def _areVehiclesSelected(self, stats):
        ...

class UnitActionsValidator(ActionsValidatorComposite):
    _stateValidator: Any
    _playerValidator: Any
    _vehiclesValidator: Any
    _levelsValidator: Any
    _slotsValidator: Any
    def __init__(self, entity):
        ...
    def getVehiclesValidator(self):
        ...
    def getPlayerValidator(self):
        ...
    def getStateValidator(self):
        ...
    def getLevelsValidator(self):
        ...
    def getSlotsValidator(self):
        ...
    def validateStateToStartBattle(self):
        ...
    def _createVehiclesValidator(self, entity):
        ...
    def _createPlayerValidator(self, entity):
        ...
    def _createStateValidator(self, entity):
        ...
    def _createLevelsValidator(self, entity):
        ...
    def _createSlotsValidator(self, entity):
        ...
