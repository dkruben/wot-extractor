# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/base/vehicles_filter_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewkeys as viewkeys
import Event as Event
from gui.impl.lobby.hangar.base.hangar_interfaces import IVehicleFilter as IVehicleFilter
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.utils.requesters import RequestCriteria as RequestCriteria
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
_VEHICLE_UPDATES: tuple

class VehiclesFilterComponent(IVehicleFilter):
    _itemsCache: Any
    __criteria: Any
    onDiff: Any
    _vehicles: Any
    def __init__(self, criteria):
        ...
    @property
    def criteria(self):
        ...
    @property
    def vehicles(self):
        ...
    def initialize(self):
        ...
    def destroy(self):
        ...
    def _setCriteria(self, criteria):
        ...
    def __onCacheResync(self, reason, diff):
        ...
    def __createVehiclesDict(self):
        ...
