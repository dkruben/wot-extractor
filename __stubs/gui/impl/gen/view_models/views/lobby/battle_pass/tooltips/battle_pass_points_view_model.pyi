# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/tooltips/battle_pass_points_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewModel as ViewModel
from gui.impl.wrappers.user_list_model import UserListModel as UserListModel
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.reward_points_model import RewardPointsModel as RewardPointsModel
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.vehicle_item_model import VehicleItemModel as VehicleItemModel

class BattlePassPointsViewModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    @property
    def rewardPoints(self):
        ...
    @staticmethod
    def getRewardPointsType():
        ...
    @property
    def vehiclesList(self):
        ...
    @staticmethod
    def getVehiclesListType():
        ...
    def getIsWotPlusShown(self):
        ...
    def setIsWotPlusShown(self, value):
        ...
    def _initialize(self):
        ...
