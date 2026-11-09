# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/veh_skill_tree_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.prestige_view_model import PrestigeViewModel as PrestigeViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.reward_screen_view_model import RewardScreenViewModel as RewardScreenViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.tree_view_model import TreeViewModel as TreeViewModel

class VehSkillTreeModel(ViewModel):
    __slots__: tuple
    INITIAL = 'initial'
    TREE = 'tree'
    PRESTIGE = 'prestige'
    def __init__(self, properties=4, commands=0):
        ...
    @property
    def tree(self):
        ...
    @staticmethod
    def getTreeType():
        ...
    @property
    def prestige(self):
        ...
    @staticmethod
    def getPrestigeType():
        ...
    @property
    def rewardScreen(self):
        ...
    @staticmethod
    def getRewardScreenType():
        ...
    def getLocationId(self):
        ...
    def setLocationId(self, value):
        ...
    def _initialize(self):
        ...
