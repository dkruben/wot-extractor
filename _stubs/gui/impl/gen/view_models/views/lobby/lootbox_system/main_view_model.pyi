# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/lootbox_system/main_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.submodels.home_view_model import HomeViewModel as HomeViewModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.submodels.multiple_boxes_rewards_view_model import MultipleBoxesRewardsViewModel as MultipleBoxesRewardsViewModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.submodels.single_box_rewards_view_model import SingleBoxRewardsViewModel as SingleBoxRewardsViewModel

class SubViewID(IntEnum):
    HOME = 0
    SINGLE_BOX_REWARDS = 1
    MULTIPLE_BOXES_REWARDS = 2

class MainViewModel(ViewModel):
    __slots__: tuple
    onResourcesLoadCompleted: Any
    def __init__(self, properties=4, commands=1):
        ...
    @property
    def home(self):
        ...
    @staticmethod
    def getHomeType():
        ...
    @property
    def singleBoxRewards(self):
        ...
    @staticmethod
    def getSingleBoxRewardsType():
        ...
    @property
    def multipleBoxesRewards(self):
        ...
    @staticmethod
    def getMultipleBoxesRewardsType():
        ...
    def getSubViewIDs(self):
        ...
    def setSubViewIDs(self, value):
        ...
    @staticmethod
    def getSubViewIDsType():
        ...
    def _initialize(self):
        ...
