# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/VehicleInBattleSwitch.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/VehicleInBattleSwitch.py
from __future__ import absolute_import
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS
from script_component.ScriptComponent import ScriptComponent

class VehicleInBattleSwitch(ScriptComponent):
    REQUIRED_BONUS_CAP = ARENA_BONUS_TYPE_CAPS.VEHICLE_IN_BATTLE_SELECTION
