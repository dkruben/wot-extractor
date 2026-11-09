# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_results/submodel_presenters/random_sub_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from gui.impl.gen.view_models.views.lobby.battle_results.random.random_battle_results_view_model import RandomBattleResultsViewModel as RandomBattleResultsViewModel
from gui.impl.lobby.battle_results.submodel_presenters.battle_info import BattleInfoSubPresenter as BattleInfoSubPresenter
from gui.impl.lobby.battle_results.submodel_presenters.player_satisfaction import PlayerSatisfactionSubPresenter as PlayerSatisfactionSubPresenter
from gui.impl.lobby.battle_results.submodel_presenters.financial_report import ManageableBonusSubPresenter as ManageableBonusSubPresenter, FinancialReportSubPresenter as FinancialReportSubPresenter
from gui.impl.lobby.battle_results.submodel_presenters.team_statistics import TeamStatisticsSubPresenter as TeamStatisticsSubPresenter
from gui.impl.lobby.battle_results.submodel_presenters.battle_achievements import BattleAchievementsSubPresenter as BattleAchievementsSubPresenter
from gui.impl.lobby.battle_results.submodel_presenters.battle_efficiency import BattleEfficiencySubPresenter as BattleEfficiencySubPresenter
from frameworks.wulf import ViewModel as ViewModel

class RandomBattleResultsSubPresenter(BattleResultsSubPresenter):
    def __init__(self, viewModel, parentView):
        ...
    @classmethod
    def getViewModelType(cls):
        ...
