# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/impl/gen/view_models/views/lobby/resources_loading_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel as VehicleInfoModel
from resource_well.gui.impl.gen.view_models.views.lobby.resources_tab_model import ResourcesTabModel as ResourcesTabModel
from resource_well.gui.impl.gen.view_models.views.lobby.vehicle_counter_model import VehicleCounterModel as VehicleCounterModel

class ProgressionState(Enum):
    ACTIVE = 'active'
    NOPROGRESS = 'noProgress'
    NOVEHICLES = 'noVehicles'

class ResourcesLoadingViewModel(ViewModel):
    __slots__: tuple
    showHangar: Any
    close: Any
    loadResources: Any
    def __init__(self, properties=7, commands=3):
        ...
    @property
    def vehicleCounter(self):
        ...
    @staticmethod
    def getVehicleCounterType():
        ...
    @property
    def vehicleInfo(self):
        ...
    @staticmethod
    def getVehicleInfoType():
        ...
    def getProgressionState(self):
        ...
    def setProgressionState(self, value):
        ...
    def getProgression(self):
        ...
    def setProgression(self, value):
        ...
    def getResourcesTabs(self):
        ...
    def setResourcesTabs(self, value):
        ...
    @staticmethod
    def getResourcesTabsType():
        ...
    def getIsLoadingError(self):
        ...
    def setIsLoadingError(self, value):
        ...
    def getShowBlur(self):
        ...
    def setShowBlur(self, value):
        ...
    def _initialize(self):
        ...
