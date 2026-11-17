# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/presenters/sub_presenters/fort_rush_personal_rewards.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from frameworks.wulf import Array as Array
from fort_rush.gui.fort_rush_presenters_packers import FortRushPersonalRewards as FortRushPersonalRewards
from fort_rush.gui.impl.gen.view_models.views.lobby.post_battle_results_view.fort_rush_reward_item_model import FortRushRewardItemModel as FortRushRewardItemModel
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from gui.battle_results.stats_ctrl import BattleResults as BattleResults

class FortRushPersonalRewardSubPresenter(BattleResultsSubPresenter):
    @classmethod
    def getViewModelType(cls):
        ...
    def packBattleResults(self, battleResults):
        ...
