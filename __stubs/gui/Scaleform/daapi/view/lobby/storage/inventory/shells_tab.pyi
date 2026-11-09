# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/inventory/shells_tab.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from future.utils import viewitems as viewitems
from constants import SHELL_TYPES as SHELL_TYPES
from gui.Scaleform.daapi.view.lobby.storage import storage_helpers as storage_helpers
from gui.Scaleform.daapi.view.lobby.storage.inventory.filters.filter_by_vehicle import FiltrableInventoryCategoryByVehicleTabView as FiltrableInventoryCategoryByVehicleTabView
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA as REQ_CRITERIA
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
_TYPE_FILTER_ITEMS: list
_TYPE_ID_BIT_TO_TYPE_ID_MAP: dict

class _ShellsFilterBit(CONST_CONTAINER):
    ARMOR_PIERCING = 1
    ARMOR_PIERCING_GR = 2
    HOLLOW_CHARGE = 4
    HIGH_EXPLOSIVE = 8

class ShellsTabView(FiltrableInventoryCategoryByVehicleTabView):
    filterItems = _TYPE_FILTER_ITEMS
    def _getClientSectionKey(self):
        ...
    def _getItemTypeID(self):
        ...
    def _getFilteredCriteria(self):
        ...
    def _getRequestCriteria(self, invVehicles):
        ...
