# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/ClientSelectableObject.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/ClientSelectableObject.py
from __future__ import absolute_import
import BigWorld, CGF, SoundGroups
from vehicle_systems.tankStructure import ColliderTypes
from hangar_selectable_objects import ISelectableObject

class ClientSelectableObject(BigWorld.Entity, ISelectableObject):

    @property
    def enabled(self):
        return self.__enabled

    def __init__(self, name='ClientSelectableObject'):
        BigWorld.Entity.__init__(self)
        ISelectableObject.__init__(self)
        self.__name = name
        self.__enabled = True
        self.__edged = False
        self.model = None
        return

    def prerequisites(self):
        if not self.modelName:
            return []
        collisionModels = self._getCollisionModelsPrereqs()
        collisionAssembler = BigWorld.CollisionAssembler(collisionModels, self.spaceID)
        return [
         self.modelName, collisionAssembler]

    def onEnterWorld(self, prereqs):
        cgfQueue = CGF.CommandQueue(self.spaceID)
        cgfQueue.setGameObjectName(self.entityGameObject, self.__name)
        if not self.modelName:
            return
        if self.modelName not in prereqs.failedIDs:
            model = prereqs[self.modelName]
            self.model = model
            self.filter = BigWorld.DumbFilter()
            self.model.addMotor(BigWorld.Servo(self.matrix))
            collisions = cgfQueue.createComponent(self.entityGameObject, BigWorld.CollisionComponent, self.spaceID, prereqs['collisionAssembler'])
            collisionData = ((0, self.model.matrix),)
            collisions.connect(self.id, ColliderTypes.DYNAMIC_COLLIDER, collisionData)

    def onLeaveWorld(self):
        self.setHighlight(False)

    def setEnable(self, enabled):
        self.__enabled = enabled
        if not self.__enabled:
            self.setHighlight(False)

    def setHighlight(self, show):
        if show:
            if not self.__edged and self.__enabled:
                self._addEdgeDetect()
                self.__edged = True
        elif self.__edged:
            self._delEdgeDetect()
            self.__edged = False

    def onMouseDown(self):
        pass

    def onMouseUp(self):
        pass

    def onMouseClick(self):
        if self.clickSoundName and self.__enabled:
            if self.isClick3DSound:
                SoundGroups.g_instance.playSoundPos(self.clickSoundName, self.model.position)
            else:
                SoundGroups.g_instance.playSound2D(self.clickSoundName)

    def _getModelHeight(self):
        return self.model.height

    def _getCollisionModelsPrereqs(self):
        collisionModels = (
         (
          0, self.modelName),)
        return collisionModels

    def _addEdgeDetect(self):
        BigWorld.wgAddEdgeDetectEntity(self, None, 0, False, self.edgeMode, False)
        return

    def _delEdgeDetect(self):
        BigWorld.wgDelEdgeDetectEntity(self)
