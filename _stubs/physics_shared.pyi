# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/physics_shared.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import copy as copy
import math as math
import collections as collections
from future.utils import viewitems as viewitems
from past.builtins import xrange as xrange
from typing import Any as Any
import BigWorld as BigWorld
import Math as Math
from items import vehicles as vehicles
from items.components.component_constants import KMH_TO_MS as KMH_TO_MS, ZERO_VECTOR3 as ZERO_VECTOR3
from items.vehicles import VEHICLE_PHYSICS_TYPE as VEHICLE_PHYSICS_TYPE, VehicleDescriptor as VehicleDescriptor, VehicleDescrType as VehicleDescrType
from constants import IS_CLIENT as IS_CLIENT, IS_EDITOR as IS_EDITOR, SERVER_TICK_LENGTH as SERVER_TICK_LENGTH, SHOT_PREDICTION_BUFFER as SHOT_PREDICTION_BUFFER, HALF_SERVER_TICK as HALF_SERVER_TICK
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION, LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR
from gun_rotation_shared import encodeRestrictedValueToUint as encodeRestrictedValueToUint, decodeRestrictedValueFromUint as decodeRestrictedValueFromUint
G = 9.81
GRAVITY_FACTOR = 1.25
WEIGHT_SCALE = 0.001
GRAVITY_FACTOR_SCALED: _Any
PHYSICAL_INF = 1000000000
SUSP_COMPRESSION_MIN = 0.85
SUSP_COMPRESSION_MIN_MASS = 60.0
SUSP_COMPRESSION_MAX = 0.88
SUSP_COMPRESSION_MAX_MASS = 30.0
BODY_HEIGHT = 1.4
ROLLER_CONTACT_IGNORE_ANGLE = 25
ROLLER_HORIZONTAL_SURFACE_ANGLE = 35
SIDE_MOVEMENT_THRESHOLD: _Any
_SIMULATION_Y_BOUND = 1000.0
FREEZE_ANG_ACCEL_EPSILON = 0.35
FREEZE_ACCEL_EPSILON = 0.4
FREEZE_VEL_EPSILON = 0.15
FREEZE_ANG_VEL_EPSILON = 0.06
WIDTH_LONG = 6.2
WIDTH_VERY_LONG = 7.0
CLEARANCE_RATIO_LONG = 5.0
NUM_SPRINGS_LONG = 5
NUM_SPRINGS_NORMAL = 5
CMY_MIN = -0.15
CMY_MID = -0.2
CMY_MAX = -0.3
DYN_RATIO_MIN = 9.5
DYN_RATIO_MID = 13.0
DYN_RATIO_MAX = 21.0
CLEARANCE = 1.75
CLEARANCE_MIN = 0.55
CLEARANCE_MAX = 0.6
HARD_RATIO_MIN = 0.5
CLEARANCE_TO_LENGTH_MIN = 0.085
HARD_RATIO_MAX = 0.52
CLEARANCE_TO_LENGTH_MAX = 0.112
TRACK_LENGTH_MIN = 0.6
TRACK_LENGTH_MAX = 0.64
VEHICLE_ON_OBSTACLE_COLLISION_BOX_MIN_HEIGHT = 1.1
_LOG_INIT_PARAMS = False
RESTITUTION = 0.5
FRICTION_RATIO = 1.0
NUM_ITERATIONS = 10
NUM_ITERATIONS_ACCURATE = 40
MID_SOLVING_ITERATIONS = 4
NUM_SUBSTEPS_IN_STANDARD_MODE = 2
USE_SSE_SOLVER_IN_STANDARD_MODE = False
NUM_SUBSTEPS_IN_DETAILED_MODE = 3
USE_SSE_SOLVER_IN_DETAILED_MODE = False
NUM_SUBSTEPS = NUM_SUBSTEPS_IN_STANDARD_MODE
WARMSTARTING_VEHICLE_VEHICLE = False
WARMSTARTING_VEHICLE_STATICS = False
WARMSTARTING_THRESHOLD = 0.1
USE_PSEUDO_CONTACTS = True
ALLOWED_PENETRATION = 0.01
CONTACT_PENETRATION = 0.1
TRACKS_PENETRATION = 0.01
CONTACT_ENERGY_POW = 3.0
CONTACT_ENERGY_POW2 = 0.75
SLOPE_FRICTION_FUNC_DEF: _Any
SLOPE_FRICTION_FUNC_VAL: _Any
SLOPE_FRICTION_MODELS_FUNC_VAL: _Any
CONTACT_FRICTION_TERRAIN = 1.0
CONTACT_FRICTION_STATICS = 0.05
CONTACT_FRICTION_EXTRA = 0.3
CONTACT_FRICTION_DESTRUCTIBLES = 1.0
CONTACT_FRICTION_VEHICLES = 0.3
VEHICLE_ON_BODY_DEFAULT_FRICTION = 0.5
ROLLER_REACTION_COEFF_FOR_STATIC = 0.2
ROLLER_FRICTION_GAIN_MIN = 0.05
ROLLER_FRICTION_GAIN_MAX = 0.25
ROLLER_FRICTION_ANGLE_MIN = 20.0
ROLLER_FRICTION_ANGLE_MAX = 45.0
ANCHOR_MAX_REACTION_FACTOR = 0.5
ANCHOR_CONST_FRACTION = 0.0
ANCHOR_VEL_FACTOR = 0.0
ARENA_BOUNDS_FRICTION_HOR = 0.2
ARENA_BOUNDS_FRICTION_VERT = 1.0
_ALLOWER_RPM_EXCESS_UNBOUNDED = 1.4
_ABSOLUTE_SPEED_LIMIT = 25
ENGINE_RADIUS = 0.020000000000000004
g_confUpdaters: list
TRACK_SCROLL_LIMITS: tuple
_DEFAULT_FAKE_GEARBOX_SETTINGS: dict

def _cosDeg(angle):
    ...
def _sinDeg(angle):
    ...
def getDefaultChassisXPhysicsCfg():
    ...
def getDeafultVehicleModelXPhysicsCfg():
    ...
def getDefaultWheeledVehicleModelXPhysicsCfg():
    ...
def getDefaultWheeledChassisXPhysicsCfg():
    ...
def getDefaultTankVehicleXPhysicsShapeCfg():
    ...
def getDefaultWheeledVehicleXPhysicsShapeCfg():
    ...
def getDefaultVehicleXPhysicsShapeCfg():
    ...
def getDefaultVehicleXPhysicsCfg():
    ...
def getDefaultTankXPhysicsCfg():
    ...
def getDefaultWheeledTechXPhysicsCfg():
    ...
def getAppliedGravityMultiplier(physics, typeDesc):
    ...
def init():
    ...
def updateCommonConf():
    ...
def updateConf():
    ...
def updatePhysicsCfg(baseCfg, typeDesc, cfg):
    ...
def applyVehDescrMiscFactors(typeDescr, mode):
    ...
def configurePhysics(physics, baseCfg, typeDescr, gravityFactor, updateSiegeModeFromCfg):
    ...
def __computeModelShape(cfg, modelShapeCfg, typeDesc, boundingBoxes):
    ...
def configureModelShapePhysics(cfg, typeDesc):
    ...
def updatePhysics(physics, typeDesc, isSoftUpdate=False, gravityMultiplier=1.0):
    ...
def configurePhysicsMode(cfg, typeDesc, gravityFactor):
    ...
def applyRotationAndPowerFactors(cfg):
    ...
def initVehiclePhysicsServer(physics, typeDesc):
    ...
def initVehiclePhysicsForced(physics, typeDesc, forcedCfg):
    ...
def initVehiclePhysicsEditor(physics, typeDesc):
    ...
def initVehiclePhysicsClient(physics, typeDesc):
    ...
def computeBarrelLocalPoint(vehDescr, turretYaw, gunPitch):
    ...
def linearInterpolate(arg, argMin, argMax, valMin, valMax):
    ...
def _computeCenterOfMassShift(mass, enginePower):
    ...
def _computeSuspCompression(mass):
    ...
def _computeTrackLength(clearance, length):
    ...
def _computeHardRatio(clearance, length):
    ...
def _powerCurve(arg, argMin, argMid, argMax, valMin, valMid, valMax):
    ...
def _clamp(minBound, arg, maxBound):
    ...
def encodeTrackScrolling(leftScroll, rightScroll):
    ...
def decodeTrackScrolling(code):
    ...
def __deepUpdate(orig_dict, new_dict):
    ...
def __buildConfigurations(configuration):
    ...
def getShootTimeCorrection(roundTripTime):
    ...
def getShotPredictionWindow(roundTripTime):
    ...
def setTrackBitToBitMask(bitMask, trackPairIdx, isLeft):
    ...
