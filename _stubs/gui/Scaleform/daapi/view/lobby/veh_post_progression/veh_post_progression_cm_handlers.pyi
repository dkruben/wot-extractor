# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/veh_post_progression/veh_post_progression_cm_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import NATION_CHANGE_VIEWED as NATION_CHANGE_VIEWED
from gui.Scaleform.daapi.view.lobby.hangar.hangar_cm_handlers import VEHICLE as VEHICLE, SimpleVehicleCMHandler as SimpleVehicleCMHandler
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.shared import event_dispatcher as shared_events
from gui.shared.gui_items.items_actions import factory as ItemsActionsFactory
from gui.shared.utils.vehicle_collector_helper import isAvailableForPurchase as isAvailableForPurchase
from gui.shop import canBuyGoldForVehicleThroughWeb as canBuyGoldForVehicleThroughWeb
from helpers import dependency as dependency
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle

class PostProgressionContextMenuHandler(SimpleVehicleCMHandler):
    __cmpBasket: Any
    __hangarSpace: Any
    __itemsCache: Any
    __lobbyContext: Any
    _vehCD: Any
    _vehInvID: Any
    def __init__(self, cmProxy, ctx=None):
        ...
    def getVehCD(self):
        ...
    def getVehInvID(self):
        ...
    def compareVehicle(self):
        ...
    def buyVehicle(self):
        ...
    def changeVehicleNation(self):
        ...
    def selectVehicle(self):
        ...
    def _initFlashValues(self, ctx):
        ...
    def _clearFlashValues(self):
        ...
    def _generateOptions(self, ctx=None):
        ...
    def __addStatsOption(self, options, vehicle):
        ...
    def __addCompareOption(self, options, vehicle):
        ...
    def __addBuyOption(self, options, vehicle):
        ...
    def __addSellOption(self, options, vehicle):
        ...
    def __addNationChangeOption(self, options, vehicle):
        ...
    def __addSelectOption(self, options, vehicle):
        ...
    def __addSeparator(self, options, isPrevSeparator):
        ...
    def __isCollectibleVehicleEnabled(self, vehicle):
        ...
    def __vehicleWasInBattle(self, vehicle):
        ...
