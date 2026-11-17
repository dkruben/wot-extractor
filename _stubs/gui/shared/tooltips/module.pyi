# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/module.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from builtins import filter as filter, next as next, range as range, zip as zip
from future.utils import itervalues as itervalues, viewvalues as viewvalues
from gui.Scaleform import MENU as MENU
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.genConsts.NODE_STATE_FLAGS import NODE_STATE_FLAGS as NODE_STATE_FLAGS
from gui.Scaleform.genConsts.SLOT_HIGHLIGHT_TYPES import SLOT_HIGHLIGHT_TYPES as SLOT_HIGHLIGHT_TYPES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.game_control.wot_plus.utils import hasFreeEquipDemountPromo as hasFreeEquipDemountPromo, hasFreeDeluxeEquipDemountPromo as hasFreeDeluxeEquipDemountPromo
from gui.impl import backport as backport
from gui.impl.backport import backport_r as backport_r
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.tank_setup.common.specialization_model import SpecializationModel as SpecializationModel
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, GUI_ITEM_ECONOMY_CODE as GUI_ITEM_ECONOMY_CODE, getKpiValueString as getKpiValueString
from gui.shared.gui_items.gui_item_economics import isItemBuyPriceAvailable as isItemBuyPriceAvailable
from gui.shared.items_parameters import params_helper as params_helper, formatters as params_formatters, bonus_helper as bonus_helper
from gui.shared.items_parameters.params_helper import SimplifiedBarVO as SimplifiedBarVO
from gui.shared.money import MONEY_UNDEFINED as MONEY_UNDEFINED, Currency as Currency
from gui.shared.tooltips import getComplexStatusWULF as getComplexStatusWULF, getUnlockPrice as getUnlockPrice, TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData, makePriceBlock as makePriceBlock, CURRENCY_SETTINGS as CURRENCY_SETTINGS, makeRemovalPriceBlock as makeRemovalPriceBlock
from gui.shared.utils import GUN_CLIP as GUN_CLIP, SHELLS_COUNT_PROP_NAME as SHELLS_COUNT_PROP_NAME, SHELL_RELOADING_TIME_PROP_NAME as SHELL_RELOADING_TIME_PROP_NAME, RELOAD_MAGAZINE_TIME_PROP_NAME as RELOAD_MAGAZINE_TIME_PROP_NAME, AIMING_TIME_PROP_NAME as AIMING_TIME_PROP_NAME, RELOAD_TIME_PROP_NAME as RELOAD_TIME_PROP_NAME, GUN_AUTO_RELOAD as GUN_AUTO_RELOAD, AUTO_RELOAD_PROP_NAME as AUTO_RELOAD_PROP_NAME, DISPERSION_RADIUS as DISPERSION_RADIUS, RELOAD_TIME_SECS_PROP_NAME as RELOAD_TIME_SECS_PROP_NAME, DUAL_GUN_RATE_TIME as DUAL_GUN_RATE_TIME, DUAL_GUN_CHARGE_TIME as DUAL_GUN_CHARGE_TIME, BURST_FIRE_RATE as BURST_FIRE_RATE, BURST_TIME_INTERVAL as BURST_TIME_INTERVAL, BURST_COUNT as BURST_COUNT, BURST_SIZE as BURST_SIZE, GUN_DUAL_GUN as GUN_DUAL_GUN, GUN_CAN_BE_CLIP as GUN_CAN_BE_CLIP, GUN_CAN_BE_AUTO_RELOAD as GUN_CAN_BE_AUTO_RELOAD, GUN_CAN_BE_DUAL_GUN as GUN_CAN_BE_DUAL_GUN, GUN_CAN_BE_AUTO_SHOOT as GUN_CAN_BE_AUTO_SHOOT, GUN_AUTO_SHOOT as GUN_AUTO_SHOOT, TURBOSHAFT_ENGINE_POWER as TURBOSHAFT_ENGINE_POWER, ROCKET_ACCELERATION_ENGINE_POWER as ROCKET_ACCELERATION_ENGINE_POWER, DUAL_ACCURACY_COOLING_DELAY as DUAL_ACCURACY_COOLING_DELAY, CONTINUOUS_SHOTS_PER_MINUTE as CONTINUOUS_SHOTS_PER_MINUTE, CONTINUOUS_DAMAGE_PER_SECOND as CONTINUOUS_DAMAGE_PER_SECOND, GUN_CAN_BE_TWIN_GUN as GUN_CAN_BE_TWIN_GUN, GUN_TWIN_GUN as GUN_TWIN_GUN, TWIN_GUN_RELOAD_ONE_GUN_TIME as TWIN_GUN_RELOAD_ONE_GUN_TIME, TWIN_GUN_RELOAD_TWO_GUN_TIME as TWIN_GUN_RELOAD_TWO_GUN_TIME, SHELL_LOADING_TIME_PROP_NAME as SHELL_LOADING_TIME_PROP_NAME
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from items.components.supply_slot_categories import SlotCategories as SlotCategories
from shared_utils import first as first
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IWotPlusController as IWotPlusController, ILoadoutController as ILoadoutController
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.gui_items import IGuiItemsFactory as IGuiItemsFactory
from vehicles.mechanics.mechanic_helpers import hasVehicleDescrMechanic as hasVehicleDescrMechanic
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
_logger: Any
_TOOLTIP_WIDTH = 468
_LOW_CHARGE_SHOT_TOOLTIP_WIDTH = 540
_DEFAULT_PADDING = 20
_EMPTY_TOOLTIP_WIDTH = 350
_AUTOCANNON_SHOT_DISTANCE = 400
_OPT_DEVICE_SPEC_ALPHA = 0.5
_OPT_DEVICE_SELECTED_SPEC_ALPHA = 1
_MECHANICS_TEXT_ROOT = R.strings.tooltips.shell.mechanics
_MECHANICS_IMAGE_ROOT = R.images.gui.maps.icons.tooltip.mechanics

class ModuleBlockTooltipData(BlocksTooltipData):
    itemsCache: Any
    itemsFactory: Any
    item: Any
    def __init__(self, context):
        ...
    def _invalidateWidth(self, width):
        ...
    def _getHighLightType(self):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def _getHeaderBlockConstructor(self):
        ...
    def _getEffectsBlockConstructor(self):
        ...
    def _getInventoryBlockConstructor(self):
        ...
    def _getStatsBlockConstructor(self):
        ...

class ModuleTooltipBlockConstructor(object):
    MAX_INSTALLED_LIST_LEN = 10
    CLIP_GUN_MODULE_PARAM = 'vehicleClipGun'
    AUTO_RELOAD_GUN_MODULE_PARAM = 'autoReloadGun'
    AUTO_SHOOT_GUN_MODULE_PARAM = 'autoShootGun'
    DUAL_GUN_MODULE_PARAM = 'dualGun'
    WEIGHT_MODULE_PARAM = 'weight'
    TURBOSHAFT_ENGINE_MODULE_PARAM = 'turboshaftEngine'
    ROCKET_ACCELERATION_ENGINE_MODULE_PARAM = 'rocketAcceleration'
    COOLDOWN_SECONDS = 'cooldownSeconds'
    RELOAD_COOLDOWN_SECONDS = 'reloadCooldownSeconds'
    CALIBER = 'caliber'
    DUAL_ACCURACY_MODULE_PARAM = 'dualAccuracy'
    MUTABLE_DAMAGE_MODULE_PARAM = 'mutableDamage'
    TWIN_GUN_MODULE_PARAM = 'twinGun'
    DEFAULT_PARAM = 'default'
    MODULE_PARAMS: dict
    HIGHLIGHT_MODULE_PARAMS: dict
    itemsCache: Any
    module: Any
    configuration: Any
    leftPadding: Any
    rightPadding: Any
    def __init__(self, module, configuration, leftPadding=..., rightPadding=...):
        ...
    def construct(self):
        ...

class HeaderBlockConstructor(ModuleTooltipBlockConstructor):
    def construct(self):
        ...
    def _getCooldownSeconds(self):
        ...
    def _getIcon(self):
        ...
    def __getOverlayData(self):
        ...

class ModuleHeaderBlockConstructor(ModuleTooltipBlockConstructor):
    def construct(self):
        ...
    def _getIcon(self):
        ...

class PriceBlockConstructor(ModuleTooltipBlockConstructor):
    wotPlusController: Any
    _valueWidth: Any
    _priceLeftPadding: Any
    def __init__(self, module, configuration, valueWidth, leftPadding, rightPadding):
        ...
    def construct(self):
        ...

class InventoryBlockConstructor(ModuleTooltipBlockConstructor):
    _inventoryPadding: Any
    _inInventoryBlockData: Any
    _onVehicleBlockData: Any
    def __init__(self, module, configuration, leftPadding, rightPadding):
        ...
    def construct(self):
        ...
    @staticmethod
    def _getInventoryBlock(count, blockData, padding):
        ...
    def _getDemountCount(self):
        ...
    def _getInstalledVehicles(self, module, inventoryVehicles):
        ...

class CommonStatsBlockConstructor(ModuleTooltipBlockConstructor):
    _valueWidth: Any
    _slotIdx: Any
    __colorScheme: Any
    def __init__(self, module, configuration, slotIdx, leftPadding, rightPadding, colorScheme=None):
        ...
    def construct(self):
        ...
    def _getHeaderBlock(self):
        ...
    def _getValueBlock(self, paramName, comparator, colorScheme):
        ...
    def _packParamBlock(self, paramName, value, highlight):
        ...
    def _getValueComparator(self, vDescr):
        ...
    @classmethod
    def __getExtraStatusBlock(cls, module, vDescr):
        ...

class TwoColumnsStatsBlockConstructor(CommonStatsBlockConstructor):
    __modifiedComparator: Any
    def __init__(self, module, configuration, slotIdx, leftPadding, rightPadding, colorScheme=None):
        ...
    def _getValueBlock(self, paramName, comparator, colorScheme):
        ...
    def _packParamBlock(self, paramName, value, highlight):
        ...
    def _getValueComparator(self, vDescr, dropMechanic=True):
        ...
    def _getHeaderBlock(self):
        ...

class ModuleReplaceBlockConstructor(ModuleTooltipBlockConstructor):
    def construct(self):
        ...

class SimplifiedStatsBlockConstructor(ModuleTooltipBlockConstructor):
    __stockParams: Any
    __comparator: Any
    __isSituational: Any
    def __init__(self, module, configuration, leftPadding, rightPadding, stockParams, comparator):
        ...
    def construct(self):
        ...

class EffectsBlockConstructor(ModuleTooltipBlockConstructor):
    lobbyContext: Any
    def construct(self):
        ...
    def _getOnUseStr(self, attribs, isRemovingStun, **kpiArgs):
        ...

class OptDeviceEffectsBlockConstructor(ModuleTooltipBlockConstructor):
    lobbyContext: Any
    def construct(self):
        ...
    def addKPITable(self, block, hasEffectDescr=False):
        ...
    def _bonusStyleTextStyle(self, text, useStyle=False):
        ...
    def __neutralFatTextStyle(self, text):
        ...
    def __getIterator(self, module, configuration):
        ...

class StatusBlockConstructor(ModuleTooltipBlockConstructor):
    def construct(self):
        ...
    def _getStatus(self):
        ...
    def _packStatusBlock(self, tooltipHeader, tooltipText, titleFormatter, padding=None, gap=1):
        ...
    def _getResearchPageStatus(self):
        ...
    def __getInstalledVehiclesBlock(self, installedVehicles, module):
        ...

class OptDeviceSlotsHeaderBlockConstructor(ModuleTooltipBlockConstructor):
    __loadoutController: Any
    def construct(self):
        ...
    def _getInstalledModule(self, vehicle, slotID):
        ...
    def _getIcon(self, module):
        ...
    def __getOverlayData(self, module):
        ...

class OptDeviceEmptyBlockTooltipData(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class AmmunitionEmptyBlockTooltipData(BlocksTooltipData):
    _HEADER = 'header'
    _BODY = 'body'
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class AmmunitionSlotSpecTooltipData(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, spec, isDyn, isClickable):
        ...

class KpiFormatter(object):
    def getValues(self):
        ...
    def getDescription(self):
        ...
    def getColumnsCount(self):
        ...
    def isHeaderShown(self):
        ...

class RegularKPIFormatter(KpiFormatter):
    kpi: Any
    def __init__(self, kpi):
        ...
    def getValues(self):
        ...
    def getDescription(self):
        ...
    def getColumnsCount(self):
        ...

class DeluxKPIFormatter(KpiFormatter):
    kpi: Any
    def __init__(self, kpi):
        ...
    def getValues(self):
        ...
    def getDescription(self):
        ...

class ComplexFormatter(KpiFormatter):
    headerResTemplate = 'None{index}_{{state}}'
    kpis: Any
    def __init__(self, *kpis):
        ...
    def getValues(self):
        ...
    def getDescription(self):
        ...
    def getColumnsCount(self):
        ...
    def isHeaderShown(self):
        ...
    def getHeaderValues(self):
        ...

class TrophyKPIComplexFormatter(ComplexFormatter):
    headerResTemplate = 'trophy_{index}_{{state}}'

class ModernizedKPIComplexFormatter(ComplexFormatter):
    headerResTemplate = 'modernized_{index}_{{state}}'

class KpiIterator(object):
    formatter = KpiFormatter
    def getKPIs(self):
        ...
    def getCurrentIndex(self):
        ...

class SimpleKPIIterator(KpiIterator):
    configuration: Any
    module: Any
    def __init__(self, configuration, module):
        ...
    def getKPIs(self):
        ...
    def getCurrentIndex(self):
        ...

class ComplexKPIIterator(KpiIterator):
    configuration: Any
    curIndex: Any
    modules: Any
    def __init__(self, configuration, curIndex, *modules):
        ...
    def getKPIs(self):
        ...
    def getCurrentIndex(self):
        ...
    def getColumsCount(self):
        ...

class DeluxKPIIterator(SimpleKPIIterator):
    formatter = DeluxKPIFormatter

class TrophyKPIIterator(ComplexKPIIterator):
    __itemsCache: Any
    formatter = TrophyKPIComplexFormatter
    def __init__(self, configuration, module):
        ...

class RegularKPIIterator(SimpleKPIIterator):
    formatter = RegularKPIFormatter
    def getCurrentIndex(self):
        ...

class ModernizedKPIIterator(ComplexKPIIterator):
    __itemsCache: Any
    formatter = ModernizedKPIComplexFormatter
    def __init__(self, configuration, module):
        ...

def _getSpecsDescAndText(categories):
    ...
def _packSpecsIconsBlockData(vehicle, categories, slotIdx, topOffset=0, leftOffset=0):
    ...
