# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/DynObstacleComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/DynObstacleComponent.py
from __future__ import absolute_import
import CGF, GenericComponents, Physics
from script_component.DynamicScriptComponent import DynamicScriptComponent

class DynObstacleComponent(DynamicScriptComponent):

    def __init__(self):
        super(DynObstacleComponent, self).__init__()
        self._gameObject = None
        return

    def _onAvatarReady(self):
        if self.isHidden:
            return
        parentGO = self.entity.entityGameObject
        cgfQueue = CGF.CommandQueue(self.spaceID)
        self._gameObject = gameObject = cgfQueue.createGameObject()
        cgfQueue.createComponent(gameObject, CGF.HierarchyComponent, parentGO)
        cgfQueue.createComponent(gameObject, CGF.TransformComponent, self.localMatrix)
        cgfQueue.createComponent(gameObject, Physics.CollidersComponent, [Physics.MeshColliderDesc(self.modelPath, '')])
        model = cgfQueue.createComponent(gameObject, GenericComponents.DynamicModelComponent, self.modelPath)
        model.setOverlayEnabled(self.applyOverlay)

    def onDestroy(self):
        if self._gameObject is not None:
            CGF.removeGameObject(self._gameObject)
            self._gameObject = None
        super(DynObstacleComponent, self).onDestroy()
        return
