# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/popover/vehicle_select_popover_base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
import nations as nations
from gui import GUI_NATIONS_ORDER_INDEX_REVERSED as GUI_NATIONS_ORDER_INDEX_REVERSED
from gui.Scaleform.daapi.view.meta.VehicleSelectPopoverMeta import VehicleSelectPopoverMeta as VehicleSelectPopoverMeta
from gui.Scaleform.framework.entities.DAAPIDataProvider import SortableDAAPIDataProvider as SortableDAAPIDataProvider
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER_INDICES_REVERSED as VEHICLE_TYPES_ORDER_INDICES_REVERSED
from gui.shared.utils import sortByFields as sortByFields

class VehicleSelectPopoverBase(VehicleSelectPopoverMeta):
    _vehDP: Any
    _isMultiSelect: Any
    def __init__(self, ctx=None):
        ...
    def setVehicleSelected(self, dbID, autoClose):
        ...
    def onWindowClose(self):
        ...
    def _initDP(self):
        ...
    def _dispose(self):
        ...
    def _updateSortField(self):
        ...

class VehiclesDataProvider(SortableDAAPIDataProvider):
    __isMultiSelect: Any
    __selectedDbID: Any
    __list: Any
    __listMapping: Any
    _sort: Any
    __sortMapping: Any
    def __init__(self, isMultiSelect=True):
        ...
    @property
    def sortedCollection(self):
        ...
    @property
    def collection(self):
        ...
    def emptyItem(self):
        ...
    def pySortOn(self, fields, order):
        ...
    def buildList(self, vehicleVOs):
        ...
    def toggleSelectionByID(self, dbID):
        ...
    def getSelected(self):
        ...
    def getLastSortMethod(self):
        ...
    def clear(self):
        ...
    def fini(self):
        ...
    def __sortingMethod(self, item, field):
        ...
