# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_matters/battle_matters_vehicle_selection_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.battle_matters.battle_matters_vehicle_model import BattleMattersVehicleModel as BattleMattersVehicleModel

class BattleMattersVehicleSelectionViewModel(ViewModel):
    __slots__: tuple
    ARG_VEHICLE_ID = 'vehCD'
    onGoBack: Any
    onShowVehicle: Any
    onCompareVehicle: Any
    onResetFilter: Any
    def __init__(self, properties=3, commands=4):
        ...
    def getEndDate(self):
        ...
    def setEndDate(self, value):
        ...
    def getTotalVehiclesCount(self):
        ...
    def setTotalVehiclesCount(self, value):
        ...
    def getVehicles(self):
        ...
    def setVehicles(self, value):
        ...
    @staticmethod
    def getVehiclesType():
        ...
    def _initialize(self):
        ...
