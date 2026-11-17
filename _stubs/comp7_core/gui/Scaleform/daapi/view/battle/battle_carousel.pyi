# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/battle_carousel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
import typing as typing
import nations as nations
from account_helpers.AccountSettings import AccountSettings as AccountSettings
from comp7_core.gui.Scaleform.daapi.view.battle.common import getSavedRowCountValue as getSavedRowCountValue, rowValueToRowCount as rowValueToRowCount
from comp7_core.gui.Scaleform.daapi.view.meta.Comp7BattleTankCarouselMeta import Comp7BattleTankCarouselMeta as Comp7BattleTankCarouselMeta
from comp7_core.gui.comp7_core_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from comp7_core_constants import ArenaPrebattlePhase as ArenaPrebattlePhase
from constants import REQUEST_COOLDOWN as REQUEST_COOLDOWN, ARENA_PERIOD as ARENA_PERIOD
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui import GUI_NATIONS_ORDER_INDEX as GUI_NATIONS_ORDER_INDEX
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.filters.carousel_filter import CarouselFilter as CarouselFilter, RoleCriteriesGroup as RoleCriteriesGroup
from gui.Scaleform import getButtonsAssetPath as getButtonsAssetPath
from gui.Scaleform.daapi.view.common.filter_contexts import getFilterSetupContexts as getFilterSetupContexts, FilterSetupContext as FilterSetupContext
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_data_provider import CarouselDataProvider as CarouselDataProvider
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView as IAbstractPeriodView
from gui.battle_control.gui_vehicle_builder import VehicleBuilder as VehicleBuilder
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER_INDICES as VEHICLE_TYPES_ORDER_INDICES
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from items import vehicles as vehicles
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.shared.gui_items import IGuiItemsFactory as IGuiItemsFactory
from gui.battle_control.arena_info.interfaces import IPrebattleSetupController as IPrebattleSetupController
_logger: Any
_FLAG_ICON_TEMPLATE = '../maps/icons/flags/160x100/%s.png'
_FLAG_SMALL_ICON_TEMPLATE = '../maps/icons/nations/155x31/%s.png'
_TYPE_ICON_TEMPLATE = '../maps/icons/vehicleTypes/big/%s.png'
_TYPE_ICON_SMALL_TEMPLATE = '../maps/icons/vehicleTypes/60x54/%s.png'

class _InBattleRentedCriteriesGroup(RoleCriteriesGroup):
    __rentedList: Any
    _criteria: Any
    def __init__(self, rentedList):
        ...
    def update(self, filters):
        ...
    def _setRentedCriteria(self, filters):
        ...

class _PrebattleCarouselFilter(CarouselFilter):
    __rentedList: Any
    _serverSections: Any
    _clientSections: Any
    _filters: Any
    _criteriesGroups: Any
    def __init__(self, serverSections, clientSections):
        ...
    def save(self):
        ...
    def load(self):
        ...
    def setRentedList(self, rentedList):
        ...
    def _setCriteriaGroups(self):
        ...

class _PrebattleCarouselDataProvider(CarouselDataProvider):
    __itemsFactory: Any
    __sessionProvider: Any
    _RawVehicleData: Any
    __vehiclesData: Any
    __selectedCD: Any
    _filteredIndices: Any
    _selectedIdx: Any
    _vehicles: Any
    _vehicleItems: Any
    def __init__(self, carouselFilter, itemsCache):
        ...
    def _dispose(self):
        ...
    def getSelectedCD(self):
        ...
    def applyFilter(self, forceApply=False):
        ...
    def getVehicleCDByIdx(self, filteredIdx):
        ...
    def setVehicles(self, vehiclesList):
        ...
    def setCurrentVehicle(self, vehicleCD):
        ...
    def _buildVehicleItems(self):
        ...
    @classmethod
    def _vehicleComparisonKey(cls, vehicle):
        ...
    def __onBanPhaseUpdated(self):
        ...
    def __getVehicleBanCtrl(self):
        ...
    @staticmethod
    def __makeGuiVehicle(vehicleData):
        ...

class PrebattleTankCarousel(Comp7BattleTankCarouselMeta, IAbstractPeriodView):
    __sessionProvider: Any
    _FILTER_SERVER_SECTIONS: tuple
    _FILTER_CLIENT_SECTIONS: tuple
    _carouselDPCls: Any
    _carouselFilterCls: Any
    __cooldownCallback: Any
    _carouselDP: Any
    def __init__(self):
        ...
    def hasRoles(self):
        ...
    def setFilter(self, idx):
        ...
    def setRowCount(self, value):
        ...
    def onViewIsHidden(self):
        ...
    def selectVehicle(self, idx):
        ...
    def setPeriod(self, period):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _initDataProvider(self):
        ...
    def _getFilters(self):
        ...
    def __isSelectionInCooldown(self):
        ...
    def __getPRBController(self):
        ...
    def __getInitialFilterVO(self, contexts):
        ...
    def __onViewLoaded(self, view, *args):
        ...
    def __onAvailableVehiclesUpdated(self, vehiclesList):
        ...
    def __onSelectedVehicleChanged(self, vehicle):
        ...
    def __onSelectionConfirmed(self):
        ...
    def __onBattleStarted(self):
        ...
    def __startCooldown(self):
        ...
    def __onCooldownExpired(self):
        ...
    def __resetCooldown(self):
        ...

def getComp7CarouselVehicleDataVO(vehicle):
    ...
