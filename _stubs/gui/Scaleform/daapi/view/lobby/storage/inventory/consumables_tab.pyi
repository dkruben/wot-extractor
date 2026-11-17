# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/inventory/consumables_tab.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from future.utils import viewitems as viewitems
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBuyEquipmentUrl as getBuyEquipmentUrl
from gui.Scaleform.daapi.view.lobby.storage.inventory.filters.filter_by_type import FiltrableRegularCategoryByTypeTabView as FiltrableRegularCategoryByTypeTabView
from gui.impl.gen import R as R
from gui.shared.event_dispatcher import showShop as showShop
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
_TYPE_FILTER_ITEMS: list
_TYPE_ID_BIT_TO_TYPE_ID_MAP: dict

class _ConsumableFilterBit(CONST_CONTAINER):
    CONSUMABLES = 1
    BATTLE_BOOSTERS = 2
    DEMOUNT_KITS = 4
    RECERTIFICATION_FORMS = 8
    MENTORING_LICENSES = 16

class ConsumablesTabView(FiltrableRegularCategoryByTypeTabView):
    filterItems = _TYPE_FILTER_ITEMS
    def navigateToStore(self):
        ...
    def _getItemTypeID(self):
        ...
    def _getClientSectionKey(self):
        ...
    def _getFilteredCriteria(self):
        ...
    def _getRequestCriteria(self, invVehicles):
        ...
