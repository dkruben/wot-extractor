# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
import math as math
from builtins import map as map
from collections import namedtuple as namedtuple, defaultdict as defaultdict
from future.moves import pickle as pickle
from future.utils import viewvalues as viewvalues
from gui.impl.lobby.collection.tooltips.collection_item_tooltip_view import CollectionItemTooltipView as CollectionItemTooltipView
from gui.impl.lobby.personal_reserves.booster_tooltip import BoosterTooltip as BoosterTooltip
from gui.impl.lobby.personal_reserves.quest_booster_tooltip import QuestBoosterTooltip as QuestBoosterTooltip
from gui.impl.lobby.personal_reserves.tooltips.personal_reserves_tooltip_view import PersonalReservesTooltipView as PersonalReservesTooltipView
from gui.impl.pub import ToolTipWindow as ToolTipWindow
from gui.impl.pub.tooltip_window import SimpleTooltipContent as SimpleTooltipContent
from helpers.i18n import makeString as makeString
import ArenaType as ArenaType
import ResMgr as ResMgr
import constants as constants
import nations as nations
from gui import g_htmlTemplates as g_htmlTemplates, makeHtmlString as makeHtmlString, GUI_NATIONS as GUI_NATIONS
from gui.Scaleform import getNationsFilterAssetPath as getNationsFilterAssetPath
from gui.Scaleform.daapi.view.lobby.rally.vo_converters import getReserveNameVO as getReserveNameVO, getDirection as getDirection
from gui.Scaleform.genConsts.BATTLE_EFFICIENCY_TYPES import BATTLE_EFFICIENCY_TYPES as BATTLE_EFFICIENCY_TYPES
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS as CURRENCIES_CONSTANTS
from gui.Scaleform.genConsts.ICON_TEXT_FRAMES import ICON_TEXT_FRAMES as ICON_TEXT_FRAMES
from gui.Scaleform.genConsts.SLOT_HIGHLIGHT_TYPES import SLOT_HIGHLIGHT_TYPES as SLOT_HIGHLIGHT_TYPES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS as VEHPREVIEW_CONSTANTS
from gui.Scaleform.locale.FORTIFICATIONS import FORTIFICATIONS as FORTIFICATIONS
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.locale.MESSENGER import MESSENGER as MESSENGER
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.clans import formatters as clans_fmts
from gui.clans.data_wrapper.utils import formatField as formatField
from gui.impl import backport as backport
from gui.impl.backport.backport_tooltip import DecoratedTooltipWindow as DecoratedTooltipWindow
from gui.impl.gen import R as R
from gui.impl.common.param_tooltip_view import ParamTooltipView as ParamTooltipView
from gui.impl.lobby.battle_pass.tooltips.vehicle_points_tooltip_view import VehiclePointsTooltipView as VehiclePointsTooltipView
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip as AdditionalRewardsTooltip
from gui.impl.lobby.tooltips.veh_post_progression_entry_point_tooltip import VehPostProgressionEntryPointTooltip as VehPostProgressionEntryPointTooltip
from gui.prb_control.items.stronghold_items import SUPPORT_TYPE as SUPPORT_TYPE, REQUISITION_TYPE as REQUISITION_TYPE, HEAVYTRUCKS_TYPE as HEAVYTRUCKS_TYPE
from gui.server_events.events_helpers import missionsSortFunc as missionsSortFunc
from gui.server_events.formatters import TOKEN_SIZES as TOKEN_SIZES, DISCOUNT_TYPE as DISCOUNT_TYPE
from gui.shared.formatters import formatActionPrices as formatActionPrices
from gui.shared.formatters import icons as icons, text_styles as text_styles
from gui.shared.formatters.icons import serverBlockerIcon as serverBlockerIcon
from gui.shared.formatters.servers import formatPingStatus as formatPingStatus
from gui.shared.formatters.text_styles import concatStylesToMultiLine as concatStylesToMultiLine
from gui.shared.formatters.time_formatters import getTimeLeftStr as getTimeLeftStr, getTillTimeByResource as getTillTimeByResource
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, ACTION_ENTITY_ITEM as ACTION_ENTITY_ITEM
from gui.shared.money import Money as Money, Currency as Currency, MONEY_UNDEFINED as MONEY_UNDEFINED
from gui.shared.tooltips import ToolTipBaseData as ToolTipBaseData, TOOLTIP_TYPE as TOOLTIP_TYPE, ACTION_TOOLTIPS_TYPE as ACTION_TOOLTIPS_TYPE, ToolTipParameterField as ToolTipParameterField, WulfTooltipData as WulfTooltipData
from gui.shared.tooltips import efficiency as efficiency
from gui.shared.tooltips import formatters as formatters
from gui.shared.utils.functions import getArenaImage as getArenaImage
from gui.shared.view_helpers import UsersInfoHelper as UsersInfoHelper
from helpers import dependency as dependency
from helpers import i18n as i18n, time_utils as time_utils, html as html, int2roman as int2roman
from messenger.gui.Scaleform.data.contacts_vo_converter import ContactConverter as ContactConverter, makeClanFullName as makeClanFullName, makeContactStatusDescription as makeContactStatusDescription
from messenger.m_constants import USER_TAG as USER_TAG
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, PlayerCtxStorage as PlayerCtxStorage, UsersStorage as UsersStorage
from predefined_hosts import g_preDefinedHosts as g_preDefinedHosts, HOST_AVAILABILITY as HOST_AVAILABILITY, PING_STATUSES as PING_STATUSES, PingData as PingData
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.game_control import IIGRController as IIGRController, IServerStatsController as IServerStatsController, IBattleRoyaleController as IBattleRoyaleController
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.techtree_events import ITechTreeEventsListener as ITechTreeEventsListener
from skeletons.gui.web import IWebController as IWebController
from soft_exception import SoftException as SoftException
_logger: Any
_UNAVAILABLE_DATA_PLACEHOLDER = '--'
_PARENTHESES_OPEN = '('
_PARENTHESES_CLOSE = ')'
_SPACE = ' '
_ITEM_TYPE_TO_TOOLTIP_DICT: dict
_DEFAULT_MARGINS: dict
_DEFAULT_MARGIN_AFTER_BLOCK = 10
_DEFAULT_MARGIN_AFTER_SEPARATOR = 17
_ENV_TOOLTIPS_PATH = '#environment_tooltips:%s'
_ENV_IMAGES_PATH = '../maps/icons/environmentTooltips/%s.png'
_ENV_IMAGES_PATH_FOR_CHECK = 'gui/maps/icons/environmentTooltips/%s.png'
_CurrencySetting: Any
_OPERATIONS_SETTINGS: dict

class FortOrderParamField(ToolTipParameterField):
    def _getValue(self):
        ...

class IgrTooltipData(ToolTipBaseData):
    igrCtrl: Any
    eventsCache: Any
    def __init__(self, context):
        ...
    def getDisplayableData(self, *args):
        ...

class BlocksTooltipData(ToolTipBaseData):
    __contentMargin: Any
    __marginAfterBlock: Any
    __marginAfterSeparator: Any
    __width: Any
    item: Any
    def __init__(self, context, toolTipType):
        ...
    @classmethod
    def addAdvancedBlock(cls, data, disableAnim):
        ...
    def getDisplayableData(self, *args, **kwargs):
        ...
    def _getContentMargin(self):
        ...
    def _setContentMargin(self, top=None, left=None, bottom=None, right=None):
        ...
    def _setMargins(self, afterBlock=..., afterSeparator=...):
        ...
    def _setWidth(self, width):
        ...
    def _getWidth(self):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def _getHighLightType(self):
        ...

class FakeTooltipData(BlocksTooltipData):
    def __init__(self, context):
        ...

class DynamicBlocksTooltipData(BlocksTooltipData):
    __isVisible: Any
    def __init__(self, context, toolTipType):
        ...
    def isDynamic(self):
        ...
    def stopUpdates(self):
        ...
    def isVisible(self):
        ...
    def changeVisibility(self, isVisible):
        ...
    def updateData(self):
        ...

class EfficiencyTooltipData(BlocksTooltipData):
    _packers: dict
    def __init__(self, context):
        ...
    def _packBlocks(self, data):
        ...

class EnvironmentTooltipData(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, tooltipId):
        ...

class ContactTooltipData(ToolTipBaseData):
    lobbyContext: Any
    usersStorage: Any
    playerCtx: Any
    __converter: Any
    def __init__(self, context):
        ...
    def getDisplayableData(self, dbID, defaultName):
        ...
    def __makeUnitStr(self, descr, val):
        ...
    def __makeIconUnitStr(self, icon, descr):
        ...
    def __addBR(self, currentUnit):
        ...
    def __addComma(self, currStr):
        ...

class StrongholdTooltipData(ToolTipBaseData):
    def _getEntity(self):
        ...
    def _getData(self):
        ...

class SortieDivisionTooltipData(StrongholdTooltipData):
    def __init__(self, context):
        ...
    def getDisplayableData(self):
        ...
    def __getPlayerLimitsStr(self, minCount, maxCount):
        ...
    def __getBonusStr(self, bonus):
        ...

class ReserveTooltipData(StrongholdTooltipData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, *args, **kwargs):
        ...
    def __getSelectReason(self, reserve, selected):
        ...

class MapTooltipData(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, arenaID):
        ...

class SettingsControlTooltipData(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, controlID):
        ...

class SettingsButtonTooltipData(BlocksTooltipData):
    item: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class ServersInfoTooltipData(BlocksTooltipData):
    serverStats: Any
    settingsCore: Any
    connectionMgr: Any
    item: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def __packServerListBlock(self, simpleHostList, currServUrl, isColorBlind=False):
        ...
    @classmethod
    def __packServerBlock(cls, name, pingData, csisStatus, isSelected=False, isColorBlind=False):
        ...
    @classmethod
    def __formatServerName(cls, name, isSelected=False):
        ...
    @classmethod
    def __getPingData(cls, url):
        ...

class ClanCommonInfoTooltipData(ToolTipBaseData):
    clanCtrl: Any
    __usersInfoHelper: Any
    def __init__(self, context):
        ...
    def getDisplayableData(self, clanDBID):
        ...

class _BattleStatus(object):
    __slots__: tuple
    level: Any
    msg: Any
    style: Any
    prefix: Any
    def __init__(self, level, msg, style, prefix):
        ...
    def getMsgText(self):
        ...
    def getResText(self, count):
        ...

class ActionTooltipData(ToolTipBaseData):
    itemsCache: Any
    eventsCache: Any
    goodiesCache: Any
    def __init__(self, context):
        ...
    def getDisplayableData(self, itemType, key, newPrice, oldPrice, isBuying, forCredits=False, rentPackage=None, checkAllCurrencies=False, **kwargs):
        ...

class ActionSlotTooltipData(ToolTipBaseData):
    eventsCache: Any
    def __init__(self, context):
        ...
    def getDisplayableData(self, newPrice, oldPrice, **kwargs):
        ...

class BaseDiscountTooltipData(ToolTipBaseData):
    def __init__(self, context):
        ...
    @classmethod
    def _packDisplayableData(cls, cost, fullCost, currencyType=...):
        ...
    @staticmethod
    def _formatPrice(cost, currencyType):
        ...

class PriceDiscountTooltipData(BaseDiscountTooltipData):
    def getDisplayableData(self, cost, fullCost, currencyType):
        ...

class FrontlineDiscountTooltipData(BaseDiscountTooltipData):
    def getDisplayableData(self, cost, fullCost, currencyType=..., frontlineDiscount=0):
        ...

class ToolTipFortWrongTime(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, wrongState, timePeriods):
        ...

class MapSmallTooltipData(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, data):
        ...

class QuestVehiclesBonusTooltipData(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, questID):
        ...

class FortSortieTooltipData(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, data):
        ...

class SettingsSwitchEquipment(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class SettingsMinimapCircles(BlocksTooltipData):
    def __init__(self, context):
        ...
    def getTextBlocksForCircleDescr(self, title, body):
        ...
    def _packBlocks(self, *args):
        ...

class SettingsShowLocationMarkers(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class CURRENCY_SETTINGS(object):
    BUY_CREDITS_PRICE = 'buyCreditsPrice'
    RESTORE_PRICE = 'restorePrice'
    BUY_GOLD_PRICE = 'buyGoldPrice'
    BUY_CRYSTAL_PRICE = 'buyCrystalPrice'
    BUY_EVENT_COIN_PRICE = 'buyEventCoinPrice'
    BUY_BPCOIN_PRICE = 'buyBpcoinPrice'
    RENT_CREDITS_PRICE = 'rentCreditsPrice'
    RENT_GOLD_PRICE = 'rentGoldPrice'
    SELL_PRICE = 'sellPrice'
    UNLOCK_PRICE = 'unlockPrice'
    REMOVAL_CREDITS_PRICE = 'removalCreditsPrice'
    REMOVAL_GOLD_PRICE = 'removalGoldPrice'
    REMOVAL_CRYSTAL_PRICE = 'removalCrystalPrice'
    REMOVAL_EQUIPCOINS_PRICE = 'removalEquipCoinsPrice'
    UPGRADABLE_CREDITS_PRICE = 'upgradableCreditsPrice'
    UPGRADABLE_EQUIPCOINS_PRICE = 'upgradableEquipCoinsPrice'
    DECONSTRUCT_EQUIPCOINS_PRICE = 'deconstructEquipCoinsPrice'
    __BUY_SETTINGS: dict
    __RENT_SETTINGS: dict
    __REMOVAL_SETTINGS: dict
    __UPGRADABLE_SETTINGS: dict
    __DECONSTRUCT_SETTINGS: dict
    @classmethod
    def getRentSetting(cls, currency):
        ...
    @classmethod
    def getBuySetting(cls, currency):
        ...
    @classmethod
    def getRemovalSetting(cls, currency):
        ...
    @classmethod
    def getUpgradableSetting(cls, currency):
        ...
    @classmethod
    def getDeconstracutSetting(cls, currency):
        ...

class SettingsBaseKey(BlocksTooltipData):
    TEMPLATE_NAME = 'html_templates:lobby/tooltips/settings_key_commands'
    _headerKey: Any
    _enemyBlockImage: Any
    _enemyBlockTitle: Any
    _allyBlockImage: Any
    _allyBlockTitle: Any
    def __init__(self, context):
        ...
    def _getEnemyDescription(self):
        ...
    def _getAllyDescription(self):
        ...
    def _packBlocks(self, *args):
        ...

class SettingsKeyChargeFire(BlocksTooltipData):
    _headerKey: Any
    _enemyBlockImage: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class SettingKeySwitchMode(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class SettingKeySpecialAbility(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class SettingsKeyHighlightLocation(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class SettingsKeyHighlightTarget(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class SettingsKeyShowRadialMenu(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class HeaderMoneyAndXpTooltipData(BlocksTooltipData):
    itemsCache: Any
    battleRoyaleController: Any
    _btnType: Any
    def __init__(self, ctx):
        ...
    def _packBlocks(self, btnType=None, hideActionBlock=False, *args, **kwargs):
        ...
    def _getValue(self):
        ...
    def _getIconYOffset(self):
        ...
    def _getIcon(self):
        ...

class MissionsToken(BlocksTooltipData):
    eventsCache: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, tokenId, questId, *args):
        ...
    def __packTitleBlock(self, token):
        ...
    def __packQuestsBlock(self, quests):
        ...
    def __packBottomBlock(self, token):
        ...

class VehicleEliteBonusTooltipData(BlocksTooltipData):
    bonusId: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class VehicleHistoricalReferenceTooltipData(BlocksTooltipData):
    bonusId: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class VehiclePointsTooltipContentWindowData(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, intCD, *args, **kwargs):
        ...

class TechTreeEventTooltipBase(BlocksTooltipData):
    _eventsListener: Any
    def __init__(self, context):
        ...
    def _actionNameBlock(self, title, description, icon):
        ...
    def _actionExpireBlock(self, actionID):
        ...

class TechTreeDiscountInfoTooltip(TechTreeEventTooltipBase):
    def _packBlocks(self, *args, **kwargs):
        ...
    def __packActionBlock(self, actionIDs, packHeader=False):
        ...

class TechTreeNationDiscountTooltip(TechTreeEventTooltipBase):
    def _packBlocks(self, nation):
        ...

class VehPostProgressionEntryPointTooltipContentWindowData(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, intCD, parentScreen, *args, **kwargs):
        ...

class AdditionalRewardsTooltipContentWindowData(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, bonuses, bonusPacker=None, *args, **kwargs):
        ...

class PersonalReservesWidgetTooltipContent(BlocksTooltipData):
    def __init__(self, ctx):
        ...
    def getDisplayableData(self, *args, **kwargs):
        ...

class CollectionItemTooltipContentWindowData(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, itemID, isDetailed, *args, **kwargs):
        ...

class ResearchButtonTooltipData(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class BoosterTooltipContent(WulfTooltipData):
    def __init__(self, context):
        ...
    def getTooltipContent(self, boosterID, *args, **kwargs):
        ...

class QuestBoosterTooltipContent(WulfTooltipData):
    def __init__(self, context):
        ...
    def getTooltipContent(self, boosterID, *args, **kwargs):
        ...

class ParamsTooltipContent(WulfTooltipData):
    def getTooltipContent(self, *args, **kwargs):
        ...

def _getCurrencySetting(key):
    ...
def getFormattedPriceString(price, currencySetting, neededValue=None):
    ...
def getFormattedNeededValue(settings, neededValue):
    ...
def makePriceBlock(price, currencySetting, neededValue=None, oldPrice=None, percent=0, valueWidth=-1, leftPadding=61, forcedText='', iconRightOffset=-1, gap=0):
    ...
def makeRemovalPriceBlock(price, currencySetting, neededValue=None, oldPrice=None, percent=0, valueWidth=-1, leftPadding=61, forcedText='', isDeluxe=False, gap=15, canUseDemountKit=False, isWotPlusEnabled=False, isFreeToDemount=False, isFreeDeluxeEnabled=False, isFreeDemountEnabled=False):
    ...
def makeCompoundPriceBlock(currencySetting, itemPrice, blockWidth=150, forcedText=''):
    ...
def getSimpleTooltipFactory(header='', body='', note='', alert=''):
    ...
