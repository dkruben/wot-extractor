# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/common/fort_rush_common/fort_rush_roster_config.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/common/fort_rush_common/fort_rush_roster_config.py
from __future__ import absolute_import
from UnitRoster import BaseUnitRoster, BaseUnitRosterLimits
from unit_roster_config import RosterSlot10
from fort_rush_common.fort_rush_constants import MAX_ELIGIBLE_VEHICLES

class FortRushRoster(BaseUnitRoster):
    MAX_SLOTS = 3
    MAX_EMPTY_SLOTS = 2
    SLOT_TYPE = RosterSlot10
    DEFAULT_SLOT_PACK = RosterSlot10().pack()
    LIMITS_TYPE = BaseUnitRosterLimits
    MAX_VEHICLES = MAX_ELIGIBLE_VEHICLES
