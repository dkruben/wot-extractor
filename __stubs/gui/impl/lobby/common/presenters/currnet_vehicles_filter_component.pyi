# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/common/presenters/currnet_vehicles_filter_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import Event as Event
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.impl.lobby.hangar.base.hangar_interfaces import IVehicleFilter as IVehicleFilter
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

class CurrentVehicleFilterComponent(IVehicleFilter):
    _itemsCache: Any
    onDiff: Any
    __prevVehicle: Any
    _vehicles: Any
    def __init__(self):
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
    def __onVehicleChanged(self):
        ...
    def __createVehiclesDict(self):
        ...
