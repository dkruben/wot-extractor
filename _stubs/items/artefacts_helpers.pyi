# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/artefacts_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from typing import Optional as Optional, Dict as Dict, Set as Set, Tuple as Tuple, List as List, TYPE_CHECKING as TYPE_CHECKING
import nations as nations
from constants import MIN_VEHICLE_LEVEL as MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL
from items import _xml as _xml, ITEM_TYPE_NAMES as ITEM_TYPE_NAMES, ITEM_TYPES as ITEM_TYPES
from items.readers.shared_readers import readAllowedTags as _readTags
from items.vehicles import VehicleType as VehicleType, VehicleDescriptor as VehicleDescriptor
_vehicleFilterItemTypes: dict

class ComponentFilter(object):
    _minLevel: Any
    _maxLevel: Any
    _tags: Any
    _mandatoryTags: Any
    def __init__(self, minLevel, maxLevel, tags, mandatoryTags):
        ...
    def __str__(self):
        ...
    @property
    def minLevel(self):
        ...
    @property
    def maxLevel(self):
        ...
    @property
    def filterTags(self):
        ...
    def isItemCompatible(self, itemDescr):
        ...
    @staticmethod
    def readComponentFilter(ctx, section, itemTypeName):
        ...
    @staticmethod
    def _readComponentFilterInfo(ctx, section, itemTypeName):
        ...

class SubFilter(object):
    _nationIDs: Any
    _typeFilter: Any
    _compFilters: Any
    def __init__(self, nationIDs, vehTypeFilter, moduleFilters):
        ...
    def __str__(self):
        ...
    @property
    def nationIDs(self):
        ...
    @property
    def vehTypeFilter(self):
        ...
    def isVehTypeCompatible(self, vehicleType):
        ...
    def isComponentsCompatible(self, vehicleDescr):
        ...
    @staticmethod
    def readSubFilter(xmlCtx, filterSection):
        ...
    @staticmethod
    def _readSubFilterInfo(xmlCtx, filterSection):
        ...

class VehicleFilter(object):
    _include: Any
    _exclude: Any
    def __init__(self, include, exclude):
        ...
    @staticmethod
    def readVehicleFilter(xmlCtx, section):
        ...
    def checkCompatibility(self, vehicleDescr):
        ...
    def checkCompatibilityWithComponents(self, vehicleDescr):
        ...
    def checkCompatibilityWithVehType(self, vehType):
        ...
    def compatibleNations(self):
        ...
    def getLevelRange(self):
        ...
    @staticmethod
    def _readVehicleFilterInfo(xmlCtx, section):
        ...
    def _checkCompatibility(self, vehicleDescr):
        ...
    def _getSubFiltersForVehType(self, vehType):
        ...
    @staticmethod
    def _getSubFilters(filters, vehType):
        ...

class _ArtefactFilter(object):
    __installed: Any
    __active: Any
    def __init__(self, xmlCtx, section, itemTypeName):
        ...
    def inInstalled(self, tags):
        ...
    def inActive(self, tags):
        ...

def readKpi(xmlCtx, section):
    ...
def _readKpiValue(xmlCtx, section, kpiType):
    ...
def _readAggregateKPI(xmlCtx, section, kpiType):
    ...
