# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/vehicle_mechanics/mechanic_detectors.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple, OrderedDict as OrderedDict
from future.utils import viewitems as viewitems
from gui.shared.utils import GUN_CAN_BE_CLIP as GUN_CAN_BE_CLIP, GUN_CLIP as GUN_CLIP, GUN_AUTO_RELOAD as GUN_AUTO_RELOAD, GUN_CAN_BE_AUTO_RELOAD as GUN_CAN_BE_AUTO_RELOAD, GUN_DUAL_GUN as GUN_DUAL_GUN, GUN_CAN_BE_DUAL_GUN as GUN_CAN_BE_DUAL_GUN, GUN_AUTO_SHOOT as GUN_AUTO_SHOOT, GUN_CAN_BE_AUTO_SHOOT as GUN_CAN_BE_AUTO_SHOOT, GUN_TWIN_GUN as GUN_TWIN_GUN, GUN_CAN_BE_TWIN_GUN as GUN_CAN_BE_TWIN_GUN, GUN_CAN_BE_LOW_CHARGE_SHOT as GUN_CAN_BE_LOW_CHARGE_SHOT, LOW_CHARGE_SHOT as LOW_CHARGE_SHOT
from gui.shared.items_parameters import isAutoReloadGun as isAutoReloadGun, isAutoShootGun as isAutoShootGun, isDualGun as isDualGun, isDualAccuracy as isDualAccuracy, isTwinGun as isTwinGun, isLowChargeShotGun as isLowChargeShotGun
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys, SpecBoostModeMechanicVariant as SpecBoostModeMechanicVariant
from vehicles.mechanics.mechanic_helpers import getMechanicFromMechanicsParams as getMechanicFromMechanicsParams
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey
from items.vehicles import VehicleDescriptor as VehicleDescriptor
ModuleMechanicData: Any
ENGINE_MECHANIC_DETECTORS: dict
ENGINE_MECHANICS_BITS: dict
CHASSIS_MECHANIC_DETECTORS: dict
CHASSIS_MECHANICS_BITS: dict
GUN_MECHANICS_TO_RELOAD_TYPES: Any
GUN_MECHANIC_DETECTORS: dict

class ChassisTypes(object):
    DEFAULT = 0
    WHEELED = 1
    ON_SPOT_ROTATION_WHEELED = 2
    AUTO_SIEGE = 3

def isCombatThrottleEngine(vDescr):
    ...
def isHydraulicChassis(vDescr):
    ...
def hasChassisMechanicBit(mask, mechanic):
    ...
