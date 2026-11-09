# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/UnitRoster.py (BYTECODE: a descompilacao falhou; sem bases, decoradores nem valores por omissao).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import struct as struct
from future.utils import viewitems as viewitems
from past.builtins import xrange as xrange
import nations as nations
from items import vehicles as vehicles
from constants import VEHICLE_CLASSES as VEHICLE_CLASSES, VEHICLE_CLASS_INDICES as VEHICLE_CLASS_INDICES, MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL
absolute_import: Any
_BAD_CLASS_INDEX: Any
_DEFAULT_ROSTER_SLOT_PACK: Any

# gerado do bytecode: classes base desconhecidas
class BaseUnitRoster:
    MAX_SLOTS: Any
    MAX_CLOSED_SLOTS: Any
    MAX_EMPTY_SLOTS: Any
    MAX_UNIT_ASSEMBLER_ARTY: Any
    SLOT_TYPE: Any
    DEFAULT_SLOT_PACK: Any
    LIMITS_TYPE: Any
    MIN_UNIT_POINTS_SUM: Any
    MAX_UNIT_POINTS_SUM: Any
    MAX_LEGIONARIES_COUNT: Any
    MIN_VEHICLES: Any
    MAX_VEHICLES: Any
    _BaseUnitRoster__checkVehicleForUnitSlot: Any
    def __init__(self, limitsDefs=..., slotDefs=..., slotCount=..., packedRoster=...):
        ...
    def __repr__(self):
        ...
    def pack(self):
        ...
    def unpack(self, packed):
        ...
    def getPacked(self):
        ...
    def isDefaultSlot(self, slot):
        ...
    def checkVehicleList(self, vehTypeCompDescrList, unitSlotIdx=...):
        ...
    def matchVehicleList(self, vehTypeCompDescrList, unitSlotIdx=...):
        ...
    def matchVehicleListToSlotList(self, vehTypeCompDescrList, unitSlotIdxList=...):
        ...
    def matchVehicleListByLevel(self, vehTypeCompDescrList):
        ...
    def checkVehicle(self, vehTypeCompDescr, unitSlotIdx=...):
        ...
    def checkVehicleLevel(self, vehTypeCompDescr):
        ...
    def getLegionariesMaxCount(self):
        ...
    def __checkVehicleForUnitSlot(self, vehTypeCompDescr, unitSlotIdx):
        ...

# gerado do bytecode: classes base desconhecidas
class BaseUnitRosterSlot:
    _BaseUnitRosterSlot__EXACT_TYPE_PREFIX: Any
    DEFAULT_LEVELS: Any
    DEFAULT_NATIONS: Any
    DEFAULT_VEHICLE_CLASSES: Any
    NATION_MASK_POWER: Any
    VEH_CLASS_MASK_POWER: Any
    _VEHICLE_MASKS: Any
    _VEHICLE_MASKS_SIZE: Any
    _VEHICLE_TYPE: Any
    _VEHICLE_TYPE_SIZE: Any
    def __init__(self, vehTypeCompDescr=..., nationNames=..., levels=..., vehClassNames=..., packed=...):
        ...
    def __repr__(self):
        ...
    def isNationMaskFull(self):
        ...
    def isVehClassMaskFull(self):
        ...
    def pack(self):
        ...
    def unpack(self, packed):
        ...
    def getPackSize(firstByte):
        ...
    def checkVehicle(self, vehTypeCompDescr):
        ...

# gerado do bytecode: classes base desconhecidas
class BaseUnitRosterLimits:
    _ROSTER_LIMIT_NAMES: Any
    _ROSTER_LIMIT_INDICES: Any
    _LIMITS_PACK_FORMAT: Any
    def __init__(self, **limitsDefs):
        ...
    def __repr__(self):
        ...
    def _packLimit(self, limitName):
        ...
    def pack(self):
        ...
    def _unpackLimit(self, limitName, packed):
        ...
    def unpack(self, packed):
        ...
    def get(self, limitName, defaultValue=...):
        ...
    def checkVehicleLevel(self, vehicleClassIdx, vehicleLevel):
        ...
    def _checkVehicleClass(self, vehicleClassIdx):
        ...
    def _checkVehicleNation(self, vehicleNationIdx):
        ...
    def _checkVehicleType(self, vehTypeCompDescr):
        ...
    def checkVehicle(self, vehTypeCompDescr):
        ...

def _makeBitMask(nameList, nameIndex, power=...):
    ...
def _reprBitMask(bitMask, nameList):
    ...
def reprBitMaskFromDict(bitMask, nameDict):
    ...
def buildNamesDict(constDefClass):
    ...
def _vehType__repr__(self):
    ...

def __getattr__(name: str) -> Any: ...  # stub incompleto (gerado do bytecode)
