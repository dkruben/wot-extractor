# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/inhangar/inhangar_cm_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.shared.cm_handlers import ContextMenu as ContextMenu, option as option, CMLabel as CMLabel
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import enoughCreditsForRestore as enoughCreditsForRestore, getVehicleRestoreInfo as getVehicleRestoreInfo
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getTradeInVehiclesUrl as getTradeInVehiclesUrl
from gui.Scaleform.framework.managers.context_menu import CM_BUY_COLOR as CM_BUY_COLOR
from gui.shared import event_dispatcher as shared_events
from gui.shared.event_dispatcher import showShop as showShop
from gui.shared.gui_items.items_actions import factory as ItemsActionsFactory
from helpers import dependency as dependency
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from items import UNDEFINED_ITEM_CD as UNDEFINED_ITEM_CD
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket, IEpicBattleMetaGameController as IEpicBattleMetaGameController, ITradeInController as ITradeInController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import NATION_CHANGE_VIEWED as NATION_CHANGE_VIEWED

class VehiclesRegularCMHandler(ContextMenu):
    __sqGen: Any
    __itemsCache: Any
    __comparisonBasket: Any
    __tradeInController: Any
    __lobbyContext: Any
    # decorador original: @option(...)
    def exchange(self):
        ...
    # decorador original: @option(...)
    def showInfo(self):
        ...
    # decorador original: @option(...)
    def goToStats(self):
        ...
    # decorador original: @option(...)
    def goToCollection(self):
        ...
    # decorador original: @option(...)
    def sell(self):
        ...
    # decorador original: @option(...)
    def addToCompare(self):
        ...
    # decorador original: @option(...)
    def showInHangar(self):
        ...
    # decorador original: @option(...)
    def changeNation(self):
        ...
    def _getOptionCustomData(self, label):
        ...
    def __canTradeOff(self):
        ...
    def __isReadyToTradeOff(self):
        ...
    def __canSell(self):
        ...
    def __canNationChange(self):
        ...
    def __isNationChangeAvailable(self):
        ...
    def __isVehicleCollectorAvailable(self):
        ...

class VehiclesRestoreCMHandler(ContextMenu):
    __sqGen: Any
    __itemsCache: Any
    __comparisonBasket: Any
    # decorador original: @option(...)
    def showInfo(self):
        ...
    # decorador original: @option(...)
    def goToStats(self):
        ...
    # decorador original: @option(...)
    def restore(self):
        ...
    # decorador original: @option(...)
    def addToCompare(self):
        ...
    def _getOptionCustomData(self, label):
        ...
    def __canRestore(self):
        ...

class VehiclesRentedCMHandler(ContextMenu):
    __sqGen: Any
    __itemsCache: Any
    __comparisonBasket: Any
    __epicController: Any
    # decorador original: @option(...)
    def showInfo(self):
        ...
    # decorador original: @option(...)
    def goToStats(self):
        ...
    # decorador original: @option(...)
    def buy(self):
        ...
    # decorador original: @option(...)
    def remove(self):
        ...
    # decorador original: @option(...)
    def addToCompare(self):
        ...
    # decorador original: @option(...)
    def showInHangar(self):
        ...
    def _getOptionCustomData(self, label):
        ...
    def __canBuy(self):
        ...
    def __canRemove(self):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def _canAddToComparisonBasket(vehicleCD, comparisonBasket=None, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _canGoToStats(vehicleCD, itemsCache=None):
    ...
