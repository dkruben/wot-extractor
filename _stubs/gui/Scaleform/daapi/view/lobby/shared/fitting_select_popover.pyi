# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/shared/fitting_select_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from CurrentVehicle import g_currentVehicle as g_currentVehicle, g_currentPreviewVehicle as g_currentPreviewVehicle
from gui.Scaleform.daapi.view.lobby.shared.fitting_select.module_extenders import fittingSelectModuleExtenders as fittingSelectModuleExtenders
from gui.Scaleform.daapi.view.meta.FittingSelectPopoverMeta import FittingSelectPopoverMeta as FittingSelectPopoverMeta
from gui.Scaleform.genConsts.FITTING_TYPES import FITTING_TYPES as FITTING_TYPES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.shared import event_dispatcher as shared_events
from gui.shared.formatters import text_styles as text_styles, getItemPricesVOWithReason as getItemPricesVOWithReason
from gui.shared.formatters.text_styles import builder as str_builder
from gui.shared.gui_items import GUI_ITEM_TYPE_INDICES as GUI_ITEM_TYPE_INDICES, GUI_ITEM_TYPE as GUI_ITEM_TYPE, GUI_ITEM_ECONOMY_CODE as GUI_ITEM_ECONOMY_CODE, GUI_ITEM_TYPE_NAMES as GUI_ITEM_TYPE_NAMES
from gui.shared.gui_items.fitting_item import FittingItem as FittingItem
from gui.shared.gui_items.items_actions import factory as ItemsActionsFactory
from gui.shared.items_parameters import params_helper as params_helper
from gui.shared.items_parameters.formatters import formatModuleParamName as formatModuleParamName, formatParameter as formatParameter
from gui.shared.utils import EXTRA_MODULE_INFO as EXTRA_MODULE_INFO
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency, i18n as i18n
from helpers.i18n import makeString as _ms
from items import getTypeInfoByName as getTypeInfoByName
from items.vehicles import VehicleDescriptor as VehicleDescriptor
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.vehicle_modules import VehicleGun as VehicleGun, VehicleRadio as VehicleRadio, VehicleEngine as VehicleEngine, VehicleTurret as VehicleTurret, VehicleChassis as VehicleChassis
from gui.Scaleform.daapi.view.lobby.shared.fitting_select.module_extenders import ModuleParamsExtender as ModuleParamsExtender
_logger: Any
FITTING_MODULES: tuple
_PARAMS_LISTS: dict
_POPOVER_FIRST_TAB_IDX = 0
_POPOVER_SECOND_TAB_IDX = 1
_TAB_IDS: tuple

class CommonFittingSelectPopover(FittingSelectPopoverMeta):
    _TAB_IDX = 0
    _TABS = None
    _slotType: Any
    __vehicle: Any
    _logicProvider: Any
    def __init__(self, vehicle, logicProvider, ctx=None):
        ...
    def showModuleInfo(self, moduleId):
        ...
    def setVehicleModule(self, newId, oldId, isRemove):
        ...
    def setCurrentTab(self, tabIndex):
        ...
    def _saveTabIndex(self, index):
        ...
    def _getInitialTabIndex(self):
        ...
    def _getVehicle(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _prepareInitialData(self):
        ...
    def _getTabsData(self):
        ...
    def _getDescText(self):
        ...
    def _getCommonData(self):
        ...

class ModuleFittingSelectPopover(CommonFittingSelectPopover):
    _itemsCache: Any
    __preferredLayout: Any
    __slotIndex: Any
    def __init__(self, ctx=None, customProviderClass=None):
        ...
    def _prepareInitialData(self):
        ...
    def _getSlotIndex(self):
        ...

class PopoverLogicProvider(object):
    _itemsCache: Any
    _settingsCore: Any
    _slotType: Any
    _slotIndex: Any
    _vehicle: Any
    _tooltipType: Any
    __modulesList: Any
    _selectedIdx: Any
    _tabIndex: Any
    __moduleExtenders: Any
    def __init__(self, slotType, slotIndex, vehicle):
        ...
    def getSelectedIdx(self):
        ...
    def getDevices(self):
        ...
    def setModule(self, newId, oldId, isRemove):
        ...
    def setTab(self, tabIndex):
        ...
    def dispose(self):
        ...
    def _buildCommonModuleData(self, module, reason):
        ...
    def _buildModuleData(self, vehicleModule, isInstalledInSlot, stats):
        ...
    def _buildList(self):
        ...
    def _getSuitableItems(self, typeId):
        ...
    def _getItemsSortingKey(self):
        ...
    def _getSpecificCriteria(self, typeID):
        ...
    def __extendByTypeSpecificData(self, moduleData, vehicleModule):
        ...

class _HangarLogicProvider(PopoverLogicProvider):
    _tooltipType: Any
    def __init__(self, slotType, slotIndex):
        ...
    def setModule(self, newId, oldId, isRemove):
        ...
    def _buildModuleData(self, vehicleModule, isInstalledInSlot, stats):
        ...

class _PreviewLogicProvider(PopoverLogicProvider):
    _tooltipType: Any
    def __init__(self, slotType, slotIndex):
        ...
    def setModule(self, newId, oldId, isRemove):
        ...
    def _buildModuleData(self, vehicleModule, isInstalledInSlot, _):
        ...

def _extendByModuleData(targetData, vehicleModule, vehDescr, extenders):
    ...
def _getInstallReason(module, vehicle, reason, slotIdx=None):
    ...
def _getStatus(reason):
    ...
def _formatValuesString(valuesStr):
    ...
def _convertTarget(target, reason):
    ...
