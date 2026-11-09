# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/battle_results/fun_battle_results_sub_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from fun_random.gui.battle_results.sub_presenters.fun_battle_info import FunBattleInfoSubPresenter as FunBattleInfoSubPresenter
from fun_random.gui.battle_results.sub_presenters.fun_personal_info import FunPersonalInfoSubPresenter as FunPersonalInfoSubPresenter
from fun_random.gui.battle_results.sub_presenters.fun_personal_efficiency import FunPersonalEfficiencySubPresenter as FunPersonalEfficiencySubPresenter
from fun_random.gui.battle_results.sub_presenters.fun_personal_rewards import FunPersonalRewardSubPresenter as FunPersonalRewardSubPresenter
from fun_random.gui.battle_results.sub_presenters.fun_premium_plus import FunPremiumPlusSubPresenter as FunPremiumPlusSubPresenter
from fun_random.gui.battle_results.sub_presenters.fun_progression import FunProgressionSubPresenter as FunProgressionSubPresenter
from fun_random.gui.battle_results.sub_presenters.fun_team_stats import FunTeamStatsSubPresenter as FunTeamStatsSubPresenter
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_battle_results_view_model import FunBattleResultsViewModel as FunBattleResultsViewModel
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from frameworks.wulf import ViewModel as ViewModel

class FunBattleResultsSubPresenter(BattleResultsSubPresenter):
    def __init__(self, viewModel, parentView):
        ...
    @classmethod
    def getViewModelType(cls):
        ...
    def createToolTip(self, event):
        ...
