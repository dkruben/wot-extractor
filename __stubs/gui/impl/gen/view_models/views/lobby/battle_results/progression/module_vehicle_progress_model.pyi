# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/progression/module_vehicle_progress_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.battle_results.progression.unlock_module_progress_model import UnlockModuleProgressModel as UnlockModuleProgressModel
from gui.impl.gen.view_models.views.lobby.battle_results.progression.unlock_vehicle_progress_model import UnlockVehicleProgressModel as UnlockVehicleProgressModel

class ModuleVehicleProgressModel(ViewModel):
    __slots__: tuple
    PATH: str
    onNavigate: Any
    def __init__(self, properties=2, commands=1):
        ...
    def getUnlockedVehicles(self):
        ...
    def setUnlockedVehicles(self, value):
        ...
    @staticmethod
    def getUnlockedVehiclesType():
        ...
    def getUnlockedModule(self):
        ...
    def setUnlockedModule(self, value):
        ...
    @staticmethod
    def getUnlockedModuleType():
        ...
    def _initialize(self):
        ...
