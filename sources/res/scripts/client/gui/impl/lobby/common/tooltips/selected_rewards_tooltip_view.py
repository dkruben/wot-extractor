# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/common/tooltips/selected_rewards_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/common/tooltips/selected_rewards_tooltip_view.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.common.tooltips.selected_rewards_tooltip_category_model import SelectedRewardsTooltipCategoryModel
from gui.impl.gen.view_models.views.lobby.common.tooltips.selected_rewards_tooltip_reward_model import SelectedRewardsTooltipRewardModel
from gui.impl.gen.view_models.views.lobby.common.tooltips.selected_rewards_tooltip_view_model import SelectedRewardsTooltipViewModel
from gui.impl.pub import ViewImpl

class SelectedRewardsTooltipView(ViewImpl):
    __slots__ = ('__cart', '__count')

    def __init__(self, cart, count):
        settings = ViewSettings(R.views.lobby.common.tooltips.SelectedRewardsTooltipView())
        settings.model = SelectedRewardsTooltipViewModel()
        self.__cart = cart
        self.__count = count
        super(SelectedRewardsTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(SelectedRewardsTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        with self.viewModel.transaction() as tx:
            tx.setTotalSelected(self.__count)
            categories = tx.getCategories()
            categories.clear()
            for tabName, tabContent in self.__cart.iteritems():
                newCategory = SelectedRewardsTooltipCategoryModel()
                newCategory.setType(tabName)
                rewards = newCategory.getRewards()
                rewards.clear()
                for rewardName, rewardList in tabContent.iteritems():
                    newReward = SelectedRewardsTooltipRewardModel()
                    newReward.setType(rewardName)
                    newReward.setCount(len(rewardList) * rewardList[0]['packSize'])
                    rewards.addViewModel(newReward)

                categories.addViewModel(newCategory)
