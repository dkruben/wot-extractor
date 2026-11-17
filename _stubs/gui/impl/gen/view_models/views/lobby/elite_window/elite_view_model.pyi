# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/elite_window/elite_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel as VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.prestige.prestige_emblem_model import PrestigeEmblemModel as PrestigeEmblemModel

class WindowType(Enum):
    STANDARD = 'standard'
    POST_PROGRESSION = 'postProgression'
    VEH_SKILL_TREE = 'vehSkillTree'

class EliteViewModel(ViewModel):
    __slots__: tuple
    onGoToProgression: Any
    onClose: Any
    def __init__(self, properties=4, commands=2):
        ...
    @property
    def vehicleInfo(self):
        ...
    @staticmethod
    def getVehicleInfoType():
        ...
    @property
    def prestigeEmblem(self):
        ...
    @staticmethod
    def getPrestigeEmblemType():
        ...
    def getType(self):
        ...
    def setType(self, value):
        ...
    def getIsPrestigeAvailable(self):
        ...
    def setIsPrestigeAvailable(self, value):
        ...
    def _initialize(self):
        ...
