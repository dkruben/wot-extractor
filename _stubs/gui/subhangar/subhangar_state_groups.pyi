# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/subhangar/subhangar_state_groups.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum

class CameraMover(object):
    def moveCamera(self, cameraManager, cameraName):
        ...
    def moveCameraFailed(self):
        ...

class SmoothCameraMover(CameraMover):
    def moveCamera(self, cameraManager, cameraName):
        ...

class SubhangarStateGroupConfig(object):
    stateGroups: Any
    cameraMover: Any
    environmentName: Any
    def __init__(self, stateGroups=..., cameraMover=..., environmentName=None):
        ...

class SubhangarStateGroupConfigProvider(object):
    def getSubhangarStateGroupConfig(self):
        ...

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
