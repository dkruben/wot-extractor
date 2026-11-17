# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/inhangar/in_hangar_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from gui.Scaleform.daapi.view.common.filter_popover import VehiclesFilterPopover as VehiclesFilterPopover
from gui.Scaleform.daapi.view.meta.StorageCategoryInHangarViewMeta import StorageCategoryInHangarViewMeta as StorageCategoryInHangarViewMeta
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS as STORAGE_CONSTANTS
from gui.Scaleform.locale.STORAGE import STORAGE as STORAGE
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
StorageCategoryInHangarDataVO: Any
_SEARCH_INPUT_MAX_CHARS = 50
_TABS_DATA: tuple
_RENT_TAB_DATA: dict

class StorageVehicleFilterPopover(VehiclesFilterPopover):
    def _getInitialVO(self, filters, xpRateMultiplier):
        ...

class StorageCategoryInHangarView(StorageCategoryInHangarViewMeta):
    _itemsCache: Any
    def setActiveState(self, isActive):
        ...
    def setActiveTab(self, tabId):
        ...
    def _populate(self):
        ...
    def getTabsData(self):
        ...
    def __canShowRentTab(self):
        ...
