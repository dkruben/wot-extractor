# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/inventory/crew_books_tab.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from gui.Scaleform.daapi.view.lobby.storage.inventory.filters.filter_by_nation import FiltrableInventoryCategoryByNationTabView as FiltrableInventoryCategoryByNationTabView
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from items.components.crew_books_constants import CREW_BOOK_RARITY as CREW_BOOK_RARITY
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_TYPE_FILTER_ITEMS: list
_TYPE_ID_BIT_TO_TYPE_ID_MAP: dict

class _CrewBooksFilterBit(CONST_CONTAINER):
    RARE_1 = 1
    RARE_2 = 2
    RARE_3 = 4
    PERSONAL = 8
    UNIVERSAL = 16

class CrewBooksTabView(FiltrableInventoryCategoryByNationTabView):
    __lobbyContext: Any
    filterItems = _TYPE_FILTER_ITEMS
    def _getClientSectionKey(self):
        ...
    def _getItemTypeID(self):
        ...
    def _getFilteredCriteria(self):
        ...
    def _getRequestCriteria(self, invVehicles):
        ...
