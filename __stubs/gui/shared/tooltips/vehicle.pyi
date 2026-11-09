# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/vehicle.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from itertools import chain as chain
import typing as typing
from future.utils import viewitems as viewitems
import constants as constants
from gui.impl.backport.backport_tooltip import DecoratedTooltipWindow as DecoratedTooltipWindow
from gui.Scaleform.daapi.view.lobby.techtree.settings import UnlockProps as UnlockProps
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.genConsts.ICON_TEXT_FRAMES import ICON_TEXT_FRAMES as ICON_TEXT_FRAMES
from gui.Scaleform.genConsts.NODE_STATE_FLAGS import NODE_STATE_FLAGS as NODE_STATE_FLAGS
from gui.Scaleform.locale.ITEM_TYPES import ITEM_TYPES as ITEM_TYPES
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import getItemUnlockPricesVO as getItemUnlockPricesVO, getItemRestorePricesVO as getItemRestorePricesVO, getItemSellPricesVO as getItemSellPricesVO
from gui.shared.gui_items.gui_item_economics import getMinRentItemPrice as getMinRentItemPrice, ItemPrice as ItemPrice
from gui.shared.formatters import text_styles as text_styles, moneyWithIcon as moneyWithIcon, getItemPricesVO as getItemPricesVO
from gui.shared.formatters.time_formatters import RentLeftFormatter as RentLeftFormatter, getTimeLeftInfo as getTimeLeftInfo
from gui.shared.gui_items import GUI_ITEM_ECONOMY_CODE as GUI_ITEM_ECONOMY_CODE
from gui.shared.gui_items.Tankman import Tankman as Tankman, CrewTypes as CrewTypes, NO_TANKMAN as NO_TANKMAN
from gui.shared.gui_items.Vehicle import VEHICLE_CLASS_NAME as VEHICLE_CLASS_NAME
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle, getBattlesLeft as getBattlesLeft, getTypeBigIconPath as getTypeBigIconPath
from gui.shared.gui_items.fitting_item import RentalInfoProvider as RentalInfoProvider
from gui.shared.items_parameters import RELATIVE_PARAMS as RELATIVE_PARAMS, params_helper as params_helper
from gui.shared.items_parameters import formatters as param_formatter
from gui.shared.items_parameters.comparator import PARAM_STATE as PARAM_STATE
from gui.shared.items_parameters.params_helper import SimplifiedBarVO as SimplifiedBarVO
from gui.shared.money import Currency as Currency
from gui.shared.tooltips import formatters as formatters, ToolTipBaseData as ToolTipBaseData
from gui.shared.tooltips import getComplexStatus as getComplexStatus, getUnlockPrice as getUnlockPrice, TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData, makeCompoundPriceBlock as makeCompoundPriceBlock, CURRENCY_SETTINGS as CURRENCY_SETTINGS
from gui.shared.utils import MAX_STEERING_LOCK_ANGLE as MAX_STEERING_LOCK_ANGLE, WHEELED_SWITCH_TIME as WHEELED_SWITCH_TIME, WHEELED_SPEED_MODE_SPEED as WHEELED_SPEED_MODE_SPEED, SHOT_DISPERSION_ANGLE as SHOT_DISPERSION_ANGLE, DUAL_GUN_CHARGE_TIME as DUAL_GUN_CHARGE_TIME, TURBOSHAFT_SPEED_MODE_SPEED as TURBOSHAFT_SPEED_MODE_SPEED, ROCKET_ACCELERATION_SPEED_LIMITS as ROCKET_ACCELERATION_SPEED_LIMITS, DUAL_ACCURACY_COOLING_DELAY as DUAL_ACCURACY_COOLING_DELAY, TWIN_GUN_SWITCH_FIRE_MODE_TIME as TWIN_GUN_SWITCH_FIRE_MODE_TIME, RELOAD_TIME_SECS_PROP_NAME as RELOAD_TIME_SECS_PROP_NAME, TWIN_GUN_RELOAD_TIME as TWIN_GUN_RELOAD_TIME
from gui.impl.lobby.crew.tooltips.vehicle_params_tooltip_view import BaseVehicleParamsTooltipView as BaseVehicleParamsTooltipView, BaseVehicleAdvancedParamsTooltipView as BaseVehicleAdvancedParamsTooltipView, VehicleAdvancedParamsTooltipView as VehicleAdvancedParamsTooltipView, VehicleAvgParamsTooltipView as VehicleAvgParamsTooltipView
from gui.shared.utils.role_presenter_helper import getRoleUserName as getRoleUserName
from helpers import i18n as i18n, time_utils as time_utils, int2roman as int2roman, dependency as dependency
from helpers.i18n import makeString as _ms
from items.components.skills_constants import ORDERED_ROLES as ORDERED_ROLES
from renewable_subscription_common.settings_constants import WotPlusState as WotPlusState
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import ITradeInController as ITradeInController, IWotPlusController as IWotPlusController, IRestBonusController as IRestBonusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui import makeHtmlString as makeHtmlString
from typing import List as List, Tuple as Tuple, Dict as Dict, Optional as Optional
from gui.shared.tooltips.contexts import ExtendedAwardContext as ExtendedAwardContext
_logger: Any
_EQUIPMENT = 'equipment'
_OPTION_DEVICE = 'optionalDevice'
_BATTLE_BOOSTER = 'battleBooster'
_IS_SENIORITY = 'isSeniority'
_HIDE_STATUS = 'hideStatus'
_ARTEFACT_TYPES: tuple
_SKILL_BONUS_TYPE = 'skill'
_PERK_BONUS_TYPE = 'perk'
_ROLE_BONUS_TYPE = 'role'
_EXTRA_BONUS_TYPE = 'extra'
_TOOLTIP_MIN_WIDTH = 420
_TOOLTIP_MAX_WIDTH = 460
_TOOLTIP_ANNOUNCEMENT_MAX_WIDTH = 310
_CREW_TOOLTIP_PARAMS: dict
_SHORTEN_TOOLTIP_CASES: tuple

class VehicleInfoTooltipData(BlocksTooltipData):
    __itemsCache: Any
    __restBonusCtrl: Any
    _LEFT_PADDING = 20
    _RIGHT_PADDING = 20
    item: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def _getCrewIconBlock(self):
        ...
    def __createStatusBlock(self, vehicle, items, statsConfig, paramsConfig, valueWidth):
        ...

class ExtendedVehicleInfoTooltipData(VehicleInfoTooltipData):
    def _packBlocks(self, *args, **kwargs):
        ...

class VehicleAnnouncementParametersTooltipData(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class BaseVehicleParametersTooltipData(ToolTipBaseData):
    def __init__(self, context):
        ...
    @staticmethod
    def getTooltipView():
        ...
    def getDisplayableData(self, paramName, *args, **kwargs):
        ...
    @staticmethod
    def readyForAdvanced(*args, **_):
        ...

class BaseVehicleAdvancedParametersTooltipData(BaseVehicleParametersTooltipData):
    @staticmethod
    def getTooltipView():
        ...

class VehicleAdvancedParametersTooltipData(BaseVehicleParametersTooltipData):
    @staticmethod
    def getTooltipView():
        ...

class VehicleAvgParameterTooltipData(BaseVehicleParametersTooltipData):
    @staticmethod
    def getTooltipView():
        ...

class DefaultCrewMemberTooltipData(BlocksTooltipData):
    __itemsCache: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, tankmanID, slotIdx):
        ...

class VehiclePreviewCrewMemberTooltipData(DefaultCrewMemberTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, role, tankmanID, slotIdx, name, vehicleName, icon, description, skillsItems, *args, **kwargs):
        ...

class VehicleTradeInTooltipData(ToolTipBaseData):
    tradeIn: Any
    def __init__(self, context):
        ...
    def getDisplayableData(self, *args, **kwargs):
        ...

class VehicleTradeInPriceTooltipData(ToolTipBaseData):
    tradeIn: Any
    __itemsCache: Any
    def __init__(self, context):
        ...
    def getDisplayableData(self, tradeInVehicleCD, tradeOffVehicleCD):
        ...

class VehicleStatusTooltipData(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class VehicleTooltipBlockConstructor(object):
    itemsCache: Any
    vehicle: Any
    configuration: Any
    leftPadding: Any
    rightPadding: Any
    def __init__(self, vehicle, configuration, leftPadding=20, rightPadding=20):
        ...
    def construct(self):
        ...

class HeaderBlockConstructor(VehicleTooltipBlockConstructor):
    def construct(self):
        ...

class CrystalBlockConstructor(VehicleTooltipBlockConstructor):
    def construct(self):
        ...

class WotPlusBlockConstructor(VehicleTooltipBlockConstructor):
    __itemsCache: Any
    __wotPlusController: Any
    __restBonusCtrl: Any
    def construct(self):
        ...

class TelecomBlockConstructor(VehicleTooltipBlockConstructor):
    lobbyContext: Any
    _valueWidth: Any
    def __init__(self, vehicle, valueWidth, leftPadding, rightPadding):
        ...
    def construct(self):
        ...

class PriceBlockConstructor(VehicleTooltipBlockConstructor):
    _valueWidth: Any
    _rentExpiryTime: Any
    _rentBattlesLeft: Any
    _rentWinsLeft: Any
    _rentSeason: Any
    _blueprintFragmentsCount: Any
    _customPrice: Any
    def __init__(self, vehicle, configuration, params, valueWidth, leftPadding, rightPadding):
        ...
    def construct(self):
        ...

class FrontlineRentBlockConstructor(VehicleTooltipBlockConstructor):
    _valueWidth: Any
    _rentExpiryTime: Any
    _rentBattlesLeft: Any
    _rentWinsLeft: Any
    _rentSeason: Any
    def __init__(self, vehicle, configuration, params, valueWidth, leftPadding, rightPadding):
        ...
    def construct(self):
        ...

class CommonStatsBlockConstructor(VehicleTooltipBlockConstructor):
    PARAMS: dict
    __CONDITIONAL_PARAMS: tuple
    __OVERRIDED_PARAM_NAMES: tuple
    _valueWidth: Any
    def __init__(self, vehicle, configuration, valueWidth, leftPadding, rightPadding):
        ...
    def construct(self):
        ...
    def __getHighlightedParams(self):
        ...
    def __getShownParameters(self, paramsDict):
        ...

class VehicleAdditionalItems(VehicleTooltipBlockConstructor):
    NO_CREW = -1
    _crewLevelValue: Any
    _showVehicleSlot: Any
    _allModulesAvailable: Any
    def __init__(self, vehicle, configuration, leftPadding=20, rightPadding=20, showVehicleSlot=False, crewLevel=..., allModulesAvailable=False):
        ...
    def construct(self):
        ...

class SimplifiedStatsBlockConstructor(VehicleTooltipBlockConstructor):
    def construct(self):
        ...

class AdditionalStatsBlockConstructor(VehicleTooltipBlockConstructor):
    _valueWidth: Any
    _roleLevel: Any
    def __init__(self, vehicle, configuration, params, valueWidth, leftPadding, rightPadding):
        ...
    def construct(self):
        ...
    def _makeStatBlock(self, current, total, text):
        ...

class LockAdditionalStatsBlockConstructor(AdditionalStatsBlockConstructor):
    def construct(self):
        ...
    def _makeLockBlock(self):
        ...
    def _makeLockHeader(self):
        ...
    def _makeLockText(self):
        ...

class RotationLockAdditionalStatsBlockConstructor(LockAdditionalStatsBlockConstructor):
    def _makeLockHeader(self):
        ...
    def _makeLockText(self):
        ...

class RoamingLockAdditionalStatsBlockConstructor(LockAdditionalStatsBlockConstructor):
    def _makeLockText(self):
        ...

class ClanLockAdditionalStatsBlockConstructor(LockAdditionalStatsBlockConstructor):
    def _makeLockText(self):
        ...

class StatusBlockConstructor(VehicleTooltipBlockConstructor):
    __lobbyContext: Any
    def construct(self):
        ...
    @classmethod
    def _getHeaderFormatter(cls, statusLevel):
        ...
    def __getTechTreeVehicleStatus(self, config, vehicle):
        ...
    def __getVehicleStatus(self, showCustomStates, vehicle):
        ...

class SimpleFormattedStatusBlockConstructor(StatusBlockConstructor):
    @classmethod
    def _getHeaderFormatter(cls, _):
        ...

def _makeModuleFitTooltipError(reason):
    ...
def _getNeedValue(price, currency):
    ...
