# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/battle_results/economics/fun_currency_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from fun_random.gui.battle_results.pbs_helpers import isPremiumAdvertisingShown as isPremiumAdvertisingShown, getAdvertising as getAdvertising
from gui.battle_results.pbs_helpers.economics import getDirectMoneyRecords as getDirectMoneyRecords
from gui.battle_results.presenters.packers.economics.crystals_packer import CrystalsPacker as CrystalsPacker
from gui.battle_results.presenters.packers.economics.credits_packer import CreditsPacker as CreditsPacker
from gui.battle_results.presenters.packers.economics.gold_records import GOLD_EVENT_PAYMENTS as GOLD_EVENT_PAYMENTS
from gui.battle_results.presenters.packers.economics.xp_packer import XpPacker as XpPacker
from gui.impl.gen import R as R
from gui.battle_results.settings import CurrenciesConstants as CurrenciesConstants
from gui.battle_results.presenters.packers.economics.currency_packers import CurrencyPacker as CurrencyPacker, CurrencyGroup as CurrencyGroup
from shared_utils import first as first
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
from fun_random.gui.impl.gen.view_models.views.lobby.tooltips.fun_random_economic_tooltip_view_model import FunRandomEconomicTooltipViewModel as FunRandomEconomicTooltipViewModel
_STR_PATH = R.strings.fun_battle_results.economy.double

class FunCreditsPacker(CreditsPacker):
    __slots__: tuple
    @classmethod
    def packModel(cls, model, currencyType, battleResults):
        ...

class FunXpPacker(XpPacker):
    __slots__: tuple
    @classmethod
    def packModel(cls, model, currencyType, battleResults):
        ...

class FunCrystalsPacker(CrystalsPacker):
    __slots__: tuple
    @classmethod
    def packModel(cls, model, currencyType, battleResults):
        ...

class FunGoldPacker(CurrencyPacker):
    _EARNED: Any
    @classmethod
    def packModel(cls, model, currencyType, battleResults):
        ...
    @classmethod
    def _getExtractors(cls, currencyType, battleResults):
        ...
