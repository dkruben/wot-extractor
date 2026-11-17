# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/contexts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import constants as constants
import gui as gui
import nations as nations
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as _CAPS
from blueprints.BlueprintTypes import BlueprintTypes as BlueprintTypes
from blueprints.FragmentTypes import getFragmentType as getFragmentType
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE, ARENA_GUI_TYPE as ARENA_GUI_TYPE
from CurrentVehicle import g_currentVehicle as g_currentVehicle, g_currentPreviewVehicle as g_currentPreviewVehicle
from dossiers2.custom.records import DB_ID_TO_RECORD as DB_ID_TO_RECORD
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as ACHIEVEMENT_BLOCK
from gui.Scaleform.daapi.view.lobby.techtree.techtree_dp import g_techTreeDP as g_techTreeDP
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers as cmp_helpers
from gui.Scaleform.daapi.view.lobby.veh_post_progression.veh_post_progression_vehicle import g_postProgressionVehicle as g_postProgressionVehicle
from gui.Scaleform.daapi.view.lobby.vehicle_compare.cmp_configurator_vehicle import g_cmpConfiguratorVehicle as g_cmpConfiguratorVehicle
from gui.battle_pass.battle_pass_helpers import getOfferTokenByGift as getOfferTokenByGift
from gui.battle_pass.rewards_sort import getItemsSortKey as getItemsSortKey
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.personal_missions_30.common.enums import ParamTooltipType as ParamTooltipType
from gui.impl.lobby.easy_tank_equip.easy_tank_equip_vehicle import g_easyTankEquipCopyVehicle as g_easyTankEquipCopyVehicle
from gui.server_events import recruit_helper as recruit_helper
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.dossier import factories as factories, loadDossier as loadDossier
from gui.shared.items_parameters import params_helper as params_helper, bonus_helper as bonus_helper
from gui.shared.items_parameters.formatters import NO_BONUS_SIMPLIFIED_SCHEME as NO_BONUS_SIMPLIFIED_SCHEME
from gui.shared.tooltips import TOOLTIP_COMPONENT as TOOLTIP_COMPONENT
from gui.shared.tooltips.personal_missions import PM_BRANCH as PM_BRANCH
from gui.shared.utils.requesters.blueprints_requester import getFragmentNationID as getFragmentNationID
from helpers import dependency as dependency
from rent_common import RENT_TYPE_TO_DURATION as RENT_TYPE_TO_DURATION
from shared_utils import first as first
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController, IBattlePassController as IBattlePassController, IHangarGuiController as IHangarGuiController, ILoadoutController as ILoadoutController
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.gui_items import IGuiItemsFactory as IGuiItemsFactory
from account_helpers.offers.events_data import OfferGift as OfferGift, OfferEventData as OfferEventData
from gui.shared.gui_items.dossier.stats import AccountTotalStatsBlock as AccountTotalStatsBlock

class StatsConfiguration(object):
    __slots__: tuple
    vehicle: Any
    sellPrice: Any
    buyPrice: Any
    minRentPrice: Any
    restorePrice: Any
    rentals: Any
    futureRentals: Any
    unlockPrice: Any
    inventoryCount: Any
    vehiclesCount: Any
    node: Any
    xp: Any
    dailyXP: Any
    showRankedBonusBattle: Any
    slotIdx: Any
    isAwardWindow: Any
    showBonus: Any
    showCompatibles: Any
    withSlots: Any
    isStaticInfoOnly: Any
    showEarnCrystals: Any
    def __init__(self):
        ...

class StatusConfiguration(object):
    __slots__: tuple
    vehicle: Any
    slotIdx: Any
    eqs: Any
    checkBuying: Any
    node: Any
    isResearchPage: Any
    isAwardWindow: Any
    checkNotSuitable: Any
    showCustomStates: Any
    useWhiteBg: Any
    withSlots: Any
    isCompare: Any
    eqSetupIDx: Any
    battleRoyale: Any
    def __init__(self):
        ...

class ParamsConfiguration(object):
    __slots__: tuple
    vehicle: Any
    params: Any
    crew: Any
    eqs: Any
    devices: Any
    dossier: Any
    dossierType: Any
    isCurrentUserDossier: Any
    historicalBattleID: Any
    simplifiedOnly: Any
    externalCrewParam: Any
    colorless: Any
    vehicleLevel: Any
    arenaType: Any
    checkAchievementExistence: Any
    showNormalizationAngle: Any
    showReboundAngle: Any
    showBasic: Any
    showPenetrationLoss: Any
    showScreensArmorMultiplier: Any
    showBasicIsUsedinCalculations: Any
    def __init__(self):
        ...

class ToolTipContext(object):
    _component: Any
    _fieldsToExclude: Any
    def __init__(self, component, fieldsToExclude=None):
        ...
    @property
    def fieldsToExclude(self):
        ...
    def buildItem(self, *args, **kwargs):
        ...
    def getStatusConfiguration(self, item):
        ...
    def getStatsConfiguration(self, item):
        ...
    def getParamsConfiguration(self, item):
        ...
    def getComponent(self):
        ...
    def getParams(self):
        ...

class EmptyOptDeviceSlotContext(ToolTipContext):
    _slotIdx: Any
    _vehicle: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, slotIdx, vehicle=None):
        ...
    def getStatusConfiguration(self, item):
        ...
    def __getVehicle(self):
        ...

class DefaultContext(ToolTipContext):
    itemsCache: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, intCD):
        ...
    def getStatusConfiguration(self, item):
        ...
    def getStatsConfiguration(self, item):
        ...
    def getParamsConfiguration(self, item):
        ...

class BadgeContext(ToolTipContext):
    __itemsCache: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def getParamsConfiguration(self, item):
        ...
    def buildItem(self, badgeID):
        ...

class ReferralProgramBadgeContext(BadgeContext):
    def getParamsConfiguration(self, item):
        ...

class AwardContext(DefaultContext):
    itemsCache: Any
    _tmanRoleLevel: Any
    _rentExpiryTime: Any
    _rentBattlesLeft: Any
    _rentWinsLeft: Any
    _seasonRent: Any
    _isSeniority: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, intCD, tmanCrewLevel=None, rentExpiryTime=None, rentBattles=None, rentWins=None, rentSeason=None, rentCycle=None, isSeniority=False):
        ...
    def getStatsConfiguration(self, item):
        ...
    def getStatusConfiguration(self, item):
        ...
    def getParamsConfiguration(self, item):
        ...
    def getParams(self):
        ...

class ExtendedAwardContext(AwardContext):
    _showCrew: Any
    _showVehicleSlot: Any
    _allModulesAvailable: Any
    _showBuyPrice: Any
    _showUnlockPrice: Any
    _isAwardWindow: Any
    def __init__(self, fieldsToExclude=None, showBuyPrice=False, showUnlockPrice=False, isAwardWindow=True):
        ...
    def buildItem(self, intCD, tmanCrewLevel=None, rentExpiryTime=None, rentBattles=None, rentWins=None, rentSeason=None, rentCycle=None, isSeniority=False, showCrew=False, showVehicleSlot=False, allModulesAvailable=False):
        ...
    def getParams(self):
        ...
    def getStatsConfiguration(self, item):
        ...
    def getStatusConfiguration(self, item):
        ...

class SeniorityAwardContext(ExtendedAwardContext):
    _showCrew: Any
    _showVehicleSlot: Any
    def __init__(self, fieldsToExclude=None):
        ...

class WinbackDiscountContext(ExtendedAwardContext):
    _blueprintsFragmentsCount: Any
    _customPrice: Any
    _hideStatus: Any
    _showDiscount: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, intCD, tmanCrewLevel=None, rentExpiryTime=None, rentBattles=None, rentWins=None, rentSeason=None, rentCycle=None, isSeniority=False, showCrew=False, showVehicleSlot=False, allModulesAvailable=False, blueprintsFragmentsCount=0, customPrice=None, hideStatus=True, showDiscount=True):
        ...
    def getParams(self):
        ...

class ShopContext(AwardContext):
    def getStatsConfiguration(self, item):
        ...

class RankedRankContext(ToolTipContext):
    rankedController: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, rankID):
        ...

class InventoryContext(ToolTipContext):
    itemsCache: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, intCD):
        ...
    def getStatsConfiguration(self, item):
        ...
    def getParamsConfiguration(self, item):
        ...

class ModuleInfoContext(ToolTipContext):
    itemsCache: Any
    itemsFactory: Any
    __vehDescr: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, intCD, vehDescr):
        ...
    def getStatusConfiguration(self, item):
        ...
    def getStatsConfiguration(self, item):
        ...
    def getParamsConfiguration(self, item):
        ...

class CarouselContext(InventoryContext):
    _component: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def getStatusConfiguration(self, item):
        ...
    def getStatsConfiguration(self, item):
        ...
    def buildItem(self, intCD):
        ...

class HangarCarouselContext(CarouselContext):
    __hangarGuiCtrl: Any
    __rankedController: Any
    def getStatsConfiguration(self, item):
        ...
    def __applyRankedStatsConfiguration(self, item, value):
        ...

class PotapovQuestsChainContext(ToolTipContext):
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, tileID, chainID):
        ...

class PersonalMissionOperationContext(ToolTipContext):
    _eventsCache: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, tileID):
        ...

class PersonalMissionCampaignContext(ToolTipContext):
    _eventsCache: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, campaignID):
        ...

class QuestContext(ToolTipContext):
    eventsCache: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, eventID):
        ...

class PersonalMissionContext(QuestContext):
    def buildItem(self, eventID, *args, **kwargs):
        ...

class BaseHangarParamContext(ToolTipContext):
    isApproximately: Any
    showTitleValue: Any
    def __init__(self, showTitleValue=False):
        ...
    def getComparator(self):
        ...
    def buildItem(self, *args, **kwargs):
        ...
    def getBonusExtractor(self, vehicle, bonuses, paramName):
        ...

class HangarParamContext(BaseHangarParamContext):
    formatters: Any
    def __init__(self):
        ...
    def getComparator(self):
        ...
    def buildItem(self, *args, **kwargs):
        ...

class PreviewParamContext(HangarParamContext):
    formatters: Any
    def __init__(self):
        ...
    def getComparator(self):
        ...
    def buildItem(self, *args, **kwargs):
        ...

class CmpParamContext(HangarParamContext):
    formatters: Any
    def __init__(self):
        ...
    def buildItem(self, *args, **kwargs):
        ...
    def getComparator(self):
        ...

class TankSetupParamContext(HangarParamContext):
    __loadoutController: Any
    formatters: Any
    def __init__(self):
        ...
    def getComparator(self):
        ...
    def buildItem(self, *args, **kwargs):
        ...
    def getBonusExtractor(self, vehicle, bonuses, paramName):
        ...
    def __getItem(self):
        ...

class PostProgressionParamContext(TankSetupParamContext):
    isApproximately: Any
    def __init__(self):
        ...
    def getComparator(self):
        ...
    def buildItem(self, *args, **kwargs):
        ...
    def getBonusExtractor(self, vehicle, bonuses, paramName):
        ...

class EasyTankEquipParamContext(HangarParamContext):
    formatters: Any
    def __init__(self):
        ...
    def getComparator(self):
        ...
    def buildItem(self, *args, **kwargs):
        ...
    def getBonusExtractor(self, vehicle, bonuses, paramName):
        ...

class HangarContext(ToolTipContext):
    itemsCache: Any
    _slotIdx: Any
    _vehicle: Any
    _historicalBattleID: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def getVehicle(self):
        ...
    def buildItem(self, intCD, slotIdx=0, historicalBattleID=-1, vehicle=None):
        ...
    def getStatusConfiguration(self, item):
        ...
    def getStatsConfiguration(self, item):
        ...
    def getParamsConfiguration(self, item):
        ...

class ArmorInspectorContext(HangarContext):
    _vehicle: Any
    def buildItem(self, intCD, vehicle):
        ...
    def getParamsConfiguration(self, item):
        ...
    def getStatsConfiguration(self, item):
        ...

class HangarCardContext(HangarContext):
    def getStatusConfiguration(self, item):
        ...
    def getStatsConfiguration(self, item):
        ...

class HangarSlotContext(HangarContext):
    def getStatsConfiguration(self, item):
        ...
    def getStatusConfiguration(self, item):
        ...

class NationChangeHangarContext(HangarContext):
    __slots__: tuple
    __layoutIDx: Any
    _vehicle: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, vehCD, intCD, layoutIDx=None):
        ...
    def getStatusConfiguration(self, item):
        ...

class PreviewContext(HangarContext):
    def getVehicle(self):
        ...

class VehCmpConfigurationContext(HangarContext):
    def getVehicle(self):
        ...
    def getStatusConfiguration(self, item):
        ...
    def getStatsConfiguration(self, item):
        ...
    def buildItem(self, intCD, slotIdx=0, historicalBattleID=-1, vehicle=None):
        ...

class VehCmpConfigurationSlotContext(VehCmpConfigurationContext):
    def getStatsConfiguration(self, item):
        ...
    def getStatusConfiguration(self, item):
        ...

class TankmanHangarContext(HangarContext):
    def buildItem(self, invID):
        ...

class NotRecruitedTankmanContext(HangarContext):
    def buildItem(self, recruitID):
        ...

class TechTreeContext(DefaultContext):
    _vehicle: Any
    _node: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, node, parentCD):
        ...
    def getStatusConfiguration(self, item):
        ...
    def getStatsConfiguration(self, item):
        ...
    def getParamsConfiguration(self, item):
        ...

class ModuleContext(TechTreeContext):
    def getStatsConfiguration(self, item):
        ...

class BlueprintContext(ToolTipContext):
    __itemsCache: Any
    __blueprintCD: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, cd=None):
        ...
    def getVehicleBlueprintData(self, vehicleCD=None):
        ...
    def getDiscountValues(self, vehicle=None):
        ...
    def getFragmentDiscounts(self, vehicle=None):
        ...
    def getFragmentConvertData(self, vLevel=None):
        ...
    def getFragmentData(self, fragmentCD=None):
        ...
    def getUniversalCount(self, vehicleCD=None):
        ...
    def getBlueprintLayout(self, vehicle=None):
        ...
    def getAllianceNationFragmentsData(self, vehicle):
        ...

class VehicleAnnouncementContext(ToolTipContext):
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, node, *args, **kwargs):
        ...

class VehCmpModulesContext(TechTreeContext):
    _vehicle: Any
    _node: Any
    def buildItem(self, node, parentCD):
        ...
    def getStatusConfiguration(self, item):
        ...
    def getStatsConfiguration(self, item):
        ...

class CmpModulesWithVehicleContext(VehCmpModulesContext):
    _vehicle: Any
    def buildItem(self, intCD, vehicle):
        ...

class TechMainContext(HangarContext):
    _eqs: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, compact, slotIdx=0, eqs=None, vehicle=None, parentCD=None):
        ...
    def getStatusConfiguration(self, item):
        ...
    def getStatsConfiguration(self, item):
        ...

class CrewSkinContext(ToolTipContext):
    itemsCache: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, skinID):
        ...

class CrewBookContext(ToolTipContext):
    itemsCache: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, bookCD):
        ...

class ProfileContext(ToolTipContext):
    _dossier: Any
    _dossierType: Any
    _isCurrentUserDossier: Any
    _vehicleLevel: Any
    _arenaType: Any
    _component: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, dossierType, dossierCompDescr, block, name, isRare, isUserDossier=True, vehicleLevel=0, arenaType=...):
        ...
    def getParamsConfiguration(self, item):
        ...

class BattleResultContext(ProfileContext):
    __itemsCache: Any
    _component: Any
    _vehicleLevel: Any
    _arenaType: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, block, name, value=0, customData=None, vehicleLevel=0, arenaType=...):
        ...
    def getParamsConfiguration(self, item):
        ...

class ShopAchievementContext(BattleResultContext):
    def buildItem(self, aID, *args):
        ...

class BattleResultMarksOnGunContext(BattleResultContext):
    _vehicleLevel: Any
    _arenaType: Any
    def buildItem(self, block, name, value=0, customData=None, vehicleLevel=0, arenaType=...):
        ...

class BattleResultMarkOfMasteryContext(BattleResultContext):
    _vehicleLevel: Any
    _arenaType: Any
    def buildItem(self, block, name, value=0, customData=None, vehicleLevel=0, arenaType=...):
        ...

class VehicleEliteBonusContext(ToolTipContext):
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, bonusId):
        ...

class VehicleHistoricalReferenceContext(ToolTipContext):
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, *args, **kwargs):
        ...

class FinalStatisticContext(ToolTipContext):
    def __init__(self, fieldsToExclude=None):
        ...

class CyberSportUnitContext(ToolTipContext):
    def __init__(self, fieldsToExclude=None):
        ...

class FortificationContext(ToolTipContext):
    def __init__(self, fieldsToExclude=None):
        ...

class ReserveContext(ToolTipContext):
    itemsCache: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, intCD):
        ...

class ClanProfileFortBuildingContext(ToolTipContext):
    def __init__(self, fieldsToExclude=None):
        ...

class ContactContext(ToolTipContext):
    def __init__(self, fieldsToExclude=None):
        ...

class BattleConsumableContext(FortificationContext):
    __itemsCache: Any
    def buildItem(self, intCD):
        ...

class HangarTutorialContext(ToolTipContext):
    def __init__(self, fieldsToExclude=None):
        ...

class FortPopoverDefResProgressContext(FortificationContext):
    ...

class SettingsMinimapContext(ToolTipContext):
    ...

class SquadRestrictionContext(ToolTipContext):
    ...

class TechCustomizationContext(ToolTipContext):
    def __init__(self, fieldsToExclude=None):
        ...
    def getStatsConfiguration(self, item):
        ...
    def getParams(self):
        ...

class SessionStatsContext(ToolTipContext):
    itemsCache: Any
    def __init__(self):
        ...
    def buildItem(self, intCD):
        ...

class ShopCustomizationContext(TechCustomizationContext):
    def getStatsConfiguration(self, item):
        ...

class BoosterInfoContext(ToolTipContext):
    _goodiesCache: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def getStatsConfiguration(self, item):
        ...
    def buildItem(self, boosterID):
        ...

class DemountKitContext(ToolTipContext):
    _goodiesCache: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, demountKitID):
        ...

class BoosterContext(BoosterInfoContext):
    def getStatsConfiguration(self, item):
        ...

class QuestsBoosterContext(BoosterInfoContext):
    def getStatsConfiguration(self, item):
        ...

class ShopBoosterContext(BoosterInfoContext):
    def getStatsConfiguration(self, item):
        ...

class ClanReserveContext(BoosterInfoContext):
    def buildItem(self, boosterID):
        ...
    def getStatsConfiguration(self, item):
        ...

class BoosterStatsConfiguration(object):
    __slots__: tuple
    buyPrice: Any
    inventoryCount: Any
    quests: Any
    activeState: Any
    effectTime: Any
    activateInfo: Any
    dueDate: Any
    def __init__(self):
        ...

class BadgeParamsConfiguration(object):
    __slots__: tuple
    showVehicle: Any
    def __init__(self):
        ...

class HangarServerStatusContext(ToolTipContext):
    def __init__(self, fieldsToExclude=None):
        ...

class BattleBoosterContext(HangarContext):
    def getStatsConfiguration(self, item):
        ...
    def getStatusConfiguration(self, item):
        ...

class InventoryBattleBoosterContext(BattleBoosterContext):
    def getStatsConfiguration(self, item):
        ...
    def getStatusConfiguration(self, item):
        ...

class AwardBattleBoosterContext(InventoryBattleBoosterContext):
    def getStatsConfiguration(self, item):
        ...
    def getStatusConfiguration(self, item):
        ...

class ShopBattleBoosterContext(AwardBattleBoosterContext):
    def getStatsConfiguration(self, item):
        ...

class DogTagInfoContext(ToolTipContext):
    def __init__(self, fieldsToExclude=None):
        ...

class BattlePassGiftTokenContext(ToolTipContext):
    __slots__: tuple
    __offersProvider: Any
    __battlePassController: Any
    __hasOffer: Any
    def __init__(self):
        ...
    def buildItem(self, tokenID, **kwargs):
        ...
    def getParams(self):
        ...

class PersonalMissionsPointsTooltipContext(ToolTipContext):
    def getParams(self):
        ...

class PersonalMissionOperationDisabledTooltipContext(ToolTipContext):
    def getParams(self):
        ...

def _getCmpVehicle():
    ...
def _getCmpInitialVehicle():
    ...
