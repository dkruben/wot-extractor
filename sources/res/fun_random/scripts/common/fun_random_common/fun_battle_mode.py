# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/common/fun_random_common/fun_battle_mode.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/common/fun_random_common/fun_battle_mode.py
from __future__ import absolute_import
from constants import PREBATTLE_TYPE, QUEUE_TYPE
from constants_utils import AbstractBattleMode
from fun_random_common.battle_results import fun_random
from fun_random_common.fun_constants import ARENA_GUI_TYPE, UNIT_MGR_FLAGS, ROSTER_TYPE, INVITATION_TYPE, ARENA_BONUS_TYPE

class FunRandomBattleMode(AbstractBattleMode):
    _PREBATTLE_TYPE = PREBATTLE_TYPE.FUN_RANDOM
    _QUEUE_TYPE = QUEUE_TYPE.FUN_RANDOM
    _ARENA_BONUS_TYPE = ARENA_BONUS_TYPE.FUN_RANDOM
    _ARENA_GUI_TYPE = ARENA_GUI_TYPE.FUN_RANDOM
    _INVITATION_TYPE = INVITATION_TYPE.FUN_RANDOM
    _UNIT_MGR_NAME = 'FunRandomUnitMgr'
    _UNIT_MGR_FLAGS = UNIT_MGR_FLAGS.FUN_RANDOM
    _ROSTER_TYPE = ROSTER_TYPE.FUN_RANDOM_ROSTER
    _BATTLE_RESULTS_CONFIG = fun_random
    _SM_TYPE_BATTLE_RESULT = 'funRandomBattleResults'
    _SM_TYPES = [_SM_TYPE_BATTLE_RESULT]

    @property
    def _rosterClass(self):
        from fun_random_common.fun_roster_config import FunRandomRoster
        return FunRandomRoster
