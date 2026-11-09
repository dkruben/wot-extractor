# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/lootbox_system/main_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/lootbox_system/main_view_model.py
from enum import IntEnum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.submodels.home_view_model import HomeViewModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.submodels.multiple_boxes_rewards_view_model import MultipleBoxesRewardsViewModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.submodels.single_box_rewards_view_model import SingleBoxRewardsViewModel

class SubViewID(IntEnum):
    HOME = 0
    SINGLE_BOX_REWARDS = 1
    MULTIPLE_BOXES_REWARDS = 2


class MainViewModel(ViewModel):
    __slots__ = ('onResourcesLoadCompleted', )

    def __init__(self, properties=4, commands=1):
        super(MainViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def home(self):
        return self._getViewModel(0)

    @staticmethod
    def getHomeType():
        return HomeViewModel

    @property
    def singleBoxRewards(self):
        return self._getViewModel(1)

    @staticmethod
    def getSingleBoxRewardsType():
        return SingleBoxRewardsViewModel

    @property
    def multipleBoxesRewards(self):
        return self._getViewModel(2)

    @staticmethod
    def getMultipleBoxesRewardsType():
        return MultipleBoxesRewardsViewModel

    def getSubViewIDs(self):
        return self._getArray(3)

    def setSubViewIDs(self, value):
        self._setArray(3, value)

    @staticmethod
    def getSubViewIDsType():
        return int

    def _initialize(self):
        super(MainViewModel, self)._initialize()
        self._addViewModelProperty('home', HomeViewModel())
        self._addViewModelProperty('singleBoxRewards', SingleBoxRewardsViewModel())
        self._addViewModelProperty('multipleBoxesRewards', MultipleBoxesRewardsViewModel())
        self._addArrayProperty('subViewIDs', Array())
        self.onResourcesLoadCompleted = self._addCommand('onResourcesLoadCompleted')
