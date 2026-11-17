# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_compare/skill_select_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel as VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.vehicle_compare.skill_select_row_model import SkillSelectRowModel as SkillSelectRowModel

class SkillSelectViewModel(ViewModel):
    __slots__: tuple
    onRestore: Any
    onCancel: Any
    onClose: Any
    onConfirm: Any
    onClick: Any
    def __init__(self, properties=4, commands=5):
        ...
    @property
    def vehicleInfo(self):
        ...
    @staticmethod
    def getVehicleInfoType():
        ...
    def getMajorSkillRows(self):
        ...
    def setMajorSkillRows(self, value):
        ...
    @staticmethod
    def getMajorSkillRowsType():
        ...
    def getBonusSkillRows(self):
        ...
    def setBonusSkillRows(self, value):
        ...
    @staticmethod
    def getBonusSkillRowsType():
        ...
    def getIsActionsDisable(self):
        ...
    def setIsActionsDisable(self, value):
        ...
    def _initialize(self):
        ...
