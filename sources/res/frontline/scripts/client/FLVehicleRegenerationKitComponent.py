# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/FLVehicleRegenerationKitComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/FLVehicleRegenerationKitComponent.py
from __future__ import absolute_import
import BigWorld
from PlayerEvents import g_playerEvents
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from frontline import invalidateVehicleMarkerState, isAvatarReady
from vehicle_systems.stricted_loading import makeCallbackWeak

class FLVehicleRegenerationKitComponent(BigWorld.DynamicScriptComponent):
    _CALLBACK_DELAY = 0.5

    def __init__(self):
        super(FLVehicleRegenerationKitComponent, self).__init__()
        if isAvatarReady():
            self.__invalidateFLRegenerationKit()
        else:
            g_playerEvents.onAvatarReady += self.__onAvatarReady

    def set_regenerationKit(self, _=None):
        self.__invalidateFLRegenerationKit()

    def onLeaveWorld(self):
        pass

    def __onAvatarReady(self):
        g_playerEvents.onAvatarReady -= self.__onAvatarReady
        BigWorld.callback(self._CALLBACK_DELAY, makeCallbackWeak(self.__invalidateFLRegenerationKit))

    def __invalidateFLRegenerationKit(self):
        healPointEnter = {'senderKey': 'healPoint', 
           'isSourceVehicle': None, 
           'isInactivation': (None if not self.regenerationKit['isActive'] else self.regenerationKit['isActive']), 
           'endTime': (self.regenerationKit['endTime']), 
           'duration': (self.regenerationKit['duration'])}
        invalidateVehicleMarkerState(self.entity, healPointEnter, self.regenerationKit, VEHICLE_VIEW_STATE.HEALING, 'invalidateFLRegenerationKit')
        return
