# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/gen/view_models/views/lobby/no_vehicles_screen_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from comp7_light.gui.impl.gen.view_models.views.lobby.schedule_info_model import ScheduleInfoModel as ScheduleInfoModel

class ErrorReason(Enum):
    DEFAULT = 'vehicleUnavailable'
    NOT_BOUGHT_VEHICLES = 'vehicleAvailableForBuy'
    CAN_RECOVER_VEHICLES = 'vehicleAvailableForRestore'

class NoVehiclesScreenModel(ViewModel):
    __slots__: tuple
    onClose: Any
    def __init__(self, properties=3, commands=1):
        ...
    @property
    def scheduleInfo(self):
        ...
    @staticmethod
    def getScheduleInfoType():
        ...
    def getVehicleLevels(self):
        ...
    def setVehicleLevels(self, value):
        ...
    @staticmethod
    def getVehicleLevelsType():
        ...
    def getErrorReason(self):
        ...
    def setErrorReason(self, value):
        ...
    def _initialize(self):
        ...
