# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_results/stored_sorting.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_results/stored_sorting.py
import typing
from account_helpers import AccountSettings
from account_helpers.AccountSettings import STATS_REGULAR_SORTING
from gui.shared.system_factory import collectBattleResultsStatsSorting, registerBattleResultsStatsSorting
from soft_exception import SoftException
from constants import ARENA_BONUS_TYPE
__all__ = ('STATS_REGULAR_SORTING', 'writeStatsSorting', 'readStatsSorting')
registerBattleResultsStatsSorting(ARENA_BONUS_TYPE.RANDOM_NP2, STATS_REGULAR_SORTING)
registerBattleResultsStatsSorting(ARENA_BONUS_TYPE.REGULAR, STATS_REGULAR_SORTING)
registerBattleResultsStatsSorting(ARENA_BONUS_TYPE.EPIC_RANDOM, STATS_REGULAR_SORTING)
registerBattleResultsStatsSorting(ARENA_BONUS_TYPE.TRAINING, STATS_REGULAR_SORTING)
registerBattleResultsStatsSorting(ARENA_BONUS_TYPE.TOURNAMENT_REGULAR, STATS_REGULAR_SORTING)
registerBattleResultsStatsSorting(ARENA_BONUS_TYPE.WINBACK, STATS_REGULAR_SORTING)
registerBattleResultsStatsSorting(ARENA_BONUS_TYPE.MAPBOX, STATS_REGULAR_SORTING)
registerBattleResultsStatsSorting(ARENA_BONUS_TYPE.GLOBAL_MAP, STATS_REGULAR_SORTING)
registerBattleResultsStatsSorting(ARENA_BONUS_TYPE.CLAN, STATS_REGULAR_SORTING)
registerBattleResultsStatsSorting(ARENA_BONUS_TYPE.SORTIE_2, STATS_REGULAR_SORTING)
registerBattleResultsStatsSorting(ARENA_BONUS_TYPE.FORT_BATTLE_2, STATS_REGULAR_SORTING)
_DEFAULT_SORTING_KEY = STATS_REGULAR_SORTING

def writeStatsSorting(bonusType, iconType, sortDirection):
    key = collectBattleResultsStatsSorting().get(bonusType, _DEFAULT_SORTING_KEY)
    value = {'iconType': iconType, 
       'sortDirection': sortDirection}
    AccountSettings.setSettings(key, value)


def readStatsSorting(key):
    if key not in (_DEFAULT_SORTING_KEY,) + tuple(collectBattleResultsStatsSorting().values()):
        raise SoftException(('Sorting key {} is invalid').format(key))
    settings = AccountSettings.getSettings(key)
    return (settings.get('iconType'), settings.get('sortDirection'))
