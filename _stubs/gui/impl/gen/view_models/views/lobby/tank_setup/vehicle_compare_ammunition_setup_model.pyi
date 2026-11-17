# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/vehicle_compare_ammunition_setup_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel as VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.tank_setup.main_tank_setup_model import MainTankSetupModel as MainTankSetupModel

class VehicleCompareAmmunitionSetupModel(ViewModel):
    __slots__: tuple
    onClose: Any
    onResized: Any
    onViewRendered: Any
    onAnimationEnd: Any
    def __init__(self, properties=4, commands=4):
        ...
    @property
    def tankSetup(self):
        ...
    @staticmethod
    def getTankSetupType():
        ...
    @property
    def vehicleInfo(self):
        ...
    @staticmethod
    def getVehicleInfoType():
        ...
    def getShow(self):
        ...
    def setShow(self, value):
        ...
    def getSelectedSlot(self):
        ...
    def setSelectedSlot(self, value):
        ...
    def _initialize(self):
        ...
