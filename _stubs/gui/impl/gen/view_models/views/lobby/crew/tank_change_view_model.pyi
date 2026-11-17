# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/tank_change_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array
from gui.impl.gen.view_models.views.lobby.crew.common.base_crew_view_model import BaseCrewViewModel as BaseCrewViewModel
from gui.impl.gen.view_models.views.lobby.crew.tank_change_vehicle_model import TankChangeVehicleModel as TankChangeVehicleModel

class TankChangeViewModel(BaseCrewViewModel):
    __slots__: tuple
    onVehicleSelected: Any
    onResetFilters: Any
    def __init__(self, properties=4, commands=6):
        ...
    def getNation(self):
        ...
    def setNation(self, value):
        ...
    def getVehicleList(self):
        ...
    def setVehicleList(self, value):
        ...
    @staticmethod
    def getVehicleListType():
        ...
    def _initialize(self):
        ...
