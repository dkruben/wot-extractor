# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/cmp_top_modules.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import operator as operator
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.items_parameters.module_params import GunParams as GunParams
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
_COMMON_CRITERIA: Any

class _BaseModuleComparator(object):
    itemsCache: Any
    __slots__: tuple
    _items: Any
    _vehicle: Any
    def __init__(self, items, vehicle):
        ...
    def clear(self):
        ...
    def maxLvl(self, excludes=None):
        ...
    def maxCreditsCost(self, excludes=None):
        ...
    def mostValuableParam(self, excludes=None):
        ...
    def _getModuleParam(self, getter, excludes=None):
        ...
    def _getValuableParam(self, paramName, excludes=None):
        ...

class TopModulesChecker(object):
    __slots__: tuple
    __vehicle: Any
    _requestCriteria: Any
    _comparators: Any
    def __init__(self, vehicle):
        ...
    def process(self):
        ...
    def clear(self):
        ...
    def __check(self, functor):
        ...

class ChassisComparator(_BaseModuleComparator):
    def __init__(self, criteria, vehicle):
        ...
    def mostValuableParam(self, excludes=None):
        ...

class TurretComparator(_BaseModuleComparator):
    def __init__(self, criteria, vehicle):
        ...
    def mostValuableParam(self, excludes=None):
        ...

class GunComparator(_BaseModuleComparator):
    __slots__: tuple
    def __init__(self, criteria, vehicle):
        ...
    def mostValuableParam(self, excludes=None):
        ...

class EngineComparator(_BaseModuleComparator):
    def __init__(self, criteria, vehicle):
        ...
    def mostValuableParam(self, excludes=None):
        ...

class RadioComparator(_BaseModuleComparator):
    def __init__(self, criteria, vehicle):
        ...
    def mostValuableParam(self, excludes=None):
        ...
