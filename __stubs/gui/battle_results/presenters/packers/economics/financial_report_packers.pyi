# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/presenters/packers/economics/financial_report_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.battle_results.pbs_helpers.economics import getDirectXpRecords as getDirectXpRecords, getDirectFreeXpRecords as getDirectFreeXpRecords, getDirectMoneyRecords as getDirectMoneyRecords
from gui.battle_results.presenters.packers.economics import free_xp_records as free_xp_records, xp_records as xp_records, common_records as common_records, credits_records as credits_records, gold_records as gold_records
from gui.battle_results.presenters.packers.economics.crystals_records import ORIGINAL_CRYSTALS as ORIGINAL_CRYSTALS, AUTO_EQUIP_CRYSTALS as AUTO_EQUIP_CRYSTALS, TOTAL_CRYSTALS as TOTAL_CRYSTALS, EVENT_CRYSTALS as EVENT_CRYSTALS
from gui.battle_results.presenters.packers.economics.currency_packers import DetailedCurrencyPacker as DetailedCurrencyPacker
from gui.shared.system_factory import collectEarnedXpDetailsPacker as collectEarnedXpDetailsPacker, collectFreeXpDetailsPacker as collectFreeXpDetailsPacker, collectCreditsStatisticsPacker as collectCreditsStatisticsPacker

class CrystalsDetailsPacker(DetailedCurrencyPacker):
    _EARNED: tuple
    _EXPENSES: tuple
    _TOTAL: tuple
    @classmethod
    def _getExtractors(cls, battleResults):
        ...

class XpDetailsPacker(DetailedCurrencyPacker):
    _EARNED: tuple
    _EXPENSES = None
    _TOTAL: tuple
    @classmethod
    def _getExtractors(cls, battleResults):
        ...
    @classmethod
    def _getEarnedConfig(cls):
        ...

class FreeXpDetailsPacker(DetailedCurrencyPacker):
    _EARNED: tuple
    _EXPENSES = None
    _TOTAL: tuple
    @classmethod
    def _getExtractors(cls, battleResults):
        ...
    @classmethod
    def _getEarnedConfig(cls):
        ...

class CreditsStatisticsPacker(DetailedCurrencyPacker):
    _EARNED: tuple
    _EXPENSES: tuple
    _TOTAL: tuple
    @classmethod
    def _getExtractors(cls, battleResults):
        ...
    @classmethod
    def _getEarnedConfig(cls):
        ...

class GoldStatisticsPacker(DetailedCurrencyPacker):
    _EARNED: tuple
    _EXPENSES = None
    _TOTAL: tuple
    @classmethod
    def _getExtractors(cls, battleResults):
        ...
