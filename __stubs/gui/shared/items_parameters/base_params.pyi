# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/items_parameters/base_params.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import defaultdict as defaultdict
import inspect as inspect
from future.utils import iteritems as iteritems, itervalues as itervalues
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.shared.items_parameters.functions import getInstalledModuleVehicle as getInstalledModuleVehicle, formatCompatibles as formatCompatibles
from gui.shared.items_parameters.params_cache import g_paramsCache as g_paramsCache

class ParameterBase(object):
    _itemDescr: Any
    _vehicleDescr: Any
    __preCachedInfo: Any
    __rawParams: Any
    def __init__(self, itemDescr, vehicleDescr=None):
        ...
    def getParamsDict(self):
        ...
    def getAllDataDict(self):
        ...
    def _getPrecachedInfo(self):
        ...
    def _getRawParams(self):
        ...
    def _extractRawParams(self):
        ...
    def _getCompatible(self):
        ...

class CompatibleParams(ParameterBase):
    @property
    def compatibles(self):
        ...
    def _getCompatible(self):
        ...

class WeightedParam(CompatibleParams):
    @property
    def weight(self):
        ...

class ParamsDictProxy(object):
    __slots__: tuple
    __paramsCalculator: Any
    __cachedParams: Any
    __allAreLoaded: Any
    __conditions: Any
    __filteredByConditions: Any
    __popped: Any
    def __init__(self, calculator, preload=False, conditions=None):
        ...
    def pop(self, item, default=None):
        ...
    def get(self, k, default=None):
        ...
    def keys(self):
        ...
    def values(self):
        ...
    def items(self):
        ...
    def iteritems(self):
        ...
    def __getitem__(self, item):
        ...
    def __iter__(self):
        ...
    def __len__(self):
        ...
    def __contains__(self, item):
        ...
    def __loadAllValues(self):
        ...
    def __checkConditions(self, key, value):
        ...
