# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/battle_control/arena_info/arena_vos.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/battle_control/arena_info/arena_vos.py
from __future__ import absolute_import
import typing
from story_mode_common.story_mode_constants import VEHICLE_BUNKER_TURRET_TAG
if typing.TYPE_CHECKING:
    from gui.battle_control.arena_info.arena_vos import VehicleTypeInfoVO

def getDisplayedClassTag(vehicleType, defaultClassTag):
    if VEHICLE_BUNKER_TURRET_TAG in vehicleType.tags:
        return VEHICLE_BUNKER_TURRET_TAG
    return defaultClassTag
