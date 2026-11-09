# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/abilities/adaptation_restore_health.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
import typing as typing
import BattleRoyaleAbilities as BattleRoyaleAbilities
import BigWorld as BigWorld
import CGF as CGF
import GenericComponents as GenericComponents
import Triggers as Triggers
from battle_royale.gui.constants import BattleRoyaleEquipments as BattleRoyaleEquipments
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from constants import IS_CLIENT as IS_CLIENT
from items import vehicles as vehicles
from vehicle_systems.model_assembler import loadAppearancePrefab as loadAppearancePrefab
from BattleRoyaleAbilities import HealthRestoreAbilityMappingEntry as HealthRestoreAbilityMappingEntry
from battle_royale_artefacts import AdaptationHealthRestore as AdaptationHealthRestore
from vehicle_systems.CompoundAppearance import CompoundAppearance as CompoundAppearance
from typing import Optional as Optional, List as List
_logger: Any
_START_ANIMATION_THRESHOLD = 0.2
_ROOT_NODE_NAME = 'AdaptationHealthRestoreAbility'

class VehicleAdaptationHealthRestoreComponent(object):
    ...

class UpgradeInProgressComponent(object):
    ...

class Vehicle(object):
    ...

class ResourceLoaded(object):
    elapsedTime: Any
    def __init__(self, elapsedTime):
        ...

# decorador original: @registerComponent
class AdaptationHealthRestoreAbilityPart(object):
    domain = CGF.Domain.Client
    editorTitle = 'Adaptation Health Restore Ability Part'
    startAnimation: Any
    cycleAnimation: Any
    endAnimation: Any

# decorador original: @registerComponent
class AdaptationHealthRestoreEffectArea(object):
    domain = CGF.Domain.Client
    editorTitle = 'Adaptation Health Restore Effect Area'
    teamMateRestoringRadius: Any

class AdaptationHealthRestoreEffectSystem(CGF.System):
    VehicleAdaptationActivated: Any
    ResourceActivated: Any
    HealthRestoreCreated: Any
    VehicleAdaptationDeactivated: Any
    UpdateProgressDeactivated: Any
    VehicleAdaptationAccess: Any
    VehicleAccess: Any
    RestoreAbilityPartAccess: Any
    RemoveDelayedAccess: Any
    TransformAccess: Any
    Reactions: Any
    def update(self):
        ...
    def onBWComponentAdded(self, gameObject, vehicleAccess):
        ...
    def inBattleUpgradeCompleted(self, gameObject, vehicleAccess):
        ...
    def hideHealthGlowEffect(self, bwComponent, entityGameObject, restoreAbilityAccess, transformAccess):
        ...
    def showHealthGlowEffect(self, gameObject, vehicleAccess):
        ...
    def initializeEffect(self, effectGO, effectComponent, vehicleAdaptationAccess, queue):
        ...
    def onResourcesLoaded(self, vehicleAdaptationAccess, effectGO, *_):
        ...
    def onResourcesLoadedAdded(self, resource, effectRoot, restoreAbilityAccess, vehicleAdaptationAccess):
        ...
    def createParts(self, config, appearance, queue):
        ...
    def spawnStartAnimation(self, partComponent, gameObject):
        ...
    def spawnCycleAnimation(self, partComponent, gameObject):
        ...
    def spawnEndAnimation(self, partComponent, gameObject, effectRoot):
        ...
    @classmethod
    def loadPostEffect(cls, postEffectTarget, transformAccess):
        ...
    def scheduleDestroy(self, effectRoot, duration, queue):
        ...
    def iterParts(self, effectRoot, restoreAbilityAccess):
        ...
    @staticmethod
    def spawnEffect(effect, gameObject, queue, loop=False):
        ...
    @staticmethod
    def getVehicleAppearance(gameObject, vehicleAccess):
        ...
    @staticmethod
    def getEquipment():
        ...
    @classmethod
    def calculateEquipmentTime(cls, bwComponent):
        ...
    def findEffectRoots(self, gameObject):
        ...
    def findEquipComp(self, gameObject, vehicleAdaptationAccess):
        ...
    def getChildren(self, gameObject):
        ...
