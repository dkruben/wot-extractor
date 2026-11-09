# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/Loot.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/Loot.py
from __future__ import absolute_import
import BigWorld, CGF, Math
from battleground.loot_object import loadLootById
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from battle_royale.gui.shared.events import LootEvent

class Loot(BigWorld.Entity):

    def __init__(self, *args, **kwargs):
        super(Loot, self).__init__(*args, **kwargs)
        self.__lootDescr = None
        return

    def onEnterWorld(self, *args):
        self.__lootDescr = loadLootById(self.typeID)
        if self.__lootDescr is not None:
            CGF.loadAndCreatePrefabWithParent(self.__lootDescr.prefab, self.entityGameObject, Math.Vector3())
        return

    def onLeaveWorld(self):
        self.__lootDescr = None
        return

    def set_pickedUpBy(self, prev=None):
        g_eventBus.handleEvent(LootEvent(LootEvent.LOOT_PICKED_UP, ctx={'id': (self.id)}), scope=EVENT_BUS_SCOPE.BATTLE)
        if self.__lootDescr is not None:
            CGF.loadAndCreatePrefab(self.__lootDescr.prefabPickup, self.spaceID, self.position)
        return
