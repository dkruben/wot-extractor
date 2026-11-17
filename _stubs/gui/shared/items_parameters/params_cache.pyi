# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/items_parameters/params_cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import itertools as itertools
import math as math
import sys as sys
import typing as typing
from collections import namedtuple as namedtuple, defaultdict as defaultdict
from functools import partial as partial
from future.utils import iteritems as iteritems, itervalues as itervalues, viewitems as viewitems
import nations as nations
import persistent_data_cache_common as pdc
from constants import BonusTypes as BonusTypes
from gui.shared.items_parameters import calcGunParams as calcGunParams, calcShellParams as calcShellParams, getEquipmentParameters as getEquipmentParameters
from gui.shared.items_parameters import xml_reader as xml_reader
from gui.shared.utils.decorators import debugTime as debugTime
from items import vehicles as vehicles, ITEM_TYPES as ITEM_TYPES, EQUIPMENT_TYPES as EQUIPMENT_TYPES
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from items.vehicles import getVehicleType as getVehicleType
from gui.shared.utils import GUN_NORMAL as GUN_NORMAL
from gui.shared.gui_items.vehicle_mechanics.mechanic_detectors import ENGINE_MECHANICS_BITS as ENGINE_MECHANICS_BITS, ENGINE_MECHANIC_DETECTORS as ENGINE_MECHANIC_DETECTORS, CHASSIS_MECHANIC_DETECTORS as CHASSIS_MECHANIC_DETECTORS, GUN_MECHANICS_TO_RELOAD_TYPES as GUN_MECHANICS_TO_RELOAD_TYPES, GUN_MECHANIC_DETECTORS as GUN_MECHANIC_DETECTORS, hasChassisMechanicBit as hasChassisMechanicBit
from post_progression_common import ACTION_TYPES as ACTION_TYPES
from soft_exception import SoftException as SoftException
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey
from gui.shared.gui_items.vehicle_mechanics.mechanic_detectors import ChassisTypes as ChassisTypes
PrecachedShell: Any
PrecachedEquipment: Any
PrecachedOptionalDevice: Any
ParamsCacheData: Any
g_paramsCache: Any

# base nao representavel no stub: namedtuple(...)
class PrecachedGun:
    @property
    def clipVehicles(self):
        ...
    @property
    def clipVehiclesNames(self):
        ...
    def hasMechanicForVehicle(self, mechanic, vehicleCD):
        ...
    def hasMechanic(self, mechanic):
        ...
    def getReloadingType(self, vehicleCD=None):
        ...
    def getTurretsForVehicle(self, vehicleCD):
        ...

class VehicleDescrsCache(object):
    __slots__: tuple
    _local: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def load(self):
        ...
    def generator(self, nationID=None):
        ...

class _ParamsCache(object):
    __slots__: tuple
    __cache: Any
    __simplifiedParamsCoefficients: Any
    __bonuses: Any
    __noCamouflageVehicles: Any
    __wheeledChassisParams: Any
    def __init__(self):
        ...
    # decorador original: @debugTime
    def init(self, vehiclesCache=None):
        ...
    def getGunReloadingSystemType(self, itemCD, vehicleCD=None):
        ...
    def getWheeledChassisAxleLockAngles(self, itemCD):
        ...
    def hasGunMechanic(self, itemCD, mechanic, vehicleCD=None):
        ...
    def hasEngineMechanic(self, itemCD, mechanic):
        ...
    def hasChassisMechanic(self, itemCD, mechanic):
        ...
    def getSimplifiedCoefficients(self):
        ...
    def getBonuses(self):
        ...
    def getPrecachedParameters(self, typeCompactDescr, default=None):
        ...
    def getComponentVehiclesNames(self, typeCompactDescr):
        ...
    def getCompatibleArtefacts(self, vehicle):
        ...
    def getVehiclesWithoutCamouflage(self):
        ...

def _getVehicleSuitablesByType(vehicleType, itemTypeId, turretPID=0):
    ...
def _readCache(vehiclesCache):
    ...
def _precacheEquipments(data):
    ...
def _precacheOptionalDevices(data):
    ...
def _precacheGuns(data):
    ...
def _precacheShells(data):
    ...
def _precacheChassis(data):
    ...
def _precacheEngines(data):
    ...
def _getVehiclesWithoutCamouflage(data):
    ...
