# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/reward_path_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from halloween.gui.impl.gen.view_models.views.lobby.reward_path_item_view_model import RewardPathItemViewModel as RewardPathItemViewModel
from halloween.gui.impl.gen.view_models.views.lobby.vehicle_title_view_model import VehicleTitleViewModel as VehicleTitleViewModel

class RewardPathViewModel(ViewModel):
    __slots__: tuple
    onClose: Any
    onPreview: Any
    onViewLoaded: Any
    goToMission: Any
    goToCrewSelect: Any
    def __init__(self, properties=5, commands=5):
        ...
    @property
    def mainGiftVehicle(self):
        ...
    @staticmethod
    def getMainGiftVehicleType():
        ...
    def getArtefacts(self):
        ...
    def setArtefacts(self, value):
        ...
    @staticmethod
    def getArtefactsType():
        ...
    def getIsCompleted(self):
        ...
    def setIsCompleted(self, value):
        ...
    def getProgress(self):
        ...
    def setProgress(self, value):
        ...
    def getSelectedArtefactID(self):
        ...
    def setSelectedArtefactID(self, value):
        ...
    def _initialize(self):
        ...
