# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/stored_sorting.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import STATS_REGULAR_SORTING as STATS_REGULAR_SORTING
from gui.shared.system_factory import collectBattleResultsStatsSorting as collectBattleResultsStatsSorting, registerBattleResultsStatsSorting as registerBattleResultsStatsSorting
from soft_exception import SoftException as SoftException
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
__all__: tuple
_DEFAULT_SORTING_KEY = STATS_REGULAR_SORTING

def writeStatsSorting(bonusType, iconType, sortDirection):
    ...
def readStatsSorting(key):
    ...
