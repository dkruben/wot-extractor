# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/BasicMine.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/BasicMine.py
from __future__ import absolute_import
from battleground.mines_object import loadMines
from entity_world_object import EntityWorldObject

class BasicMine(EntityWorldObject):

    def set_isDetonated(self, prev=None):
        if self.isDetonated:
            if self.worldObject is not None:
                self.worldObject.detonate()
        return

    def _loadWorldObject(self):
        return loadMines(self.ownerVehicleID, self._registerWorldObject)

    def _registerWorldObject(self, worldObject):
        worldObject.setPosition(self.position)
        worldObject.setIsEnemyMarkerEnabled(self.isMarkerEnabled)
        worldObject.setIsActivated(self.isActivated)
        worldObject.setActivationTimeDelay(self.activationTimeDelay)
        worldObject.setMineNumber(self.mineNumber)
        super(BasicMine, self)._registerWorldObject(worldObject)

    def set_isActivated(self, prev=None):
        if self.isActivated:
            if self.worldObject is not None:
                self.worldObject.activateMine()
        return

    def set_isMarkerEnabled(self, prev=None):
        if self.worldObject is not None:
            self.worldObject.enableEnemyIdleEffect(self.isMarkerEnabled)
        return
