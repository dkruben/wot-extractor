# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/whats_new_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.schedule_info_model import ScheduleInfoModel as ScheduleInfoModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel as VehicleModel

class WhatsNewViewModel(ViewModel):
    __slots__: tuple
    onClose: Any
    onVideoOpen: Any
    def __init__(self, properties=2, commands=2):
        ...
    @property
    def scheduleInfo(self):
        ...
    @staticmethod
    def getScheduleInfoType():
        ...
    def getRentalVehicles(self):
        ...
    def setRentalVehicles(self, value):
        ...
    @staticmethod
    def getRentalVehiclesType():
        ...
    def _initialize(self):
        ...
