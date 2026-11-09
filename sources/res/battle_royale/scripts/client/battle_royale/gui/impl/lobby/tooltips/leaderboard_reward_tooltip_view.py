# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/tooltips/leaderboard_reward_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/lobby/tooltips/leaderboard_reward_tooltip_view.py
from __future__ import absolute_import
from battle_royale.gui.impl.gen.view_models.views.lobby.tooltips.leaderboard_reward_tooltip_model import LeaderboardRewardTooltipModel
from battle_royale.gui.shared.tooltips.helper import fillProgressionPointsTableModel
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.game_control import IBattleRoyaleController

class LeaderboardRewardTooltipView(ViewImpl):
    battleRoyale = dependency.descriptor(IBattleRoyaleController)
    __slots__ = ()

    def __init__(self):
        settings = ViewSettings(R.views.battle_royale.mono.lobby.tooltips.leaderboard_reward_tooltip_view())
        settings.model = LeaderboardRewardTooltipModel()
        super(LeaderboardRewardTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(LeaderboardRewardTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        fillProgressionPointsTableModel(self.viewModel, self.battleRoyale.getProgressionPointsTableData())
