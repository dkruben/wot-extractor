# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/reusable/sort_keys.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.shared.gui_items import Vehicle as Vehicle
from gui.shared.sort_key import SortKey as SortKey

class AchievementSortKey(SortKey):
    __slots__: tuple
    achievement: Any
    def __init__(self, achievement):
        ...
    def _cmp(self, other):
        ...

class _VehicleSortKey(SortKey):
    __slots__: tuple
    info: Any
    def __init__(self, vehicleInfo):
        ...
    def _cmp(self, other):
        ...

class VehicleInfoSortKey(_VehicleSortKey):
    __slots__: tuple
    def _cmp(self, other):
        ...

class TeamItemSortKey(_VehicleSortKey):
    __slots__: tuple
    def _cmp(self, other):
        ...

class VehicleXpSortKey(_VehicleSortKey):
    __slots__: tuple
    def _cmp(self, other):
        ...

class RankedVehicleXpSortKey(_VehicleSortKey):
    __slots__: tuple
    def _cmp(self, other):
        ...

def placeSortKey(a):
    ...
