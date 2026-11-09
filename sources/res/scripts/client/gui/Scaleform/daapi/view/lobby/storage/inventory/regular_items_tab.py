# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/inventory/regular_items_tab.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/storage/inventory/regular_items_tab.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBuyOptionalDevicesUrl, getBuyEquipmentUrl
from gui.Scaleform.daapi.view.meta.RegularItemsTabViewMeta import RegularItemsTabViewMeta
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS
from gui.shared.event_dispatcher import showShop, showBattleBoosterSellDialog
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.gui_items.items_actions import factory as ItemsActionsFactory
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache

class RegularItemsTabView(RegularItemsTabViewMeta):
    __itemsCache = dependency.descriptor(IItemsCache)
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def sellItem(self, itemId):
        dataCompactId = int(itemId)
        item = self.__itemsCache.items.getItemByCD(dataCompactId)
        if item.itemTypeID == GUI_ITEM_TYPE.BATTLE_BOOSTER:
            showBattleBoosterSellDialog(dataCompactId)
        else:
            self._sellItems(itemId)

    def upgradeItem(self, itemId):
        module = self.__itemsCache.items.getItemByCD(int(itemId))
        ItemsActionsFactory.doAction(ItemsActionsFactory.UPGRADE_OPT_DEVICE, module, None, None, None)
        return

    def navigateToStore(self):
        if self._currentTabId == STORAGE_CONSTANTS.INVENTORY_TAB_ALL:
            showShop()
        if self._currentTabId == STORAGE_CONSTANTS.INVENTORY_TAB_EQUIPMENT:
            showShop(getBuyOptionalDevicesUrl())
        elif self._currentTabId == STORAGE_CONSTANTS.INVENTORY_TAB_CONSUMABLE:
            showShop(getBuyEquipmentUrl())

    def _buildItems(self):
        super(RegularItemsTabView, self)._buildItems()
        self.as_showDummyScreenS(len(self._dataProvider.collection) == 0)
