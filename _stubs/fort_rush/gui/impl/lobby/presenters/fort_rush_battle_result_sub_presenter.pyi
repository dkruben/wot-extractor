# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/presenters/fort_rush_battle_result_sub_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from fort_rush.gui.impl.gen.view_models.views.lobby.post_battle_results_view.post_battle_results_view_model import PostBattleResultsViewModel as PostBattleResultsViewModel
from fort_rush.gui.impl.lobby.presenters.sub_presenters.battle_efficiency import FortRushBattleEfficiencySubPresenter as FortRushBattleEfficiencySubPresenter
from fort_rush.gui.impl.lobby.presenters.sub_presenters.battle_info import FortRushBattleInfoSubPresenter as FortRushBattleInfoSubPresenter
from fort_rush.gui.impl.lobby.presenters.sub_presenters.fort_rush_personal_rewards import FortRushPersonalRewardSubPresenter as FortRushPersonalRewardSubPresenter
from fort_rush.gui.impl.lobby.presenters.sub_presenters.team_statistics import FortRushTeamStatisticsSubPresenter as FortRushTeamStatisticsSubPresenter
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from frameworks.wulf import ViewModel as ViewModel

class FortRushBattleResultsSubPresenter(BattleResultsSubPresenter):
    def __init__(self, viewModel, parentView):
        ...
    @classmethod
    def getViewModelType(cls):
        ...
