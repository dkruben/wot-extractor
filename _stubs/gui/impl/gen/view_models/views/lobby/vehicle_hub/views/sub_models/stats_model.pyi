# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/stats_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import Array as Array, Map as Map, ViewModel as ViewModel
from gui.impl.gen.view_models.common.vehicle_mechanic_model import VehicleMechanicModel as VehicleMechanicModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.special_shell_param_model import SpecialShellParamModel as SpecialShellParamModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.special_vehicle_param_model import SpecialVehicleParamModel as SpecialVehicleParamModel

class StatsModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    @property
    def specialMechanic(self):
        ...
    @staticmethod
    def getSpecialMechanicType():
        ...
    def getSpecialMechanicParams(self):
        ...
    def setSpecialMechanicParams(self, value):
        ...
    @staticmethod
    def getSpecialMechanicParamsType():
        ...
    def getShellParams(self):
        ...
    def setShellParams(self, value):
        ...
    @staticmethod
    def getShellParamsType():
        ...
    def _initialize(self):
        ...
