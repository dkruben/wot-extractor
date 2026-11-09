# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/battle_results/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/battle_results/__init__.py
from __future__ import absolute_import
from fun_random_common.fun_constants import ARENA_BONUS_TYPE, FunSubModeImpl
from fun_random.gui.battle_results.fun_battle_results_sub_presenter import FunBattleResultsSubPresenter
from fun_random.gui.shared.fun_system_factory import registerBattleResultsSubPresenter
from account_helpers.AccountSettings import STATS_FUN_RANDOM_SORTING
from gui.shared.system_factory import registerBattleResultsStatsSorting
from gui.impl.gen import R
registerBattleResultsStatsSorting(ARENA_BONUS_TYPE.FUN_RANDOM, STATS_FUN_RANDOM_SORTING)
registerBattleResultsSubPresenter(FunSubModeImpl.DEFAULT, FunBattleResultsSubPresenter, R.views.fun_random.mono.lobby.battle_results())
