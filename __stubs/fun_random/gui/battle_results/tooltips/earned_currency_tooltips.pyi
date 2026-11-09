# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/battle_results/tooltips/earned_currency_tooltips.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from fun_random.gui.battle_results.economics.fun_tmen_xp_packer import FunTmenXpPacker as FunTmenXpPacker
from fun_random.gui.battle_results.economics.fun_currency_packers import FunCreditsPacker as FunCreditsPacker, FunCrystalsPacker as FunCrystalsPacker, FunXpPacker as FunXpPacker, FunGoldPacker as FunGoldPacker
from fun_random.gui.impl.gen.view_models.views.lobby.tooltips.fun_random_economic_tooltip_view_model import CurrencyType as CurrencyType
from gui.battle_results.presenters.packers.interfaces import ITooltipPacker as ITooltipPacker
from gui.battle_results.settings import CurrenciesConstants as CurrenciesConstants
from fun_random.gui.impl.gen.view_models.views.lobby.tooltips.fun_random_economic_tooltip_view_model import FunRandomEconomicTooltipViewModel as FunRandomEconomicTooltipViewModel
from gui.battle_results.stats_ctrl import BattleResults as BattleResults

class FunEarnedCurrencyTooltipsPacker(ITooltipPacker):
    __slots__: tuple
    _CURRENCY_VALUES_PACKERS: dict
    @classmethod
    def packTooltip(cls, model, battleResults, ctx=None):
        ...
