# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/presenters/frontline_battle_result_sub_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.post_battle_results_view_model import PostBattleResultsViewModel as PostBattleResultsViewModel
from frontline.gui.impl.lobby.presenters.sub_presenters.battle_achievements import FrontlineBattleAchievementsSubPresenter as FrontlineBattleAchievementsSubPresenter
from frontline.gui.impl.lobby.presenters.sub_presenters.team_statistics import FrontlineTeamStatisticsSubPresenter as FrontlineTeamStatisticsSubPresenter
from frontline.gui.impl.lobby.presenters.sub_presenters.battle_info import FrontlineBattleInfoSubPresenter as FrontlineBattleInfoSubPresenter
from frontline.gui.impl.lobby.presenters.sub_presenters.financial_report import FrontlineFinancialReportSubPresenter as FrontlineFinancialReportSubPresenter
from frontline.gui.impl.lobby.presenters.sub_presenters.battle_efficiency import FrontlineBattleEfficiencySubPresenter as FrontlineBattleEfficiencySubPresenter
from frameworks.wulf import ViewModel as ViewModel

class FrontlineBattleResultsSubPresenter(BattleResultsSubPresenter):
    def __init__(self, viewModel, parentView):
        ...
    @classmethod
    def getViewModelType(cls):
        ...
