# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/CompoundAppearance.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import math as math
import typing as typing
from Compound import AppearanceDeactivatedEvent as AppearanceDeactivatedEvent
from builtins import range as range
from functools import partial as partial
from math import tan as tan
from enum import IntEnum as IntEnum
import BigWorld as BigWorld
import CGF as CGF
import GenericComponents as GenericComponents
import Math as Math
import Vehicular as Vehicular
import constants as constants
import items.vehicles
import BattleReplay as BattleReplay
import SoundGroups as SoundGroups
import Compound as Compound
from CustomEffect import EffectSettings as EffectSettings
from CustomEffectManager import CustomEffectManager as CustomEffectManager
from Event import Event as Event
from vehicle_hierarchy import ReparentToRootOnHierarchyDestroy as ReparentToRootOnHierarchyDestroy
from debug_utils import LOG_ERROR as LOG_ERROR
from aih_constants import ShakeReason as ShakeReason
from shared_utils import findFirst as findFirst
from items.components.component_constants import MAIN_TRACK_PAIR_IDX as MAIN_TRACK_PAIR_IDX, DEFAULT_TRACK_HIT_VECTOR as DEFAULT_TRACK_HIT_VECTOR
from vehicle_systems.components.hull_aiming_controller import HullAimingController as HullAimingController
from vehicle_systems.components.terrain_circle_component import TerrainCircleComponent as TerrainCircleComponent
from vehicle_systems.components import engine_state as engine_state
from vehicle_systems.components.vehicle_shadow_manager import VehicleShadowManager as VehicleShadowManager
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak, loadingPriority as loadingPriority
from vehicle_systems.tankStructure import VehiclePartsTuple as VehiclePartsTuple, TankNodeNames as TankNodeNames, TankPartIndexes as TankPartIndexes, TankSoundObjectsIndexes as TankSoundObjectsIndexes
from vehicle_systems.components.highlighter import Highlighter as Highlighter
from vehicle_systems.vehicle_composition import removeComposition as removeComposition
from helpers.EffectsList import SpecialKeyPointNames as SpecialKeyPointNames
from vehicle_systems import camouflages as camouflages
from vehicle_systems import model_assembler as model_assembler
from VehicleEffects import DamageFromShotDecoder as DamageFromShotDecoder
from vehicle_appearance.constants import DIRT_UPDATE_MIN_TIME as DIRT_UPDATE_MIN_TIME
from vehicle_appearance.component import VehicleAppearanceComponent as VehicleAppearanceComponent
from vehicle_appearance.common_tank_appearance import CommonTankAppearance as CommonTankAppearance
from vehicle_systems.components.CrashedTracks import CrashedTracksController as CrashedTracksController
from vehicle_systems.components.siegeEffectsController import SiegeEffectsController as SiegeEffectsController
from Vehicle import Vehicle as Vehicle
from VehicleStickers import DamageStickerData as DamageStickerData
from vehicle_appearance.common_tank_appearance import ActivateContext as ActivateContext, UpdateContext as UpdateContext, DeactivateContext as DeactivateContext, DestroyContext as DestroyContext
_ROOT_NODE_NAME = 'V'
_GUN_RECOIL_NODE_NAME = 'G'
_PERIODIC_TIME_DIRT: tuple
_DIRT_ALPHA: Any
_MOVE_THROUGH_WATER_SOUND = '/vehicles/tanks/water'
_CAMOUFLAGE_MIN_INTENSITY = 1.0
_PITCH_SWINGING_MODIFIERS: tuple
_MIN_DEPTH_FOR_HEAVY_SPLASH = 0.5
_logger: Any
_PostmortemContext: Any
UpdateDirtContext: Any

class CompoundHolder(object):
    compound: Any
    def __init__(self, compound):
        ...

class PartsGameObjects(object):
    __gameObjects: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def getExistingGameObject(self, partName):
        ...
    def getPartGameObject(self, partName, spaceID, parentGO):
        ...

class _ActivationState(IntEnum):
    NOT_ACTIVATED = 0
    ACTIVATED = 1
    MODEL_UPDATING = 2
    MODEL_UPDATED = 3
    DEACTIVATED = 4

class CompoundAppearance(CommonTankAppearance):
    wheelsState: Any
    wheelsSteering: Any
    burnoutLevel: Any
    highlighter: Any
    turretMatrix: Any
    gunMatrix: Any
    __originalFilter: Any
    __terrainCircle: Any
    __showCircleDelayed: Any
    onModelChanged: Any
    __activationState: Any
    __dirtLastUpdateTime: Any
    __dirtNextUpdateTime: Any
    __inSpeedTreeCollision: Any
    __tmpGameObjects: Any
    __engineStarted: Any
    __engineStartScheduled: Any
    __turbochargerSoundPlaying: Any
    partsGameObjects: Any
    __resourceLoadID: Any
    __highlighter: Any
    _vehicle: Any
    _entityGameObject: Any
    _isPlayerVehicle: Any
    __customEffectsEnabled: Any
    _splineTracks: Any
    _loadingQueue: Any
    _isTurretDetached: Any
    _commonSlip: Any
    _commonScroll: Any
    _compoundModel: Any
    def __init__(self):
        ...
    def setVehicle(self, vehicle):
        ...
    def setVehicleInfo(self, vehInfo):
        ...
    def _initDirtComponent(self, ctx):
        ...
    def __arenaPeriodChanged(self, period, *otherArgs):
        ...
    @property
    def _vehicleColliderInfo(self):
        ...
    def onActivate(self, ctx):
        ...
    def disableCustomEffects(self):
        ...
    def deactivate(self):
        ...
    def onDeactivate(self, ctx):
        ...
    def isActualVehicle(self, vehicle):
        ...
    def _startSystems(self, ctx):
        ...
    def _onEngineStart(self):
        ...
    def __destroyEngineAudition(self, queue=None):
        ...
    def __processPostmortemComponents(self, postmrtCtx):
        ...
    def __prepareSystemsForDamagedVehicle(self, vehicle, isTurretDetached, postmrtCtx):
        ...
    def onDestroy(self, ctx):
        ...
    def construct(self, isPlayer, resourceRefs):
        ...
    def addTempGameObject(self, component, name):
        ...
    def removeTempGameObject(self, name):
        ...
    def removeTempGameObjectIfExists(self, name):
        ...
    def showStickers(self, show):
        ...
    def showTerrainCircle(self, radius=None, terrainCircleSettings=None):
        ...
    def hideTerrainCircle(self):
        ...
    @property
    def isTerrainCircleVisible(self):
        ...
    def updateTurretVisibility(self):
        ...
    def changeVisibility(self, modelVisible):
        ...
    def changeDrawPassVisibility(self, visibilityMask):
        ...
    def onVehicleHealthChanged(self, showEffects=True):
        ...
    def showAmmoBayEffect(self, mode, fireballVolume):
        ...
    def stopSwinging(self):
        ...
    def removeDamageSticker(self, code):
        ...
    def addDamageSticker(self, code, stickerID, prefabEffIndex, data, isActive=False):
        ...
    def receiveShotImpulse(self, direction, impulse):
        ...
    def addCrashedTrack(self, isLeft, pairIndex=0, index=None):
        ...
    def addSimulatedCrashedTrack(self, index, trackInAir, hitPoint=None):
        ...
    def delCrashedTrack(self, isLeft, pairIndex=0):
        ...
    def onChassisDestroySound(self, isLeft, destroy, wheelsIdx=-1, trackPairIdx=...):
        ...
    def turretDamaged(self):
        ...
    def maxTurretRotationSpeed(self):
        ...
    def _prepareOutfit(self, outfitCD):
        ...
    def _initiateRecoil(self, gunNodeName, gunFireNodeName, gunRecoil):
        ...
    def _getWheelsFilters(self):
        ...
    def __applyVehicleOutfit(self):
        ...
    def getBounds(self, partIdx):
        ...
    def __requestModelsRefresh(self):
        ...
    def __onModelsRefresh(self, modelState, resourceList):
        ...
    def __reparentEffects(self):
        ...
    def __activateOnModelUpdate(self, ctx):
        ...
    def __onCrewKilled(self):
        ...
    def onWaterSplash(self, waterHitPoint, isHeavySplash):
        ...
    def onUnderWaterSwitch(self, isUnderWater):
        ...
    def updateTracksScroll(self, leftScroll, rightScroll):
        ...
    def _periodicUpdate(self, ctx):
        ...
    def updateDirt(self, ctx):
        ...
    def deviceStateChanged(self, deviceName, state):
        ...
    def __linkCompound(self):
        ...
    def _attachStickers(self, collisionComponent):
        ...
    def __updateStickers(self):
        ...
    def __updateClanSticker(self):
        ...
    def __updateInsigniaSticker(self):
        ...
    def __createTerrainCircle(self):
        ...
    def __attachTerrainCircle(self):
        ...
    def computeFullVehicleLength(self):
        ...
    def setupGunMatrixTargets(self, target):
        ...
    def onFriction(self, otherID, frictionPoint, state):
        ...
    def _onCameraChanged(self, cameraName, currentVehicleId=None):
        ...
    def __updateTransmissionScroll(self, wheelsAnimator):
        ...
    def addCameraCollider(self, collisions=None):
        ...
    def removeCameraCollider(self):
        ...
    def onEngineDamageRisk(self, risk):
        ...
    def getWheelsSteeringMax(self):
        ...
    def __vehicleUpdated(self, vehicleId):
        ...
    def __setTurbochargerSound(self, optDevices):
        ...
