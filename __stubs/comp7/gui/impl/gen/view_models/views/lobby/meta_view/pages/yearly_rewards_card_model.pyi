# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/meta_view/pages/yearly_rewards_card_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.comp7_bonus_model import Comp7BonusModel as Comp7BonusModel
from comp7.gui.impl.gen.view_models.views.lobby.season_point_model import SeasonPointModel as SeasonPointModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel as VehicleModel

class RewardsState(Enum):
    GUARANTEED = 'guaranteed'
    POSSIBLE = 'possible'
    NOTAVAILABLE = 'notAvailable'
    CLAIMED = 'claimed'

class YearlyRewardsCardModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=4, commands=0):
        ...
    @property
    def vehicle(self):
        ...
    @staticmethod
    def getVehicleType():
        ...
    def getRewards(self):
        ...
    def setRewards(self, value):
        ...
    @staticmethod
    def getRewardsType():
        ...
    def getSeasonPoints(self):
        ...
    def setSeasonPoints(self, value):
        ...
    @staticmethod
    def getSeasonPointsType():
        ...
    def getRewardsState(self):
        ...
    def setRewardsState(self, value):
        ...
    def _initialize(self):
        ...
