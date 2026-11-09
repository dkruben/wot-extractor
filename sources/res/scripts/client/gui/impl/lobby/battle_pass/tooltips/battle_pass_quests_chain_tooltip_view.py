# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/battle_pass/tooltips/battle_pass_quests_chain_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/battle_pass/tooltips/battle_pass_quests_chain_tooltip_view.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.battle_pass_quests_chain_tooltip_view_model import BattlePassQuestsChainTooltipViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.key_value_model import KeyValueModel
from gui.impl.pub import ViewImpl
from gui.impl.wrappers.user_list_model import UserListModel
from helpers import dependency
from shared_utils import first
from skeletons.gui.server_events import IEventsCache

class BattlePassQuestsChainTooltipView(ViewImpl):
    __slots__ = ('__token', )
    __eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self, token):
        settings = ViewSettings(R.views.mono.battle_pass.tooltips.quest_chain())
        settings.model = BattlePassQuestsChainTooltipViewModel()
        super(BattlePassQuestsChainTooltipView, self).__init__(settings)
        self.__token = token

    @property
    def viewModel(self):
        return super(BattlePassQuestsChainTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(BattlePassQuestsChainTooltipView, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as tx:
            self.__setRewards(tx.rewards)

    def __setRewards(self, rewardsVM):
        rewardsVM.clearItems()
        rewards = rewardsVM.getItems()
        for bonus in self.__getBonuses():
            reward = KeyValueModel()
            reward.setKey(bonus.getName())
            reward.setValue(bonus.getValue())
            rewards.addViewModel(reward)

        rewardsVM.invalidate()

    def __getBonuses(self):
        return first(self.__eventsCache.getAllQuests((lambda q: q.getID() == self.__token)).values()).getBonuses()
