# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/hangar_cm_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from logging import getLogger as getLogger
from typing import TYPE_CHECKING as TYPE_CHECKING
import BigWorld as BigWorld
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from adisp import adisp_process as adisp_process
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getTradeInVehiclesUrl as getTradeInVehiclesUrl
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity as EventSystemEntity
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler as AbstractContextMenuHandler, CM_BUY_COLOR as CM_BUY_COLOR
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.impl.lobby.hangar.buy_vehicle_view import VehicleBuyActionTypes as VehicleBuyActionTypes
from gui.prb_control import prbDispatcherProperty as prbDispatcherProperty
from gui.shared import event_dispatcher as shared_events
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showShop as showShop, showTelecomRentalPage as showTelecomRentalPage
from gui.shared.events import HangarVehicleEvent as HangarVehicleEvent
from gui.shared.gui_items.items_actions import factory as ItemsActionsFactory
from gui.shared.gui_items.processors.vehicle import VehicleFavoriteProcessor as VehicleFavoriteProcessor
from helpers import dependency as dependency
from items import UNDEFINED_ITEM_CD as UNDEFINED_ITEM_CD
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket, IEpicBattleMetaGameController as IEpicBattleMetaGameController, ITradeInController as ITradeInController, IVehiclePlaylistsController as IVehiclePlaylistsController, IHangarGuiController as IHangarGuiController, IWotPlusController as IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import NATION_CHANGE_VIEWED as NATION_CHANGE_VIEWED
from typing import Optional as Optional
from gui.shared.gui_items import Vehicle as Vehicle
_logger: Any

class MODULE(object):
    INFO = 'moduleInfo'
    CANCEL_BUY = 'cancelBuy'
    UNLOAD = 'unload'
    UNLOCK = 'unlock'
    EQUIP = 'equip'
    SELL = 'sell'
    BUY_AND_EQUIP = 'buyAndEquip'

class VEHICLE(object):
    EXCHANGE = 'exchange'
    INFO = 'vehicleInfo'
    PREVIEW = 'preview'
    STATS = 'showVehicleStatistics'
    UNLOCK = 'unlock'
    SELECT = 'selectVehicle'
    SELL = 'sell'
    BUY = 'buy'
    RESEARCH = 'vehicleResearch'
    POST_PROGRESSION = 'vehiclePostProgression'
    RENEW = 'vehicleRentRenew'
    REMOVE = 'vehicleRemove'
    CHECK = 'vehicleCheck'
    UNCHECK = 'vehicleUncheck'
    COMPARE = 'compare'
    BLUEPRINT = 'blueprint'
    NATION_CHANGE = 'nationChange'
    GO_TO_COLLECTION = 'goToCollection'
    TELECOM_RENT = 'telecomRent'
    VEH_SKILL_TREE = 'vehSkillTree'
    MANAGE_PLAYLISTS = 'managePlaylists'
    CREATE_PLAYLIST = 'createPlaylist'

class TechnicalMaintenanceCMHandler(AbstractContextMenuHandler, EventSystemEntity):
    itemsCache: Any
    _equipmentCD: Any
    _isCanceled: Any
    def __init__(self, cmProxy, ctx=None):
        ...
    def showModuleInfo(self):
        ...
    def resetSlot(self):
        ...
    def _initFlashValues(self, ctx):
        ...
    def _clearFlashValues(self):
        ...
    def _generateOptions(self, ctx=None):
        ...

class SimpleVehicleCMHandler(AbstractContextMenuHandler, EventSystemEntity):
    itemsCache: Any
    def getVehCD(self):
        ...
    def getVehInvID(self):
        ...
    def showVehicleInfo(self):
        ...
    def showVehicleStats(self):
        ...
    def sellVehicle(self):
        ...
    def buyVehicle(self):
        ...
    def _generateOptions(self, ctx=None):
        ...

class VehicleContextMenuHandler(SimpleVehicleCMHandler):
    _comparisonBasket: Any
    _epicController: Any
    _tradeInController: Any
    _lobbyContext: Any
    __hangarGuiCtrl: Any
    __vehiclePlaylistsCtrl: Any
    _wotPlusController: Any
    vehInvID: Any
    vehCD: Any
    def __init__(self, cmProxy, ctx=None):
        ...
    # decorador original: @prbDispatcherProperty
    def prbDispatcher(self):
        ...
    def getVehCD(self):
        ...
    def getVehInvID(self):
        ...
    def toResearch(self):
        ...
    def showPostProgression(self):
        ...
    def showVehSkillTree(self):
        ...
    def showManagePlaylists(self):
        ...
    def showVehicleExchange(self):
        ...
    def checkFavoriteVehicle(self):
        ...
    def uncheckFavoriteVehicle(self):
        ...
    def compareVehicle(self):
        ...
    def changeVehicleNation(self):
        ...
    def goToCollection(self):
        ...
    def showTelecomRent(self):
        ...
    def _initFlashValues(self, ctx):
        ...
    def _clearFlashValues(self):
        ...
    def _generateOptions(self, ctx=None):
        ...
    def _manageVehCompareOptions(self, options, vehicle):
        ...
    # decorador original: @adisp_process
    def __favoriteVehicle(self, isFavorite):
        ...
