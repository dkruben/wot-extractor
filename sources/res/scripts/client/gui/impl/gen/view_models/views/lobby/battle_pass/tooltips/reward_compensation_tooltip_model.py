# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/tooltips/reward_compensation_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/tooltips/reward_compensation_tooltip_model.py
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel

class RewardCompensationTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(RewardCompensationTooltipModel, self).__init__(properties=properties, commands=commands)

    @property
    def initialReward(self):
        return self._getViewModel(0)

    @staticmethod
    def getInitialRewardType():
        return RewardItemModel

    @property
    def compensationReward(self):
        return self._getViewModel(1)

    @staticmethod
    def getCompensationRewardType():
        return RewardItemModel

    def _initialize(self):
        super(RewardCompensationTooltipModel, self)._initialize()
        self._addViewModelProperty('initialReward', UserListModel())
        self._addViewModelProperty('compensationReward', UserListModel())
