# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/VehicleBRStPatrickComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/VehicleBRStPatrickComponent.py
from __future__ import absolute_import
import BigWorld
from script_component.DynamicScriptComponent import DynamicScriptComponent
import Event
from debug_utils import LOG_DEBUG

class VehicleBRStPatrickComponent(DynamicScriptComponent):
    onCoinsAdded = Event.Event()

    def set_coinsCount(self, prev):
        LOG_DEBUG('VehicleBRStPatrickComponent.set_coinsCount prev', prev, 'coinsCount', self.coinsCount)
        if self.__observedVehicleMatches():
            self.onCoinsAdded(self.coinsCount - prev, self.totalCoins, False)

    def set_teammateCoinsCount(self, prev):
        LOG_DEBUG('VehicleBRStPatrickComponent.set_teammateCoinsCount prev', prev, 'teammateCoinsCount', self.teammateCoinsCount)
        if self.__observedVehicleMatches():
            self.onCoinsAdded(self.teammateCoinsCount - prev, self.totalCoins, True)

    @property
    def totalCoins(self):
        return self.coinsCount + self.teammateCoinsCount

    def __observedVehicleMatches(self):
        attachedVehicle = BigWorld.player().getVehicleAttached()
        if attachedVehicle:
            return attachedVehicle.id == self.entity.id
        return False
