# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/LootArenaInfo.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/LootArenaInfo.py
from __future__ import absolute_import
import BigWorld
from gui.shared import EVENT_BUS_SCOPE, g_eventBus
from battle_royale.gui.shared.events import AirDropEvent

class LootArenaInfo(BigWorld.DynamicScriptComponent):

    def set_lootPositions(self, prevLootPositions):
        for item in prevLootPositions:
            event = AirDropEvent(AirDropEvent.AIR_DROP_LEFT, ctx=item)
            g_eventBus.handleEvent(event, scope=EVENT_BUS_SCOPE.BATTLE)

        for item in self.lootPositions:
            event = AirDropEvent(AirDropEvent.AIR_DROP_ENTERED, ctx=item)
            g_eventBus.handleEvent(event, scope=EVENT_BUS_SCOPE.BATTLE)

    def setSlice_lootPositions(self, path, oldValue):
        addedItems = _getNewValue(self.lootPositions, path)
        removedItems = oldValue
        for item in addedItems:
            event = AirDropEvent(AirDropEvent.AIR_DROP_ENTERED, ctx=item)
            g_eventBus.handleEvent(event, scope=EVENT_BUS_SCOPE.BATTLE)

        for item in removedItems:
            event = AirDropEvent(AirDropEvent.AIR_DROP_LEFT, ctx=item)
            g_eventBus.handleEvent(event, scope=EVENT_BUS_SCOPE.BATTLE)


def _getNewValue(sequence, path):
    startIndex, endIndex = path[-1]
    return sequence[startIndex:endIndex]
