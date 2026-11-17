# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/battle_results/reusable/shared.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.battle_results.reusable.shared import VehicleDetailedInfo as VehicleDetailedInfo, VehicleSummarizeInfo as VehicleSummarizeInfo, no_key_error as no_key_error
from constants import DEATH_REASON_ALIVE as DEATH_REASON_ALIVE

class Comp7CoreVehicleDetailedInfo(VehicleDetailedInfo):
    __slots__: tuple
    _prestigePoints: Any
    _roleSkillUsed: Any
    _healthRepair: Any
    _alliedHealthRepair: Any
    _entityCaptured: Any
    def __init__(self, vehicleID, vehicle, player, deathReason=...):
        ...
    @property
    def prestigePoints(self):
        ...
    @property
    def roleSkillUsed(self):
        ...
    @property
    def healthRepair(self):
        ...
    @property
    def alliedHealthRepair(self):
        ...
    @property
    def entityCaptured(self):
        ...
    @classmethod
    # decorador original: @no_key_error
    def makeForVehicle(cls, vehicleID, vehicle, player, vehicleRecords, critsRecords=None):
        ...

class Comp7CoreVehicleSummarizeInfo(VehicleSummarizeInfo):
    @property
    def prestigePoints(self):
        ...
    @property
    def roleSkillUsed(self):
        ...
    @property
    def healthRepair(self):
        ...
    @property
    def alliedHealthRepair(self):
        ...
    @property
    def entityCaptured(self):
        ...
