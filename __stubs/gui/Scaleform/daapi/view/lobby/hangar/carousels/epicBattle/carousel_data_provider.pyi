# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/epicBattle/carousel_data_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import UNLOCK_VEHICLES_IN_BATTLE_HINTS as UNLOCK_VEHICLES_IN_BATTLE_HINTS
from constants import MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL, MIN_VEHICLE_LEVEL as MIN_VEHICLE_LEVEL
from gui import GUI_NATIONS_ORDER_INDEX as GUI_NATIONS_ORDER_INDEX
from gui.Scaleform.daapi.view.lobby.epicBattle.epic_helpers import isVehLevelUnlockableInBattle as isVehLevelUnlockableInBattle
from gui.Scaleform.daapi.view.lobby.hangar.carousels.basic.carousel_data_provider import HangarCarouselDataProvider as HangarCarouselDataProvider, _SUPPLY_ITEMS as _SUPPLY_ITEMS, _FRONT_SUPPLY_ITEMS as _FRONT_SUPPLY_ITEMS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle, VEHICLE_TYPES_ORDER_INDICES as VEHICLE_TYPES_ORDER_INDICES
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import dependency as dependency, int2roman as int2roman
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController

class EpicBattleCarouselDataProvider(HangarCarouselDataProvider):
    __epicController: Any
    __separatorItems: Any
    __filteredSeparators: Any
    __indexToScroll: Any
    _filteredIndices: Any
    _selectedIdx: Any
    def __init__(self, carouselFilter, itemsCache):
        ...
    def _getFrontIndices(self):
        ...
    @property
    def collection(self):
        ...
    def getCurrentVehiclesCount(self):
        ...
    def clear(self):
        ...
    def getIndexToScroll(self):
        ...
    def updateVehicles(self, vehiclesCDs=None, filterCriteria=None, forceUpdate=False):
        ...
    def applyFilter(self, forceApply=False):
        ...
    def _buildVehicleItems(self):
        ...
    def __buildSeparatorItems(self):
        ...
    @classmethod
    def _vehicleComparisonKey(cls, vehicle):
        ...
    @classmethod
    def _isSuitableForQueue(cls, vehicle):
        ...
    def _buildVehicle(self, vehicle):
        ...
    def _getSupplyIndices(self):
        ...
    def __getLevelInfo(self, level):
        ...
    def __isHintsShown(self):
        ...
