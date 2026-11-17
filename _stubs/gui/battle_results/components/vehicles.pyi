# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/components/vehicles.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import DEATH_REASON_ALIVE as DEATH_REASON_ALIVE
from epic_constants import EPIC_BATTLE_TEAM_ID as EPIC_BATTLE_TEAM_ID
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES as RANKEDBATTLES_ALIASES
from gui.Scaleform.locale.BATTLE_RESULTS import BATTLE_RESULTS as BATTLE_RESULTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.settings import ICONS_SIZES as ICONS_SIZES
from gui.battle_results.components import base as base, shared as shared, style as style, ranked as ranked
from gui.battle_results.components.base import PropertyValue as PropertyValue
from gui.battle_results.components.personal import fillKillerInfoBlock as fillKillerInfoBlock, NO_OWNER_DEATH_REASON_IDS as NO_OWNER_DEATH_REASON_IDS
from gui.battle_results.reusable import sort_keys as sort_keys
from gui.battle_results.reusable.avatars import AvatarInfo as AvatarInfo
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.Vehicle import getSmallIconPath as getSmallIconPath, getIconPath as getIconPath
from helpers import dependency as dependency, i18n as i18n
from messenger.m_constants import USER_TAG as USER_TAG
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_STAT_VALUES_VO_REPLACER: dict
_STAT_STUN_FIELD_NAMES: tuple

class TeamPlayerNameBlock(shared.PlayerNameBlock):
    __slots__: tuple
    igrType: Any
    def setPlayerInfo(self, playerInfo):
        ...
    def setRecord(self, result, reusable):
        ...

class RegularVehicleStatsBlock(base.StatsBlock):
    __slots__: tuple
    _isObserver: Any
    isPersonal: Any
    isPersonalSquad: Any
    isTeamKiller: Any
    isKilledByTeamKiller: Any
    vehicleSort: Any
    suffixBadgeIcon: Any
    suffixBadgeStripIcon: Any
    hasSelectedBadge: Any
    badge: Any
    playerID: Any
    player: Any
    squadIndex: Any
    kills: Any
    tkills: Any
    realKills: Any
    damageDealt: Any
    statValues: Any
    achievementsCount: Any
    achievements: Any
    killerID: Any
    deathReason: Any
    intCD: Any
    vehicleName: Any
    vehicleShortName: Any
    vehicleIcon: Any
    vehicles: Any
    xp: Any
    xpSort: Any
    vehicleState: Any
    vehicleStatePrefix: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...
    def _setBadge(self, result, reusable):
        ...
    def _processVehicles(self, result):
        ...
    def _setVehicleInfo(self, vehicle):
        ...
    def _setPlayerInfo(self, player):
        ...
    def _setTotalStats(self, result, noPenalties):
        ...
    def _setVehiclesStats(self, result, reusable):
        ...
    def _setAchievements(self, result, reusable):
        ...
    def _setVehicleState(self, result, reusable):
        ...

class EpicVehicleStatsBlock(RegularVehicleStatsBlock):
    __slots__: tuple
    vehicles: Any
    __allAdded: Any
    playerRank: Any
    respawns: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def _processVehicles(self, result):
        ...
    def _setVehicleInfo(self, vehicle):
        ...
    def setRecord(self, result, reusable):
        ...
    def getVO(self):
        ...

class StrongholdVehicleStatsBlock(RegularVehicleStatsBlock):
    ...

class RegularVehicleStatValuesBlock(base.StatsBlock):
    __slots__: tuple
    lobbyContext: Any
    _filters: Any
    _isPersonal: Any
    __rawDamageAssistedStun: Any
    __rawStunNum: Any
    shots: Any
    hits: Any
    explosionHits: Any
    damageDealt: Any
    sniperDamageDealt: Any
    directHitsReceived: Any
    piercingsReceived: Any
    noDamageDirectHitsReceived: Any
    explosionHitsReceived: Any
    damageBlockedByArmor: Any
    teamHitsDamage: Any
    spotted: Any
    damagedKilled: Any
    damageAssisted: Any
    damageAssistedStun: Any
    stunNum: Any
    stunDuration: Any
    capturePoints: Any
    mileage: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setPersonal(self, flag):
        ...
    def addFilters(self, filters):
        ...
    def setRecord(self, result, reusable):
        ...
    def getVO(self):
        ...

class RankedVehicleStatValuesBlock(RegularVehicleStatValuesBlock):
    __slots__: tuple
    xp: Any
    xpForAttack: Any
    xpForAssist: Any
    xpOther: Any
    def setRecord(self, result, reusable):
        ...

class StrongholdVehicleStatValuesBlock(RegularVehicleStatValuesBlock):
    __slots__: tuple
    artilleryFortEquipDamageDealt: Any
    def setRecord(self, result, reusable):
        ...

class EpicVehicleStatValuesBlock(base.StatsBlock):
    __slots__: tuple
    _filters: Any
    _isPersonal: Any
    timesDestroyed: Any
    _team: Any
    __rawDamageAssistedStun: Any
    __rawStunNum: Any
    shots: Any
    directHits: Any
    piercingHits: Any
    explosionHits: Any
    damageDealt: Any
    sniperDamageDealt: Any
    destructiblesDamageDealt: Any
    equipmentDamageDealt: Any
    directHitsReceived: Any
    piercingsReceived: Any
    noDamageDirectHitsReceived: Any
    explosionHitsReceived: Any
    damageBlockedByArmor: Any
    teamHitsDamage: Any
    spotted: Any
    damagedKilled: Any
    damageAssisted: Any
    equipmentDamageAssisted: Any
    damageAssistedStun: Any
    stunNum: Any
    capturePoints: Any
    teamSpecificStat: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setPersonal(self, flag):
        ...
    def addFilters(self, filters):
        ...
    def setRecord(self, result, reusable):
        ...
    def getVO(self):
        ...

class AllRegularVehicleStatValuesBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class AllEpicVehicleStatValuesBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class AllStrongholdVehicleStatValuesBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class PersonalVehiclesRegularStatsBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class PersonalVehiclesRankedStatsBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class PersonalVehiclesEpicStatsBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class PersonalVehiclesStrongholdStatsBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class TeamStatsBlock(base.StatsBlock):
    __slots__: tuple
    __class: Any
    def __init__(self, class_, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...

class RegularTeamStatsBlock(TeamStatsBlock):
    __slots__: tuple
    def __init__(self, meta=None, field='', *path):
        ...

class EpicTeamStatsBlock(TeamStatsBlock):
    __slots__: tuple
    def __init__(self, meta=None, field='', *path):
        ...

class StrongholdTeamStatsBlock(TeamStatsBlock):
    __slots__: tuple
    def __init__(self, meta=None, field='', *path):
        ...

class TwoTeamsStatsBlock(shared.BiDiStatsBlock):
    __slots__: tuple
    def addComponent(self, index, component):
        ...
    def setRecord(self, result, reusable):
        ...

class RankedResultsTeamStatsBlock(shared.BiDiStatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class RankedResultsTeamDataStatsBlock(base.StatsBlock):
    __slots__: tuple
    teamList: Any
    title: Any
    titleAlpha: Any
    def setRecord(self, result, reusable):
        ...
    def __getIsWinTeam(self, currentTeam, playerTeam, winTeam):
        ...
    @staticmethod
    def __fillIncompleteTeam(membersCount, maxCount, lists, listsSteps):
        ...
    @staticmethod
    def __getPlayerListIndex(playerIndex, listsSteps):
        ...
    @staticmethod
    def __createListsAndSteps(listsData):
        ...

class RankedResultsTeamPartDataStatsBlock(base.StatsBlock):
    __slots__: tuple
    settingsCore: Any
    listData: Any
    backgroundType: Any
    backgroundBlink: Any
    icon: Any
    iconType: Any
    capacity: Any
    isColorBlind: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def appendPlayer(self, playerItem):
        ...
    def getPlayersNumber(self):
        ...
    def setListResources(self, listInfo, isTopList=False):
        ...
    def setListBlink(self, isBlink):
        ...
    def getListCapacity(self):
        ...
    def isTopList(self):
        ...

class RankedResultsListItemStatsBlock(base.StatsBlock):
    __slots__: tuple
    settingsCore: Any
    nickName: Any
    nickNameHuge: Any
    fakeName: Any
    fakeNameHuge: Any
    points: Any
    pointsHuge: Any
    selected: Any
    standoff: Any
    tags: Any
    def setRecord(self, result, reusable):
        ...

class BadgeBlock(base.StatsBlock):
    __slots__: tuple
    icon: Any
    content: Any
    sizeContent: Any
    isDynamic: Any
    isAtlasSource: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...

def _getStunFilter():
    ...
