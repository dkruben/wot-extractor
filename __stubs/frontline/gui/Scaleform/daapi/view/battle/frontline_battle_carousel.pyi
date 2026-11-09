# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_battle_carousel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import weakref as weakref
from future.utils import listvalues as listvalues
import BigWorld as BigWorld
import Event as Event
from account_helpers.AccountSettings import EPICBATTLE_CAROUSEL_FILTER_1 as EPICBATTLE_CAROUSEL_FILTER_1, EPICBATTLE_CAROUSEL_FILTER_2 as EPICBATTLE_CAROUSEL_FILTER_2, EPICBATTLE_CAROUSEL_FILTER_CLIENT_2 as EPICBATTLE_CAROUSEL_FILTER_CLIENT_2
from frontline.gui.Scaleform.daapi.view.battle.frontline_battle_carousel_filters import FLRentedCriteriaGroup as FLRentedCriteriaGroup, FL_RENT as FL_RENT
from frontline.gui.Scaleform.daapi.view.meta.BattleTankCarouselMeta import BattleTankCarouselMeta as BattleTankCarouselMeta
from frontline.gui.Scaleform.genConsts.FRONTLINE_BATTLE_VIEW_ALIASES import FRONTLINE_BATTLE_VIEW_ALIASES as FRONTLINE_BATTLE_VIEW_ALIASES
from gui import GUI_NATIONS_ORDER_INDEX as GUI_NATIONS_ORDER_INDEX
from gui.filters.carousel_filter import CarouselFilter as CarouselFilter, FILTER_KEYS as FILTER_KEYS
from gui.Scaleform import getButtonsAssetPath as getButtonsAssetPath
from gui.Scaleform.daapi.view.common.filter_contexts import getFilterSetupContexts as getFilterSetupContexts
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_data_provider import CarouselDataProvider as CarouselDataProvider
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.prb_control.settings import VEHICLE_LEVELS as VEHICLE_LEVELS
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER_INDICES as VEHICLE_TYPES_ORDER_INDICES
from gui.impl.gen import R as R
from gui.impl import backport as backport
from helpers import dependency as dependency
import nations as nations
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.Scaleform.daapi.view.battle.shared.respawn import respawn_utils as respawn_utils
from gui.shared.gui_items import ItemsCollection as ItemsCollection
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController, IVehiclePlaylistsController as IVehiclePlaylistsController
from skeletons.gui.shared.gui_items import IGuiItemsFactory as IGuiItemsFactory
_logger: Any
_CAROUSEL_FILTERS: tuple
DEFAULT_VEHICLE_PLAY_LIST = ''

class BattleCarouselFilter(CarouselFilter):
    __epicController: Any
    __vehiclePlaylistsCtrl: Any
    _serverSections: Any
    _clientSections: Any
    _criteriesGroups: Any
    def __init__(self):
        ...
    def _setCriteriaGroups(self):
        ...

class BattleCarouselDataProvider(CarouselDataProvider):
    sessionProvider: Any
    __vehPlaylistsCtrl: Any
    __separatorItems: Any
    __filteredSeparators: Any
    __availableLevels: Any
    __indexToScroll: Any
    __currentVehicle: Any
    _showVehicleStats: Any
    _filteredIndices: Any
    _selectedIdx: Any
    def __init__(self, carouselFilter, itemsCache):
        ...
    def hasRentedVehicles(self):
        ...
    @property
    def collection(self):
        ...
    def getCurrentVehiclesCount(self):
        ...
    def setShowStats(self, showVehicleStats):
        ...
    def clear(self):
        ...
    def getIndexToScroll(self):
        ...
    def getAvailableLevels(self):
        ...
    def applyFilter(self, forceApply=False):
        ...
    def getVehiclePlayList(self):
        ...
    def getVisibleVehiclesIntCDs(self, vehLevelsToScroll):
        ...
    def updateVehicleStates(self, slotsStatesData):
        ...
    def selectVehicle(self, filteredIdx):
        ...
    def getSelectedVehicle(self):
        ...
    def selectVehicleByID(self, vehicleID):
        ...
    def _buildVehicleItems(self):
        ...
    def _buildVehicle(self, vehicle):
        ...
    def _getVehicleStats(self, vehicle):
        ...
    def _syncRandomStats(self):
        ...
    @classmethod
    def _vehicleComparisonKey(cls, vehicle):
        ...
    def __isVehicleLevelsFilterNeeded(self):
        ...
    def __calculateCountOfVehicleLevels(self):
        ...
    def __buildSeparatorItems(self):
        ...
    @staticmethod
    def __getVehLevelsUnlockInBattle():
        ...

class VehicleData(object):
    sessionProvider: Any
    itemsFactory: Any
    items: Any
    __carouselRef: Any
    __vehicles: Any
    __eManager: Any
    onSyncCompleted: Any
    def __init__(self, carousel):
        ...
    def dispose(self):
        ...
    def isSynced(self):
        ...
    def getVehicles(self, criteria=None):
        ...
    def getRawVehicleData(self, invID):
        ...
    def __updateRespawnVehicles(self, vehs):
        ...

class BattleTankCarousel(BattleTankCarouselMeta):
    _DISABLED_FILTERS: list
    sessionProvider: Any
    __vehiclePlaylistsCtrl: Any
    _carouselDPCls: Any
    _carouselFilterCls: Any
    __vehicleData: Any
    __isUnlockedVehiclesShown: Any
    _carouselDP: Any
    def __init__(self):
        ...
    def sortVehicles(self, _):
        ...
    def resetPlaylistAndFilters(self):
        ...
    def setFilter(self, idx):
        ...
    def updateVehicleStates(self, slotsStatesData):
        ...
    def getSelectedVehicle(self):
        ...
    def getVehiclePlayList(self):
        ...
    def selectVehicleByID(self, vehicleID):
        ...
    def latePopulate(self):
        ...
    def getCustomParams(self):
        ...
    def show(self):
        ...
    def hasRentedVehicles(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _initDataProvider(self):
        ...
    def _getFiltersVisible(self):
        ...
    def _getInitialFilterVO(self, contexts):
        ...
    @classmethod
    def _makeFilterVO(cls, filterID, contexts, filters):
        ...
    def _getFilters(self):
        ...
    def __onViewLoaded(self, view, *args):
        ...

def getEpicVehicleDataVO(vehicle):
    ...
