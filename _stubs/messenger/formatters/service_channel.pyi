# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/formatters/service_channel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import operator as operator
import time as time
import typing as typing
from collections import OrderedDict as OrderedDict, defaultdict as defaultdict, deque as deque
from copy import copy as copy, deepcopy as deepcopy
from itertools import islice as islice
from future.moves.queue import Queue as Queue
from future.utils import iteritems as iteritems, itervalues as itervalues, viewitems as viewitems, viewvalues as viewvalues
from past.builtins import basestring as basestring
import BigWorld as BigWorld
import ArenaType as ArenaType
import constants as constants
import nations as nations
import personal_missions as personal_missions
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from shared_utils import BoundMethodWeakref as BoundMethodWeakref, first as first
from achievements20.cache import ALLOWED_ACHIEVEMENT_TYPES as ALLOWED_ACHIEVEMENT_TYPES
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS
from battle_pass_common import BATTLE_PASS_CHOICE_REWARD_OFFER_GIFT_TOKENS as BATTLE_PASS_CHOICE_REWARD_OFFER_GIFT_TOKENS, BATTLE_PASS_TOKEN_3D_STYLE as BATTLE_PASS_TOKEN_3D_STYLE, NON_CHAPTER_ID as NON_CHAPTER_ID, BattlePassRewardReason as BattlePassRewardReason, CurrencyBP as CurrencyBP, FinalReward as FinalReward, isPostProgressionChapter as isPostProgressionChapter
from battle_royale.skeletons.game_controller import IBRProgressionOnTokensController as IBRProgressionOnTokensController
from blueprints.BlueprintTypes import BlueprintTypes as BlueprintTypes
from blueprints.FragmentTypes import getFragmentType as getFragmentType
from cache import cached_property as cached_property
from chat_shared import SYS_MESSAGE_TYPE as SYS_MESSAGE_TYPE, MapRemovalReason as MapRemovalReason, decompressSysMessage as decompressSysMessage
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE, AUTO_MAINTENANCE_RESULT as AUTO_MAINTENANCE_RESULT, AUTO_MAINTENANCE_TYPE as AUTO_MAINTENANCE_TYPE, FAIRPLAY_VIOLATION_SYS_MSG_SAVED_DATA as FAIRPLAY_VIOLATION_SYS_MSG_SAVED_DATA, FINISH_REASON as FINISH_REASON, INVOICE_ASSET as INVOICE_ASSET, KICK_REASON as KICK_REASON, KICK_REASON_NAMES as KICK_REASON_NAMES, NC_MESSAGE_PRIORITY as NC_MESSAGE_PRIORITY, NC_MESSAGE_TYPE as NC_MESSAGE_TYPE, OFFER_TOKEN_PREFIX as OFFER_TOKEN_PREFIX, PREBATTLE_TYPE as PREBATTLE_TYPE, PREMIUM_ENTITLEMENTS as PREMIUM_ENTITLEMENTS, PREMIUM_TYPE as PREMIUM_TYPE, RESTRICTION_TYPE as RESTRICTION_TYPE, SCENARIO_RESULT as SCENARIO_RESULT, SYS_MESSAGE_CLAN_EVENT as SYS_MESSAGE_CLAN_EVENT, SYS_MESSAGE_CLAN_EVENT_NAMES as SYS_MESSAGE_CLAN_EVENT_NAMES, SYS_MESSAGE_FORT_EVENT_NAMES as SYS_MESSAGE_FORT_EVENT_NAMES, SwitchState as SwitchState
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV, LOG_ERROR as LOG_ERROR
from dog_tags_common.components_config import componentConfigAdapter as componentConfigAdapter
from dog_tags_common.config.common import ComponentPurpose as ComponentPurpose, ComponentViewType as ComponentViewType
from dossiers2.custom.records import DB_ID_TO_RECORD as DB_ID_TO_RECORD
from dossiers2.custom.collector20 import COLLECTOR20_BADGE_IDS as COLLECTOR20_BADGE_IDS, COLLECTOR20_MEDAL_ID as COLLECTOR20_MEDAL_ID
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as ACHIEVEMENT_BLOCK, BADGES_BLOCK as BADGES_BLOCK
from dossiers2.ui.layouts import IGNORED_BY_BATTLE_RESULTS as IGNORED_BY_BATTLE_RESULTS
from epic_constants import EPIC_BATTLE_LEVEL_IMAGE_INDEX as EPIC_BATTLE_LEVEL_IMAGE_INDEX
from exchange.personal_discounts_constants import EXCHANGE_RATE_FREE_XP_NAME as EXCHANGE_RATE_FREE_XP_NAME, EXCHANGE_RATE_GOLD_NAME as EXCHANGE_RATE_GOLD_NAME
from exchange.personal_discounts_parser import convertTokensToExchangeDiscounts as convertTokensToExchangeDiscounts
from fairplay_violation_types import FAIRPLAY_EXCLUDED_ARENA_BONUS_TYPES as FAIRPLAY_EXCLUDED_ARENA_BONUS_TYPES, getFairplayViolationLocale as getFairplayViolationLocale, getPenaltyTypeAndViolationName as getPenaltyTypeAndViolationName
from goodies.goodie_constants import GOODIE_VARIETY as GOODIE_VARIETY
from gui import GUI_NATIONS as GUI_NATIONS, GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS as CURRENCIES_CONSTANTS
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES as RANKEDBATTLES_ALIASES
from gui.SystemMessages import SM_TYPE as SM_TYPE
from gui.achievements.achievements_constants import Achievements20SystemMessages as Achievements20SystemMessages
from gui.clans.formatters import getClanFullName as getClanFullName
from gui.collection.collections_constants import COLLECTION_ITEM_PREFIX_NAME as COLLECTION_ITEM_PREFIX_NAME
from gui.dog_tag_composer import dogTagComposer as dogTagComposer
from gui.game_control.blueprints_convert_sale_controller import BCSActionState as BCSActionState
from gui.impl import backport as backport
from gui.impl.backport import getNiceNumberFormat as getNiceNumberFormat, getShortDateTimeFormat as getShortDateTimeFormat
from gui.impl.gen import R as R
from gui.impl.lobby.winback.winback_helpers import getDiscountFromBlueprint as getDiscountFromBlueprint, getDiscountFromGoody as getDiscountFromGoody, getLevelFromSelectableToken as getLevelFromSelectableToken
from gui.impl.lobby.premacc.premacc_helpers import getDeltaTimeHelper as getDeltaTimeHelper
from gui.mapbox.mapbox_helpers import formatMapboxRewards as formatMapboxRewards
from gui.prb_control.formatters import getPrebattleFullDescription as getPrebattleFullDescription
from gui.prestige.prestige_helpers import getCurrentGrade as getCurrentGrade, hasVehiclePrestige as hasVehiclePrestige, mapGradeIDToUI as mapGradeIDToUI, needShowPrestigeMilestonesRewardWindow as needShowPrestigeMilestonesRewardWindow, needShowPrestigeRewardWindow as needShowPrestigeRewardWindow, prestigePointsToXP as prestigePointsToXP
from gui.ranked_battles.constants import YEAR_AWARD_SELECTABLE_OPT_DEVICE_PREFIX as YEAR_AWARD_SELECTABLE_OPT_DEVICE_PREFIX, YEAR_POINTS_TOKEN as YEAR_POINTS_TOKEN
from gui.ranked_battles.ranked_helpers import getBonusBattlesIncome as getBonusBattlesIncome, getQualificationBattlesCountFromID as getQualificationBattlesCountFromID, isQualificationQuestID as isQualificationQuestID
from gui.ranked_battles.ranked_models import PostBattleRankInfo as PostBattleRankInfo, RankChangeStates as RankChangeStates
from gui.server_events.finders import PERSONAL_MISSION_TOKEN as PERSONAL_MISSION_TOKEN, isPMPoints as isPMPoints
from gui.server_events.awards_formatters import BATTLE_BONUS_X5_TOKEN as BATTLE_BONUS_X5_TOKEN, CREW_BONUS_X3_TOKEN as CREW_BONUS_X3_TOKEN, CompletionTokensBonusFormatter as CompletionTokensBonusFormatter
from gui.server_events.bonuses import EntitlementBonus as EntitlementBonus, MetaBonus as MetaBonus, SelectableBonus as SelectableBonus, getMergedBonusesFromDicts as getMergedBonusesFromDicts
from gui.server_events.recruit_helper import getRecruitInfo as getRecruitInfo
from gui.shared import formatters as shared_fmts
from gui.shared.formatters import icons as icons, text_styles as text_styles
from gui.shared.formatters.currency import applyAll as applyAll, getBWFormatter as getBWFormatter, getStyle as getStyle
from gui.shared.formatters.time_formatters import RentDurationKeys as RentDurationKeys, getTillTimeByResource as getTillTimeByResource, getTimeLeftInfo as getTimeLeftInfo
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, getItemTypeID as getItemTypeID
from gui.shared.gui_items.Tankman import BaseBookConvertingFormatter as BaseBookConvertingFormatter, Tankman as Tankman
from gui.shared.gui_items.Vehicle import getShortUserName as getShortUserName, getUserName as getUserName, getWotPlusExclusiveVehicleTypeUserName as getWotPlusExclusiveVehicleTypeUserName
from gui.shared.gui_items.crew_skin import localizedFullName as localizedFullName
from gui.shared.gui_items.dossier.achievements.abstract.class_progress import ClassProgressAchievement as ClassProgressAchievement
from gui.shared.gui_items.dossier.factories import getAchievementFactory as getAchievementFactory
from gui.shared.gui_items.fitting_item import RentalInfoProvider as RentalInfoProvider
from gui.shared.money import MONEY_UNDEFINED as MONEY_UNDEFINED, ZERO_MONEY as ZERO_MONEY, Currency as Currency, Money as Money
from gui.shared.notifications import NotificationGroup as NotificationGroup, NotificationGuiSettings as NotificationGuiSettings, NotificationPriorityLevel as NotificationPriorityLevel
from gui.shared.system_factory import collectLootBoxAutoOpenSubFormatters as collectLootBoxAutoOpenSubFormatters, collectModeNameKwargsByBonusType as collectModeNameKwargsByBonusType, collectTokenQuestsSubFormatters as collectTokenQuestsSubFormatters
from gui.shared.utils.requesters.ShopRequester import _NamedGoodieData as _NamedGoodieData
from gui.shared.utils.requesters.blueprints_requester import getFragmentNationID as getFragmentNationID, getUniqueBlueprints as getUniqueBlueprints
from gui.shared.utils.transport import z_loads as z_loads
from helpers import dependency as dependency, getLocalizedData as getLocalizedData, html as html, i18n as i18n, int2roman as int2roman, time_utils as time_utils
from items import ITEM_TYPE_NAMES as ITEM_TYPE_NAMES
from items import ITEM_TYPES as I_T
from items import getTypeInfoByIndex as getTypeInfoByIndex, getTypeInfoByName as getTypeInfoByName, tankmen as tankmen
from items import vehicles as vehicles_core
from items.components.c11n_constants import UNBOUND_VEH_KEY as UNBOUND_VEH_KEY, CustomizationType as CustomizationType, CustomizationTypeNames as CustomizationTypeNames
from items.components.crew_books_constants import CREW_BOOK_RARITY as CREW_BOOK_RARITY
from items.components.crew_skins_constants import NO_CREW_SKIN_ID as NO_CREW_SKIN_ID
from items.tankmen import RECRUIT_TMAN_TOKEN_PREFIX as RECRUIT_TMAN_TOKEN_PREFIX
from items.vehicles import getVehicleType as getVehicleType
from maps_training_common.maps_training_constants import SCENARIO_INDEXES as SCENARIO_INDEXES
from messenger import g_settings as g_settings
from messenger.ext import passCensor as passCensor
from messenger.formatters import NCContextItemFormatter as NCContextItemFormatter, TimeFormatter as TimeFormatter
from messenger.formatters.service_channel_helpers import EOL as EOL, MessageData as MessageData, extractLockedStyle as extractLockedStyle, getCustomizationItem as getCustomizationItem, getCustomizationItemData as getCustomizationItemData, getRewardsForQuests as getRewardsForQuests, mergeRewards as mergeRewards, parseTokenBonusCount as parseTokenBonusCount, popCollectionEntitlements as popCollectionEntitlements
from messenger.proto.bw.wrappers import ServiceChannelMessage as ServiceChannelMessage
from nations import NAMES as NAMES
from skeletons.gui.battle_matters import IBattleMattersController as IBattleMattersController
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from helpers.rest_bonus import getRestBonusData as getRestBonusData
from skeletons.gui.game_control import IBattlePassController as IBattlePassController, IBattleRoyaleController as IBattleRoyaleController, ICollectionsSystemController as ICollectionsSystemController, IEpicBattleMetaGameController as IEpicBattleMetaGameController, IFunRandomController as IFunRandomController, ILootBoxSystemController as ILootBoxSystemController, IMapboxController as IMapboxController, IRankedBattlesController as IRankedBattlesController, IRestBonusController as IRestBonusController, IWinbackController as IWinbackController
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from skeletons.gui.platform.catalog_service_controller import IPurchaseCache as IPurchaseCache
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Any as Any, Dict as Dict, List as List, Tuple as Tuple, Callable as Callable, Optional as Optional, Union as Union
from account_helpers.offers.events_data import OfferEventData as OfferEventData, OfferGift as OfferGift
from gui.platform.catalog_service.controller import _PurchaseDescriptor as _PurchaseDescriptor
from gui.goodies.goodie_items import Booster as Booster
_logger: _Any
_TEMPLATE = 'template'
_RENT_TYPE_NAMES: dict
_PREMIUM_MESSAGES: dict
_PREMIUM_TEMPLATES: dict
EPIC_LEVELUP_TOKEN_TEMPLATE = 'epicmetagame:levelup:'

class ServiceChannelFormatter(object):
    def format(self, data, *args):
        ...
    def isNotify(self):
        ...
    def isAsync(self):
        ...
    def canBeEmpty(self):
        ...
    def _getGuiSettings(self, data, key=None, priorityLevel=None, messageType=None, messageSubtype=None, decorator=None):
        ...

class SimpleFormatter(ServiceChannelFormatter):
    _template: _Any
    def __init__(self, templateName):
        ...
    def format(self, message, *args):
        ...
    def getCtx(self, message, *args):
        ...

class GeneralFormatter(SimpleFormatter):
    def getCtx(self, message, *args):
        ...
    def getTitle(self, message, *args):
        ...
    def getText(self, message, *args):
        ...
    def getValues(self, message, *args):
        ...

class ExclusiveVehicleWotPlusFormatter(ServiceChannelFormatter):
    template: _Any
    def __init__(self, isEnabled=False):
        ...
    def format(self, message, *args):
        ...
    def __getVehicleName(self, vehTypeCD):
        ...
    def __getVehicleType(self, vehTypeCD):
        ...

class WaitItemsSyncFormatter(ServiceChannelFormatter):
    _itemsCache: _Any
    __callbackQueue: _Any
    def __init__(self):
        ...
    def isAsync(self):
        ...
    # decorador original: @adisp_async
    def _waitForSyncItems(self, callback):
        ...
    def __registerHandler(self, callback):
        ...
    def __unregisterHandler(self):
        ...
    def __onSyncCompleted(self, *_):
        ...

class ServerRebootFormatter(ServiceChannelFormatter):
    def format(self, message, *args):
        ...

class ServerRebootCancelledFormatter(ServiceChannelFormatter):
    def format(self, message, *args):
        ...

class FormatSpecialReward(object):
    __lobbyContext: _Any
    __battleMattersController: _Any
    __winbackController: _Any
    __funRandomController: _Any
    def getString(self, message):
        ...
    def __formattedItems(self, message):
        ...
    def __getCrewBookNames(self, items):
        ...
    def __getBlueprintNames(self, blueprints):
        ...
    def __extractExcludedItems(self, data):
        ...

class BattleResultsFormatter(WaitItemsSyncFormatter):
    __rankedController: _Any
    __battleRoyaleController: _Any
    __lobbyContext: _Any
    __battleRoyaleProgressionCtrl: _Any
    __eventsCache: _Any
    __restBonusCtrl: _Any
    _battleResultKeys: dict
    __FLResultsKeys: dict
    __BRResultKeys: dict
    __StPatrickKeys: dict
    __MTResultKeys: dict
    __goldTemplateKey = 'battleResultGold'
    __questsTemplateKey = 'battleQuests'
    def isNotify(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    @staticmethod
    def _getBattleTypeDescr(data):
        ...
    def _formatMessages(self, message, arenaType, arenaCreateTime):
        ...
    def _getBattleResultsKey(self, battleResults):
        ...
    def _getFairplayData(self, message):
        ...
    def _prepareFormatData(self, message):
        ...
    def __makeFLModifierString(self, battleResults, ctx):
        ...
    def _getAdditionalBonusValue(self, detailedRewards, bonusName):
        ...
    def __makeMapsTrainingMsgCtx(self, battleResults, ctx):
        ...
    def __makeMapsTrainingRewardsMsg(self, battleResults):
        ...
    def __makeQuestsAchieve(self, message):
        ...
    def __makeVehicleLockString(self, vehicleNames, battleResults):
        ...
    def __makeXpExString(self, xp, battleResKey, xpPenalty, battleResults):
        ...
    def __getRestBonusXPFactor(self, battleResults):
        ...
    def __makeCreditsExString(self, accCredits, creditsPenalty, creditsContributionIn, creditsContributionOut):
        ...
    def __makeGoldString(self, gold):
        ...
    def __makeCurrencyString(self, currency, credit):
        ...
    def __makeAchievementsAndBadgesStrings(self, battleResults):
        ...
    def __makeRankedFlowStrings(self, battleResults):
        ...
    def __makeRankedBonusString(self, battleResults):
        ...
    def __makeBattlePassProgressionString(self, guiType, battleResults):
        ...
    def __makeCommendationsString(self, battleResults):
        ...
    def __makePiggyBankString(self, credits_):
        ...
    def __makeBRCoinString(self, battleResults):
        ...
    def __makeSTPCoinString(self, battleResults):
        ...
    def __getCoinsQuestBonus(self, battleResults, currencyCode):
        ...
    def __makeBRProgressionTokenString(self, battleResults):
        ...
    def __getBrProgressionTokenQuestBonus(self, completedQuestIDs):
        ...

class AutoMaintenanceFormatter(WaitItemsSyncFormatter):
    itemsCache: _Any
    __serviceChannelMessages = R.strings.messenger.serviceChannelMessages
    __messages: dict
    __currencyTemplates: dict
    _overriddenMessages: dict
    def isNotify(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    def _getTemplateByCurrency(self, currency):
        ...

class AchievementFormatter(ServiceChannelFormatter):
    _HIDDEN_ACHIEVES: set
    _HIDDEN_BADGE_IDS: _Any
    def isNotify(self):
        ...
    def isAsync(self):
        ...
    def canBeEmpty(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...

class CurrencyUpdateFormatter(ServiceChannelFormatter):
    _AUCTION_EMITTER_ID: _Any
    _EMITTER_ID_TO_TITLE: dict
    _DEFAULT_TITLE: _Any
    __FREE_XP_ICON = 'freeXPSmallIcon'
    __CURRENCY_ICONS: dict
    _CURRENCY_TO_STYLE: dict
    def format(self, message, *args):
        ...
    def __ifPlatformCurrency(self, currencyCode):
        ...
    def __getCurrencyString(self, currencyCode, amountDelta):
        ...
    def __getCurrencyStyle(self, currencyCode):
        ...

class GiftReceivedFormatter(ServiceChannelFormatter):
    __handlers: dict
    def format(self, message, *args):
        ...
    def __formatMoneyGiftMsg(self, keys, data):
        ...
    def __formatXPGiftMsg(self, key, data):
        ...
    def __formatPremiumGiftMsg(self, key, data):
        ...
    def __formatItemGiftMsg(self, key, data):
        ...
    def __formatVehicleGiftMsg(self, key, data):
        ...

class InvoiceReceivedFormatter(WaitItemsSyncFormatter):
    __purchaseCache: _Any
    __assetHandlers: dict
    __currencyToInvoiceAsset: dict
    __operationTemplateKeys: dict
    __blueprintsTemplateKeys: dict
    __messageTemplateKeys: dict
    __INVALID_TYPE_ASSET = -1
    __auxMessagesHandlers: dict
    __DESTROY_PAIR_MODIFICATIONS_MSG_TEMPLATE = 'DestroyAllPairsModifications'
    __goodiesCache: _Any
    __eventsCache: _Any
    __dossierResult: _Any
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    @classmethod
    def getBlueprintString(cls, blueprints):
        ...
    @classmethod
    def getVehiclesString(cls, vehicles, htmlTplPostfix='InvoiceReceived'):
        ...
    def canBeEmpty(self):
        ...
    @classmethod
    def _getCustomizationCompensationString(cls, compensationMoney, strItemType, strItemName, amount, htmlTplPostfix):
        ...
    @classmethod
    def getVehiclesCompensationString(cls, vehicles, htmlTplPostfix='InvoiceReceived'):
        ...
    @classmethod
    def getCustomizationCompensationString(cls, customizationItem, htmlTplPostfix='InvoiceReceived'):
        ...
    @classmethod
    def getTankmenString(cls, tmen, dismiss=False):
        ...
    @classmethod
    def getGoodiesString(cls, goodies, exclude=None):
        ...
    @classmethod
    def getEnhancementsString(cls, enhancements):
        ...
    @staticmethod
    def getEntitlementsString(entitlements):
        ...
    @staticmethod
    def getRankedBonusBattlesString(persistentBattles, dailyBattles):
        ...
    def getInvoiceDataAuxMessages(self, data):
        ...
    def _composeOperations(self, data):
        ...
    def _formatData(self, assetType, data):
        ...
    def _formatAmount(self, assetType, data):
        ...
    def _formatPurchase(self, assetType, data):
        ...
    def _getMessageTemplateKey(self, data):
        ...
    @classmethod
    def _getOperationTimeString(cls, data):
        ...
    @classmethod
    def _getVehicleNames(cls, vehicles):
        ...
    @classmethod
    def _getCompensationString(cls, compensationMoney, strItemNames, htmlTplPostfix):
        ...
    @classmethod
    def _processCompensations(cls, data):
        ...
    @classmethod
    def __getBlueprintContext(cls, count):
        ...
    @classmethod
    def __formatBlueprintsString(cls, fragmentType, count, ctx):
        ...
    def __prerocessRareAchievements(self, data):
        ...
    def __getDossierString(self):
        ...
    def __getFinOperationString(self, assetType, amount, formatter=None):
        ...
    def __getItemsString(self, items, installed=False):
        ...
    @classmethod
    def __getSlotsString(cls, slots):
        ...
    @classmethod
    def __getTankPremiumString(cls, expireTime):
        ...
    @classmethod
    def __getBerthsString(cls, berths):
        ...
    @classmethod
    def __getPrestigePointsString(cls, prestigePoints):
        ...
    @classmethod
    def __getTankmenFreeXPString(cls, data):
        ...
    @classmethod
    def __getL10nDescription(cls, data):
        ...
    @classmethod
    def __getVehicleInfo(cls, vehData, isWithdrawn):
        ...
    @staticmethod
    def __processRentVehicleData(rentData):
        ...
    @classmethod
    def __getVehicleName(cls, vehCompDescr):
        ...
    def __getTokensString(self, data):
        ...
    def __getLootBoxString(self, data):
        ...
    def __getEntitlementsString(self, data):
        ...
    def __getRankedBonusBattlesString(self, persistentBattles, dailyBattles):
        ...
    def __getPlatformCurrenciesString(self, data):
        ...
    def __getDiscardPairModificationsMsg(self, data):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def __waitForSyncData(self, data, callback):
        ...
    def __getMetaUrlData(self, data):
        ...

class AdminMessageFormatter(ServiceChannelFormatter):
    def format(self, message, *args):
        ...

class AccountTypeChangedFormatter(ServiceChannelFormatter):
    def format(self, message, *args):
        ...

class _PremiumActionFormatter(ServiceChannelFormatter):
    _templateKey = None
    _msgTemplateKey = None
    def format(self, message, *args):
        ...
    def _getMessage(self, isPremium, premiumType, expiryTime):
        ...

class PremiumBoughtFormatter(_PremiumActionFormatter):
    _templateKey: _Any
    _msgTemplateKey: _Any
    def _getMessage(self, isPremium, premiumType, expiryTime):
        ...

class PremiumExtendedFormatter(PremiumBoughtFormatter):
    _templateKey: _Any

class PremiumChangedFormatter(PremiumBoughtFormatter):
    _templateKey: _Any

class PremiumExpiredFormatter(_PremiumActionFormatter):
    _templateKey: _Any
    _msgTemplateKey: _Any
    def _getMessage(self, isPremium, premiumType, expiryTime):
        ...

class PrebattleFormatter(ServiceChannelFormatter):
    __battleTypeByPrebattleType: dict
    _battleFinishReasonKeys: dict
    _defaultBattleFinishReasonKey: tuple
    def isNotify(self):
        ...
    def _getIconId(self, prbType):
        ...
    def _makeBattleTypeString(self, prbType):
        ...
    def _makeDescriptionString(self, data, showBattlesCount=True):
        ...
    def _getOpponentsString(self, opponents):
        ...
    def _getBattleResultString(self, winner, team):
        ...
    def _makeBattleResultString(self, finishReason, winner, team):
        ...

class PrebattleArenaFinishFormatter(PrebattleFormatter):
    _battleFinishReasonKeys: dict
    def format(self, message, *args):
        ...

class PrebattleKickFormatter(PrebattleFormatter):
    def format(self, message, *args):
        ...

class PrebattleDestructionFormatter(PrebattleFormatter):
    _battleFinishReasonKeys: dict
    def format(self, message, *args):
        ...

class VehCamouflageTimedOutFormatter(ServiceChannelFormatter):
    def isNotify(self):
        ...
    def format(self, message, *args):
        ...

class VehEmblemTimedOutFormatter(ServiceChannelFormatter):
    def isNotify(self):
        ...
    def format(self, message, *args):
        ...

class VehInscriptionTimedOutFormatter(ServiceChannelFormatter):
    def isNotify(self):
        ...
    def format(self, message, *args):
        ...

class ConverterFormatter(ServiceChannelFormatter):
    __itemsCache: _Any
    __CONVERTER_BLUEPRINTS_TEMPLATE = 'ConverterBlueprintsNotify'
    def __i18nValue(self, key, isReceived, **kwargs):
        ...
    def __vehName(self, vehCompDescr):
        ...
    def format(self, message, *args):
        ...
    def __getBlueprintsMessageText(self, blueprints):
        ...

class ClientSysMessageFormatter(ServiceChannelFormatter):
    __templateKey = '%sSysMessage'
    def format(self, data, *args):
        ...
    def _getGuiSettings(self, data, key=None, priorityLevel=None, groupID=None):
        ...

class PremiumAccountExpiryFormatter(ClientSysMessageFormatter):
    def format(self, data, *args):
        ...

class SessionControlFormatter(ServiceChannelFormatter):
    def _doFormat(self, text, key, auxData):
        ...

class AOGASNotifyFormatter(SessionControlFormatter):
    def format(self, data, *args):
        ...

class KoreaParentalControlFormatter(SessionControlFormatter):
    def format(self, data, *args):
        ...

class VehicleTypeLockExpired(ServiceChannelFormatter):
    def format(self, message, *args):
        ...

class ServerDowntimeCompensation(ServiceChannelFormatter):
    __templateKey = 'serverDowntimeCompensation'
    def format(self, message, *args):
        ...

class ActionNotificationFormatter(ClientSysMessageFormatter):
    __templateKey = 'action%s'
    def format(self, message, *args):
        ...

class QuestAchievesFormatter(object):
    _SEPARATOR = '<br/>'
    __lobbyContext: _Any
    __goodiesCache: _Any
    __lootboxSystem: _Any
    _itemsCache: _Any
    _c11nService: _Any
    @classmethod
    def formatQuestAchieves(cls, data, asBattleFormatter, processCustomizations=True, processTokens=True):
        ...
    @classmethod
    def getFormattedAchieves(cls, data, asBattleFormatter, processCustomizations=True, processTokens=True):
        ...
    @classmethod
    def _processTokens(cls, data):
        ...
    @classmethod
    def _processLootBoxToken(cls, tokenID, count):
        ...
    @classmethod
    def _processDogTags(cls, dogTags):
        ...
    @classmethod
    def _extractAchievements(cls, data):
        ...
    @staticmethod
    def __extractBadges(data):
        ...
    @staticmethod
    def __extractPets(data):
        ...
    @classmethod
    def __makeQuestsAchieve(cls, key, **kwargs):
        ...

class TokenQuestsFormatter(WaitItemsSyncFormatter):
    __eventsCache: _Any
    __MESSAGE_TEMPLATE = 'tokenQuests'
    _achievesFormatter: _Any
    __subFormatters: _Any
    def __init__(self, subFormatters=...):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    def canBeEmpty(self):
        ...
    @classmethod
    def __processMetaActions(cls, questID):
        ...
    def __collectSubFormatters(self):
        ...
    def __formatSimpleTokenQuests(self, message, questIDs, popUps):
        ...

class NCMessageFormatter(ServiceChannelFormatter):
    __templateKeyFormat = 'notificationsCenterMessage_{0}'
    def format(self, message, *args):
        ...
    def __getTemplateKey(self, data):
        ...
    def __getGuiPriority(self, data):
        ...
    def __getTopic(self, data):
        ...
    def __getBody(self, data):
        ...
    def __fetchPollData(self, data, settings):
        ...
    def __formatContext(self, ctx):
        ...

class ClanMessageFormatter(ServiceChannelFormatter):
    __templates: dict
    def format(self, message, *args):
        ...

class StrongholdMessageFormatter(ServiceChannelFormatter):
    __templates: dict
    DEFAULT_WARNING = 'fortMessageWarning'
    __messagesFormatters: _Any
    def __init__(self):
        ...
    def format(self, message, *args):
        ...
    def _buildMessage(self, event, ctx=None):
        ...
    def getOrderUserString(self, orderTypeID):
        ...
    def _reserveActivatedMessage(self, data):
        ...
    def _reserveExpiredMessage(self, data):
        ...

class VehicleRentedFormatter(ServiceChannelFormatter):
    _templateKey = 'vehicleRented'
    def format(self, message, *args):
        ...
    def _getMessage(self, vehTypeCD, expiryTime):
        ...

class RentalsExpiredFormatter(ServiceChannelFormatter):
    _templateKey = 'rentalsExpired'
    def format(self, message, *args):
        ...
    def _getMessage(self, vehTypeCD):
        ...

class PersonalMissionsQuestAchievesFormatter(QuestAchievesFormatter):
    __eventsCache: _Any
    @classmethod
    def _processTokens(cls, data):
        ...

class PMMedalsFormatter(object):
    @classmethod
    def _extractAchievements(cls, data):
        ...
    @classmethod
    def formatPopUpRecords(cls, data):
        ...

class LootBoxAchievesFormatter(QuestAchievesFormatter):
    @classmethod
    def _processTokens(cls, data):
        ...
    @classmethod
    def _extractAchievements(cls, data):
        ...

class LootBoxSystemAchievesFormatter(QuestAchievesFormatter):
    __itemsCache: _Any
    _BULLET = '\u2022'
    @classmethod
    def formatQuestAchieves(cls, data, asBattleFormatter, processCustomizations=True, processTokens=True):
        ...
    @classmethod
    def _processTokens(cls, data):
        ...
    @classmethod
    def __getLootBoxString(cls, token, tokenData):
        ...

class BattlePassQuestAchievesFormatter(QuestAchievesFormatter):
    __offersProvider: _Any
    _BULLET = '\u2022 '
    @classmethod
    def formatQuestAchieves(cls, data, asBattleFormatter, processCustomizations=True, processTokens=True):
        ...
    @classmethod
    def _processTokens(cls, data):
        ...
    @classmethod
    def _extractAchievements(cls, data):
        ...
    @classmethod
    def _processLootBoxToken(cls, tokenID, count):
        ...
    @classmethod
    def __processLootBoxTokens(cls, tokens):
        ...
    @classmethod
    def __processStyleTokens(cls, tokens):
        ...
    @classmethod
    def __processRewardChoiceTokens(cls, tokens):
        ...
    @classmethod
    def __getFormattedStyleProgress(cls, token):
        ...

class CollectionsFormatter(QuestAchievesFormatter):
    __BULLET = '\u2022 '
    @classmethod
    def formatQuestAchieves(cls, data, asBattleFormatter, processCustomizations=True, processTokens=True):
        ...
    @classmethod
    def __formatItems(cls, items):
        ...

class SeniorityAwardsInvoiceReceivedFormatter(InvoiceReceivedFormatter):
    _BULLET = '\u2022 '
    _SEPARATOR: _Any
    @classmethod
    def getVehiclesString(cls, vehicles, htmlTplPostfix='InvoiceReceived'):
        ...

class SeniorityAwardsQuestAchievesFormatter(QuestAchievesFormatter):
    _BASIC_FORMATER = SeniorityAwardsInvoiceReceivedFormatter
    @classmethod
    def formatQuestAchieves(cls, data, asBattleFormatter, processCustomizations=True, processTokens=True):
        ...

class BattleMattersQuestAchievesFormatter(QuestAchievesFormatter):
    __battleMattersController: _Any
    @classmethod
    def _processTokens(cls, data):
        ...
    @classmethod
    def isWithSelectableReward(cls, awardsDict):
        ...

class WinbackQuestAchievesFormatter(QuestAchievesFormatter):
    __winbackController: _Any
    @classmethod
    def getSelectableRewards(cls, awardsDict):
        ...
    @classmethod
    def formatQuestAchieves(cls, data, asBattleFormatter, processCustomizations=True, processTokens=True):
        ...
    @classmethod
    def _formatDiscounts(cls, rewards):
        ...
    @classmethod
    def _processTokens(cls, data):
        ...

class _GoodyFormatter(WaitItemsSyncFormatter):
    __goodiesCache: _Any
    _VARIETY_TO_TEMPLATE: dict
    def getBoosterAdditionalParams(self, message):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    def getContext(self, goodie):
        ...
    def canBeEmpty(self):
        ...
    def _getTemplateName(self, goodieType):
        ...

class GoodyRemovedFormatter(_GoodyFormatter):
    _VARIETY_TO_TEMPLATE: dict

class GoodiesExpiredFormatter(WaitItemsSyncFormatter):
    @classmethod
    def _buildCtx(cls, message):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    def canBeEmpty(self):
        ...

class GoodyDisabledFormatter(_GoodyFormatter):
    _VARIETY_TO_TEMPLATE: dict

class GoodieEnabledFormatter(_GoodyFormatter):
    _VARIETY_TO_TEMPLATE: dict

class TelecomStatusFormatter(WaitItemsSyncFormatter):
    __itemsCache: _Any
    __lobbyContext: _Any
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    @staticmethod
    def __addProviderToRes(res, provider):
        ...
    def __getMessageContext(self, data):
        ...
    @classmethod
    def __getVehicleUserNames(cls, vehTypeCompDescrs):
        ...

class TelecomReceivedInvoiceFormatter(InvoiceReceivedFormatter):
    __itemsCache: _Any
    __lobbyContext: _Any
    @staticmethod
    def invoiceHasCrew(data):
        ...
    @staticmethod
    def invoiceHasBrotherhood(data):
        ...
    @staticmethod
    def _addProviderToRes(res, provider):
        ...
    def _getProvider(self, data):
        ...
    @classmethod
    def _isValidCD(cls, vehCompDescr):
        ...
    def _getVehicles(self, data):
        ...
    def _getMessageTemplateKey(self, data):
        ...
    def _getMessageContext(self, data, vehicleNames):
        ...
    def _formatData(self, assetType, data):
        ...

class TelecomRemovedInvoiceFormatter(TelecomReceivedInvoiceFormatter):
    @classmethod
    def _isValidCD(cls, vehCompDescr):
        ...
    def _getMessageTemplateKey(self, data):
        ...
    def _getVehicles(self, data):
        ...
    def _getMessageContext(self, data, vehicleNames):
        ...

class PrbVehicleKickFormatter(ServiceChannelFormatter):
    __itemsCache: _Any
    typeKick = 'prbVehicleKick'
    def format(self, message, *args):
        ...

class PrbVehicleKickFilterFormatter(PrbVehicleKickFormatter):
    typeKick = 'prbVehicleKickFilter'

class PrbVehicleMaxCountKickFormatter(ServiceChannelFormatter):
    __itemsCache: _Any
    def format(self, message, *args):
        ...

class RotationGroupLockFormatter(ServiceChannelFormatter):
    def format(self, message, *args):
        ...
    def _getMessageTemplateKey(self):
        ...

class RotationGroupUnlockFormatter(RotationGroupLockFormatter):
    def _getMessageTemplateKey(self):
        ...

class RankedQuestAchievesFormatter(QuestAchievesFormatter):
    __rankAwardsFormatters: _Any
    __offersDP: _Any
    __awardsStyles: dict
    def packRankAwards(self, awardsDict):
        ...
    def packAwards(self, awardsDict, formattersList):
        ...
    @classmethod
    def _processTokens(cls, data):
        ...
    @classmethod
    def __getYearPointsAmount(cls, awardsDict):
        ...
    @classmethod
    def __getSelectableAwardCount(cls, awardsDict):
        ...
    def __packAward(self, key, value):
        ...

class BRQuestsFormatter(TokenQuestsFormatter):
    __eventsCache: _Any
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    def __formatEveryLevel(self, completedQuestIDs, data):
        ...
    def _packTitleAwards(self, awardsDict):
        ...
    @classmethod
    def __getLevel(cls, quest):
        ...

class RankedQuestFormatter(WaitItemsSyncFormatter):
    __eventsCache: _Any
    __rankedController: _Any
    __achievesFormatter: _Any
    def __init__(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback=None):
        ...
    def __formatRankedQuests(self, completedQuestIDs, data):
        ...

class PersonalMissionFailedFormatter(WaitItemsSyncFormatter):
    _eventsCache: _Any
    _template = 'PersonalMissionFailedMessage'
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback=None):
        ...

class CustomizationChangedFormatter(WaitItemsSyncFormatter):
    _template = 'CustomizationRemoved'
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback=None):
        ...

class LootBoxAutoOpenFormatter(WaitItemsSyncFormatter):
    __MESSAGE_TEMPLATE = 'LootBoxRewardsSysMessage'
    _achievesFormatter: _Any
    __subFormatters: _Any
    def __init__(self, subFormatters=...):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    def __formatSimpleBoxes(self, message, openedBoxesIDs):
        ...
    def __collectSubFormatters(self):
        ...

class ProgressiveRewardFormatter(WaitItemsSyncFormatter):
    _template = 'ProgressiveRewardMessage'
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback=None):
        ...

class PiggyBankSmashedFormatter(ServiceChannelFormatter):
    _piggyBankTemplate = 'PiggyBankSmashedMessage'
    _goldReserveTemplate = 'GoldReserveSmashedMessage'
    _currenciesTemplate = 'CurrenciesReservesSmashedMessage'
    def format(self, message, *args):
        ...

class BlackMapRemovedFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'BlackMapRemovedMessage'
    __REASONS_SETTINGS: dict
    def format(self, message, *args):
        ...

class EnhancementRemovedFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'EnhancementRemovedMessage'
    def format(self, message, *args):
        ...

class EnhancementsWipedFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'EnhancementsWipedMessage'
    def format(self, message, *args):
        ...

class EnhancementsWipedOnVehiclesFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'EnhancementsWipedOnVehiclesMessage'
    def format(self, message, *args):
        ...

class BattlePassRewardFormatter(WaitItemsSyncFormatter):
    __itemsCache: _Any
    __battlePass: _Any
    __collections: _Any
    __REWARD_TEMPLATE = 'BattlePassRewardSysMessage'
    __COLLECTION_ITEMS_TEMPLATE = 'CollectionItemsSysMessage'
    __PROGRESSION_BUTTON_TEMPLATE = 'BattlePassRewardWithProgressionButtonMessage'
    __CURRENCY_TEMPLATE_KEY = 'battlePassCurrency'
    __MESSAGES = R.strings.messenger.serviceChannelMessages
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback=None):
        ...
    def __makeAfterBattle(self, ctx):
        ...
    def __makeAfterLevelsPurchase(self, ctx):
        ...
    def __makeAfterBattlePassPurchase(self, ctx):
        ...
    def __makeAfterBattlePassWithLevelsPurchase(self, ctx):
        ...
    def __makeAfterChapterSelect(self, ctx):
        ...
    def __makePriceString(self, chapterID):
        ...
    def __getChapterPrice(self, chapterID):
        ...
    def __getLevelsPrice(self, levelsCount):
        ...
    def __makeCurrencyString(self, currency, amount):
        ...
    def __makeStarterPackText(self, starterPack):
        ...
    def __makeCollectionMessage(self, entitlements, message):
        ...

class BattlePassBoughtFormatter(WaitItemsSyncFormatter):
    __battlePass: _Any
    __MESSAGES = R.strings.messenger.serviceChannelMessages
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback=None):
        ...
    def __makeStarterPackText(self, chapterID, starterPack):
        ...
    def __makeDescription(self, chapterID):
        ...
    def __makeAdditionalText(self, chapterID):
        ...

class BattlePassReachedCapFormatter(WaitItemsSyncFormatter):
    __itemsCache: _Any
    __template = 'BattlePassReachedCapMessage'
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback=None):
        ...

class BattlePassStyleReceivedFormatter(WaitItemsSyncFormatter):
    __itemsCache: _Any
    __battlePass: _Any
    __template = 'BattlePassStyleReceivedMessage'
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback=None):
        ...

class BattlePassSeasonEndFormatter(WaitItemsSyncFormatter):
    __battlePass: _Any
    __itemsCache: _Any
    __template = 'BattlePassSeasonEndMessage'
    __rewardTemplate = 'battlePassDefaultRewardReceived'
    _BULLET = '\u2022 '
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback=None):
        ...

class BattlePassPostProgressionActivatedFormatter(ServiceChannelFormatter):
    __template = 'BattlePassPostProgressionActivatedMessage'
    def format(self, message, *args):
        ...

class BattlePassPostProgressionPausedFormatter(ServiceChannelFormatter):
    __template = 'BattlePassPostProgressionPausedMessage'
    def format(self, message, *args):
        ...

class EpicLevelUpFormatter(WaitItemsSyncFormatter):
    __itemsCache: _Any
    __epicController: _Any
    __template = 'EpicLevelUpMessage'
    __iconPrefix = 'epicSysMsgLevel'
    __rewardTemplate = 'epicDefaultRewardReceived'
    __gotLevelTemplate = 'epicGotLevel'
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback=None):
        ...
    @staticmethod
    def _getLevelUpIconId(level):
        ...

class EpicQuestAchievesFormatter(QuestAchievesFormatter):
    __offersProvider: _Any
    __itemsCache: _Any
    __goodiesCache: _Any
    _SEPARATOR = '<br>'
    __rEpicReward = R.strings.messenger.serviceChannelMessages.epicReward
    __rewardTemplate = 'epicLevelUpReward'
    __GOODIE_ITEMS: dict
    @classmethod
    def formatQuestAchieves(cls, data, asBattleFormatter, processCustomizations=True, processTokens=True):
        ...
    @classmethod
    def __processCrewBook(cls, data, result):
        ...
    @classmethod
    def getGoodieCount(cls, goodieID, ginfo, itemInShop, goodiesCacheGetter):
        ...
    @classmethod
    def applyQuestsAchieveResult(cls, count, messengerID, result):
        ...
    @classmethod
    def __processGoodiesResult(cls, data, result):
        ...
    @classmethod
    def __processCrystal(cls, data, result):
        ...
    @classmethod
    def __processBattlePassPoints(cls, data, result):
        ...
    @classmethod
    def __processAbilityPoints(cls, data, result):
        ...
    @classmethod
    def __processTokens(cls, data, result):
        ...
    @classmethod
    def __makeQuestsAchieve(cls, key, **kwargs):
        ...

class EpicSeasonEndFormatter(WaitItemsSyncFormatter):
    __itemsCache: _Any
    __template = 'EpicSeasonEndMessage'
    __rewardTemplate = 'epicDefaultRewardReceived'
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback=None):
        ...
    def __formatItemsStrings(self, items):
        ...
    def __formatRewardChoiceTokenString(self, itemCD, count, itemTypeID):
        ...
    def __formatCrewBookString(self, itemCD, count):
        ...

class BattlePassFreePointsUsedFormatter(ServiceChannelFormatter):
    __battlePass: _Any
    __template = 'BattlePassFreePointsUsedMessage'
    def format(self, message, *args):
        ...

class CollectibleVehiclesUnlockedFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'UnlockedCollectibleVehiclesMessage'
    def format(self, message, *args):
        ...

class TechTreeActionDiscountFormatter(ServiceChannelFormatter):
    __template = 'TechTreeActionDiscountMessage'
    def format(self, message, *args):
        ...

class BlueprintsConvertSaleFormatter(ServiceChannelFormatter):
    __templates: dict
    def format(self, message, *args):
        ...

class CustomizationProgressFormatter(WaitItemsSyncFormatter):
    itemsCache: _Any
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    @staticmethod
    def __getMessageText(itemName, level, vehicleName=''):
        ...

class CustomizationProgressionChangedFormatter(WaitItemsSyncFormatter):
    REQUIRED_KEYS: set
    IGNORE: set
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback=None):
        ...

class PrbEventEnqueueDataFormatter(ServiceChannelFormatter):
    __itemsCache: _Any
    def format(self, message, *args):
        ...

class DogTagFormatter(ServiceChannelFormatter):
    # decorador original: @cached_property
    def serviceMessageSource(self):
        ...
    # decorador original: @cached_property
    def viewTypes(self):
        ...
    def getViewTypeText(self, viewType):
        ...

class DogTagComponentUnlockFormatter(DogTagFormatter):
    def format(self, message, *args):
        ...

class DogTagComponentGradingFormatter(DogTagFormatter):
    grades: dict
    def format(self, message, *args):
        ...

class DedicationRewardFormatter(ServiceChannelFormatter):
    _template = 'DedicationRewardMessage'
    @classmethod
    def _getCountOfCustomizations(cls, rewards):
        ...
    def format(self, message, *args):
        ...

class MapboxStartedFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'MapboxStartedMessage'
    def format(self, message, *args):
        ...

class MapboxEndedFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'Mapbox{}Message'
    __REWARDS_LEFT_MSG = 'Ended'
    __NO_REWARDS_LEFT_MSG = 'EndedNoRewards'
    def format(self, message, *args):
        ...

class BattleMattersTokenAward(ServiceChannelFormatter):
    __TEMPLATE = 'BattleMattersTokenAward'
    def format(self, message, *args):
        ...

class WinbackSelectableAward(ServiceChannelFormatter):
    __TEMPLATE = 'WinbackSelectedAward'
    def format(self, message, *args):
        ...

class MapboxSurveyAvailableFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'MapboxSurveyAvailableMessage'
    __STR_PATH = R.strings.messenger.serviceChannelMessages.mapbox
    def format(self, message, *args):
        ...

class MapboxRewardReceivedFormatter(ServiceChannelFormatter):
    __mapboxCtrl: _Any
    __TEMPLATE = 'MapboxRewardReceivedMessage'
    __STR_PATH = R.strings.messenger.serviceChannelMessages.mapbox
    def format(self, message, *args):
        ...

class TelecomMergeResultsFormatter(WaitItemsSyncFormatter):
    __TEMPLATE = 'telecomMergeResultsMessage'
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback=None):
        ...

class MentorAssignmentUsedFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'MentorAssignmentSysMessage'
    __messageData: dict
    def format(self, message, *args):
        ...

class RecertificationResetUsedFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'RecertificationResetUsedSysMessage'
    __messageData: dict
    def format(self, message, *args):
        ...

class RecertificationResetFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'RecertificationInformationSysMessage'
    def format(self, message, *args):
        ...

class RecertificationAvailabilityFormatter(ServiceChannelFormatter):
    __messageData: dict
    def format(self, message, *args):
        ...

class RecertificationFinancialFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'RecertificationFinancialSysMessage'
    __messageData: dict
    def format(self, message, *args):
        ...

class Customization2DProgressionChangedFormatter(WaitItemsSyncFormatter):
    __itemsCache: _Any
    REQUIRED_KEYS: set
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback, *args):
        ...
    def __getLevelText(self, level):
        ...

class FairplayFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'InformationHeaderSysMessage'
    def format(self, message, *args):
        ...
    def __getBanStoppedMessage(self, extraData, restrType):
        ...

class IntegratedAuctionLostRateFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'IntegratedAuctionLostErrorSysMessage'
    __AUCTION_MESSAGES = R.strings.messenger.serviceChannelMessages.integratedAuction.lostRate
    __CURRENCY_TO_STYLE: dict
    __FREE_XP = 'free_xp'
    __WGM_CURRENCY_TO_NAME: dict
    def format(self, message, *args):
        ...
    def __getCurrencyString(self, currency, amount):
        ...
    def __getCurrencyStyle(self, currencyCode):
        ...

class CollectionsItemsFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'CollectionItemsSysMessage'
    __collections: _Any
    def format(self, message, *args):
        ...

class CollectionsRewardFormatter(ServiceChannelFormatter):
    __MESSAGES = R.strings.collections.notifications
    __ITEMS_TEMPLATE = 'CollectionItemsSysMessage'
    __REWARD_TEMPLATE = 'CollectionRewardsSysMessage'
    __collections: _Any
    def format(self, message, *args):
        ...
    def __makeMessageData(self, collectionID, feature, season, isFinal, message):
        ...
    def __makeFinalMessageData(self, collectionID, feature, season, message):
        ...

class AchievementsEarningSMFormatter(ClientSysMessageFormatter):
    def format(self, message, *args):
        ...
    def __getCtx(self, header, body):
        ...

class AchievementsSMFormatter(ClientSysMessageFormatter):
    __ACHIEVEMENTS_MESSAGES = R.strings.achievements_page.notifications
    __ACHIEVEMENTS_IMAGES = R.images.gui.maps.icons.achievements
    def format(self, message, *args):
        ...
    def __getSavedDate(self, type, rank=None, subRank=None):
        ...
    def __getCtx(self, type, rank=None, subRank=None):
        ...
    def __getTemplate(self, type):
        ...
    def __getLevel(self, rank=None, subRank=None):
        ...

class PrestigeFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'PrestigeLevelUpMessage'
    __LVLUP_MESSAGES = R.strings.messenger.serviceChannelMessages.prestige.lvlUp
    __itemsCache: _Any
    def format(self, message, *args):
        ...
    def __makeMessageData(self, message, vehCD, lvl):
        ...

class CrewBooksConversionFormatter(WaitItemsSyncFormatter, BaseBookConvertingFormatter):
    __TEMPLATE = 'CrewBooksConversionMessage'
    __itemsCache: _Any
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    def __makeMessageData(self, message, crewBooks):
        ...

class PostProgressionUnlockedFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'PostProgressionUnlocked'
    __MESSAGES_TEXT = R.strings.messenger.serviceChannelMessages.postProgression.unlocked
    def format(self, message, *args):
        ...
    def __makeMessageData(self, message):
        ...

class PostProgressionCompletedFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'PostProgressionCompleted'
    __MESSAGES_TEXT = R.strings.messenger.serviceChannelMessages.postProgression.completed
    def format(self, message, *args):
        ...
    def __makeMessageData(self, message):
        ...

class SkillsCrewBoostersConversionFormatter(WaitItemsSyncFormatter, ServiceChannelFormatter):
    __TEMPLATE = 'SkillsCrewBoostersConversion'
    __MESSAGES_TEXT = R.strings.system_messages.skillsCrewBoostersConversion
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    def __makeMessageData(self, message):
        ...

class ExternalVehicleRentFormatter(ServiceChannelFormatter):
    template: _Any
    def __init__(self, isStarted=False):
        ...
    def format(self, message, *args):
        ...

class GFSMFormatter(ClientSysMessageFormatter):
    def format(self, message, *args):
        ...

class ResourceWellOperationFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'ResourceWellOperationMessage'
    __RESOURCE_WELL_MESSAGES = R.strings.messenger.serviceChannelMessages.resourceWell
    __BULLET = '\u2022 '
    __NONE_NATION_NAME = 'intelligence'
    __NO_NATION_INDEX = 0
    __NATIONS_ORDER: dict
    __CURRENCY_ORDER: dict
    __FULL_PROGRESS = 100.0
    def format(self, message, *args):
        ...
    def __formatResources(self, resources):
        ...
    def __formatBlueprints(self, blueprintResources):
        ...
    def __formatCurrencies(self, currencyResources):
        ...
    def __formatCurrencyCount(self, currencyName, count):
        ...
    def __formatBlueprintCount(self, count):
        ...

class PMCompletionFormatter(QuestAchievesFormatter):
    _BULLET = '\u2022'
    __TANKMAN_BONUS_NAME = 'tmanToken'
    @classmethod
    def formatQuestAchieves(cls, data, asBattleFormatter, processCustomizations=True, processTokens=True):
        ...
    @classmethod
    def _processTokens(cls, data):
        ...

class ChallengesAchievesFormatter(QuestAchievesFormatter):
    @classmethod
    def _processTokens(cls, data):
        ...

class PrestigeMilestoneRewardFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'PrestigeMilestoneRewardMessage'
    __MESSAGES = R.strings.messenger.serviceChannelMessages.prestigeMilestone
    def format(self, message, *args):
        ...
    @staticmethod
    def __getTextInfoByItemTypeID(itemTypeID):
        ...

class PrestigeMilestoneErrorFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'ErrorSysMessage'
    __MESSAGES = R.strings.messenger.serviceChannelMessages.prestigeMilestone
    def format(self, message, *args):
        ...

class PetSystemPetAddedFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'PetSystemPetAddedMessage'
    def format(self, message, *args):
        ...

class PetSystemSynergyLevelUpFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'PetSystemSynergyLevelUpMessage'
    def format(self, message, *args):
        ...

class PetSystemSynergyMaxLevelFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'PetSystemSynergyMaxLevelMessage'
    def format(self, message, *args):
        ...

class PetSystemPetPurchaseFormatter(ServiceChannelFormatter):
    __TEMPLATE_GOLD = 'PurchaseForGoldSysMessage'
    __TEMPLATE_CREDITS = 'PurchaseForCreditsSysMessage'
    def format(self, message, *args):
        ...

class PetSystemEventCreditsReceivedFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'PetSystemEventsCreditsReceived'
    def format(self, message, *args):
        ...

class PetSystemEventItemsReceivedFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'PetSystemEventsItemsReceived'
    def format(self, message, *args):
        ...

class Collector20RewardReceivedFormatter(ServiceChannelFormatter):
    __itemsCache: _Any
    __TEMPLATE = 'Collector20RewardReceivedMessage'
    __LINE_SPACER = '<br/><font size="6"> </font></br>'
    __locale = R.strings.messenger.serviceChannelMessages.collector20
    def format(self, message, *args):
        ...
    def __formatAchievements(self, data):
        ...
    def __formatLines(self, lines):
        ...

class PiggyBankCreditsFullFormatter(ServiceChannelFormatter):
    __lobbyContext: _Any
    __TEMPLATE = 'PiggyBankCreditsFullMessage'
    __TIME_LEFT = R.strings.premacc.piggyBankCard.timeLeft
    def format(self, message, *args):
        ...

def _getTimeStamp(message):
    ...
def _extendCustomizationData(newData, extendable, htmlTplPostfix):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _extendCrewSkinsData(newData, extendable, lobbyContext=None, itemsCache=None):
    ...
def _processRareAchievements(rares):
    ...
def _getRareAchievements(dossiers):
    ...
def _toPairLists(dct):
    ...
def _composeAchievements(dossiers):
    ...
def _updateUnique(recType, recData, uniqueAchieves, nonMerged):
    ...
def _getFormatAchieveString(name, block, recData):
    ...
def _getRaresAchievementsStrings(battleResults):
    ...
def _getCrewBookUserString(itemDescr):
    ...
def _getAchievementsFromQuestData(data):
    ...
def _processTankmanToken(tokenName):
    ...
def _processOfferToken(tokenName, count):
    ...
def _processPersonalExchangeRateToken(data, itemsCache):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _getCollectionItemName(entitlementName, collections=None):
    ...
