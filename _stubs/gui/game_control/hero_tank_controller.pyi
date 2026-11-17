# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/hero_tank_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import random as random
from collections import namedtuple as namedtuple
from future.utils import iteritems as iteritems, viewitems as viewitems, viewvalues as viewvalues
import Event as Event
import ResMgr as ResMgr
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from helpers import dependency as dependency
from items import vehicles as vehicles, tankmen as tankmen
from shared_utils import first as first
from skeletons.gui.game_control import IHeroTankController as IHeroTankController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any
_HERO_VEHICLES = 'hero_vehicles'
_ADD_HERO_STEP_NAME = 'add_HeroVehicle'
_HeroTankInfo: Any

class HeroTankController(IHeroTankController):
    itemsCache: Any
    lobbyContext: Any
    _eventsCache: Any
    __data: Any
    __invVehiclesIntCD: Any
    __debugTankCD: Any
    __isEnabled: Any
    __currentTankCD: Any
    onUpdated: Any
    onInteractive: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def __onEventsCacheSyncCompleted(self, *_):
        ...
    def onLobbyStarted(self, ctx):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def isEnabled(self):
        ...
    def setEnabled(self, isEnabled):
        ...
    def getRandomTankCD(self):
        ...
    def getCurrentTankCD(self):
        ...
    def getCurrentTankStyleId(self):
        ...
    def getCurrentRelatedURL(self):
        ...
    def getCurrentShopUrl(self):
        ...
    def getCurrentTankCrew(self):
        ...
    def getCurrentVehicleName(self):
        ...
    def getCurrentFromBoxes(self):
        ...
    def setInteractive(self, interactive):
        ...
    def setDebugTankCD(self, debugTankCD):
        ...
    def __fullUpdate(self):
        ...
    def __updateInventoryVehiclesData(self, reason, diff):
        ...
    def __onServerSettingsChanged(self, diff):
        ...
    def __updateSettings(self):
        ...
    def __applyActions(self):
        ...
    def __addActionVehicle(self, params):
        ...
    def __createCrew(self, crewXml, vCompDescr):
        ...
