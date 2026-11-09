# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/battle_results/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/battle_results/__init__.py
from __future__ import absolute_import
from account_helpers.AccountSettings import STATS_REGULAR_SORTING
from constants import ARENA_BONUS_TYPE
from gui.shared.system_factory import registerBattleResultsStatsSorting
registerBattleResultsStatsSorting(ARENA_BONUS_TYPE.EPIC_BATTLE, STATS_REGULAR_SORTING)
