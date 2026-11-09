# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/LSNitroAccelerationControl.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/LSNitroAccelerationControl.py
from __future__ import absolute_import
import BigWorld, Event, CommandMapping

class LSNitroAccelerationControl(BigWorld.DynamicScriptComponent):

    def __init__(self):
        super(LSNitroAccelerationControl, self).__init__()
        self._eManager = Event.EventManager()
        self.onActivate = Event.Event(self._eManager)

    def onDestroy(self):
        self._eManager.clear()

    def handleKey(self, isDown, key, _):
        cmdMap = CommandMapping.g_instance
        keyCaptured = cmdMap.isFired(CommandMapping.CMD_CM_VEHICLE_SWITCH_AUTOROTATION, key) and isDown
        if not keyCaptured:
            return False
        else:
            vehicle = BigWorld.player().getVehicleAttached()
            if vehicle is not None and vehicle.isPlayerVehicle and vehicle.isAlive():
                self.onActivate()
            return True
