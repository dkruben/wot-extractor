# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/presenters/packers/economics/crystals_packer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen import R as R
from gui.battle_results.presenters.packers.economics.currency_packers import CurrencyPacker as CurrencyPacker, CurrencyGroup as CurrencyGroup
from gui.battle_results.presenters.packers.economics.crystals_records import ORIGINAL_CRYSTALS as ORIGINAL_CRYSTALS, EVENT_CRYSTALS as EVENT_CRYSTALS, AUTO_EQUIP_CRYSTALS as AUTO_EQUIP_CRYSTALS, TOTAL_CRYSTALS as TOTAL_CRYSTALS
_STR_PATH = R.strings.battle_results.details.calculations

class CrystalsPacker(CurrencyPacker):
    _EARNED: Any
    _EXPENSES: Any
    _TOTAL: Any
    @classmethod
    def _getExtractors(cls, currencyType, battleResults):
        ...
