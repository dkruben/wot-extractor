# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/presenters/packers/economics/credits_packer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.battle_results.presenters.packers.economics import credits_records as credits_records
from gui.battle_results.presenters.packers.economics.currency_packers import CurrencyPacker as CurrencyPacker, CurrencyGroup as CurrencyGroup
from gui.battle_results.presenters.packers.economics.common_records import AOGAS_FACTOR as AOGAS_FACTOR, AFK_VIOLATION as AFK_VIOLATION, DESERTER_VIOLATION as DESERTER_VIOLATION, SUICIDE_VIOLATION as SUICIDE_VIOLATION
from gui.battle_results.presenters.packers.economics.gold_records import GOLD_PIGGY_BANK as GOLD_PIGGY_BANK, GOLD_EVENT_PAYMENTS as GOLD_EVENT_PAYMENTS
from gui.battle_results.pbs_helpers.economics import getDirectMoneyRecords as getDirectMoneyRecords
from gui.impl.gen import R as R
_STR_PATH = R.strings.battle_results.details.calculations

class CreditsPacker(CurrencyPacker):
    _EARNED: Any
    _EXPENSES: Any
    _TOTAL: Any
    _ADDITIONAL: Any
    @classmethod
    def _getExtractors(cls, currencyType, battleResults):
        ...
