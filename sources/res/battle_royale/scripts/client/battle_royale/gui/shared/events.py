# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/shared/events.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/shared/events.py
from __future__ import absolute_import
from gui.shared.events import HasCtxEvent

class DeathZoneEvent(HasCtxEvent):
    UPDATE_DEATH_ZONE = 'deathZone/update'


class AirDropEvent(HasCtxEvent):
    AIR_DROP_SPAWNED = 'onAirDropSpawned'
    AIR_DROP_LANDED = 'onAirDropLanded'
    AIR_DROP_ENTERED = 'onAirDropEntered'
    AIR_DROP_LEFT = 'onAirDropLeft'
    AIR_DROP_NXT_SPAWNED = 'onAirDropNxtSpawned'


class LootEvent(HasCtxEvent):
    LOOT_PICKED_UP = 'onLootPickedUp'
