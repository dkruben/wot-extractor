# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/abilities/shot_passion.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import BigWorld as BigWorld
import CGF as CGF
import Math as Math
from typing import List as List, Any as Any
from battle_royale.gui.constants import BattleRoyaleEquipments as BattleRoyaleEquipments
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from constants import IS_CLIENT as IS_CLIENT
from Event import EventsSubscriber as EventsSubscriber
from helpers import dependency as dependency
import math_utils as math_utils
import GenericComponents as GenericComponents
from items import vehicles as vehicles
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicle_systems.model_assembler import loadAppearancePrefab as loadAppearancePrefab
from vehicle_systems.tankStructure import TankNodeNames as TankNodeNames, TankPartNames as TankPartNames
from battle_royale.abilities.common import getEffectSuffixForGunLength as getEffectSuffixForGunLength
_GUN_LENGTH_RANGES: dict
_NODE_NAME_IDX: dict

class VehicleShotPassionComponent(object):
    ...

class UpgradeInProgressComponent(object):
    ...

# decorador original: @registerComponent
class ShotPassionComponent(object):
    editorTitle = 'Shot Passion Component'
    group = 'Abilities'
    domain = CGF.Domain.Client
    turretNode: _Any
    gunNode: _Any

# decorador original: @registerComponent
class ShotPassionNodeComponent(object):
    editorTitle = 'Shot Passion Node Component'
    group = 'Abilities'
    domain = CGF.Domain.Client
    effectTemplate: _Any
    maxAnimationStage: _Any

class ShotPassionSystem(CGF.System):
    __guiSessionProvider: _Any
    VehicleShotPassionActivated: _Any
    UpgradeDeactivated: _Any
    ShotPassionAccess: _Any
    ShotPassionNodeAccess: _Any
    Reactions: _Any
    __eventSubscriber: _Any
    def update(self):
        ...
    def __init__(self):
        ...
    def onMappingUnloaded(self):
        ...
    def visualizeShotPassion(self, shotPassionComponent):
        ...
    def endShotPassion(self, vehicle):
        ...
    def __launch(self, vehicleShotPassionComponent):
        ...
    def __setupPostLoadVFX(self, nodeGO, stage, appearance, nodeType, queue):
        ...
    def __onEquipmentComponentUpdated(self, _, vehicleID, data):
        ...
    def __setupVFX(self, nodeGO, queue, stage, appearance, nodeType, nodeAccess):
        ...
    def getEffectGO(self, partGO):
        ...
    def inBattleUpgradeCompleted(self, shotPassionComponent):
        ...
