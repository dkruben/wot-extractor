# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/battle_results/sub_presenters/fun_personal_info.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.battle_results.presenters.packers.user_info import PersonalInfo as PersonalInfo
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_battle_results_view_model import FunBattleResultsViewModel as FunBattleResultsViewModel
from frameworks.wulf import ViewModel as ViewModel
from gui.battle_results.stats_ctrl import BattleResults as BattleResults

class FunPersonalInfoSubPresenter(BattleResultsSubPresenter):
    @classmethod
    def getViewModelType(cls):
        ...
    def packBattleResults(self, battleResults):
        ...
