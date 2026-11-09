# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/subhangar/subhangar_state_groups.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/subhangar/subhangar_state_groups.py
from enum import Enum

class CameraMover(object):

    def moveCamera(self, cameraManager, cameraName):
        cameraManager.switchByCameraName(cameraName)

    def moveCameraFailed(self):
        pass


class SmoothCameraMover(CameraMover):

    def moveCamera(self, cameraManager, cameraName):
        cameraManager.switchByCameraName(cameraName, False)


class SubhangarStateGroupConfig(object):

    def __init__(self, stateGroups=(), cameraMover=CameraMover(), environmentName=None):
        self.stateGroups = stateGroups
        self.cameraMover = cameraMover
        self.environmentName = environmentName


class SubhangarStateGroupConfigProvider(object):

    def getSubhangarStateGroupConfig(self):
        raise NotImplementedError


class SubhangarStateGroups(Enum):
    Customization = 'CustomizationStates'
    PersonalMissions = 'PersonalMissionsStates'
    VehicleHub = 'VehicleHubStates'
    PetDenStorage = 'PetDenStorage'
    VehicleHubOverviewLargeTank = 'VehicleHubOverviewLargeTankStates'
    VehicleHubModulesLargeTank = 'VehicleHubModulesLargeTankStates'
    VehicleHubUpgradesLargeTank = 'VehicleHubUpgradesLargeTankStates'
    VehicleHubArmorLargeTank = 'VehicleHubArmorLargeTankStates'
    VehicleHubStatsLargeTank = 'VehicleHubStatsLargeTankStates'
    VehicleHubOverviewMediumTank = 'VehicleHubOverviewMediumTankStates'
    VehicleHubModulesMediumTank = 'VehicleHubModulesMediumTankStates'
    VehicleHubUpgradesMediumTank = 'VehicleHubUpgradesMediumTankStates'
    VehicleHubStatsMediumTank = 'VehicleHubStatsMediumTankStates'
    VehicleHubArmorMediumTank = 'VehicleHubArmorMediumTankStates'
    VehicleHubOverviewSmallTank = 'VehicleHubOverviewSmallTankStates'
    VehicleHubModulesSmallTank = 'VehicleHubModulesSmallTankStates'
    VehicleHubUpgradesSmallTank = 'VehicleHubUpgradesSmallTankStates'
    VehicleHubStatsSmallTank = 'VehicleHubStatsSmallTankStates'
    VehicleHubArmorSmallTank = 'VehicleHubArmorSmallTankStates'
    PostBattleSmall = 'PostBattleSmallStates'
    PostBattleMedium = 'PostBattleMediumStates'
    PostBattleLarge = 'PostBattleLargeStates'
    PostBattleVictory = 'PostBattleVictoryStates'
    PostBattleDefeat = 'PostBattleDefeatStates'
    PostBattleCommon = 'PostBattleCommonStates'
    Comp7PostBattleSmall = 'Comp7PostBattleSmallStates'
    Comp7PostBattleMedium = 'Comp7PostBattleMediumStates'
    Comp7PostBattleLarge = 'Comp7PostBattleLargeStates'
    Comp7PostBattleVictory = 'Comp7PostBattleVictoryStates'
    Comp7PostBattleDefeat = 'Comp7PostBattleDefeatStates'
    Comp7PostBattleCommon = 'Comp7PostBattleCommonStates'
