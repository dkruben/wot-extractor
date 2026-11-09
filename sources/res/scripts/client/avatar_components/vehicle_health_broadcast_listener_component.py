# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/avatar_components/vehicle_health_broadcast_listener_component.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/avatar_components/vehicle_health_broadcast_listener_component.py
from __future__ import absolute_import
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class VehicleHealthBroadcastListenerComponent(object):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def onEnterWorld(self, prereqs=None):
        pass

    def onLeaveWorld(self):
        pass

    def handleKey(self, isDown, key, mods):
        pass

    def onBecomePlayer(self):
        pass

    def onBecomeNonPlayer(self):
        pass

    def onVehicleHealthChanged(self, vehicleID, newHealth, attackerID, attackReasonID, attackReasonExtID):
        self.guiSessionProvider.setVehicleHealth(False, vehicleID, newHealth, attackerID, attackReasonID)
