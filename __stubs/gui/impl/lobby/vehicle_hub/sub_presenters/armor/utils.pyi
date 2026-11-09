# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/sub_presenters/armor/utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import typing as typing
from collections import OrderedDict as OrderedDict
from builtins import round as round
from future.utils import listvalues as listvalues
import BigWorld as BigWorld
import GUI as GUI
import armor_inspector as armor_inspector
import math_utils as math_utils
from constants import VehicleArmorTags as VehicleArmorTags, VehicleTurretTags as VehicleTurretTags
from AvatarInputHandler import cameras as cameras
from helpers.collisions import SegmentCollisionResultExt as SegmentCollisionResultExt
from account_helpers.AccountSettings import AccountSettings as AccountSettings, AttackerVehicleConfiguration as AttackerVehicleConfiguration
from account_helpers.settings_core.settings_constants import ArmorInspector as ArmorInspectorSettingsKeys
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_value_model import ArmorValueModel as ArmorValueModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_model import MinorShortTooltipTypes as MinorShortTooltipTypes
from gui.impl.lobby.vehicle_hub.sub_presenters.armor.config import getConfig as getConfig
from items import vehicles as vehicles
from shared_utils.vehicle_utils import getMatinfo as getMatinfo
from vehicle_systems.tankStructure import TankPartIndexes as TankPartIndexes
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_model import ArmorModel as ArmorModel
from HangarVehicle import HangarVehicle as HangarVehicle
from gui.impl.lobby.vehicle_hub.sub_presenters.armor.config.models import ArmorScaleModel as ArmorScaleModel
from frameworks.wulf import Array as Array
from items.vehicles import VehicleDescriptor as VehicleDescriptor
from typing import Optional as Optional
from gui.impl.lobby.vehicle_hub.sub_presenters.armor.penetration_utils import ShellParams as ShellParams
MatInfo: Any
MIN_HIT_ANGLE_COS = 1e-05
COLLISION_RAY_LENGTH = 1500
RAD_TO_DEG: Any
_HALF_PI: Any
SPACED_ARMOR_DAMAGE_FACTOR = 0.0
AP_SHELLS_NORMALIZATION: Any
PENETRATION_SEGMENTS = 5
COMMON_MATERIALS_INDEX = 1000
LEFT_TRACK = 'leftTrack'
RIGHT_TRACK = 'rightTrack'
SURVEYING_DEVICE = 'surveyingDevice'
ARMOR_INSPECTOR_NAMES: tuple
NOMINAL_ARMOR_PARTS_LIST: tuple
DEFAULT_ATTACKER_GUN_SHOT_INDEX = 0
MINOR_SHORT_TOOLTIP_DATA: dict

class MaterialUIData(object):
    __slots__: tuple
    partName: Any
    nominalArmor: Any
    viewAngle: Any
    resArmor: Any
    color: Any
    count: Any
    isSpacedArmor: Any
    def __init__(self, partName, viewAngle, isSpacedArmor, nominalArmor, resArmor=None, color='', count=1):
        ...

def _calculateSegmentCount(scaleMin, scaleMax, colorLen, maxArmor):
    ...
def _fillArmorValues(model, colorList, scale, maxArmor):
    ...
def _fillPenetrationValues(model):
    ...
def _fillNoDamageValues(model, ricochetColor, noDamageColor):
    ...
def fillArmorData(model, tier, normalArmorMax, spacedArmorMax, isColorBlind):
    ...
def getMaterialsAtCursor(vehicleEntity, collisions=None, shellParams=None):
    ...
def _calculateEffectiveArmor(matInfo, hitAngleCos, shellParams):
    ...
def applyNormalizationForArmor(hitAngleCos, armorValue, matInfo, normalizationAngle, shellCaliber):
    ...
def getModuleForTurretRotation(vehicleEntity):
    ...
def getCollisionsAtCursor(vehicleEntity):
    ...
def _normalizedToPixels(xNorm, yNorm, screenWidth, screenHeight):
    ...
def _convertMatInfo(matInfo):
    ...
def _buildStaticMatInfos(vehicle):
    ...
def _buildDynamicMatInfos(vehicle):
    ...
def _buildWheelsMatInfos(vehicle):
    ...
def getAllMatInfos(vehicle):
    ...
def getCursorPositionInPixels():
    ...
def colorInt2Str(value):
    ...
def stackMaterials(materials, tier):
    ...
def getMaxArmor(vehicle):
    ...
def getArmorInspectorSetting(settingName):
    ...
def setArmorInspectorSetting(settingName, settingValue):
    ...
def getDefaultAttackerVehicleConfigByCD(compactDescr):
    ...
def getDefaultAttackerVehicleConfigByLvl(level):
    ...
def getArmorInspectorAttackerVehicleConfig(level):
    ...
def setArmorInspectorAttackerVehicleConfig(level, compactDescr=None, gunCompactDescr=None, activeGunShotIndex=None):
    ...
