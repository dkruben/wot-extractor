# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/common/frontline_common/frontline_roster_config.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/common/frontline_common/frontline_roster_config.py
from __future__ import absolute_import
from UnitRoster import BaseUnitRoster, BaseUnitRosterLimits, BaseUnitRosterSlot

class EpicSlot(BaseUnitRosterSlot):
    DEFAULT_LEVELS = (8, 9)


class EpicRoster(BaseUnitRoster):
    MAX_SLOTS = 3
    MAX_EMPTY_SLOTS = 2
    SLOT_TYPE = EpicSlot
    DEFAULT_SLOT_PACK = EpicSlot().pack()
    LIMITS_TYPE = BaseUnitRosterLimits
    MIN_VEHICLES = 1
    MAX_VEHICLES = 10000
