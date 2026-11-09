# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/battle_results/sub_presenters/fun_personal_rewards.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from frameworks.wulf import Array as Array
from fun_random.gui.battle_results.packers.fun_packers import FunRandomPersonalRewards as FunRandomPersonalRewards
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_random_reward_item_model import FunRandomRewardItemModel as FunRandomRewardItemModel
from fun_random.gui.impl.lobby.tooltips.fun_random_battle_results_economic_tooltip_view import FunRandomBattleResultsEconomicTooltipView as FunRandomBattleResultsEconomicTooltipView
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from gui.impl.gen import R as R
from gui.shared import events as events
from frameworks.wulf import ViewModel as ViewModel
from gui.battle_results.stats_ctrl import BattleResults as BattleResults

class FunPersonalRewardSubPresenter(BattleResultsSubPresenter):
    @classmethod
    def getViewModelType(cls):
        ...
    def packBattleResults(self, battleResults):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getListeners(self):
        ...
    def __onXpBonusStatusChanged(self, _=None):
        ...
