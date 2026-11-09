# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/SMVehicleRespawnComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/SMVehicleRespawnComponent.py
from __future__ import absolute_import
import BigWorld
from VehicleRespawnComponent import VehicleRespawnComponent
from aih_constants import CTRL_MODE_NAME

class SMVehicleRespawnComponent(VehicleRespawnComponent):

    def _onVehicleAppeared(self):
        super(SMVehicleRespawnComponent, self)._onVehicleAppeared()
        avatar = BigWorld.player()
        inputHandler = avatar.inputHandler
        if avatar.playerVehicleID == self.entity.id and inputHandler is not None and inputHandler.ctrlModeName != CTRL_MODE_NAME.ARCADE:
            inputHandler.onControlModeChanged(CTRL_MODE_NAME.ARCADE)
        return

    def _explodeVehicleBeforeRespawn(self):
        if self.explodeVehicle:
            super(SMVehicleRespawnComponent, self)._explodeVehicleBeforeRespawn()
