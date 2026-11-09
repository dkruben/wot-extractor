# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/trade_in.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from contextlib import contextmanager as contextmanager
import typing as typing
from enum import Enum as Enum
from future.utils import iteritems as iteritems, itervalues as itervalues, viewvalues as viewvalues
from cache import cached_property as cached_property
from gui import SystemMessages as SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared import g_eventBus as g_eventBus
from gui.shared.events import VehicleBuyEvent as VehicleBuyEvent
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.money import Money as Money, Currency as Currency, MONEY_ZERO_GOLD as MONEY_ZERO_GOLD
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from items import UNDEFINED_ITEM_CD as UNDEFINED_ITEM_CD
from skeletons.gui.game_control import ITradeInController as ITradeInController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from trade_in_common.constants_types import TradeInInfo as TradeInInfo, ConversionRule as ConversionRule, CONFIG_NAME as TRADE_IN_CONFIG_NAME
from typing import List as List, Set as Set, Optional as Optional, Dict as Dict
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.server_events.event_items import Action as Action
_logger: Any

class TradeInState(Enum):
    UNDEFINED = 0
    AVAILABLE = 1
    UNAVAILABLE = 2

class TradeInDiscounts(object):
    minDiscountVehicleCD: Any
    minDiscountPrice: Any
    maxDiscountVehicleCD: Any
    maxDiscountPrice: Any
    freeExchange: Any
    def __init__(self, minDiscountVehicleCD, minDiscountPrice, maxDiscountVehicleCD, maxDiscountPrice, freeExchange):
        ...
    @property
    def hasMultipleTradeOffs(self):
        ...
    def __str__(self):
        ...
    def __eq__(self, other):
        ...
    def __hash__(self):
        ...

class TradeInConfig(object):
    lobbyContext: Any
    itemsCache: Any
    _config: Any
    def __init__(self):
        ...
    # decorador original: @cached_property
    def tradeInInfoList(self):
        ...
    # decorador original: @cached_property
    def allAccessTokenSet(self):
        ...
    # decorador original: @cached_property
    def hasOfferVisibleForEveryone(self):
        ...
    def getVehiclesInGroup(self, groupId):
        ...
    def getTradeInInfoByVehicleToSell(self, vehCD):
        ...
    def getTradeInInfosByVehicleToBuy(self, vehCD):
        ...
    def getSellPriceFactorFor(self, vehCD):
        ...

class _TradeInInfoWithVehicles(object):
    tradeInInfo: Any
    vehiclesCDs: Any
    def __init__(self, tradeInInfo, vehiclesCDs=None):
        ...

class _TradeInVehicle(object):
    itemsCache: Any
    vehicleCD: Any
    possibleVehiclesToTradeInCDs: Any
    def __init__(self, vehicleCD=..., possibleVehiclesToTradeInCDs=None):
        ...
    def isSelected(self):
        ...
    @property
    def vehicle(self):
        ...

class _TradeInVehicleToBuy(_TradeInVehicle):
    ...

class _TradeInVehicleToSell(_TradeInVehicle):
    conversionRule: Any
    def __init__(self, vehicleCD=..., possibleVehiclesToTradeInCDs=None, conversionRule=None):
        ...

class _TradeInEventBus(object):
    events: Any
    lockLevel: Any
    def __init__(self):
        ...
    # decorador original: @contextmanager
    def getTransaction(self):
        ...
    def startTransaction(self):
        ...
    def commitTransaction(self, force=False):
        ...
    def call(self, event):
        ...

class TradeInController(ITradeInController):
    eventsCache: Any
    itemsCache: Any
    lobbyContext: Any
    __cache: Any
    __config: Any
    _vehicleToSellInfo: Any
    _vehicleToBuyInfo: Any
    _cachedState: Any
    _eventBus: Any
    def __init__(self):
        ...
    def selectVehicleToBuy(self, vehCD):
        ...
    def getSelectedVehicleToBuy(self):
        ...
    def selectVehicleToSell(self, vehCD):
        ...
    def getSelectedVehicleToSell(self):
        ...
    def isEnabled(self):
        ...
    def getActionExpirationTime(self):
        ...
    def getTokenExpirationTime(self):
        ...
    def getExpirationTime(self):
        ...
    def getConfig(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def onLobbyInited(self, event):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onDisconnected(self):
        ...
    def getTradeInDiscounts(self, vehicle):
        ...
    def getAllPossibleVehiclesToSell(self):
        ...
    def getAllPossibleVehiclesToBuy(self):
        ...
    def getPossibleVehiclesToBuy(self):
        ...
    def getVehiclesToSell(self, respectSelectedVehicleToBuy):
        ...
    def getVehiclesToBuy(self, respectSelectedVehicleToSell):
        ...
    def validatePossibleVehicleToBuy(self, vehicle):
        ...
    def getTradeInPrice(self, vehicle):
        ...
    def addTradeInPriceIfNeeded(self, vehicle, money):
        ...
    def __changeCachedState(self, newState):
        ...
    def __fillConfig(self):
        ...
    def __clearConfig(self):
        ...
    def __clearCache(self):
        ...
    def __fillCache(self):
        ...
    def __resetSelectedVehiclesIfNeeded(self):
        ...
    def hasAvailableOffer(self):
        ...
    def __onServerSettingsChanged(self, diff):
        ...
    def __onSync(self, updateReason, diff):
        ...
    def _onTokensUpdated(self, diff):
        ...
    def __canSetVehicleToSell(self, newVehicleToSellCD):
        ...
    def __canSetVehicleToBuy(self, newVehicleToBuyCD):
        ...
