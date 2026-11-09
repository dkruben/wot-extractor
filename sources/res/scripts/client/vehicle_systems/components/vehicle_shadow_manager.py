# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicle_systems/components/vehicle_shadow_manager.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicle_systems/components/vehicle_shadow_manager.py
from __future__ import absolute_import
import BigWorld, CGF
from aih_constants import CTRL_MODE_NAME
from cgf_script.registration import registerComponent

@registerComponent
class VehicleShadowManager(object):
    domain = CGF.Domain.ClientEditor
    userVisible = False
    vseVisible = False

    def __init__(self, compound=None, playerTargetChangeEvent=None, cameraChangeModeEvent=None):
        self.__compoundModel = None
        self.__playerTargetChangeEvent = playerTargetChangeEvent
        self.__cameraChangeModeEvent = cameraChangeModeEvent
        self.__prevCameraMode = None
        if compound is not None:
            self.registerCompoundModel(compound)
        return

    def changePlayerTarget(self, isStatic):
        vehicle = BigWorld.player().getVehicleAttached()
        if vehicle is not None and vehicle.appearance is not None:
            self.updatePlayerTarget(vehicle.appearance.compoundModel)
        else:
            self.updatePlayerTarget(None)
        return

    def changeCameraMode(self, cameraMode, currentVehicleId=None):
        vehicle = BigWorld.player().getVehicleAttached()
        self.__prevCameraMode = cameraMode
        isValidMode = cameraMode in (CTRL_MODE_NAME.VIDEO, CTRL_MODE_NAME.DEBUG)
        if isValidMode:
            self.updatePlayerTarget(None)
        elif vehicle is not None and vehicle.appearance is not None:
            self.updatePlayerTarget(vehicle.appearance.compoundModel)
        return

    def activate(self):
        if self.__playerTargetChangeEvent:
            self.__playerTargetChangeEvent += self.changePlayerTarget
        if self.__cameraChangeModeEvent:
            self.__cameraChangeModeEvent += self.changeCameraMode

    def deactivate(self):
        if self.__playerTargetChangeEvent:
            self.__playerTargetChangeEvent -= self.changePlayerTarget
        if self.__cameraChangeModeEvent:
            self.__cameraChangeModeEvent -= self.changeCameraMode
        if self.__compoundModel is not None:
            BigWorld.resetPlayerTargetFrom(self.__compoundModel)
        return

    def updatePlayerTarget(self, compoundModel):
        BigWorld.setPlayerTargetTo(compoundModel)

    def registerCompoundModel(self, compoundModel):
        self.__compoundModel = compoundModel
        BigWorld.registerShadowCaster(compoundModel)

    def unregisterCompoundModel(self, compoundModel):
        BigWorld.unregisterShadowCaster(compoundModel)

    def reattachCompoundModel(self, vehicle, oldCompoundModel, newCompoundModel):
        self.unregisterCompoundModel(oldCompoundModel)
        self.registerCompoundModel(newCompoundModel)
        if BigWorld.player().getVehicleAttached() is vehicle:
            self.updatePlayerTarget(newCompoundModel)


class VehicleShadowSystem(CGF.System):
    ManagerActivated = CGF.ActivateReaction(CGF.ReactRw(VehicleShadowManager))
    ManagerDeactivated = CGF.DeactivateReaction(CGF.ReactRw(VehicleShadowManager))
    Reactions = CGF.Reactions(ManagerActivated, ManagerDeactivated)

    def update(self):
        for manager in self.reaction(self.ManagerActivated):
            self.__activateManager(manager)

        for manager in self.reaction(self.ManagerDeactivated):
            self.__deactivateManager(manager)

    def __activateManager(self, manager):
        manager.activate()

    def __deactivateManager(self, manager):
        manager.deactivate()
