# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/DetachedTurret.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import GenericComponents as GenericComponents
from cgf_modules import game_events as game_events
from cgf_modules.game_events import ArmorHitPlacement as ArmorHitPlacement
from helpers.prefab_effects import resolveShotPrefabEffect as resolveShotPrefabEffect
from soft_exception import SoftException as SoftException
import math_utils as math_utils
import BigWorld as BigWorld
import CGF as CGF
import Math as Math
import logging as logging
import material_kinds as material_kinds
from VehicleEffects import DamageFromShotDecoder as DamageFromShotDecoder
from VehicleStickers import VehicleStickers as VehicleStickers
from vehicle_systems import vehicle_composition as vehicle_composition
from vehicle_systems.camouflages import prepareBattleOutfit as prepareBattleOutfit
from vehicle_systems.tankStructure import TankPartNames as TankPartNames, TankNodeNames as TankNodeNames, ColliderTypes as ColliderTypes, getPartModelsFromDesc as getPartModelsFromDesc, ModelsSetParams as ModelsSetParams, ModelStates as ModelStates
from helpers.EffectMaterialCalculation import calcSurfaceMaterialNearPoint as calcSurfaceMaterialNearPoint
from helpers.EffectsList import EffectsListPlayer as EffectsListPlayer, SoundStartParam as SoundStartParam, SpecialKeyPointNames as SpecialKeyPointNames
from helpers.bound_effects import ModelBoundEffects as ModelBoundEffects
from items import vehicles as vehicles
from constants import SERVER_TICK_LENGTH as SERVER_TICK_LENGTH, VEHICLE_HIT_EFFECT as VEHICLE_HIT_EFFECT
from debug_utils import LOG_DEBUG as LOG_DEBUG
_logger: Any
_MIN_COLLISION_SPEED = 3.5

class DetachedTurret(BigWorld.Entity):
    allTurrets: list
    __vehDescr: Any
    filter: Any
    __detachConfirmationTimer: Any
    __detachmentEffects: Any
    targetFullBounds: Any
    targetCaps: Any
    __componentsDesc: Any
    __vehicleStickers: Any
    model: Any
    __detachmentModel: Any
    def __init__(self):
        ...
    def reload(self):
        ...
    def __prepareModelAssembler(self):
        ...
    def __getModels(self):
        ...
    def prerequisites(self):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onActivated(self, collisions, effects):
        ...
    def update(self, effects):
        ...
    def show(self):
        ...
    def hide(self):
        ...
    def isAlive(self):
        ...
    def removeEdge(self):
        ...
    def drawEdge(self):
        ...
    def __createAndAttachStickers(self):
        ...
    def onLeaveWorld(self):
        ...
    def onStaticCollision(self, energy, point, normal):
        ...
    def showDamageFromShot(self, points, effectsIndex, prefabEffectsIndex, shellVelocity):
        ...
    def set_isUnderWater(self, prev):
        ...
    def stopDetachmentEffects(self, forceDelete=False, effects=None):
        ...
    def playDetachmentEffects(self, effect=...):
        ...
    def set_isCollidingWithWorld(self, prev):
        ...
    def changeAppearanceVisibility(self, isVisible):
        ...
    def __checkIsBeingPulled(self, effects):
        ...

class _TurretDetachmentEffects(object):
    __EFFECT_NAMES: dict
    _MAX_COLLISION_ENERGY = 98.10000000000001
    _MIN_COLLISION_ENERGY: Any
    _MIN_NORMALIZED_ENERGY = 0.1
    _DROP_ENERGY_PARAM = 'RTPC_ext_drop_energy'
    __turretModel: Any
    __detachmentEffectsDesc: Any
    __stateEffectListPlayer: Any
    __pullEffectListPlayer: Any
    __detachmentModel: Any
    __state: Any
    class State(object):
        FLYING = 0
        ON_GROUND = 1
    def __init__(self, turretModel, detachmentEffectsDesc, onGround):
        ...
    def destroy(self):
        ...
    def __stopStateEffects(self, forceDelete=False):
        ...
    def __stopPullEffects(self, forceDelete=False):
        ...
    def stopEffects(self, forceDelete=False):
        ...
    def notifyAboutCollision(self, energy, collisionPoint, effectMaterialIdx, groundEffect, underWater):
        ...
    def notifyAboutBeingPulled(self, isPulled, effectMaterialIdx):
        ...
    def __playPullEffect(self, effectMaterialIdx):
        ...
    def playStateEffect(self, startKeyPoint=...):
        ...
    def __normalizeEnergy(self, energy):
        ...

class _HitEffects(ModelBoundEffects):
    def __init__(self, model):
        ...
    def showHit(self, shotPoint, effectsIndex, nodeName, excludeTags=None):
        ...

class VehicleEnterTimer(object):
    isRunning: Any
    __vehicleID: Any
    __time: Any
    __maxTime: Any
    __timeOut: Any
    __callbackId: Any
    def __init__(self, vehicleID):
        ...
    def getVehicle(self):
        ...
    def __startCallback(self):
        ...
    def __onCallback(self):
        ...
    def start(self):
        ...
    def cancel(self):
        ...
    def _onDirectTick(self, vehicle):
        ...
    def _onCallbackTick(self, vehicle):
        ...
    def _onTimedOutTick(self):
        ...
    def _onSearchProgress(self, ratio):
        ...
    def _canAcceptVehicle(self, vehicle):
        ...

class SynchronousDetachment(VehicleEnterTimer):
    __turret: Any
    __entered: Any
    __finished: Any
    __acceptAnyVehicle: Any
    def __init__(self, turret):
        ...
    def onInit(self):
        ...
    def onEnterWorld(self):
        ...
    def __updateVisibility(self):
        ...
    def _onDirectTick(self, vehicle):
        ...
    def _onCallbackTick(self, vehicle):
        ...
    def _onTimedOutTick(self):
        ...
    def _onSearchProgress(self, ratio):
        ...
    def _canAcceptVehicle(self, vehicle):
        ...
    @staticmethod
    def needSynchronousDetachment(turret):
        ...
    @staticmethod
    def transferInputs(vehicle, turret):
        ...

class DetachedTurretSystem(CGF.System):
    DetachedTurretActivate: Any
    DetachedTurretIterate: Any
    Reactions: Any
    def commonUpdate(self):
        ...
    def periodUpdate(self):
        ...
