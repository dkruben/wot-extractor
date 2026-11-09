# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/battle_results/sub_presenters/fun_battle_info.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from fun_random.gui.battle_results.packers.fun_packers import FunRandomBattleInfo as FunRandomBattleInfo
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_random_battle_info_model import FunRandomBattleInfoModel as FunRandomBattleInfoModel
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from frameworks.wulf import ViewModel as ViewModel
from gui.battle_results.stats_ctrl import BattleResults as BattleResults

class FunBattleInfoSubPresenter(BattleResultsSubPresenter):
    _PACKER_CLS = FunRandomBattleInfo
    @classmethod
    def getViewModelType(cls):
        ...
    def packBattleResults(self, battleResults):
        ...
