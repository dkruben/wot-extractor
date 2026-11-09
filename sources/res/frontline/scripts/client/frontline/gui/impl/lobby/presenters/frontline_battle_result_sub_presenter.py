# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/presenters/frontline_battle_result_sub_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/impl/lobby/presenters/frontline_battle_result_sub_presenter.py
from __future__ import absolute_import
import typing
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.post_battle_results_view_model import PostBattleResultsViewModel
from frontline.gui.impl.lobby.presenters.sub_presenters.battle_achievements import FrontlineBattleAchievementsSubPresenter
from frontline.gui.impl.lobby.presenters.sub_presenters.team_statistics import FrontlineTeamStatisticsSubPresenter
from frontline.gui.impl.lobby.presenters.sub_presenters.battle_info import FrontlineBattleInfoSubPresenter
from frontline.gui.impl.lobby.presenters.sub_presenters.financial_report import FrontlineFinancialReportSubPresenter
from frontline.gui.impl.lobby.presenters.sub_presenters.battle_efficiency import FrontlineBattleEfficiencySubPresenter
if typing.TYPE_CHECKING:
    from frameworks.wulf import ViewModel

class FrontlineBattleResultsSubPresenter(BattleResultsSubPresenter):

    def __init__(self, viewModel, parentView):
        super(FrontlineBattleResultsSubPresenter, self).__init__(viewModel, parentView)
        self.addSubPresenter(FrontlineBattleEfficiencySubPresenter(viewModel, parentView))
        self.addSubPresenter(FrontlineBattleAchievementsSubPresenter(viewModel.getAchievements(), parentView))
        self.addSubPresenter(FrontlineTeamStatisticsSubPresenter(viewModel.teamStats, parentView))
        self.addSubPresenter(FrontlineBattleInfoSubPresenter(viewModel.battleInfo, parentView))
        self.addSubPresenter(FrontlineFinancialReportSubPresenter(viewModel.financialReport, parentView))

    @classmethod
    def getViewModelType(cls):
        return PostBattleResultsViewModel
