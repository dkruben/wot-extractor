# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/AtGunpoint.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/AtGunpoint.py
from __future__ import absolute_import
import BigWorld
from helpers import dependency
from math_utils import almostZero
from skeletons.gui.battle_session import IBattleSessionProvider
ARTY_HIT_PREDICTION_EPSILON_YAW = 1e-05

class AtGunpoint(BigWorld.DynamicScriptComponent):
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        BigWorld.DynamicScriptComponent.__init__(self)

    def _avatar(self):
        avatar = BigWorld.player()
        if avatar.isObserver():
            attachedVehicle = avatar.getVehicleAttached()
            if not attachedVehicle or attachedVehicle.id != self.entity.id:
                return None
        return avatar

    def onDestroy(self):
        if self.entity.isMyVehicle:
            if self.attackers is not None:
                for hitYaw in self.attackers:
                    self.__guiSessionProvider.shared.hitDirection.removeArtyHitPrediction(hitYaw)

        return

    def setSlice_attackers(self, path, prev):
        if self.entity.isMyVehicle:
            if self.attackers is not None and self.entity.isAlive():
                newAttackers = self.attackers[path[-1][0]:path[-1][1]]
                for hitYaw in newAttackers:
                    if not prev or all(not self.__isSameYaw(prevHitYaw, hitYaw) for prevHitYaw in prev):
                        if self._avatar() is not None:
                            self.__guiSessionProvider.shared.hitDirection.addArtyHitPrediction(hitYaw)

            if prev is not None:
                for prevHitYaw in prev:
                    if not self.attackers or all(not self.__isSameYaw(prevHitYaw, hitYaw) for hitYaw in self.attackers):
                        self.__guiSessionProvider.shared.hitDirection.removeArtyHitPrediction(prevHitYaw)

        return

    def __isSameYaw(self, a, b):
        return almostZero(a - b, epsilon=ARTY_HIT_PREDICTION_EPSILON_YAW)
