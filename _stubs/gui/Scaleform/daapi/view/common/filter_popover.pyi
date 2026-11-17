# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/common/filter_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import itertools as itertools
import logging as logging
import typing as typing
from future.utils import viewvalues as viewvalues
import constants as constants
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import VEHICLE_CAROUSEL_COUNTERS_SEEN as VEHICLE_CAROUSEL_COUNTERS_SEEN
from account_helpers.settings_core import settings_constants as settings_constants
from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS as SETTINGS_SECTIONS
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as _CAPS
from gui import GUI_NATIONS as GUI_NATIONS
from gui.Scaleform import getNationsFilterAssetPath as getNationsFilterAssetPath, getVehicleTypeAssetPath as getVehicleTypeAssetPath, getLevelsAssetPath as getLevelsAssetPath, getButtonsAssetPath as getButtonsAssetPath, getCustomizationTypeAssetPath as getCustomizationTypeAssetPath
from gui.Scaleform.daapi.view.common.common_constants import FILTER_POPOVER_SECTION as FILTER_POPOVER_SECTION
from gui.Scaleform.daapi.view.common.shared import isVehicleFilterNew as isVehicleFilterNew
from gui.Scaleform.daapi.view.common.filter_contexts import FilterSetupContext as FilterSetupContext, getFilterPopoverSetupContexts as getFilterPopoverSetupContexts
from gui.filters.carousel_filter import FILTER_KEYS as FILTER_KEYS
from gui.Scaleform.daapi.view.lobby.hangar.carousels.battle_pass import BattlePassFilterConsts as BattlePassFilterConsts
from gui.Scaleform.daapi.view.meta.TankCarouselFilterPopoverMeta import TankCarouselFilterPopoverMeta as TankCarouselFilterPopoverMeta
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TANK_CAROUSEL_FILTER import TANK_CAROUSEL_FILTER as TANK_CAROUSEL_FILTER
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.prb_control.settings import VEHICLE_LEVELS as VEHICLE_LEVELS
from gui.shared.formatters import text_styles as text_styles
from gui.shared.formatters.ranges import toRomanRangeString as toRomanRangeString
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER as VEHICLE_TYPES_ORDER, VEHICLE_ROLES_LABELS as VEHICLE_ROLES_LABELS, VEHICLE_CLASS_NAME as VEHICLE_CLASS_NAME, VEHICLE_ROLES_LABELS_BY_CLASS as VEHICLE_ROLES_LABELS_BY_CLASS
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IBattlePassController as IBattlePassController, IHangarGuiController as IHangarGuiController
from skeletons.gui.shared import IItemsCache as IItemsCache
from uilogging.customization_3d_objects.logger import CustomizationHangarVehicleFilterLogger as CustomizationHangarVehicleFilterLogger
from uilogging.customization_3d_objects.logging_constants import CustomizationButtons as CustomizationButtons, CustomizationViewKeys as CustomizationViewKeys
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_environment import ICarouselEnvironment as ICarouselEnvironment
_logger: Any
_VEHICLE_LEVEL_FILTERS: list

class VehiclesFilterPopover(TankCarouselFilterPopoverMeta):
    itemsCache: Any
    _carousel: Any
    _isFrontline: Any
    _isRanked: Any
    _isComp7: Any
    _withRoles: Any
    _mapping: Any
    __usedFilters: Any
    def __init__(self, ctx):
        ...
    def setTankCarousel(self, carousel):
        ...
    def changeFilter(self, sectionId, itemId):
        ...
    def changeSearchNameVehicle(self, inputText):
        ...
    def _getUpdateVO(self, filters):
        ...
    def _getInitialVO(self, filters, xpRateMultiplier):
        ...
    def _packSpecial(self, entry, filterCtx, isSelected, tooltipRes, enabled):
        ...
    def _dispose(self):
        ...
    def _update(self, isInitial=False):
        ...
    @classmethod
    def _generateMapping(cls, hasRented, hasEvent, hasRoles, hasCustomization, **kwargs):
        ...
    def __getSelectedVehType(self, filters):
        ...
    def __onCarouselSwitched(self):
        ...
    @staticmethod
    def __getRolesLabel(vehType):
        ...
    @staticmethod
    def __getRoleVO(role, filters):
        ...
    def __markAsSeen(self, entry):
        ...
    def __getSeenEnties(self):
        ...

class StorageBlueprintsFilterPopover(VehiclesFilterPopover):
    def _getInitialVO(self, filters, xpRateMultiplier):
        ...
    def _generateMapping(self, hasRented, hasEvent, hasRoles, hasCustomization, **kwargs):
        ...

class TankCarouselFilterPopover(VehiclesFilterPopover):
    _BASE_SPECIALS_LIST: list
    __settingsCore: Any
    _carouselRowCount: Any
    def __init__(self, ctx):
        ...
    def switchCarouselType(self, selected):
        ...
    @classmethod
    def _hasClanWarsVehicles(cls):
        ...
    @classmethod
    def _getBaseSpecialsList(cls):
        ...
    @classmethod
    def _generateMapping(cls, hasRented, hasEvent, hasRoles, hasCustomization, **kwargs):
        ...
    def _dispose(self):
        ...
    def _getInitialVO(self, filters, xpRateMultiplier):
        ...
    def _readRowCount(self, _):
        ...
    def _saveRowCount(self):
        ...
    def _update(self, isInitial=False):
        ...

class HangarTankCarouselFilterPopover(TankCarouselFilterPopover):
    __hangarGuiCtrl: Any
    __settingsCore: Any
    __uiCustomizationLogger: Any
    def __init__(self, ctx):
        ...
    def _getInitialVO(self, filters, xpRateMultiplier):
        ...
    @classmethod
    def _getBaseSpecialsList(cls):
        ...
    def changeFilter(self, sectionId, itemId):
        ...

class BattlePassCarouselFilterPopover(HangarTankCarouselFilterPopover):
    __battlePassController: Any
    @classmethod
    def _generateMapping(cls, hasRented, hasEvent, hasRoles, hasCustomization, **kwargs):
        ...
    def _getInitialVO(self, filters, xpRateMultiplier):
        ...
