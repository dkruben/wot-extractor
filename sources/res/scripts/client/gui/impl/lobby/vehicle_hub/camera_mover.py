# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/camera_mover.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/vehicle_hub/camera_mover.py
from __future__ import absolute_import
import math, CGF
from CameraComponents import OrbitComponent
from gui.subhangar.subhangar_state_groups import CameraMover
from helpers import dependency
from math_utils import reduceToPI
from skeletons.gui.shared.utils import IHangarSpace

class VehicleHubCameraMover(CameraMover):
    __hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self, transitionDuration):
        self._moveInstantly = True
        self._transitionDuration = transitionDuration

    def moveCamera(self, cameraManager, cameraName):
        moveInstantly = self._moveInstantly
        self._moveInstantly = False
        if moveInstantly:
            cameraManager.switchByCameraName(cameraName, instantly=True)
            return
        cameraManager.switchByCameraName(cameraName, instantly=True, resetTransform=False, forceUpdate=False)
        cameraGo = cameraManager.findCameraGameObjectByName(cameraName)
        if not cameraGo:
            cameraManager.switchByCameraName(cameraName, instantly=True)
            return
        hierarchy = CGF.findHierarchySingleton(self.__hangarSpace.spaceID)
        parentTransformComponent = hierarchy.getParent(cameraGo).findRead(CGF.TransformComponent)
        orbitComponent = cameraGo.findRead(OrbitComponent)
        if not orbitComponent or not parentTransformComponent:
            cameraManager.switchByCameraName(cameraName, instantly=True)
            return
        worldYaw = parentTransformComponent.worldTransform.yaw
        worldPitch = parentTransformComponent.worldTransform.pitch
        yaw = reduceToPI(orbitComponent.currentYaw + worldYaw + math.pi)
        pitch = reduceToPI(orbitComponent.currentPitch + worldPitch)
        targetPos = parentTransformComponent.worldTransform.translation
        distConstraints = orbitComponent.distLimits
        cameraManager.moveCamera(targetPos, yaw, pitch, distance=orbitComponent.currentDist, duration=self._transitionDuration, distConstraints=distConstraints)
