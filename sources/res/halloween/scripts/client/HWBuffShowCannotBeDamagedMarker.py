# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/HWBuffShowCannotBeDamagedMarker.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/HWBuffShowCannotBeDamagedMarker.py
from __future__ import absolute_import
import BigWorld
from helpers import dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent
from HWArenaPhasesComponent import HWArenaPhasesComponent
from skeletons.gui.battle_session import IBattleSessionProvider
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as _FET
from halloween_common.halloween_constants import BOSS_ROLE_TAG

def isInvulnerableBoss(vehicleID):
    vehicle = BigWorld.entities.get(vehicleID)
    if vehicle is None:
        return False
    else:
        if BOSS_ROLE_TAG not in vehicle.typeDescriptor.type.tags:
            return False
        arenaPhases = HWArenaPhasesComponent.getInstance()
        if arenaPhases is not None:
            return not arenaPhases.isBossVulnerable
        return False


class HWBuffShowCannotBeDamagedMarker(DynamicScriptComponent):
    _guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, *args, **kwargs):
        super(HWBuffShowCannotBeDamagedMarker, self).__init__(*args, **kwargs)
        self._alreadyShown = False

    def onDestroy(self):
        if self._isAvatarReady and not self._alreadyShown:
            self._setVehicleState()
        super(HWBuffShowCannotBeDamagedMarker, self).onDestroy()

    def _onAvatarReady(self):
        super(HWBuffShowCannotBeDamagedMarker, self)._onAvatarReady()
        self._setVehicleState()

    def _setVehicleState(self):
        self._alreadyShown = True
        if self.entity.isDestroyed:
            return
        isInvulnerable = isInvulnerableBoss(self.entity.id)
        feedback = self._guiSessionProvider.shared.feedback
        if isInvulnerable and feedback:
            feedback.setVehicleState(self.entity.id, _FET.VEHICLE_HIT)
