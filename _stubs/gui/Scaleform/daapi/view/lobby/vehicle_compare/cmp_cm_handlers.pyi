# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/cmp_cm_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.hangar.hangar_cm_handlers import SimpleVehicleCMHandler as SimpleVehicleCMHandler, VEHICLE as VEHICLE
from gui.Scaleform.daapi.view.lobby.techtree.techtree_dp import g_techTreeDP as g_techTreeDP
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE as VEH_COMPARE
from gui.shop import canBuyGoldForVehicleThroughWeb as canBuyGoldForVehicleThroughWeb
from gui.shared import event_dispatcher as shared_events
from gui.shared.gui_items.items_actions import factory as ItemsActionsFactory
from gui.shared.utils.vehicle_collector_helper import isAvailableForPurchase as isAvailableForPurchase
from helpers import dependency as dependency
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import NATION_CHANGE_VIEWED as NATION_CHANGE_VIEWED

class _OptIds(object):
    COPY = 'copy'

class CommonContextMenuHandler(SimpleVehicleCMHandler):
    _lobbyContext: Any
    __itemIndexInBasket: Any
    vehCD: Any
    def __init__(self, cmProxy, ctx=None, handlers=None):
        ...
    def showVehiclePreview(self):
        ...
    def selectVehicleInHangar(self):
        ...
    def sellVehicle(self):
        ...
    def buyVehicle(self):
        ...
    def researchVehicle(self):
        ...
    def getVehCD(self):
        ...
    def changeVehicleNation(self):
        ...
    def _generateOptions(self, ctx=None):
        ...
    def _manageStartOptions(self, options, vehicle):
        ...
    def _manageEndOptions(self, options, vehicle):
        ...
    def _initFlashValues(self, ctx):
        ...
    def __isCollectibleVehicleEnabled(self, vehicle):
        ...
    @classmethod
    def __getVehicle(cls, intCD):
        ...
    @staticmethod
    def __isResearchEnabled(vehicle):
        ...
    @staticmethod
    def __isPurchaseEnabled(vehicle):
        ...

class VehicleCompareContextMenuHandler(CommonContextMenuHandler):
    comparisonBasket: Any
    __itemIndexInBasket: Any
    def __init__(self, cmProxy, ctx=None):
        ...
    def copyComparedVehicle(self):
        ...
    def _manageStartOptions(self, options, vehicle):
        ...
    def _manageEndOptions(self, options, vehicle):
        ...
    def _initFlashValues(self, ctx):
        ...
