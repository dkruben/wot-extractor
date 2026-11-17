# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/vehicle_appearance/common_tank_appearance.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import random as random
import logging as logging
import typing as typing
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from past.builtins import xrange as xrange
import BigWorld as BigWorld
import WoT as WoT
import CGF as CGF
import GenericComponents as GenericComponents
import Triggers as Triggers
import Math as Math
import Vehicular as Vehicular
import NetworkFilters as NetworkFilters
import material_kinds as material_kinds
from Event import SafeEvent as SafeEvent, EventManager as EventManager
from cgf_client_common.prefab_loader import PrefabLoader as PrefabLoader
from cgf_modules.variable_components import VariableStorageComponent as VariableStorageComponent
from constants import IS_EDITOR as IS_EDITOR, VEHICLE_SIEGE_STATE as VEHICLE_SIEGE_STATE, UNKNOWN_RESPAWN_ID as UNKNOWN_RESPAWN_ID
from CustomEffectManager import CustomEffectManager as CustomEffectManager, EffectSettings as EffectSettings
from helpers.EffectMaterialCalculation import calcEffectMaterialIndex as calcEffectMaterialIndex
from helpers.prefab_effects import resolveGunPrefabEffects as resolveGunPrefabEffects
from VehicleStickers import VehicleStickers as VehicleStickers
from items.components.component_constants import MAIN_TRACK_PAIR_IDX as MAIN_TRACK_PAIR_IDX
from items.vehicle_items import CHASSIS_ITEM_TYPE as CHASSIS_ITEM_TYPE
from objects_hierarchy import ExtraSlotsMapItem as ExtraSlotsMapItem
from objects_hierarchy import PrefabsMapItem as PrefabsMapItem
from vehicle_systems import model_assembler as model_assembler
from vehicle_systems import camouflages as camouflages
from vehicle_systems.components.highlighter import Highlighter as Highlighter
from vehicle_systems.vehicle_composition import getExtraSlotMap as getExtraSlotMap, getObjectSlots as getObjectSlots, createVehicleComposition as createVehicleComposition, VehicleSlots as VehicleSlots, removeComposition as removeComposition
from vehicle_systems.vehicle_damage_state import VehicleDamageState as VehicleDamageState
from vehicle_systems.tankStructure import VehiclePartsTuple as VehiclePartsTuple, ModelsSetParams as ModelsSetParams, TankPartNames as TankPartNames, ColliderTypes as ColliderTypes, TankPartIndexes as TankPartIndexes, TankNodeNames as TankNodeNames, CgfTankNodes as CgfTankNodes, TankSoundObjectsIndexes as TankSoundObjectsIndexes, TankRenderMode as TankRenderMode
from vehicle_systems.components.CrashedTracks import CrashedTracksController as CrashedTracksController
from vehicle_systems.components.hull_aiming_controller import HullAimingController as HullAimingController
from vehicle_systems.components.vehicleDecal import VehicleDecal as VehicleDecal
from vehicle_systems.components.siegeEffectsController import SiegeEffectsController as SiegeEffectsController
from vehicle_systems.components.vehicle_shadow_manager import VehicleShadowManager as VehicleShadowManager
from vehicle_appearance.constants import DEFAULT_STICKERS_ALPHA as DEFAULT_STICKERS_ALPHA, AppearanceState as AppearanceState
from vehicle_appearance.component import VehicleAppearanceComponent as VehicleAppearanceComponent
from helpers import bound_effects as bound_effects, gEffectsDisabled as gEffectsDisabled
from vehicle_outfit.outfit import Outfit as Outfit
from items.battle_royale import isSpawnedBot as isSpawnedBot
from helpers import isPlayerAvatar as isPlayerAvatar
from ModelHitTester import ModelStatus as ModelStatus
from vehicle_systems.components.debris_crashed_track_component import DebrisCrashedTrackComponent as DebrisCrashedTrackComponent
from Vehicle import Vehicle as Vehicle
_logger: Any
MATKIND_COUNT = 3
MATKIND_COUNT_RANGE: Any
MAX_DISTANCE = 500
VEHICLE_PRIORITY_GROUP = 1
WHEELED_CHASSIS_PRIORITY_GROUP = 2
TANK_FRICTION_EVENT = 'collision_tank_friction_pc'
_LOD_DISTANCE_EXHAUST = 200.0
_LOD_DISTANCE_TRAIL_PARTICLES = 100.0
ActivateContext: Any
DeactivateContext: Any
DestroyContext: Any
UpdateContext: Any

class PartProperties(object):
    HIGHLIGHTABLE = 1
    HIGHLIGHTBYVISUAL = 2

class GunAnimators(object):
    _animatorsLinks: Any
    def __init__(self):
        ...
    def setup(self, count):
        ...
    def get(self, index):
        ...
    def set(self, index, gameObject):
        ...

class CommonTankAppearance(PrefabLoader):
    state: Any
    isConstructed: Any
    isComponentsCreated: Any
    compoundModel: Any
    boundEffects: Any
    fashions: Any
    fashion: Any
    typeDescriptor: Any
    id: Any
    vStrCD: Any
    vRespawnID: Any
    isAlive: Any
    isDestroyed: Any
    isCrewActive: Any
    isObserver: Any
    outfit: Any
    renderMode: Any
    terrainEffectMaterialNames: Any
    isInWater: Any
    isUnderwater: Any
    waterHeight: Any
    damageState: Any
    modelsSetParams: Any
    attachments: Any
    splineTracks: Any
    isFlying: Any
    isLeftSideFlying: Any
    isRightSideFlying: Any
    trackScrollController: Any
    wheelsState: Any
    wheelsSteering: Any
    burnoutLevel: Any
    transmissionSlip: Any
    vehicleStickers: Any
    isTurretDetached: Any
    weaponEnergy: Any
    isCompositionReady: Any
    filter: Any
    collisions: Any
    crashedTracksController: Any
    customEffectManager: Any
    detailedEngineState: Any
    detailedGunState: Any
    engineAudition: Any
    flyingInfoProvider: Any
    frictionAudition: Any
    gearbox: Any
    gunRecoil: Any
    gunAnimators: Any
    hullAimingController: Any
    leveredSuspension: Any
    suspension: Any
    suspensionSound: Any
    swingingAnimator: Any
    tracks: Any
    vehicleTraces: Any
    waterSensor: Any
    wheelsAnimator: Any
    collisionObstaclesCollector: Any
    tessellationCollisionSensor: Any
    __fashions: Any
    __outfit: Any
    _vehicle: Any
    _isPlayerVehicle: Any
    __wheelsGameObject: Any
    __filter: Any
    __typeDesc: Any
    __crashedTracksController: Any
    __currentDamageState: Any
    terrainMatKind: Any
    terrainGroundType: Any
    __terrainEffectMaterialNames: Any
    _chassisDecal: Any
    __splodge: Any
    __boundEffects: Any
    _splineTracks: Any
    __trackScrollCtl: Any
    __weaponEnergy: Any
    __systemStarted: Any
    _isTurretDetached: Any
    __isObserver: Any
    __attachments: Any
    __modelAnimators: Any
    turretMatrix: Any
    gunMatrix: Any
    _commonScroll: Any
    _commonSlip: Any
    _compoundModel: Any
    __filterRetrieversGo: Any
    _vehicleStickers: Any
    _vehicleInfo: Any
    __vID: Any
    __vStrCD: Any
    __vRespawnID: Any
    __renderMode: Any
    __forceDynAttachmentLoading: Any
    customizationGameObjects: Any
    __customEffectsEnabled: Any
    __useEngStartControlIdle: Any
    __ignoreEngineStart: Any
    _entityGameObject: Any
    __isCompositionReady: Any
    __eventManager: Any
    onComponentsCreated: Any
    onAppearanceActivated: Any
    _swingingAnimator: Any
    _gunRecoilLink: Any
    _gunAnimators: Any
    _engineAudition: Any
    _flyingInfoProvider: Any
    _frictionAudition: Any
    _hullAimingController: Any
    _vehicleTraces: Any
    _waterSensor: Any
    _collisions: Any
    _suspension: Any
    _leveredSuspension: Any
    _suspensionSound: Any
    _detailedEngineState: Any
    _detailedGunState: Any
    _gearbox: Any
    _generalWheelsAnimator: Any
    _tankWheelsAnimator: Any
    _tracks: Any
    _customEffectManager: Any
    _collisionObstaclesCollector: Any
    _tessellationCollisionSensor: Any
    _state: Any
    def isReady(self):
        ...
    def _setFashions(self, fashions, isTurretDetached=False):
        ...
    def _setOutfit(self, outfitCD):
        ...
    def __init__(self, spaceID):
        ...
    @property
    def slotPrefabs(self):
        ...
    def prerequisites(self, vID, vInfo, renderMode=None):
        ...
    def actualize(self, vInfo):
        ...
    def construct(self, isPlayer, resourceRefs):
        ...
    def destroy(self):
        ...
    def onDestroy(self, ctx):
        ...
    def onComponentsCreate(self):
        ...
    def activate(self, parentUuid):
        ...
    def onActivate(self, ctx):
        ...
    def deactivate(self):
        ...
    def onDeactivate(self, ctx):
        ...
    def update(self, ctx):
        ...
    def getVehicle(self):
        ...
    def isActualVehicle(self, vehicle):
        ...
    def setIgnoreEngineStart(self):
        ...
    def isIgnoreEngineStart(self):
        ...
    def setSwingingAnimator(self, gameObject):
        ...
    def resetSwingingAnimator(self):
        ...
    def setGunRecoil(self, gameObject):
        ...
    def setVehicleInfo(self, vehInfo):
        ...
    def setupGunMatrixTargets(self, target):
        ...
    def receiveShotImpulse(self, direction, impulse):
        ...
    def recoil(self):
        ...
    def multiGunRecoil(self, indexes):
        ...
    def computeFullVehicleLength(self):
        ...
    def setUseEngStartControlIdle(self, useIdle=False):
        ...
    def _initiateRecoil(self, gunNodeName, gunFireNodeName, gunRecoil):
        ...
    def _connectCollider(self, collisions):
        ...
    def computeVehicleHeight(self, collisions):
        ...
    def onWaterSplash(self, waterHitPoint, isHeavySplash):
        ...
    def onUnderWaterSwitch(self, isUnderWater):
        ...
    def getWheelsSteeringMax(self):
        ...
    def setCompositionReady(self, ready):
        ...
    def _initDirtComponent(self, ctx):
        ...
    def _initEngineAudition(self, ctx):
        ...
    def _initLodLinks(self, ctx):
        ...
    def _initDrivetrain(self, ctx):
        ...
    def _prepareOutfit(self, outfitCD):
        ...
    def _calcWeaponEnergy(self, collisions):
        ...
    def _setupModels(self):
        ...
    def _createStickers(self):
        ...
    def _destroyStickers(self):
        ...
    def _attachStickers(self, collisionComponent):
        ...
    def _detachStickers(self):
        ...
    @property
    def _vehicleColliderInfo(self):
        ...
    def _startSystems(self, ctx):
        ...
    def _stopSystems(self, ctx):
        ...
    def _destroySystems(self):
        ...
    def _onRequestModelsRefresh(self):
        ...
    def __updateModelStatus(self):
        ...
    def _onEngineStart(self):
        ...
    @staticmethod
    def _getShotEffectSlotName():
        ...
    def _getShotEffectCompositionItems(self):
        ...
    def createVehicleComposition(self, queue):
        ...
    def __assembleNonDamagedOnly(self, resourceRefs, isPlayer, queue):
        ...
    def _setupTracks(self, resourceRefs, queue):
        ...
    def __postSetupFilter(self, suspension, leveredSuspension):
        ...
    def _periodicUpdate(self, ctx):
        ...
    def __updateEffectsLOD(self, lodCalculator, customEffectManager, waterSensor):
        ...
    def _stopEffects(self, forceDelete=False):
        ...
    def playEffectWithStopCallback(self, effects):
        ...
    def playEffect(self, kind, *modifs):
        ...
    def _updateCurrTerrainMatKinds(self, terrainMatKindSensor, vehicleTraces):
        ...
    def onSiegeStateChanged(self, newState):
        ...
    def changeEngineMode(self, mode, forceSwinging=False):
        ...
    def changeSiegeState(self, siegeState):
        ...
    def turretDamaged(self):
        ...
    def maxTurretRotationSpeed(self):
        ...
    def _onCameraChanged(self, cameraName, currentVehicleId=None):
        ...
    def __onEngineStateGearUp(self):
        ...
    def __animatorCallback(self, name, time):
        ...
    def getCurrentModelsSet(self):
        ...
    def getTrackStates(self):
        ...
    def __shouldCreatePhysicalDestroyedTracks(self):
        ...
    def __shouldUseTrackCrashWithDebris(self, pairIndex, shouldCreateDebris):
        ...
    def _getTrackPairIndicesToDestroy(self, pairIndex):
        ...
    def _addCrashedTrack(self, isLeft, pairIndex, isSideFlying, hitPoint):
        ...
    def _delCrashedTrack(self, isLeft, pairIndex):
        ...
    def _updateAttachments(self):
        ...
    def _getWheelsFilters(self):
        ...
    def _initWheelsLinks(self, generalWheelsAnimator):
        ...
