# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/battle_results/sub_presenters/fun_personal_efficiency.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from frameworks.wulf import Array as Array
from fun_random.gui.battle_results.packers.fun_packers import FunRandomPersonalEfficiency as FunRandomPersonalEfficiency
from fun_random.gui.battle_results.tooltips.total_efficiency_tooltips import FunEfficiencyTooltipsPacker as FunEfficiencyTooltipsPacker
from fun_random.gui.impl.lobby.tooltips.fun_random_battle_results_efficiency_tooltip_view import PersonalEfficiencyParamTooltip as PersonalEfficiencyParamTooltip
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_results.personal_efficiency_model import PersonalEfficiencyModel as PersonalEfficiencyModel
from frameworks.wulf import ViewModel as ViewModel
from gui.battle_results.stats_ctrl import BattleResults as BattleResults

class FunPersonalEfficiencySubPresenter(BattleResultsSubPresenter):
    _PACKER_CLS = FunRandomPersonalEfficiency
    @classmethod
    def getViewModelType(cls):
        ...
    def packBattleResults(self, battleResults):
        ...
    def createToolTipContent(self, event, contentID):
        ...
