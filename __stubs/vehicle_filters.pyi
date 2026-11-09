# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/vehicle_filters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from typing import Optional as Optional, List as List, Type as Type, Union as Union
from extension_utils import ResMgr as ResMgr
import section2dict as section2dict
from dict2model import models as models, fields as fields, schemas as schemas, validate as validate, exceptions as exceptions
from debug_utils import LOG_ERROR as LOG_ERROR
from items.vehicles import VehicleDescriptor as VehicleDescriptor
FILTERS_PATH = 'scripts/item_defs/vehicle_filters.xml'
filterValuesSchema: Any
filterSchema: Any
vehicleFiltersSchema: Any
_g_filters = None

class BaseModel(models.Model):
    def isVehicleMatch(self, descr):
        ...

class BaseIncludeExcludeModel(BaseModel):
    __slots__: tuple
    include: Any
    exclude: Any
    def __init__(self, include=None, exclude=None):
        ...

class BaseValueInIncludeExcludeModel(BaseIncludeExcludeModel):
    def _isValueIn(self, value):
        ...

class BaseValuesInIncludeExcludeModel(BaseIncludeExcludeModel):
    def _isValuesIn(self, values):
        ...

class BaseBooleanModel(BaseModel):
    __slots__: tuple
    value: Any
    def __init__(self, value=None):
        ...
    def _isValue(self, value):
        ...

class VehNamesModel(BaseValueInIncludeExcludeModel):
    def isVehicleMatch(self, descr):
        ...

class VehClassesModel(BaseValueInIncludeExcludeModel):
    def isVehicleMatch(self, descr):
        ...

class LevelModel(BaseValueInIncludeExcludeModel):
    def isVehicleMatch(self, descr):
        ...

class TagsModel(BaseValuesInIncludeExcludeModel):
    def isVehicleMatch(self, descr):
        ...

class GunTagsModel(BaseValuesInIncludeExcludeModel):
    def isVehicleMatch(self, descr):
        ...

class BurstModel(BaseBooleanModel):
    def isVehicleMatch(self, descr):
        ...

class FilterValuesModel(models.Model):
    __slots__: tuple
    vehNames: Any
    vehClasses: Any
    level: Any
    tags: Any
    gunTags: Any
    burst: Any
    def __init__(self, vehNames=None, vehClasses=None, level=None, tags=None, gunTags=None, burst=None):
        ...
    def isVehicleMatch(self, vehDesc):
        ...

class FilterModel(models.Model):
    __slots__: tuple
    name: Any
    values: Any
    def __init__(self, name, values):
        ...
    def isVehicleMatch(self, vehDesc):
        ...

class VehicleFiltersModel(models.Model):
    __slots__: tuple
    filters: Any
    _filterByNames: Any
    def __init__(self, filters):
        ...
    def getFilterNames(self):
        ...
    def getFilter(self, filterName):
        ...
    def isVehicleMatchByFilter(self, filterName, vehDesc):
        ...

class BooleanSchema(schemas.Schema):
    def __init__(self, modelClass):
        ...

class IncludeExcludeSchema(schemas.Schema):
    def __init__(self, modelClass):
        ...

def checkIncludeExcludeValue(model):
    ...
def init():
    ...
def getVehicleFilters():
    ...
