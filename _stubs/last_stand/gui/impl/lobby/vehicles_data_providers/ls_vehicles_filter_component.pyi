# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/vehicles_data_providers/ls_vehicles_filter_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import Event as Event
from gui.impl.lobby.hangar.base.hangar_interfaces import IVehicleFilter as IVehicleFilter
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from last_stand.skeletons.ls_controller import ILSController as ILSController
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
_VEHICLE_UPDATES: tuple
ALL_MODE_VEHICLE_CRITERIA: Any

class LSVehiclesFilterComponent(IVehicleFilter):
    _itemsCache: Any
    _lsCtrl: Any
    onDiff: Any
    __vehicles: Any
    __criteria: Any
    def __init__(self, onlySuitableVehicles=True):
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
    def __onCacheResync(self, reason, diff):
        ...
    def __createVehiclesDict(self):
        ...
