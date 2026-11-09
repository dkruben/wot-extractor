# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/basic/carousel_data_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
from account_helpers.telecom_rentals import TelecomRentals as TelecomRentals
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as _CAPS
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.filters.carousel_filter import FILTER_KEYS as FILTER_KEYS
from gui.Scaleform import MENU as MENU
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_data_provider import CarouselDataProvider as CarouselDataProvider
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_data_provider import getStatusStrings as getStatusStrings
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.tooltips import ACTION_TOOLTIPS_TYPE as ACTION_TOOLTIPS_TYPE
from gui.shared.tooltips.formatters import packActionTooltipData as packActionTooltipData
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.game_control import IHangarGuiController as IHangarGuiController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from telecom_rentals_common import ROSTER_EXPIRATION_TOKEN_NAME as ROSTER_EXPIRATION_TOKEN_NAME, PARTNERSHIP_TOKEN_NAME as PARTNERSHIP_TOKEN_NAME

class _FRONT_SUPPLY_ITEMS(object):
    RENT_TANK = 0
    ALL: tuple

class _SUPPLY_ITEMS(object):
    BUY_TANK = 0
    RESTORE_TANK = 1
    BUY_SLOT = 2
    ALL: tuple

class HangarCarouselDataProvider(CarouselDataProvider):
    _lobbyContext: Any
    __hangarGuiCtrl: Any
    _serverSettings: Any
    _frontSupplyItems: Any
    _telecomRentalsVehicles: Any
    _supplyItems: Any
    _emptySlotsCount: Any
    _restorableVehiclesCount: Any
    _telecomRentals: Any
    _dynamicFiltersState: Any
    _baseCriteria: Any
    def __init__(self, carouselFilter, itemsCache):
        ...
    @property
    def collection(self):
        ...
    def getCurrentVehiclesCount(self):
        ...
    def getHiddenDynamicFilters(self):
        ...
    def clear(self):
        ...
    def updateDynamicFilters(self):
        ...
    def updateSupplies(self):
        ...
    @staticmethod
    def _isSuitableForQueue(vehicle):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _isTelecomRentalsEnabled(self):
        ...
    def _getAdditionalItemsIndexes(self):
        ...
    def _getFrontIndices(self):
        ...
    def _getFrontAdditionalItemsIndexes(self):
        ...
    def _getSupplyIndices(self):
        ...
    def _setBaseCriteria(self):
        ...
    def _onTelecomRentalsChanged(self, diff):
        ...
    def _onTelecomPendingRentChanged(self, vehCD):
        ...
    def _buildTelecomRentalVehicleItems(self):
        ...
    def _buildRentPromitionVehicleItems(self):
        ...
    def _buildFrontSupplyItems(self):
        ...
    def _buildVehicle(self, vehicle):
        ...
    def _buildVehicleItems(self):
        ...
    def _buildSupplyItems(self):
        ...
    def _updateDynamicFilters(self):
        ...
