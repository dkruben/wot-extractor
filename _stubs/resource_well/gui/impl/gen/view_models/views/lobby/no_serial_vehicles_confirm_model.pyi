# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/impl/gen/view_models/views/lobby/no_serial_vehicles_confirm_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from resource_well.gui.impl.gen.view_models.views.lobby.vehicle_counter_model import VehicleCounterModel as VehicleCounterModel

class NoSerialVehiclesConfirmModel(ViewModel):
    __slots__: tuple
    confirm: Any
    cancel: Any
    close: Any
    def __init__(self, properties=2, commands=3):
        ...
    @property
    def vehicleCounter(self):
        ...
    @staticmethod
    def getVehicleCounterType():
        ...
    def getVehicleName(self):
        ...
    def setVehicleName(self, value):
        ...
    def _initialize(self):
        ...
