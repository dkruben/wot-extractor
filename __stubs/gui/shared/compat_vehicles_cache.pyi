# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/compat_vehicles_cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import defaultdict as defaultdict
from future.utils import itervalues as itervalues
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle

class CompatVehiclesCache(object):
    __slots__: tuple
    _COMPAT_TYPES: tuple
    _FITTED_TYPES: tuple
    __compatCache: Any
    __fittedCache: Any
    __invVehicles: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def getCompatCache(self, proxy):
        ...
    def getFittedCache(self, proxy):
        ...
    def invalidateFullData(self, proxy):
        ...
    def invalidateData(self, proxy, invalidItems):
        ...
    def __invalidateFittedCache(self, proxy):
        ...
    def __invalidateCompatCache(self, proxy, addedVehicle, removedVehicle):
        ...
    def __addCacheForVehicle(self, vehicle, collectItems):
        ...
    def __removeCacheForVehicle(self, vehicleIntCD, collectItems):
        ...

def getItemsByType(itemType, proxy):
    ...
