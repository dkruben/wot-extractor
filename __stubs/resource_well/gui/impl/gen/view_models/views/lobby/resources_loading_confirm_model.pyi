# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/impl/gen/view_models/views/lobby/resources_loading_confirm_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from resource_well.gui.impl.gen.view_models.views.lobby.loading_resource_model import LoadingResourceModel as LoadingResourceModel
from resource_well.gui.impl.gen.view_models.views.lobby.vehicle_counter_model import VehicleCounterModel as VehicleCounterModel

class OperationType(IntEnum):
    RETURN = 0
    CONTRIBUTE = 1
    SWITCH = 2

class ResourcesLoadingConfirmModel(ViewModel):
    __slots__: tuple
    confirm: Any
    cancel: Any
    close: Any
    def __init__(self, properties=5, commands=3):
        ...
    @property
    def vehicleCounter(self):
        ...
    @staticmethod
    def getVehicleCounterType():
        ...
    def getOperationType(self):
        ...
    def setOperationType(self, value):
        ...
    def getProgressDiff(self):
        ...
    def setProgressDiff(self, value):
        ...
    def getVehicleName(self):
        ...
    def setVehicleName(self, value):
        ...
    def getResources(self):
        ...
    def setResources(self, value):
        ...
    @staticmethod
    def getResourcesType():
        ...
    def _initialize(self):
        ...
