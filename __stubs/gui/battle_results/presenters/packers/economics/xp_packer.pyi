# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/presenters/packers/economics/xp_packer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as _CAPS
from gui.battle_results.presenters.packers.economics.currency_packers import CurrencyPacker as CurrencyPacker, CurrencyGroup as CurrencyGroup
from gui.battle_results.presenters.packers.economics import xp_records as xp_records, free_xp_records as free_xp_records, common_records as common_records
from gui.battle_results.pbs_helpers.economics import getDirectFreeXpRecords as getDirectFreeXpRecords, getDirectXpRecords as getDirectXpRecords
from gui.battle_results.settings import CurrenciesConstants as CurrenciesConstants
_logger: Any

class XpPacker(CurrencyPacker):
    _EARNED: Any
    _EXPENSES = None
    _TOTAL: Any
    _EXTRACTORS: dict
    @classmethod
    def _getExtractors(cls, currencyType, battleResults):
        ...
