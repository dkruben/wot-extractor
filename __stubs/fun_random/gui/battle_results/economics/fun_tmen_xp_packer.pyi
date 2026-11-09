# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/battle_results/economics/fun_tmen_xp_packer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
from itertools import chain as chain
import typing as typing
from fun_random.gui.battle_results.pbs_helpers import isPremiumAdvertisingShown as isPremiumAdvertisingShown, getTotalTMenXPToShow as getTotalTMenXPToShow
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.battle_results.presenters.packers.economics.currency_packers import CurrencyRecord as CurrencyRecord
from gui.battle_results.presenters.packers.economics.currency_packers import CurrencyPacker as CurrencyPacker, CurrencyGroup as CurrencyGroup
from gui.battle_results.presenters.packers.economics.common_records import DESERTER_VIOLATION as DESERTER_VIOLATION, SUICIDE_VIOLATION as SUICIDE_VIOLATION, AFK_VIOLATION as AFK_VIOLATION
from gui.battle_results.settings import CurrenciesConstants as CurrenciesConstants
from shared_utils import first as first
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
_STR_PATH = R.strings.battle_results.details.calculations
TOTAL_TMEN_XP: Any

class FunTmenXpPacker(CurrencyPacker):
    _EARNED: Any
    _TOTAL: Any
    @classmethod
    def packModel(cls, model, currencyType, battleResults):
        ...
    @classmethod
    def _getExtractors(cls, currencyType, battleResults):
        ...
    @classmethod
    def _getEarnedConfig(cls, battleResults):
        ...

def _getTmenXpValue(records, _, __, tID, xpList):
    ...
