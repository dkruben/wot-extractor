# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/veh_skill_tree_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/veh_skill_tree_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.prestige_view_model import PrestigeViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.reward_screen_view_model import RewardScreenViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.tree_view_model import TreeViewModel

class VehSkillTreeModel(ViewModel):
    __slots__ = ()
    INITIAL = 'initial'
    TREE = 'tree'
    PRESTIGE = 'prestige'

    def __init__(self, properties=4, commands=0):
        super(VehSkillTreeModel, self).__init__(properties=properties, commands=commands)

    @property
    def tree(self):
        return self._getViewModel(0)

    @staticmethod
    def getTreeType():
        return TreeViewModel

    @property
    def prestige(self):
        return self._getViewModel(1)

    @staticmethod
    def getPrestigeType():
        return PrestigeViewModel

    @property
    def rewardScreen(self):
        return self._getViewModel(2)

    @staticmethod
    def getRewardScreenType():
        return RewardScreenViewModel

    def getLocationId(self):
        return self._getString(3)

    def setLocationId(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(VehSkillTreeModel, self)._initialize()
        self._addViewModelProperty('tree', TreeViewModel())
        self._addViewModelProperty('prestige', PrestigeViewModel())
        self._addViewModelProperty('rewardScreen', RewardScreenViewModel())
        self._addStringProperty('locationId', '')
