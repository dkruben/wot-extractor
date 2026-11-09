# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/messages/vehicle_messages.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/messages/vehicle_messages.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.messages import VehicleMessages

class LSVehicleMessages(VehicleMessages):
    _SKIP_EVENT_KEYS = ('DEVICE_CRITICAL_AT_WORLD_COLLISION', 'DEVICE_DESTROYED_AT_WORLD_COLLISION',
                        'DEVICE_CRITICAL_AT_RAMMING', 'DEVICE_DESTROYED_AT_RAMMING',
                        'DEVICE_STARTED_FIRE_AT_RAMMING', 'TANKMAN_HIT_AT_WORLD_COLLISION',
                        'DEVICE_CRITICAL_AT_SHOT', 'DEVICE_DESTROYED_AT_SHOT', 'DEVICE_STARTED_FIRE_AT_SHOT',
                        'TANKMAN_HIT_AT_SHOT', 'TANKMAN_RESTORED', 'TANKMAN_HIT_AT_MEDKIT_OVER',
                        'DEVICE_CRITICAL_AT_FIRE', 'DEVICE_DESTROYED_AT_FIRE', 'DEVICE_REPAIRED_TO_CRITICAL',
                        'DEVICE_REPAIRED', 'DEVICE_CRITICAL_AT_REPAIRKIT_OVER', 'ENGINE_CRITICAL_AT_UNLIMITED_RPM',
                        'ENGINE_DESTROYED_AT_UNLIMITED_RPM', 'ENGINE_CRITICAL_AT_BURNOUT',
                        'ENGINE_DESTROYED_AT_BURNOUT', 'FIRE_STOPPED', 'OPT_DEVICE_USED',
                        'SCREENSHOT_CREATED', 'DRR_SCALE_STEP_UP', 'DRR_SCALE_STEP_DOWN')

    def showMessage(self, key, args=None, extra=None, postfix=''):
        if any(key.startswith(event) for event in self._SKIP_EVENT_KEYS):
            return
        super(LSVehicleMessages, self).showMessage(key, args, extra, postfix)

    def _addGameListeners(self):
        super(LSVehicleMessages, self)._addGameListeners()
        ctrl = self.sessionProvider.shared.vehicleState
        if ctrl is not None:
            ctrl.onPostMortemSwitched += self._onPostMortemSwitched
        return

    def _removeGameListeners(self):
        super(LSVehicleMessages, self)._removeGameListeners()
        ctrl = self.sessionProvider.shared.vehicleState
        if ctrl is not None:
            ctrl.onPostMortemSwitched -= self._onPostMortemSwitched
        return

    def _onPostMortemSwitched(self, noRespawnPossible, respawnAvailable):
        self.clear()

    def _getPlayerInfo(self, entityID):
        ctx = self.sessionProvider.getCtx()
        vInfo = ctx.getArenaDP().getVehicleInfo(entityID)
        if vInfo.isEnemy():
            return vInfo.vehicleType.name
        return super(LSVehicleMessages, self)._getPlayerInfo(entityID)
