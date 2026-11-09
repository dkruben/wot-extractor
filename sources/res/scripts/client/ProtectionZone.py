# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/ProtectionZone.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/ProtectionZone.py
from __future__ import absolute_import
import BigWorld, Math
from debug_utils import LOG_DEBUG

class ProtectionZone(BigWorld.Entity):

    def __init__(self):
        super(ProtectionZone, self).__init__(self)
        self.__lowerLeft = Math.Vector2(0, 0)
        self.__upperRight = Math.Vector2(0, 0)

    def onEnterWorld(self, prereqs):
        LOG_DEBUG('ProtectionZone added ', self.zoneID)
        self.__lowerLeft = Math.Vector2(self.position.x - self.lengthX * 0.5, self.position.z - self.lengthZ * 0.5)
        self.__upperRight = Math.Vector2(self.position.x + self.lengthX * 0.5, self.position.z + self.lengthZ * 0.5)
        protectionZoneComponent = BigWorld.player().arena.componentSystem.protectionZoneComponent
        if protectionZoneComponent is not None:
            protectionZoneComponent.addProtectionZone(self)
            if self.isActive:
                protectionZoneComponent.setProtectionZoneActive(self.zoneID, self.isActive)
        return

    def onLeaveWorld(self):
        protectionZoneComponent = BigWorld.player().arena.componentSystem.protectionZoneComponent
        if protectionZoneComponent is not None:
            protectionZoneComponent.removeProtectionZone(self)
        return

    def set_isActive(self, oldValue):
        LOG_DEBUG('ProtectionZone active: ' + str(self.isActive))
        protectionZoneComponent = BigWorld.player().arena.componentSystem.protectionZoneComponent
        if protectionZoneComponent is not None:
            protectionZoneComponent.setProtectionZoneActive(self.zoneID, self.isActive)
        return

    @property
    def bound(self):
        return (self.__lowerLeft, self.__upperRight)
