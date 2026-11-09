# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/veh_skill_tree/alternate_configuration_dialog_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel as VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.alternate_configuration_dialog_loadout_model import AlternateConfigurationDialogLoadoutModel as AlternateConfigurationDialogLoadoutModel

class AlternateConfigurationDialogModel(ViewModel):
    __slots__: tuple
    onClose: Any
    onAffirmate: Any
    def __init__(self, properties=3, commands=2):
        ...
    @property
    def vehicleInfo(self):
        ...
    @staticmethod
    def getVehicleInfoType():
        ...
    def getLoadouts(self):
        ...
    def setLoadouts(self, value):
        ...
    @staticmethod
    def getLoadoutsType():
        ...
    def getNodeID(self):
        ...
    def setNodeID(self, value):
        ...
    def _initialize(self):
        ...
