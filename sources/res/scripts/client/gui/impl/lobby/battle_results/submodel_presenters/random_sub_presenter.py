# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/battle_results/submodel_presenters/random_sub_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/battle_results/submodel_presenters/random_sub_presenter.py
import typing
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter
from gui.impl.gen.view_models.views.lobby.battle_results.random.random_battle_results_view_model import RandomBattleResultsViewModel
from gui.impl.lobby.battle_results.submodel_presenters.battle_info import BattleInfoSubPresenter
from gui.impl.lobby.battle_results.submodel_presenters.player_satisfaction import PlayerSatisfactionSubPresenter
from gui.impl.lobby.battle_results.submodel_presenters.financial_report import ManageableBonusSubPresenter, FinancialReportSubPresenter
from gui.impl.lobby.battle_results.submodel_presenters.team_statistics import TeamStatisticsSubPresenter
from gui.impl.lobby.battle_results.submodel_presenters.battle_achievements import BattleAchievementsSubPresenter
from gui.impl.lobby.battle_results.submodel_presenters.battle_efficiency import BattleEfficiencySubPresenter
if typing.TYPE_CHECKING:
    from frameworks.wulf import ViewModel

class RandomBattleResultsSubPresenter(BattleResultsSubPresenter):

    def __init__(self, viewModel, parentView):
        super(RandomBattleResultsSubPresenter, self).__init__(viewModel, parentView)
        self.addSubPresenter(BattleEfficiencySubPresenter(viewModel, parentView))
        self.addSubPresenter(BattleAchievementsSubPresenter(viewModel.getAchievements(), parentView))
        self.addSubPresenter(TeamStatisticsSubPresenter(viewModel.teamStats, parentView))
        self.addSubPresenter(BattleInfoSubPresenter(viewModel.battleInfo, parentView))
        self.addSubPresenter(ManageableBonusSubPresenter(viewModel.additionalBonus, parentView))
        self.addSubPresenter(FinancialReportSubPresenter(viewModel.financialReport, parentView))
        self.addSubPresenter(PlayerSatisfactionSubPresenter(viewModel.playerSatisfaction, parentView))

    @classmethod
    def getViewModelType(cls):
        return RandomBattleResultsViewModel
