# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/arena_info/arena_vos.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import operator as operator
from collections import defaultdict as defaultdict
import typing as typing
from enum import Enum as Enum
from functools import total_ordering as total_ordering
from future.utils import lmap as lmap, viewvalues as viewvalues
from past.builtins import cmp as cmp
import nations as nations
from constants import IGR_TYPE as IGR_TYPE, FLAG_ACTION as FLAG_ACTION, ARENA_GUI_TYPE as ARENA_GUI_TYPE, ROLE_TYPE as ROLE_TYPE, BOT_DISPLAY_STATUS as BOT_DISPLAY_STATUS, BOT_DISPLAY_CLASS_NAMES as BOT_DISPLAY_CLASS_NAMES, LocalizableBotName as LocalizableBotName, BotNamingType as BotNamingType, TEAM_PANEL_MODE as TEAM_PANEL_MODE
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from debug_utils import LOG_ERROR as LOG_ERROR
from gui import makeHtmlString as makeHtmlString
from gui.battle_control import avatar_getter as avatar_getter, vehicle_getter as vehicle_getter
from gui.battle_control.arena_info import settings as settings
from gui.battle_control.arena_info.settings import VehicleSpottedStatus as VehicleSpottedStatus
from gui.battle_control.dog_tag_composer import layoutComposer as layoutComposer
from gui.doc_loaders.badges_loader import getSelectedByLayout as getSelectedByLayout
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.gui_items import Vehicle as Vehicle
from gui.shared.gui_items.Vehicle import VEHICLE_TAGS as VEHICLE_TAGS, VEHICLE_CLASS_NAME as VEHICLE_CLASS_NAME
from gui.shared.system_factory import registerGameModeArenaInfoKeys as registerGameModeArenaInfoKeys, collectGameModeArenaInfoKeys as collectGameModeArenaInfoKeys, collectDisplayedClassTagGetter as collectDisplayedClassTagGetter
from helpers import dependency as dependency, i18n as i18n
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from skeletons.gui.server_events import IEventsCache as IEventsCache
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanics as getVehicleDescrMechanics, getVehicleDescrMechanicParams as getVehicleDescrMechanicParams
_INVALIDATE_OP = settings.INVALIDATE_OP
_VEHICLE_STATUS = settings.VEHICLE_STATUS
_PLAYER_STATUS = settings.PLAYER_STATUS
_DELIVERY_STATUS = settings.INVITATION_DELIVERY_STATUS
_DEFAULT_PLAYER_GROUP = 1
_DEFAULT_PLAYER_RANK = 0
_DEFAULT_PHYSICAL_SECTOR = 1
_DEFAULT_HAS_RESPAWNS = True
_BOT_NAME_PLACE_HOLDER = '{0} ({1})'
_BOT_SUFFIX_BY_STATUS: dict
_BOT_CLASS_NAME_BY_STATUS: dict

class EPIC_RANDOM_KEYS(object):
    PLAYER_GROUP = 'playerGroup'
    @staticmethod
    def getKeys(static=True):
        ...
    @staticmethod
    def getSortingKeys(static=True):
        ...

class BattleRoyaleKeys(Enum):
    RANK = 'playerRank'
    @staticmethod
    def getKeys(static=True):
        ...
    @staticmethod
    def getSortingKeys(static=True):
        ...

class EPIC_BATTLE_KEYS(object):
    RANK = 'playerRank'
    PLAYER_GROUP = 'playerGroup'
    PHYSICAL_SECTOR = 'physicalSector'
    HAS_RESPAWNS = 'hasRespawns'
    @staticmethod
    def getKeys(static=True):
        ...
    @staticmethod
    def getSortingKeys(static=True):
        ...

class GameModeDataVO(object):
    __slots__: tuple
    __internalData: Any
    __sortingKeys: Any
    def __init__(self, gameMode, static=True):
        ...
    def update(self, data):
        ...
    def getValue(self, key, default=None):
        ...
    def getValues(self, keys):
        ...

# decorador original: @total_ordering
class PlayerInfoVO(object):
    __slots__: tuple
    __hash__ = None
    eventsCache: Any
    accountDBID: Any
    avatarSessionID: Any
    name: Any
    fakeName: Any
    clanAbbrev: Any
    igrType: Any
    personaMissionIDs: Any
    personalMissionInfo: Any
    isPrebattleCreator: Any
    forbidInBattleInvitations: Any
    isTeamKiller: Any
    def __init__(self, accountDBID=0, avatarSessionID='', name=None, clanAbbrev='', igrType=..., personalMissionIDs=None, personalMissionInfo=None, isPrebattleCreator=False, forbidInBattleInvitations=False, fakeName='', **kwargs):
        ...
    def __eq__(self, other):
        ...
    def __lt__(self, other):
        ...
    @property
    def isBot(self):
        ...
    @property
    def isBotWithCustomName(self):
        ...
    def update(self, invalidate=..., name=None, accountDBID=0, avatarSessionID='', clanAbbrev='', isPrebattleCreator=False, igrType=..., forbidInBattleInvitations=False, fakeName='', **kwargs):
        ...
    def getPlayerLabel(self):
        ...
    def getPlayerFakeLabel(self):
        ...
    def getRandomPersonalMissions(self):
        ...
    def __getPersonaMissionIDs(self, pQuests):
        ...
    def __compare(self, other):
        ...

# decorador original: @total_ordering
class VehicleTypeInfoVO(object):
    __slots__: tuple
    __hash__ = None
    improvedRammingAnimationDamage: Any
    compactDescr: Any
    strCompactDescr: Any
    tags: Any
    classTag: Any
    isObserver: Any
    isPremiumIGR: Any
    turretYawLimits: Any
    isDualGunVehicle: Any
    isTwinGunVehicle: Any
    hasDualAccuracy: Any
    isAutoShootGunVehicle: Any
    vehicleMechanics: Any
    chassisType: Any
    shortName: Any
    name: Any
    shortNameWithPrefix: Any
    guiName: Any
    nationID: Any
    level: Any
    maxHealth: Any
    isOnlyForBattleRoyaleBattles: Any
    iconName: Any
    iconPath: Any
    role: Any
    def __init__(self, vehicleType=None, maxHealth=None, **kwargs):
        ...
    def __repr__(self):
        ...
    def __eq__(self, other):
        ...
    def __lt__(self, other):
        ...
    def update(self, invalidate=..., vehicleType=None, maxHealth=None, **kwargs):
        ...
    def __setVehicleData(self, vehicleDescr=None, maxHealth=None):
        ...
    def getClassName(self):
        ...
    def getOrderByClass(self):
        ...
    def __compare(self, other):
        ...

# decorador original: @total_ordering
class VehicleArenaInfoVO(object):
    __slots__: tuple
    vehicleID: Any
    team: Any
    player: Any
    vehicleType: Any
    prebattleID: Any
    vehicleStatus: Any
    playerStatus: Any
    invitationDeliveryStatus: Any
    events: Any
    squadIndex: Any
    ranked: Any
    gameModeSpecific: Any
    classTagGetter: Any
    overriddenBadge: Any
    badges: Any
    __prefixBadge: Any
    __suffixBadge: Any
    dogTagModel: Any
    prestigeLevel: Any
    prestigeGradeMarkID: Any
    teamPanelMode: Any
    botDisplayStatus: Any
    def __init__(self, vehicleID, team=0, isAlive=None, isAvatarReady=None, isTeamKiller=None, prebattleID=None, events=None, forbidInBattleInvitations=False, ranked=None, badges=None, overriddenBadge=None, prestigeLevel=None, prestigeGradeMarkID=None, teamPanelMode=..., botDisplayStatus=..., **kwargs):
        ...
    def __repr__(self):
        ...
    def __eq__(self, other):
        ...
    def __lt__(self, other):
        ...
    def __hash__(self):
        ...
    @property
    def selectedBadge(self):
        ...
    @property
    def selectedSuffixBadge(self):
        ...
    def getBadgeExtraInfo(self):
        ...
    def updateVehicleStatus(self, invalidate=..., isAlive=None, isAvatarReady=None, stopRespawn=False, **kwargs):
        ...
    def updatePlayerStatus(self, invalidate=..., isTeamKiller=None, isSquadMan=None, **kwargs):
        ...
    def updateInvitationStatus(self, invalidate=..., include=..., exclude=..., forbidInBattleInvitations=False, **kwargs):
        ...
    def updateRanked(self, invalidate=..., ranked=None, **kwargs):
        ...
    def updateEvents(self, invalidate=..., events=None, **kwargs):
        ...
    def updatePrestige(self, invalidate=..., prestigeLevel=None, prestigeGradeMarkID=None, **kwargs):
        ...
    def updateGameModeSpecificStats(self, *args):
        ...
    def updateVehicleDogTag(self, invalidate=..., dogTag=None, **kwargs):
        ...
    def update(self, **kwargs):
        ...
    def getSquadID(self):
        ...
    def isSquadMan(self, prebattleID=None, playerTeam=None):
        ...
    def isSquadCreator(self):
        ...
    def isTeamKiller(self, playerTeam=None):
        ...
    def getPlayerStatusInTeam(self, playerTeam=None):
        ...
    def isAlive(self):
        ...
    def isReady(self):
        ...
    def isObserver(self):
        ...
    def isEnemy(self):
        ...
    def isSPG(self):
        ...
    def isAutoShootGunVehicle(self):
        ...
    def isDualGunVehicle(self):
        ...
    def isTwinGunVehicle(self):
        ...
    def isActionsDisabled(self):
        ...
    def isPlayer(self):
        ...
    def isPlayerVehicle(self):
        ...
    def isChatCommandsDisabled(self, isAlly):
        ...
    def hasDualAccuracy(self):
        ...
    def getTypeInfo(self):
        ...
    def getIGRLabel(self):
        ...
    def getDisplayedName(self, name=None):
        ...
    def getDisplayedClassTag(self):
        ...
    def getImprovedRammingAnimationDamage(self):
        ...
    def _applyBotName(self, name):
        ...
    def _applyBotDisplayStatus(self, classTag):
        ...
    @staticmethod
    def __getVehicleStatus(isAlive=None, isAvatarReady=None, stopRespawn=False):
        ...
    def __getPlayerStatus(self, isTeamKiller=None):
        ...
    @staticmethod
    def __getInvitationStatus(forbidInBattleInvitations=False):
        ...
    def __compare(self, other):
        ...

class VehicleArenaInteractiveStatsVO(object):
    __slots__: tuple
    xp: Any
    damageDealt: Any
    capturePts: Any
    flagActions: Any
    winPoints: Any
    deathCount: Any
    resourceAbsorbed: Any
    stopRespawn: Any
    equipmentDamage: Any
    equipmentKills: Any
    teamWinPoints: Any
    def __init__(self, xp=0, damageDealt=0, capturePts=0, flagActions=None, winPoints=0, deathCount=0, resourceAbsorbed=0, stopRespawn=False, equipmentDamage=0, equipmentKills=0, *args):
        ...
    def clear(self):
        ...
    def update(self, xp=0, damageDealt=0, capturePts=0, flagActions=None, winPoints=0, deathCount=0, resourceAbsorbed=0, stopRespawn=False, equipmentDamage=0, equipmentKills=0, *args):
        ...
    def getCapturedFlags(self):
        ...
    def getTotalDamage(self):
        ...

class VehicleArenaStatsVO(object):
    __slots__: tuple
    vehicleID: Any
    __frags: Any
    __tkills: Any
    __chatCommand: Any
    __spottedStatus: Any
    __interactive: Any
    __gameModeSpecific: Any
    def __init__(self, vehicleID, frags=0, tkills=0, **kwargs):
        ...
    def __repr__(self):
        ...
    @property
    def frags(self):
        ...
    @property
    def enemyKills(self):
        ...
    @property
    def tkills(self):
        ...
    @property
    def interactive(self):
        ...
    @property
    def gameModeSpecific(self):
        ...
    @property
    def stopRespawn(self):
        ...
    @property
    def winPoints(self):
        ...
    @property
    def chatCommandState(self):
        ...
    @property
    def spottedStatus(self):
        ...
    def clearInteractiveStats(self):
        ...
    def clearGameModeSpecificStats(self):
        ...
    def updateInteractiveStats(self, *args):
        ...
    def updateGameModeSpecificStats(self, *args):
        ...
    def updateChatCommandState(self, chatCommandState):
        ...
    def updateSpottedStatus(self, spottedStatus):
        ...
    def updateVehicleStats(self, frags=0, tkills=0, **kwargs):
        ...

class PlayerRankedInfoVO(object):
    __slots__: tuple
    rank: Any
    rankStep: Any
    def __init__(self, rank=None):
        ...

class ChatCommandVO(object):
    __slots__: tuple
    activeChatCommand: Any
    chatCommandFlags: Any
    def __init__(self, chatCmd='', chatCommandFlags=0):
        ...

class VehicleArenaStatsDict(defaultdict):
    def __missing__(self, key):
        ...
    def clearInteractiveStats(self):
        ...

class VehicleActions(object):
    __ACTIONS: dict
    @staticmethod
    def getBitMask(actions):
        ...
    @staticmethod
    def isHunting(actions):
        ...

def isObserver(tags):
    ...
def isPremium(tags):
    ...
def isPremiumIGR(tags):
    ...
def isBattleRoyaleTank(tags):
    ...
