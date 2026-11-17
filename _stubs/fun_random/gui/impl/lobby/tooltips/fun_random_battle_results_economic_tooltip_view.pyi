# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/tooltips/fun_random_battle_results_economic_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from fun_random.gui.battle_results.tooltips.earned_currency_tooltips import FunEarnedCurrencyTooltipsPacker as FunEarnedCurrencyTooltipsPacker
from fun_random.gui.impl.gen.view_models.views.lobby.tooltips.fun_random_economic_tooltip_view_model import FunRandomEconomicTooltipViewModel as FunRandomEconomicTooltipViewModel
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService

class FunRandomBattleResultsEconomicTooltipView(ViewImpl):
    __battleResults: Any
    __arenaUniqueID: Any
    __currencyType: Any
    def __init__(self, arenaUniqueID, currencyType):
        ...
    @property
    def arenaUniqueID(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __invalidateAll(self):
        ...
