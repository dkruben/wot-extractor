# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/battleground/simulated_scene.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import logging as logging
import typing as typing
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import Event as Event
import BigWorld as BigWorld
import Math as Math
import SimulatedVehicle as SimulatedVehicle
import math_utils as math_utils
import CGF as CGF
from GenericComponents import Sequence as Sequence, StateSwitcherComponent as StateSwitcherComponent
import AreaDestructibles as AreaDestructibles
from avatar_components.avatar_postmortem_component import SimulatedVehicleType as SimulatedVehicleType
from avatar_components.CombatEquipmentManager import CombatEquipmentManager as CombatEquipmentManager
from battleground.kill_cam_visuals import EffectsController as EffectsController
from battleground.simulation_movement_tracker import SimulationMovementTracker as SimulationMovementTracker, SimulationMovementData as SimulationMovementData
from cgf_components.sequence_components import SequencePauseComponent as SequencePauseComponent, SequenceSnapshotComponent as SequenceSnapshotComponent
from cgf_components_common.vehicle_components import VehicleSequenceParamsAttachedComponent as VehicleSequenceParamsAttachedComponent
from constants import SHELL_TYPES as SHELL_TYPES, DEFAULT_GUN_INSTALLATION_INDEX as DEFAULT_GUN_INSTALLATION_INDEX
from gui.shared.gui_items.Vehicle import VEHICLE_CLASS_NAME as VEHICLE_CLASS_NAME
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackPauseManager as CallbackPauseManager, TimeDeltaMeter as TimeDeltaMeter
from items.components.gun_installation_components import GunInstallationSlot as GunInstallationSlot
from math_common import decimal_round as decimal_round
from skeletons.map_activities import IMapActivities as IMapActivities
from VehicleEffects import DamageFromShotDecoder as DamageFromShotDecoder
from vehicle_systems.tankStructure import TankPartNames as TankPartNames
from vehicles.mechanics.gun_mechanics.low_charge_shot.public.mechanic_events import postLowChargeShotInitialEvent as postLowChargeShotInitialEvent
from wotdecorators import noexcept as noexcept
from typing import Dict as Dict, List as List, Optional as Optional
_ANIMATION_EASING_CURVE = math_utils.linearTween
_ANIMATION_DISTANCE_UPPER_LIMIT = 8.0
ANIMATION_DURATION_BEFORE_SHOT = 3.0
ANIMATION_REAL_TIME_DURATION = 1.0
DATA_POINTS_AMOUNT = 5
_GAMEPLAY_ENTITIES_TO_HIDE: list
PostEffectSettings: Any
_logger: Any

class _SimulationTimeScale(object):
    PAUSED = 0.0
    REAL_TIME = 1.0

class SimulatedScene(object):
    __enabled: Any
    __postFx: Any
    __vehicleAnimators: Any
    __animatorsInProgress: Any
    __allAppearanceReadyVehicles: Any
    __allSimulatedVehicles: Any
    __rawSimulationData: Any
    __trajectoryPoints: Any
    __killerIsSpotted: Any
    __simulatedKillerID: Any
    __simulatedVictimID: Any
    __effectsController: Any
    __deathSceneObject: Any
    onAllVehiclesLoaded: Any
    onSimulatedSceneHasEnded: Any
    onAnimationsCompleted: Any
    __movementTracker: Any
    __killCamPostEffectSettings: Any
    __defaultPostEffectSettings: Any
    class _PostEffectsManager(object):
        __killCamPostEffectSettings: Any
        __defaultPostEffectSettings: Any
        def __init__(self, data):
            ...
        def destroy(self):
            ...
        def __getDefaultSettings(self):
            ...
        def enablePostEffects(self):
            ...
        def disablePostEffects(self):
            ...
    def __init__(self, dataSettings):
        ...
    @property
    def simulatedKillerID(self):
        ...
    @property
    def simulatedVictimID(self):
        ...
    def create(self):
        ...
    def destroy(self):
        ...
    def enableScene(self, rawSimulationData, trajectoryPoints, killerIsSpotted):
        ...
    def startAnimations(self, shotID):
        ...
    def disableScene(self):
        ...
    def hideEdgeEffects(self):
        ...
    def updateParticlesTimeScale(self, isPause=False):
        ...
    def updateVehicleEntities(self):
        ...
    def pauseOrResumeAnimations(self, isPause):
        ...
    def vehicleLoaded(self, vehicleID):
        ...
    def displayEffects(self, vehicleID):
        ...
    def saveKillSnapshot(self):
        ...
    def setPendingShotID(self, shotID):
        ...
    def getMovementData(self, shotID):
        ...
    def __onAnimatorFinished(self):
        ...
    def __simulatedVehiclesAppearanceReady(self):
        ...
    def __createSimulatedVehicle(self, simulatedData, isPlayerVehicle=False):
        ...
    def __truncateMovementData(self, movementDataT0, movementDataT1):
        ...
    @staticmethod
    def __pauseParticlesAndEffects(isPause):
        ...
    def __isVehicleAnimationInProgress(self):
        ...
    def __hideGameplayEntities(self):
        ...
    def __showGameplayEntities(self):
        ...
    def __pauseSequences(self, isPaused):
        ...
    def __createSimulatedVehicles(self):
        ...
    def __prepareAnimations(self):
        ...
    def __onSimulatedSceneEnded(self):
        ...
    def __isAttackerSPG(self):
        ...
    def __getTurretAndGunLimits(self, simVeh):
        ...
    def __getMechanicsInfo(self, simVehID):
        ...

class SimulationAnimator(CallbackPauseManager, TimeDeltaMeter):
    __TIME_SCALE: Any
    _pos0: Any
    _pos1: Any
    _rot0: Any
    _rot1: Any
    _tRot0: Any
    _tRot1: Any
    _duration: Any
    _simulatedVehicle: Any
    _vehicleRadius: Any
    _trackScroll: Any
    _posError: Any
    _engineMode: Any
    __timeScale: Any
    __speed: Any
    __yawSpeed: Any
    onFinished: Any
    __movementData: Any
    __section: Any
    __lastSection: Any
    __sectionDuration: Any
    __sectionElapsedTime: Any
    _numOfMovementData: Any
    _trackStates: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def start(self, vehicle, movementData):
        ...
    def finish(self):
        ...
    def __onFinish(self):
        ...
    def isInProcess(self):
        ...
    def stop(self):
        ...
    def pause(self, isInPause):
        ...
    def setTimeScale(self, timeScale):
        ...
    def reset(self):
        ...
    # decorador original: @noexcept
    def tick(self):
        ...
    def __stopTick(self):
        ...
    def __initSection(self, section):
        ...
    def __startSection(self, p0, p1, r0, r1, tY0, tY1, gP0, gP1, duration):
        ...
    def __setVehiclePosition(self, position, direction, turretYaw, gunPitch):
        ...
    def __updateTrackAndWheelScroll(self, leftScroll, rightScroll):
        ...

def _calculateWorldHitPoint(vehicle, segments):
    ...
def _updateDynAttachments(simulatedVehicle, dynAttachmentInfo):
    ...
