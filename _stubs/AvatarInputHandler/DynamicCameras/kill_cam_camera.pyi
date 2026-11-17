# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/DynamicCameras/kill_cam_camera.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import math as math
from collections import namedtuple as namedtuple
from enum import Enum as Enum
from typing import Callable as Callable
import BigWorld as BigWorld
import Math as Math
import BattleReplay as BattleReplay
import math_utils as math_utils
from AvatarInputHandler.DynamicCameras.arcade_camera_helper import MinMax as MinMax
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from AvatarInputHandler.DynamicCameras.ArcadeCamera import ArcadeCamera as ArcadeCamera
from Math import MatrixAnimation as MatrixAnimation, Vector2 as Vector2, Vector3 as Vector3
from gui.shared.events import DeathCamEvent as DeathCamEvent
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackPauseManager as CallbackPauseManager
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any
PausedMomentInfo: Any
_MIN_TIME_TO_PLAYER = 2.0
_MAX_TIME_TO_PLAYER = 4.0
_MIN_DISTANCE_TO_PLAYER = 50
_MAX_DISTANCE_TO_PLAYER = 200
_FINISH_MOVE_DEGREE = 7
_LOOK_AT_KILLER_PITCH_OFFSET = 0.15
_SPOTTED_TRAJECTORY_DELAY = 0.5
_LOOK_AT_KILLER_YAW_OFFSET = 0.0
LOOK_AT_KILLER_DURATION = 5.0
_LOOK_AT_KILLER_TRANSITION = 1.0
_RESUME_TIME_SPEED = 0.2
_QUICK_SPIN_DURATION = 0.8
_TRAJECTORY_TIME_FOLLOW_SETBACK = 0.5
_FINAL_SPIN_DEGREE = 55
_KILLER_MARKER_DELAY = 1.0
_UNSPOTTED_MARKER_DELAY = 0.5
_PHASE_TRANSITION_DELAY = 0.5
_MARKER_FADEOUT_DELAY = 0.5
_HIDE_BUSHES_DURING_TRAJECTORY = False
_WATER_COLLISION_MAX_DISTANCE = 1000

class StartCamDirection(Enum):
    AWAY_FROM_TARGET = 'fromKiller'
    TOWARDS_TARGET = 'towardsKiller'

class KillCamera(ArcadeCamera):
    __guiSessionProvider: Any
    delayMgr: Any
    __isPaused: Any
    __bVisionActive: Any
    __cbIDWait: Any
    __spinManagerConfig: Any
    __delayMgr: Any
    __killerHuskID: Any
    __playerHuskID: Any
    __matrixAnimator: Any
    __currentState: Any
    __pausedInfo: Any
    __trajectoryPoints: Any
    __isCamAngleInverted: Any
    __originalVehicleProvider: Any
    __projectileTriNorm: Any
    __hasProjectilePierced: Any
    __hasNonPiercedDamage: Any
    __isSPG: Any
    __projectileData: Any
    __isRicochet: Any
    __onEndingCallback: Any
    __configCamDistance: Any
    __configPivotSettings: Any
    __cameraCollisionScaleMult: Any
    __configMovementDuration: Any
    __totalSpinDuration: Any
    __spinVectorAttacker: Any
    __spinVectorPlayer: Any
    __pauseDistRange: Any
    __pauseAngleRange: Any
    __defaultAngleRange: Any
    __defaultDistanceRange: Any
    __timeInMovement: Any
    __prevTime: Any
    __phase3EndAngleHE: Any
    __spottedKillerRadius: Any
    __spottedPlayerRadius: Any
    __spottedPlayerHERadiusOffset: Any
    __spottedKillerExplosionPitchOffset: Any
    __spottedKillerExplosionYawOffset: Any
    __spottedPhase1MarkerFadeOut: Any
    __spottedPhase2MarkerFadeOut: Any
    __trajectoryDelay: Any
    __finalSpinDelay: Any
    __unspottedRadius: Any
    __unspottedHERadiusOffset: Any
    __unspottedInitAngle: Any
    __unspottedPhase1Angle: Any
    __unspottedToPhase1SpinDuration: Any
    __unspottedPhase1FreezeDuration: Any
    __unspottedPhase2Angle: Any
    __unspottedToPhase2SpinDuration: Any
    __unspottedPhase2FreezeDuration: Any
    __unspottedPhase3Angle: Any
    __unspottedToPhase3SpinDuration: Any
    __unspottedPhase3FreezeDuration: Any
    __unspottedPitchOffset: Any
    vehicleMProv: Any
    _distRange: Any
    def __init__(self, dataSec, defaultOffset=None):
        ...
    @staticmethod
    def _getConfigsKey():
        ...
    def _createCamera(self, enable):
        ...
    @property
    def trajectoryPoints(self):
        ...
    @trajectoryPoints.setter
    def trajectoryPoints(self, value):
        ...
    @property
    def playerHuskID(self):
        ...
    @playerHuskID.setter
    def playerHuskID(self, value):
        ...
    @property
    def projectileTriNorm(self):
        ...
    @property
    def hasProjectilePierced(self):
        ...
    @property
    def hasNonPiercedDamage(self):
        ...
    @property
    def currentState(self):
        ...
    @projectileTriNorm.setter
    def projectileTriNorm(self, value):
        ...
    @hasProjectilePierced.setter
    def hasProjectilePierced(self, value):
        ...
    @hasNonPiercedDamage.setter
    def hasNonPiercedDamage(self, value):
        ...
    @property
    def isSPG(self):
        ...
    @isSPG.setter
    def isSPG(self, value):
        ...
    @property
    def isNonPenetratingExplosion(self):
        ...
    def setTestData(self, projectileData=None, isRicochet=None, isSPG=None, movementDuration=None):
        ...
    def enable(self, vehicleMProv=None, preferredPos=None, closesDist=False, turretYaw=None, gunPitch=None, camTransitionParams=None, initialPivotSettings=None):
        ...
    def disable(self):
        ...
    def resetCamera(self):
        ...
    def stopActiveVision(self):
        ...
    def setCollisionsOnlyAtPos(self, enable, cameraCollisionScaleMult=4.0):
        ...
    def calculatePhaseDurations(self, isSpotted):
        ...
    def isCameraRotationInverted(self, forInitialSpin=False):
        ...
    def setCameraToLookTowards(self, sourceVehicleID, targetVehicleID=None, mode=None, firstPoint=None, lastPoint=None, isInstant=True, isInverted=False, originatesFromVehicle=True):
        ...
    def startKillerVision(self, killerVehicleID, playerVehicleID, isRicochet, projData, onEndingCallback=...):
        ...
    def startPlayerVision(self, projData, onEndingCallback=...):
        ...
    @staticmethod
    def calculateProperTravelTime(points):
        ...
    def _updateProperties(self, state=None):
        ...
    def _updateCameraSettings(self, newDist):
        ...
    def __getCameraLength(self):
        ...
    def __getPointBeforeCollision(self, position, cameraLength):
        ...
    def __getPointAboveWater(self, position, cameraLength):
        ...
    def __shouldHideBushes(self, state):
        ...
    def __setCurrentState(self, state):
        ...
    def __enableTreeHiding(self, isHidden):
        ...
    def __setCursorCollision(self):
        ...
    def __collisionLoop(self, spaceID):
        ...
    def __setupCameraYawPitchBeforeSpin(self, spinVector, isInverted):
        ...
    def __onKillerVisionFinished(self):
        ...
    def __moveCameraTo(self, vehicleID, sourceVehicleID=None):
        ...
    def __setCameraSettings(self, targetMP=None, pivotSettings=None, cameraDistance=None, yawPitch=None):
        ...
    def __startPhaseOneUnspotted(self):
        ...
    def __transitionToUnspottedPhaseTwo(self):
        ...
    def __startPhaseTwoUnspotted(self):
        ...
    def __transitionToUnspottedPhaseThree(self):
        ...
    def __startPhaseThreeUnspotted(self):
        ...
    def __transitionToUnspottedFinish(self):
        ...
    def __startPhaseOneSpotted(self):
        ...
    def __transitionToSpottedPhaseTwo(self):
        ...
    def __startPhaseTwoSpotted(self):
        ...
    def __transitionToSpottedPhaseThree(self):
        ...
    def __startPhaseThreeSpotted(self):
        ...
    def __transitionToSpottedFinish(self):
        ...
    def __prepareMatrixWithTrajectoryPoints(self):
        ...
    def userInterruption(self, isPaused):
        ...
    def update(self, dx, dy, dz, rotateMode=True, zoomMode=True, updatedByKeyboard=False):
        ...
    def __pauseMove(self):
        ...
    def __resumeMove(self):
        ...
    def __setKillCamDistance(self, distance, spgOffset, duration=0):
        ...
    def __updateCameraSettingsOnPause(self, isPaused):
        ...
    def __startTransitionPhase(self):
        ...
    def __adjustCameraDistance(self, distance):
        ...

def _floatFromString(value):
    ...
def _boolFromString(value):
    ...
def _registerLocalConstantWatcher(constants, name, convert):
    ...
def getCameraAsSettingsHolder(settingsDataSec):
    ...
def convertDegreeToRad(angleDegree):
    ...
