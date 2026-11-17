# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/base/squad/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import VEHICLE_CLASS_INDICES as VEHICLE_CLASS_INDICES
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator as BaseActionsValidator
from gui.prb_control.entities.base.unit.actions_validator import UnitActionsValidator as UnitActionsValidator, UnitVehiclesValidator as UnitVehiclesValidator
from gui.prb_control.items import ValidationResult as ValidationResult, unit_items as unit_items
from gui.prb_control.settings import UNIT_RESTRICTION as UNIT_RESTRICTION
from helpers import dependency as dependency
from shared_utils import findFirst as findFirst
from skeletons.gui.server_events import IEventsCache as IEventsCache

class SquadBalanceValidator(BaseActionsValidator):
    eventsCache: Any
    def _validate(self):
        ...
    def _isEnabled(self):
        ...

class SquadVehiclesValidator(UnitVehiclesValidator):
    def _getVehiclesInfo(self):
        ...

class SquadActionsValidator(UnitActionsValidator):
    def __init__(self, entity):
        ...
    def _createVehiclesValidator(self, entity):
        ...
    def _createSlotsValidator(self, entity):
        ...
    def _createLevelsValidator(self, entity):
        ...
