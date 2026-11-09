# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/veh_skill_tree/tooltips/prestige_reward_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/veh_skill_tree/tooltips/prestige_reward_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData
from gui.impl.lobby.vehicle_hub.sub_presenters.veh_skill_tree.utils import getVehSkillTreeRewardTooltipViewBonusPacker
from gui.impl.gen.view_models.views.lobby.veh_skill_tree.tooltips.prestige_reward_tooltip_model import PrestigeRewardTooltipModel

class PrestigeRewardTooltipView(ViewImpl):

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.mono.vehicle_hub.tooltips.prestige_reward_tooltip())
        settings.model = PrestigeRewardTooltipModel()
        settings.args = args
        settings.kwargs = kwargs
        super(PrestigeRewardTooltipView, self).__init__(settings, *args, **kwargs)

    @property
    def viewModel(self):
        return self.getViewModel()

    def _onLoading(self, bonus, *args, **kwargs):
        super(PrestigeRewardTooltipView, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as vm:
            rewardArray = vm.getRewards()
            rewardArray.clear()
            packBonusModelAndTooltipData([
             bonus], rewardArray, packer=getVehSkillTreeRewardTooltipViewBonusPacker())
