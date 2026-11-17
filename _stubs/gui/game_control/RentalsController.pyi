# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/RentalsController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import copy as copy
import typing as typing
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from operator import itemgetter as itemgetter
from sys import maxsize as maxsize
import BigWorld as BigWorld
import Event as Event
from constants import RentType as RentType, SEASON_NAME_BY_TYPE as SEASON_NAME_BY_TYPE, IS_RENTALS_ENABLED as IS_RENTALS_ENABLED
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA as REQ_CRITERIA
from gui.shared.money import Money as Money
from helpers import dependency as dependency
from helpers import time_utils as time_utils
from skeletons.gui.game_control import IRentalsController as IRentalsController, ISeasonsController as ISeasonsController, IEpicBattleMetaGameController as IEpicBattleMetaGameController
from skeletons.gui.shared import IItemsCache as IItemsCache
from rent_common import SeasonRentDuration as SeasonRentDuration, calculateSeasonRentPrice as calculateSeasonRentPrice
from gui.shared.gui_items.fitting_item import RentalInfoProvider as RentalInfoProvider
from season_common import GameSeason as GameSeason
RENT_TYPE_WEIGHTS: dict

class RentalsController(IRentalsController):
    itemsCache: Any
    seasonsController: Any
    epicController: Any
    onRentChangeNotify: Any
    __rentNotifyTimeCallback: Any
    __vehiclesForUpdate: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def onLobbyInited(self, event):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onDisconnected(self):
        ...
    def isEnabled(self):
        ...
    def _stop(self):
        ...
    def __onSyncCompleted(self, _, invalidItems):
        ...
    def _update(self, *args):
        ...
    def filterRentPackages(self, rentPrices):
        ...
    def getRentPackagesInfo(self, rentPrices, currentRentInfo):
        ...
    def getRentPriceOfPackage(self, vehicle, rentType, packageID, package):
        ...
    @staticmethod
    def getDeltaPeriod(delta):
        ...
    @staticmethod
    def __filterSeasonCyclePackages(packagesToFilter, filterFunc):
        ...
    def __startRentTimeNotifyCallback(self):
        ...
    def __notifyRentTime(self):
        ...
    def __clearRentTimeNotifyCallback(self):
        ...
    def __seasonFilter(self, seasonID, seasonType, package):
        ...
    def __cycleFilter(self, cycleID, seasonType, _):
        ...
