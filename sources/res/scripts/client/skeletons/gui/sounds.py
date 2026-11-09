# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/skeletons/gui/sounds.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/sounds.py
from __future__ import absolute_import
import typing
from gui.battle_control.controllers.interfaces import IBattleController

class ISoundsController(object):

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    def stop(self, isDisconnected=False):
        raise NotImplementedError

    @property
    def system(self):
        raise NotImplementedError

    def enable(self):
        raise NotImplementedError

    def disable(self):
        raise NotImplementedError

    def isEnabled(self):
        raise NotImplementedError

    def setEnvForSpace(self, spaceID, newEnv):
        raise NotImplementedError


class IShotsResultSoundController(IBattleController):

    def getBestSoundEventName(self, bestSound):
        raise NotImplementedError

    def getBestShotResultSound(self, currBest, newSoundName, otherData):
        raise NotImplementedError

    def getVehicleHitResultSound(self, enemyVehID, hitFlags, enemiesHitCount):
        raise NotImplementedError
