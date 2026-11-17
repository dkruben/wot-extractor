# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/VehicleGunRotator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import weakref as weakref
from collections import namedtuple as namedtuple
from functools import partial as partial
from future.utils import lrange as lrange
from math import pi as pi, fmod as fmod
import BattleReplay as BattleReplay
import BigWorld as BigWorld
import Math as Math
import math_utils as math_utils
from AvatarInputHandler import AimingSystems as AimingSystems
from constants import SERVER_TICK_LENGTH as SERVER_TICK_LENGTH, AIMING_MODE as AIMING_MODE, VEHICLE_SIEGE_STATE as VEHICLE_SIEGE_STATE, DEFAULT_GUN_INSTALLATION_INDEX as DEFAULT_GUN_INSTALLATION_INDEX
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID
from gun_rotation_shared import calcPitchLimitsFromDesc as calcPitchLimitsFromDesc, calcGunPitchCorrection as calcGunPitchCorrection, getLocalAimPoint as getLocalAimPoint
from helpers import dependency as dependency
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from projectile_trajectory import getShotAngles as getShotAngles
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicles.mechanics.mechanic_helpers import getVehicleMechanicComponent as getVehicleMechanicComponent
GunMarkerInfo: Any

class VehicleGunRotator(object):
    __INSUFFICIENT_TIME_DIFF = 0.02
    __MAX_TIME_DIFF = 0.2
    ANGLE_EPS = 1e-06
    __ROTATION_TICK_LENGTH = SERVER_TICK_LENGTH
    __AIMING_PERFECTION_DELAY = 1.0
    __AIMING_PERFECTION_RANGE: Any
    __TURRET_YAW_ALLOWED_ERROR_FACTOR = 0.4
    __TURRET_YAW_ALLOWED_ERROR_CONST: Any
    USE_LOCK_PREDICTION = True
    settingsCore: Any
    __sessionProvider: Any
    clientMode: Any
    showServerMarker: Any
    targetLastShotPoint: Any
    shotPointSourceFunctor: Any
    turretMatrix: Any
    gunMatrix: Any
    turretRotationSpeed: Any
    maxturretRotationSpeed: Any
    dispersionAngle: Any
    markerInfo: Any
    turretYaw: Any
    gunPitch: Any
    _avatar: Any
    __isStarted: Any
    __prevSentShotPoint: Any
    __targetLastShotPoint: Any
    __lastShotPoint: Any
    __shotPointSourceFunctor: Any
    __maxTurretRotationSpeed: Any
    __maxGunRotationSpeed: Any
    __speedsInitialized: Any
    __turretYaw: Any
    __gunPitch: Any
    __turretRotationSpeed: Any
    __dispersionAngles: Any
    __markerInfo: Any
    __clientMode: Any
    __showServerMarker: Any
    __time: Any
    __timerID: Any
    __turretMatrixAnimator: Any
    __gunMatrixAnimator: Any
    __isLocked: Any
    estimatedTurretRotationTime: Any
    __aimingPerfectionStartTime: Any
    __gunPosition: Any
    __gunIndex: Any
    __transitionCallbackID: Any
    __fixedShotAngles: Any
    ignoreAimingMode: Any
    def __init__(self, avatar):
        ...
    def destroy(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def applySettings(self, diff):
        ...
    def lock(self, isLocked):
        ...
    def reset(self):
        ...
    def update(self, turretYaw, gunPitch, maxTurretRotationSpeed, maxGunRotationSpeed):
        ...
    def forceGunParams(self, turretYaw, gunPitch, dispAngle):
        ...
    def fixShotPosition(self, turretYaw, gunPitch):
        ...
    def unFixShotPosition(self):
        ...
    def setShotPosition(self, vehicleID, shotPos, shotVec, dispersionAngle, forceValueRefresh=False):
        ...
    def predictLockedTargetShotPoint(self):
        ...
    def getShotParams(self, targetPoint, ignoreYawLimits=False, overrideShotDescr=None):
        ...
    def getCurShotPosition(self):
        ...
    def getCurShotDispersionAngles(self):
        ...
    def __set_clientMode(self, value):
        ...
    def __set_showServerMarker(self, value):
        ...
    def __set_targetLastShotPoint(self, value):
        ...
    def __set_shotPointSourceFunctor(self, value):
        ...
    def __shotPointSourceFunctor_Default(self):
        ...
    def updateRotationAndGunMarker(self, shotPoint, timeDiff):
        ...
    def __onTick(self):
        ...
    def __getTimeDiff(self):
        ...
    def __calcAngleBetweenShotPointAndMarker(self):
        ...
    def __trackPointOnServer(self, shotPoint):
        ...
    def stopTrackingOnServer(self):
        ...
    def __stopTrackingWithPerfection(self):
        ...
    def __updateShotPointOnServer(self, shotPoint):
        ...
    def __rotate(self, shotPoint, timeDiff):
        ...
    def __updateGunMarker(self, forceRelaxTime=None):
        ...
    def getNextTurretYaw(self, curAngle, shotAngle, speedLimit, angleLimits):
        ...
    def __syncWithServerTurretYaw(self, turretYaw):
        ...
    def __getRotationWays(self, curAngle, shotAngle):
        ...
    def __isOutOfLimits(self, angle, limits):
        ...
    def __applyTurretYawLimits(self, diff, angle, limits):
        ...
    def __getTurretYawWithSpeedLimit(self, angle, diff, limit):
        ...
    def getNextGunPitch(self, curAngle, shotAngle, timeDiff, angleLimits):
        ...
    def __getShotPosition(self, turretYaw, gunPitch, gunOffset=None, shotDescr=None):
        ...
    def getAttachedVehicleID(self):
        ...
    def updateMultiGunCollisionData(self):
        ...
    def __getGunMarkerInfo(self, shotPos, shotVec, dispersionAngles, gunIndex):
        ...
    def __getSupportMarkersInfo(self):
        ...
    def __getTargetedEnemyForGun(self, gunShotPosition, excludeTeam):
        ...
    def __getGunInstallationShotsInfo(self, gunInstallationIndex):
        ...
    def __getCappedShotTargetInfo(self, shotPos, shotVec, shotDescr):
        ...
    def __updateTurretMatrix(self, yaw, time):
        ...
    def __updateGunMatrix(self, pitch, time):
        ...
    def getAvatarOwnVehicleStabilisedMatrix(self):
        ...
    def switchActiveGun(self, activeGuns):
        ...
    def __onVehicleFeedbackReceived(self, eventID, vehicleID, value):
        ...
    def __getGunPitchLimits(self):
        ...
    def __getGunStaticPitch(self):
        ...
    def __getTurretYawLimits(self):
        ...
    def __getTurretStaticYaw(self):
        ...

class MatrixAnimator(object):
    matrix: Any
    __animMat: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def update(self, matrix, time):
        ...
