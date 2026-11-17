# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/financial_report_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import lzip as lzip
from future.moves.itertools import zip_longest as zip_longest
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from gui.battle_results.pbs_helpers.economics import getDirectXpRecords as getDirectXpRecords, FinancialRecordValues as FinancialRecordValues, getDirectFreeXpRecords as getDirectFreeXpRecords, getDirectMoneyRecords as getDirectMoneyRecords
from gui.battle_results.presenters.packers.economics import xp_records as xp_records, common_records as common_records, free_xp_records as free_xp_records, credits_records as credits_records, gold_records as gold_records
from gui.battle_results.presenters.packers.economics.crystals_records import ORIGINAL_CRYSTALS as ORIGINAL_CRYSTALS, EVENT_CRYSTALS as EVENT_CRYSTALS, AUTO_EQUIP_CRYSTALS as AUTO_EQUIP_CRYSTALS, TOTAL_CRYSTALS as TOTAL_CRYSTALS
from gui.battle_results.presenters.packers.economics.currency_packers import DetailedCurrencyPacker as DetailedCurrencyPacker, CurrencyRecord as CurrencyRecord
from gui.battle_results.presenters.packers.economics.value_extractors import getBaseAccountValue as getBaseAccountValue, getPremiumAccountValue as getPremiumAccountValue
from gui.battle_results.reusable.records import RecordsIterator as RecordsIterator
from gui.battle_results.settings import CurrenciesConstants as CurrenciesConstants
from gui.impl.gen import R as R
from shared_utils import first as first
from soft_exception import SoftException as SoftException
RANK_BONUS_XP: Any

class FrontlineDetailedCurrencyPacker(DetailedCurrencyPacker):
    @classmethod
    def packModel(cls, model, currencyType, battleResults, vehIdx=-1):
        ...

class FrontlineXpDetailsPacker(FrontlineDetailedCurrencyPacker):
    _EARNED: tuple
    _EXPENSES = None
    _TOTAL: tuple
    @classmethod
    def _getExtractors(cls, battleResults):
        ...

class FrontlineCrystalsDetailsPacker(FrontlineDetailedCurrencyPacker):
    _EARNED: tuple
    _EXPENSES: tuple
    _TOTAL: tuple
    @classmethod
    def _getExtractors(cls, battleResults):
        ...

class FrontlineFreeXpDetailsPacker(FrontlineDetailedCurrencyPacker):
    _EARNED: tuple
    _EXPENSES = None
    _TOTAL: tuple
    @classmethod
    def _getExtractors(cls, battleResults):
        ...

class FrontlineCreditsStatisticsPacker(FrontlineDetailedCurrencyPacker):
    _EARNED: tuple
    _EXPENSES: tuple
    _TOTAL: tuple
    @classmethod
    def _getExtractors(cls, battleResults):
        ...

class FrontlineGoldStatisticsPacker(FrontlineDetailedCurrencyPacker):
    _EARNED: tuple
    _EXPENSES = None
    _TOTAL: tuple
    @classmethod
    def _getExtractors(cls, battleResults):
        ...
