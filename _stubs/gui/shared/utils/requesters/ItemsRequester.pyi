# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/requesters/ItemsRequester.py (BYTECODE: a descompilacao falhou; sem bases, decoradores nem valores por omissao).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import operator as operator
from builtins import range as range, zip as zip
from collections import defaultdict as defaultdict, namedtuple as namedtuple
from future.utils import iteritems as iteritems, itervalues as itervalues, lfilter as lfilter, listvalues as listvalues, viewitems as viewitems, viewvalues as viewvalues
from past.builtins import unicode as unicode
from typing import TYPE_CHECKING as TYPE_CHECKING
import BigWorld as BigWorld
import constants as constants
import dossiers2 as dossiers2
import nations as nations
from PlayerEvents import g_playerEvents as g_playerEvents
from account_shared import LayoutIterator as LayoutIterator
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from battle_pass_common import BATTLE_PASS_PDATA_KEY as BATTLE_PASS_PDATA_KEY
from constants import CustomizationInvData as CustomizationInvData, SkinInvData as SkinInvData
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_NOTE as LOG_NOTE, LOG_WARNING as LOG_WARNING
from dossiers2.ui.achievements import BADGES_BLOCK as BADGES_BLOCK
from goodies.goodie_constants import GOODIE_STATE as GOODIE_STATE
from gui.game_loading.resources.consts import Milestones as Milestones
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, GUI_ITEM_TYPE_NAMES as GUI_ITEM_TYPE_NAMES, ItemsCollection as ItemsCollection, checkForTags as checkForTags, getVehicleSuitablesByType as getVehicleSuitablesByType
from gui.shared.gui_items.Vehicle import VEHICLE_TAGS as VEHICLE_TAGS
from gui.shared.gui_items.gui_item_economics import ITEM_PRICE_EMPTY as ITEM_PRICE_EMPTY
from gui.shared.utils.requesters import vehicle_items_getter as vehicle_items_getter
from gui.shared.utils.tankmen_stats_cache import TankmenStatsCache as TankmenStatsCache
from helpers import dependency as dependency, isPlayerAvatar as isPlayerAvatar
from items import getTypeOfCompactDescr as getTypeOfCompactDescr, makeIntCompactDescrByID as makeIntCompactDescrByID, tankmen as tankmen, vehicles as vehicles
from items.components.c11n_constants import CustomizationDisplayType as CustomizationDisplayType, SeasonType as SeasonType
from items.components.crew_skins_constants import CrewSkinType as CrewSkinType
from nation_change.nation_change_helpers import isMainInNationGroupSafe as isMainInNationGroupSafe, iterVehiclesWithNationGroupInOrder as iterVehiclesWithNationGroupInOrder, iterVehTypeCDsInNationGroup as iterVehTypeCDsInNationGroup
from shared_utils.account_helpers.diff_utils import synchronizeDicts as synchronizeDicts
from skeletons.gui.game_control import IVehiclePostProgressionController as IVehiclePostProgressionController
from skeletons.gui.shared import IItemsCache as IItemsCache, IItemsRequester as IItemsRequester
from skeletons.gui.shared.gui_items import IGuiItemsFactory as IGuiItemsFactory
from gui.shared.system_factory import GuiItemsCacheInvalidatorParams as GuiItemsCacheInvalidatorParams, collectGuiItemsCacheInvalidators as collectGuiItemsCacheInvalidators
from wg_async import wg_async as wg_async, wg_await as wg_await, distributeLoopOverTicks as distributeLoopOverTicks
from typing import Optional as Optional, Dict as Dict, List as List
import gui as gui
from skeletons.gui.shared.utils import requesters as requesters
from disjoint_set import DisjointSet as DisjointSet
from gui.shared.gui_items.badge import Badge as Badge
from gui.shared.gui_items.Tankman import Tankman as Tankman
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.veh_post_progression.models.progression import PostProgressionItem as PostProgressionItem
from items.vehicles import VehicleType as VehicleType
from gui.shared.gui_items.customization.c11n_items import Customization as Customization
absolute_import: Any
_logger: Any
DO_LOG_BROKEN_SYNC: Any

# gerado do bytecode: classes base desconhecidas
class _CriteriaCondition:
    def __call__(self, item):
        ...

# gerado do bytecode: classes base desconhecidas
class PredicateCondition:
    def __init__(self, predicate):
        ...
    def __call__(self, item):
        ...
    def lookInInventory(self):
        ...
    def getIntCDProtector(self):
        ...

# gerado do bytecode: classes base desconhecidas
class InventoryPredicateCondition:
    def lookInInventory(self):
        ...

# gerado do bytecode: classes base desconhecidas
class CompoundPredicateCondition:
    def __init__(self, *predicates):
        ...
    def lookInInventory(self):
        ...
    def __call__(self, item):
        ...

# gerado do bytecode: classes base desconhecidas
class NegativeCompoundPredicateCondition:
    def __call__(self, item):
        ...
    def lookInInventory(self):
        ...

# gerado do bytecode: classes base desconhecidas
class OrCompoundPredicateCondition:
    def __call__(self, item):
        ...
    def lookInInventory(self):
        ...

# gerado do bytecode: classes base desconhecidas
class IntCDProtector:
    __slots__: Any
    def __init__(self, *intCDs):
        ...
    def isUnlinked(self):
        ...
    def isTriggered(self, intCD):
        ...

# gerado do bytecode: classes base desconhecidas
class SelectDistinctFilter:
    def __init__(self, dsu):
        ...
    def __call__(self, item):
        ...

# gerado do bytecode: classes base desconhecidas
class RequestCriteria:
    def __init__(self, *args):
        ...
    def __call__(self, item):
        ...
    def __or__(self, other):
        ...
    def __invert__(self):
        ...
    def __xor__(self, other):
        ...
    def getConditions(self):
        ...
    def getIntCDProtector(self):
        ...
    def lookInInventory(self):
        ...
    def conditions(self):
        ...

# gerado do bytecode: classes base desconhecidas
class IntCDProtectionRequestCriteria:
    def __init__(self, condition, intCDs):
        ...

# gerado do bytecode: classes base desconhecidas
class VehsSuitableCriteria:
    def __init__(self, vehsItems, itemTypeIDs=...):
        ...
    def _selectAllSuitableItemsByVehicle(self, vehicle, itemTypeID, outSuitableCompDescrs):
        ...
    def _selectAllSuitableItemsByVehicleDescr(vehicleDescr, itemTypeID, outSuitableCompDescrs):
        ...

# gerado do bytecode: classes base desconhecidas
class VehsMultiNationSuitableCriteria:
    itemsCache: Any
    def _selectAllSuitableItemsByVehicle(self, vehicle, itemTypeID, outSuitableCompDescrs):
        ...

# gerado do bytecode: classes base desconhecidas
class VehicleCanInstallC11nCriteria:
    _itemsCache: Any
    def __init__(self, itemTypeID, criteria, items):
        ...

# gerado do bytecode: classes base desconhecidas
class REQ_CRITERIA:
    EMPTY: Any
    ALL: Any
    NONE: Any
    CUSTOM: Any
    HIDDEN: Any
    SECRET: Any
    COLLECTIBLE: Any
    DISCLOSABLE: Any
    UNLOCKED: Any
    REMOVABLE: Any
    INVENTORY: Any
    NATIONS: Any
    INNATION_IDS: Any
    ITEM_TYPES: Any
    ITEM_TYPES_NAMES: Any
    IN_CD_LIST: Any
    INVENTORY_OR_UNLOCKED: Any
    DISCOUNT_BUY: Any
    DISCOUNT_SELL: Any
    IN_OWNERSHIP: Any
    TYPE_CRITERIA: Any
    # gerado do bytecode: classes base desconhecidas
    class VEHICLE:
        ACTIVE_IN_NATION_GROUP: Any
        ACTIVE_OR_MAIN_IN_NATION_GROUP: Any
        FAVORITE: Any
        PREMIUM: Any
        READY: Any
        OBSERVER: Any
        EARN_CRYSTALS: Any
        LOCKED: Any
        CLASSES: Any
        LEVELS: Any
        ROLES: Any
        LEVEL: Any
        SPECIFIC_BY_CD: Any
        SPECIFIC_BY_NAME: Any
        SPECIFIC_BY_INV_ID: Any
        SUITABLE: Any
        SUITABLE_FOR_MULTI_NATION: Any
        RENT: Any
        TELECOM: Any
        ACTIVE_RENT: Any
        EXPIRED_RENT: Any
        IS_OUTFIT_LOCKED: Any
        IS_STORAGE_HIDDEN: Any
        EXPIRED_IGR_RENT: Any
        RENT_PROMOTION: Any
        EXTERNAL_RENT: Any
        WOT_PLUS_VEHICLE: Any
        TELECOM_RENT: Any
        SEASON_RENT: Any
        DISABLED_IN_PREM_IGR: Any
        IS_PREMIUM_IGR: Any
        ELITE: Any
        IS_BOT: Any
        IS_CREW_LOCKED: Any
        IS_CREW_HIDDEN: Any
        FULLY_ELITE: Any
        EVENT: Any
        EVENT_BATTLE: Any
        EPIC_BATTLE: Any
        BATTLE_ROYALE: Any
        MAPS_TRAINING: Any
        CLAN_WARS: Any
        COMP7: Any
        MODE_HIDDEN: Any
        HAS_XP_FACTOR: Any
        IS_RESTORE_POSSIBLE: Any
        CAN_TRADE_IN: Any
        CAN_TRADE_OFF: Any
        CAN_SELL: Any
        CAN_NOT_BE_SOLD: Any
        IS_IN_BATTLE: Any
        SECRET: Any
        FORBIDDEN_VEHICLE_TO_BATTLE: Any
        NAME_VEHICLE: Any
        NAME_VEHICLE_WITH_SHORT: Any
        DISCOUNT_RENT_OR_BUY: Any
        HAS_TAGS: Any
        HAS_ANY_TAG: Any
        HAS_NO_TAG: Any
        FOR_ITEM: Any
        HAS_ROLE: Any
        HAS_ROLES: Any
        CAN_INSTALL_C11N: Any
    # gerado do bytecode: classes base desconhecidas
    class TANKMAN:
        IN_TANK: Any
        ROLES: Any
        TANKMAN_HAS_ROLE: Any
        NATIVE_TANKS: Any
        SPECIFIC_BY_NAME: Any
        SPECIFIC_BY_NAME_OR_SKIN: Any
        VEHICLE_BATTLE_ROYALE: Any
        VEHICLE_EVENT_BATTLES: Any
        VEHICLE_HIDDEN_IN_HANGAR: Any
        VEHICLE_NATIVE_TYPE: Any
        VEHICLE_NATIVE_TYPES: Any
        VEHICLE_NATIVE_LEVELS: Any
        NATION: Any
        IS_LOCK_CREW: Any
        IS_POST_PROGRESSION_AVAILABLE: Any
        IS_LOW_EFFICIENCY: Any
        DISMISSED: Any
        ACTIVE: Any
    # gerado do bytecode: classes base desconhecidas
    class RECRUIT:
        ROLES: Any
        NATION: Any
        SPECIFIC_BY_NAME: Any
    # gerado do bytecode: classes base desconhecidas
    class CREW_ITEM:
        IN_ACCOUNT: Any
        BOOK_RARITIES: Any
        ID: Any
        NATIONS: Any
    # gerado do bytecode: classes base desconhecidas
    class BOOSTER:
        ENABLED: Any
        IN_ACCOUNT: Any
        ACTIVE: Any
        IS_READY_TO_ACTIVATE: Any
        BOOSTER_TYPES: Any
        BOOSTER_CATEGORIES: Any
        IN_BOOSTER_ID_LIST: Any
        QUALITY: Any
        LIMITED: Any
    # gerado do bytecode: classes base desconhecidas
    class DEMOUNT_KIT:
        IS_ENABLED: Any
        IN_ACCOUNT: Any
    # gerado do bytecode: classes base desconhecidas
    class RECERTIFICATION_FORM:
        IS_ENABLED: Any
        IN_ACCOUNT: Any
    # gerado do bytecode: classes base desconhecidas
    class MENTORING_LICENSE:
        IS_ENABLED: Any
        IN_ACCOUNT: Any
    # gerado do bytecode: classes base desconhecidas
    class EQUIPMENT:
        BUILTIN: Any
        TAGS: Any
    # gerado do bytecode: classes base desconhecidas
    class BATTLE_BOOSTER:
        ALL: Any
        CREW_EFFECT: Any
        OPTIONAL_DEVICE_EFFECT: Any
    # gerado do bytecode: classes base desconhecidas
    class SHELL:
        TYPE: Any
    # gerado do bytecode: classes base desconhecidas
    class ARTEFACT:
        DESCRIPTOR_NAME: Any
    # gerado do bytecode: classes base desconhecidas
    class OPTIONAL_DEVICE:
        SIMPLE: Any
        DELUXE: Any
        TROPHY: Any
        MODERNIZED: Any
        HAS_ANY_FROM_CATEGORIES: Any
        HAS_ANY_FROM_TAGS: Any
        HAS_ANY_BY_ARCHETYPE: Any
        IS_COMPATIBLE_WITH_VEHICLE: Any
    # gerado do bytecode: classes base desconhecidas
    class BADGE:
        SELECTED: Any
        PREFIX_LAYOUT: Any
        ACHIEVED: Any
    # gerado do bytecode: classes base desconhecidas
    class CUSTOMIZATION:
        SUMMER: Any
        WINTER: Any
        DESERT: Any
        ALL_SEASON: Any
        SEASON: Any
        HISTORICAL: Any
        NON_HISTORICAL: Any
        FANTASTICAL: Any
        FOR_VEHICLE: Any
        UNLOCKED_BY: Any
        IS_UNLOCKED: Any
        PRICE_GROUP: Any
        PRICE_GROUP_TAG: Any
        FREE_OR_IN_INVENTORY: Any
        ONLY_IN_GROUP: Any
        DISCLOSABLE: Any
        IS_INSTALLED_ON_VEHICLE: Any
        HAS_TAGS: Any
        FULL_INVENTORY: Any
        ON_ACCOUNT: Any
    # gerado do bytecode: classes base desconhecidas
    class CREW_SKINS:
        NATIONS: Any

# gerado do bytecode: classes base desconhecidas
class RESEARCH_CRITERIA:
    VEHICLE_TO_UNLOCK: Any

# gerado do bytecode: classes base desconhecidas
class ItemsRequester:
    itemsFactory: Any
    _ItemsRequester__vehPostProgressionCtrl: Any
    _AccountItem: Any
    _ItemsRequester__deleteItemFromCache: Any
    _ItemsRequester__getAccountDossierDescr: Any
    _ItemsRequester__getTankmanDossierDescr: Any
    _ItemsRequester__getVehicleDossierDescr: Any
    _ItemsRequester__makeItem: Any
    _ItemsRequester__restoreItemCustomState: Any
    _ItemsRequester__makeVehicle: Any
    _ItemsRequester__makeTankman: Any
    _ItemsRequester__makeDismissedTankman: Any
    _ItemsRequester__makeSimpleItem: Any
    _ItemsRequester__makeSimpleItemsByType: Any
    _ItemsRequester__makeBadge: Any
    _ItemsRequester__getTankmenIDsForVehicle: Any
    _ItemsRequester__getTankmenIDsForTankman: Any
    _ItemsRequester__getVehicleCDForTankman: Any
    _ItemsRequester__checkFittingItemsSync: Any
    def __init__(self, inventory, stats, dossiers, goodies, shop, recycleBin, vehicleRotation, ranked, battleRoyale, badges, epicMetaGame, tokens, festivityRequester, blueprints=..., sessionStatsRequester=..., anonymizerRequester=..., battlePassRequester=..., giftSystemRequester=..., gameRestrictionsRequester=..., achievements20Requester=..., petSystemRequester=..., challengesRequester=...):
        ...
    def inventory(self):
        ...
    def stats(self):
        ...
    def dossiers(self):
        ...
    def goodies(self):
        ...
    def shop(self):
        ...
    def recycleBin(self):
        ...
    def vehicleRotation(self):
        ...
    def ranked(self):
        ...
    def battleRoyale(self):
        ...
    def badges(self):
        ...
    def epicMetaGame(self):
        ...
    def blueprints(self):
        ...
    def festivity(self):
        ...
    def tokens(self):
        ...
    def sessionStats(self):
        ...
    def anonymizer(self):
        ...
    def battlePass(self):
        ...
    def giftSystem(self):
        ...
    def gameRestrictions(self):
        ...
    def achievements20(self):
        ...
    def petSystem(self):
        ...
    def challenges(self):
        ...
    def tankmenStatsCache(self):
        ...
    def request(self, callback=...):
        ...
    def isSynced(self):
        ...
    def requestUserDossier(self, databaseID, callback):
        ...
    def unloadUserDossier(self, databaseID):
        ...
    def requestUserVehicleDossier(self, databaseID, vehTypeCompDescr, callback):
        ...
    def clear(self):
        ...
    def onDisconnected(self):
        ...
    def fini(self):
        ...
    def invalidateCache(self, diff=...):
        ...
    def getVehicle(self, vehInvID):
        ...
    def getStockVehicle(self, typeCompDescr):
        ...
    def getVehicleCopy(self, vehicle):
        ...
    def getVehicleCopyByCD(self, typeCompDescr):
        ...
    def getLayoutsVehicleCopy(self, vehicle, ignoreDisabledProgression=...):
        ...
    def getTankman(self, tmanInvID):
        ...
    def getCrewSkin(self, skinID):
        ...
    def getItems(self, itemTypeID=..., criteria=..., nationID=..., onlyWithPrices=..., limit=...):
        ...
    def getItemsAsync(self, itemTypeID=..., criteria=..., nationID=..., onlyWithPrices=..., callback=...):
        ...
    def getTankmen(self, criteria=...):
        ...
    def getInventoryTankmen(self, criteria=..., limit=...):
        ...
    def getInventoryTankmenRO(self):
        ...
    def getDismissedTankmen(self, criteria=...):
        ...
    def removeUnsuitableTankmen(self, allTankmen, criteria=...):
        ...
    def tankmenInBarracksCount(self):
        ...
    def hasAnyTmanInBarracks(self):
        ...
    def freeTankmenBerthsCount(self):
        ...
    def getVehicles(self, criteria=..., limit=...):
        ...
    def getStyles(self, criteria=...):
        ...
    def getBadges(self, criteria=...):
        ...
    def getReceivedBadges(self, onlySelected=...):
        ...
    def getBadgeByID(self, badgeID):
        ...
    def getItemByCD(self, typeCompDescr, playerIsAvatar=...):
        ...
    def getTypedItemsByCDs(self, itemType, itemCDs):
        ...
    def getItem(self, itemTypeID, nationID, innationID):
        ...
    def getTankmanDossier(self, tmanInvID):
        ...
    def getVehicleDossier(self, vehTypeCompDescr, databaseID=...):
        ...
    def getVehicleDossiersIterator(self):
        ...
    def getAccountDossier(self, databaseID=...):
        ...
    def getClanInfo(self, databaseID=...):
        ...
    def getDogTag(self, databaseID=...):
        ...
    def getServiceRecordCustomization(self, databaseID=...):
        ...
    def getWTR(self, databaseID=...):
        ...
    def getLayout(self, databaseID=...):
        ...
    def getLayoutState(self, databaseID=...):
        ...
    def getBattleRoyaleStats(self, arenaType, databaseID=..., vehicleIntCD=...):
        ...
    def getVehPostProgression(self, vehIntCD, vehType=...):
        ...
    def getPreviousItem(self, itemTypeID, invDataIdx):
        ...
    def doesVehicleExist(self, intCD):
        ...
    def _invalidateItems(self, itemTypeID, uniqueIDs):
        ...
    def _invalidateUnlocks(self, unlocked, result):
        ...
    def __deleteItemFromCache(self, cache, uid, itemTypeID):
        ...
    def __getAccountDossierDescr(self):
        ...
    def __getTankmanDossierDescr(self, tmanInvID):
        ...
    def __getVehicleDossierDescr(self, vehTypeCompDescr):
        ...
    def __makeItem(self, itemTypeIdx, uid, playerIsAvatar=..., *args, **kwargs):
        ...
    def __restoreItemCustomState(self, itemTypeIdx, uid, item):
        ...
    def __makeVehicle(self, typeCompDescr, vehInvData=..., playerIsAvatar=...):
        ...
    def __makeTankman(self, tmanInvID, tmanInvData=...):
        ...
    def __makeDismissedTankman(self, tmanID, tmanData):
        ...
    def __makeSimpleItem(self, typeCompDescr, playerIsAvatar=...):
        ...
    def __makeSimpleItemsByType(self, itemType, typeCompDescrs):
        ...
    def __makeBadge(self, badgeID, badgeData=..., receivedBadges=...):
        ...
    def __getTankmenIDsForVehicle(self, vehData):
        ...
    def __getTankmenIDsForTankman(self, tmanData):
        ...
    def __getVehicleCDForTankman(self, tmanData):
        ...
    def __checkFittingItemsSync(self, itemTypeID):
        ...

def getDiffID(itemdID):
    ...
def _hasSuitableC11n(vehicle, items):
    ...

def __getattr__(name: str) -> Any: ...  # stub incompleto (gerado do bytecode)
