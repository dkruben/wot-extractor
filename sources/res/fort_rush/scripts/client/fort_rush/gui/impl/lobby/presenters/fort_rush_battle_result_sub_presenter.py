# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/presenters/fort_rush_battle_result_sub_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/impl/lobby/presenters/fort_rush_battle_result_sub_presenter.py
from __future__ import absolute_import
import typing
from fort_rush.gui.impl.gen.view_models.views.lobby.post_battle_results_view.post_battle_results_view_model import PostBattleResultsViewModel
from fort_rush.gui.impl.lobby.presenters.sub_presenters.battle_efficiency import FortRushBattleEfficiencySubPresenter
from fort_rush.gui.impl.lobby.presenters.sub_presenters.battle_info import FortRushBattleInfoSubPresenter
from fort_rush.gui.impl.lobby.presenters.sub_presenters.fort_rush_personal_rewards import FortRushPersonalRewardSubPresenter
from fort_rush.gui.impl.lobby.presenters.sub_presenters.team_statistics import FortRushTeamStatisticsSubPresenter
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter
if typing.TYPE_CHECKING:
    from frameworks.wulf import ViewModel

class FortRushBattleResultsSubPresenter(BattleResultsSubPresenter):

    def __init__(self, viewModel, parentView):
        super(FortRushBattleResultsSubPresenter, self).__init__(viewModel, parentView)
        self.addSubPresenter(FortRushBattleEfficiencySubPresenter(viewModel, parentView))
        self.addSubPresenter(FortRushTeamStatisticsSubPresenter(viewModel.teamStats, parentView))
        self.addSubPresenter(FortRushBattleInfoSubPresenter(viewModel.battleInfo, parentView))
        self.addSubPresenter(FortRushPersonalRewardSubPresenter(viewModel.getRewards(), parentView))

    @classmethod
    def getViewModelType(cls):
        return PostBattleResultsViewModel
