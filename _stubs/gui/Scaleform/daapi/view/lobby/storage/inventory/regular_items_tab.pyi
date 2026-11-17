# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/inventory/regular_items_tab.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBuyOptionalDevicesUrl as getBuyOptionalDevicesUrl, getBuyEquipmentUrl as getBuyEquipmentUrl
from gui.Scaleform.daapi.view.meta.RegularItemsTabViewMeta import RegularItemsTabViewMeta as RegularItemsTabViewMeta
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS as STORAGE_CONSTANTS
from gui.shared.event_dispatcher import showShop as showShop, showBattleBoosterSellDialog as showBattleBoosterSellDialog
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.items_actions import factory as ItemsActionsFactory
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache

class RegularItemsTabView(RegularItemsTabViewMeta):
    __itemsCache: Any
    __lobbyContext: Any
    def sellItem(self, itemId):
        ...
    def upgradeItem(self, itemId):
        ...
    def navigateToStore(self):
        ...
    def _buildItems(self):
        ...
