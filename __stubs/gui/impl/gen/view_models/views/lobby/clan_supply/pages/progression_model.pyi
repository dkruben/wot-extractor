# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/clan_supply/pages/progression_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.clan_supply.clan_supply_vehicle_model import ClanSupplyVehicleModel as ClanSupplyVehicleModel
from gui.impl.gen.view_models.views.lobby.clan_supply.pages.stage_model import StageModel as StageModel
from gui.impl.gen.view_models.views.lobby.clan_supply.stage_info_model import StageInfoModel as StageInfoModel

class ScreenStatus(IntEnum):
    PENDING = 0
    ERROR = 1
    LOADED = 2

class ProgressionModel(ViewModel):
    __slots__: tuple
    onPreviewClick: Any
    onBuyStage: Any
    onSelectStage: Any
    onRefresh: Any
    def __init__(self, properties=7, commands=4):
        ...
    @property
    def stageInfo(self):
        ...
    @staticmethod
    def getStageInfoType():
        ...
    @property
    def vehicleInfo(self):
        ...
    @staticmethod
    def getVehicleInfoType():
        ...
    def getStatus(self):
        ...
    def setStatus(self, value):
        ...
    def getSelectedStageID(self):
        ...
    def setSelectedStageID(self, value):
        ...
    def getIsCompleted(self):
        ...
    def setIsCompleted(self, value):
        ...
    def getIsMainRewardAvailable(self):
        ...
    def setIsMainRewardAvailable(self, value):
        ...
    def getStages(self):
        ...
    def setStages(self, value):
        ...
    @staticmethod
    def getStagesType():
        ...
    def _initialize(self):
        ...
