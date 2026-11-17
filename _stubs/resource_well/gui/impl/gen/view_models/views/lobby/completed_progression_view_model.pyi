# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/impl/gen/view_models/views/lobby/completed_progression_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel as VehicleInfoModel

class CompletedProgressionViewModel(ViewModel):
    __slots__: tuple
    onViewLoaded: Any
    onClose: Any
    onShowVehicle: Any
    onAboutClick: Any
    def __init__(self, properties=3, commands=4):
        ...
    @property
    def vehicleInfo(self):
        ...
    @staticmethod
    def getVehicleInfoType():
        ...
    def getHasStyle(self):
        ...
    def setHasStyle(self, value):
        ...
    def getPersonalNumber(self):
        ...
    def setPersonalNumber(self, value):
        ...
    def _initialize(self):
        ...
