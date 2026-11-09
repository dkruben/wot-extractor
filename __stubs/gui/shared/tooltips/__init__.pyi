# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import sys as sys
import weakref as weakref
import typing as typing
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from frameworks.wulf import WindowFlags as WindowFlags
from gui.Scaleform.daapi.view.lobby.techtree.settings import UNKNOWN_VEHICLE_LEVEL as UNKNOWN_VEHICLE_LEVEL, UnlockProps as UnlockProps
from gui.Scaleform.daapi.view.lobby.techtree.techtree_dp import g_techTreeDP as g_techTreeDP
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.app_loader import sf_lobby as sf_lobby
from gui.impl.pub import WindowImpl as WindowImpl
from gui.shared.formatters import icons as icons
from helpers import dependency as dependency
from helpers.i18n import makeString as makeString
from items import vehicles as vehicles
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.impl import backport as backport
from gui.impl.gen import R as R
from soft_exception import SoftException as SoftException

class TOOLTIP_TYPE(CONST_CONTAINER):
    VEHICLE = 'vehicle'
    TANKMAN = 'tankman'
    NOT_RECRUITED_TANKMAN = 'notRecruitedTankman'
    SPECIAL_TANKMAN = 'specialTankman'
    SKILL = 'skill'
    CREW_SKIN = 'crew_skin'
    CREW_BOOK = 'crew_book'
    CREW_BUNDLE = 'crewBundle'
    ACHIEVEMENT = 'achievement'
    ACHIEVEMENT_ATTR = 'achievementAttr'
    MODULE = 'module'
    SHELL = 'shell'
    EQUIPMENT = 'equipment'
    EFFICIENCY = 'efficiency'
    FORTIFICATIONS = 'fortification'
    IGR = 'igr'
    CYBER_SPORT = 'cyberSport'
    MAP = 'map'
    CONTROL = 'control'
    PRIVATE_QUESTS = 'privateQuests'
    CONTACT = 'contact'
    QUESTS = 'quests'
    EPIC_QUESTS = 'epicQuests'
    HANGAR_TUTORIAL = 'hangarTutorial'
    CLAN_PROFILE = 'clanProfile'
    TECH_CUSTOMIZATION = 'techCustomization'
    BOOSTER = 'booster'
    VEHICLE_FILTER = 'vehicleFilter'
    VEH_CMP_CUSTOMIZATION = 'vehCmpCustomization'
    RESERVE = 'reserve'
    RANKED_STEP = 'rankedStep'
    RANKED_RANK = 'rankedRank'
    RANKED_CALENDAR_DAY = 'rankedCalendarDayInfo'
    RANKED_CALENDAR_DAY_EXTENDED = 'rankedCalendarDayInfoExtended'
    RANKED_SELECTOR_INFO = 'rankedSelectorInfo'
    RANKED_DIVISION_INFO = 'rankedDivisionInfo'
    RANKED_YEAR_REWARD = 'rankedYearReward'
    RANKED_QUESTS_PREVIEW = 'rankedQuestsPreview'
    FAKE = 'fake'
    VEHICLE_ELITE_BONUS = 'vehicleEliteBonus'
    VEHICLE_HISTORICAL_REFERENCE = 'vehicleHistoricalReference'
    MARATHON = 'marathon'
    EPIC_SKILL_INFO = 'epicSkillInfo'
    BLUEPRINTS = 'blueprintsInfo'
    FRONTLINE = 'frontlineInfo'
    BATTLE_ROYALE_SELECTOR_INFO = 'battleRoyaleSelectorInfo'
    BATTLE_ROYALE_SELECTOR_CALENDAR_INFO = 'battleRoyaleSelectorCalendarInfo'
    BATTLE_ROYALE_WIDGET_INFO = 'battleRoyaleWidgetInfo'
    SESSION_STATS = 'sessionStats'
    TRADE_IN_INFO = 'tradeInInfo'
    TRADE_IN_INFO_NOT_AVAILABLE = 'tradeInInfoNotAvailable'
    TRADE_IN_STATE_NOT_AVAILABLE = 'tradeInStateNotAvailable'
    DEMOUNT_KIT = 'demountKit'
    VEHICLE_COLLECTOR = 'vehicleCollector'
    BATTLE_PASS_GIFT_TOKEN = 'battlePassGiftToken'
    BATTLE_PASS_POINTS = 'battlePassPoints'
    EPIC_BATTLE_GIFT_TOKEN = 'epicBattleGiftToken'
    MAPBOX_SELECTOR_INFO = 'mapboxSelectorInfo'
    MAPBOX_CALENDAR_DAY = 'mapboxCalendarDay'
    REFERRAL_PROGRAMM = 'referralProgram'
    EPIC_RANK_UNLOCK = 'epicRankUnlock'
    RANKED_SELECTABLE_REWARD = 'rankedSelectableReward'

class TOOLTIP_COMPONENT(CONST_CONTAINER):
    TECH_MAIN = 'technical_maintenance'
    HANGAR = 'hangar'
    SHOP = 'shop'
    INVENTORY = 'inventory'
    PERSONAL_CASE = 'personal_case'
    CAROUSEL = 'carousel'
    RESEARCH = 'research'
    PROFILE = 'profile'
    PROFILE_VEHICLE = 'profileVehicle'
    FINAL_STATISTIC = 'FinalStatistic'
    CYBER_SPORT_UNIT = 'CyberSportUnit'
    FORTIFICATIONS = 'fortification'
    CLAN_PROFILE = 'clanProfile'
    SETTINGS = 'settings'
    CUSTOMIZATION = 'customization'
    CONTACT = 'contact'
    HANGAR_TUTORIAL = 'hangarTutorial'
    TECH_CUSTOMIZATION = 'techCustomization'
    BOOSTER = 'booster'
    BADGE = 'badge'
    RANK = 'ranked'
    RESERVE = 'reserve'
    BLUEPRINT = 'blueprints'
    SESSION_STATS = 'sessionStats'
    CREW = 'crew'
    CREW_BOOK = 'crewBook'
    TRADE_IN = 'tradeIn'
    DEMOUNT_KIT = 'demountKit'
    MODULE_INFO = 'moduleInfo'
    BATTLE_PASS = 'battlePass'
    EPIC_BATTLE = 'epicBattle'
    RECERTIFICATION_FORM = 'recertificationForm'
    MENTOR_LICENSE = 'mentorLicense'
    FULL_STATS = 'fullStats'

class ACTION_TOOLTIPS_TYPE(CONST_CONTAINER):
    ECONOMICS = 'economics'
    ITEM = 'item'
    BOOSTER = 'booster'
    CAMOUFLAGE = 'camouflage'
    EMBLEMS = 'emblems'
    AMMO = 'ammo'
    RENT = 'rent'

class ACTION_TOOLTIPS_STATE(CONST_CONTAINER):
    DISCOUNT = 'discount'
    PENALTY = 'penalty'

class ToolTipBaseData(object):
    _context: Any
    _toolTipType: Any
    calledBy: Any
    def __init__(self, context, toolTipType):
        ...
    # decorador original: @sf_lobby
    def app(self):
        ...
    @property
    def context(self):
        ...
    def isDynamic(self):
        ...
    def getDisplayableData(self, *args, **kwargs):
        ...
    def buildToolTip(self, *args, **kwargs):
        ...
    def getType(self):
        ...

class ToolTipData(ToolTipBaseData):
    item: Any
    fields: Any
    def __init__(self, context, toolTipType):
        ...
    def getDisplayableData(self, *args, **kwargs):
        ...

class WulfTooltipData(ToolTipData):
    def getDisplayableData(self, *args, **kwargs):
        ...
    def buildToolTip(self, *args, **kwargs):
        ...
    def getTooltipContent(self, *args, **kwargs):
        ...

class ToolTipDataField(object):
    _tooltip: Any
    _name: Any
    _isAvailable: Any
    def __init__(self, tooltip, name):
        ...
    def buildData(self):
        ...
    @property
    def isAvailable(self):
        ...
    def _getValue(self):
        ...

class ToolTipAttrField(ToolTipDataField):
    _attr: Any
    def __init__(self, context, name, attr=None):
        ...
    def _getItem(self):
        ...
    def _getValue(self):
        ...

class ToolTipMethodField(ToolTipDataField):
    _method: Any
    _args: Any
    def __init__(self, context, name, method=None, args=None):
        ...
    def _getItem(self):
        ...
    def _getValue(self):
        ...

class ToolTipAttrCheckField(ToolTipAttrField):
    _value: Any
    def __init__(self, context, name, value, attr=None):
        ...
    def _getValue(self):
        ...

class ToolTipMethodCheckField(ToolTipMethodField):
    _value: Any
    def __init__(self, context, name, value, method=None, args=None):
        ...
    def _getValue(self):
        ...

class ToolTipParameterField(ToolTipDataField):
    def _getParameterValue(self, *args):
        ...

def getComplexStatus(statusKey, **kwargs):
    ...
def getComplexStatusWULF(statusKey, **kwargs):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getUnlockPrice(compactDescr, parentCD=None, vehicleLevel=..., blueprintCount=0, itemsCache=None):
    ...
