# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/views/lobby/post_battle_results_view/vehicle_stats_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.battle_results.detailed_stats_parameter_model import DetailedStatsParameterModel as DetailedStatsParameterModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel as VehicleModel

class VehicleStatsModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    @property
    def vehicle(self):
        ...
    @staticmethod
    def getVehicleType():
        ...
    def getIsGeneralInfo(self):
        ...
    def setIsGeneralInfo(self, value):
        ...
    def getDetailedStatistics(self):
        ...
    def setDetailedStatistics(self, value):
        ...
    @staticmethod
    def getDetailedStatisticsType():
        ...
    def _initialize(self):
        ...
