# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/common/fun_random_common/fun_roster_config.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/common/fun_random_common/fun_roster_config.py
from __future__ import absolute_import
from UnitRoster import BaseUnitRoster, BaseUnitRosterLimits
from unit_roster_config import RosterSlot11

class FunRandomRoster(BaseUnitRoster):
    MAX_SLOTS = 3
    MAX_EMPTY_SLOTS = 2
    SLOT_TYPE = RosterSlot11
    DEFAULT_SLOT_PACK = RosterSlot11().pack()
    LIMITS_TYPE = BaseUnitRosterLimits
