# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/reusable/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import typing as typing
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as _CAPS
from account_helpers import getAccountDatabaseID as getAccountDatabaseID
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from debug_utils import LOG_WARNING as LOG_WARNING
from gui.Scaleform.daapi.view.lobby.server_events.events_helpers import BattlePassProgress as BattlePassProgress
from gui.battle_control.arena_info import squad_finder as squad_finder
from gui.battle_results.reusable import sort_keys as sort_keys
from gui.battle_results.reusable.extension_utils import ReusableInfoFactory as ReusableInfoFactory
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD, PLAYER_TEAM_RESULT as _TEAM_RESULT, PREMIUM_STATE as PREMIUM_STATE
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.battle_results.reusable.avatars import AvatarsInfo as AvatarsInfo, AvatarInfo as AvatarInfo
from gui.battle_results.reusable.common import CommonInfo as CommonInfo
from gui.battle_results.reusable.personal import PersonalInfo as PersonalInfo, SquadBonusInfo as SquadBonusInfo
from gui.battle_results.reusable.players import PlayersInfo as PlayersInfo, PlayerInfo as PlayerInfo
from gui.battle_results.reusable.shared import TeamBasesInfo as TeamBasesInfo, VehicleDetailedInfo as VehicleDetailedInfo, VehicleSummarizeInfo as VehicleSummarizeInfo, FairplayViolationsInfo as FairplayViolationsInfo
from gui.battle_results.reusable.vehicles import VehiclesInfo as VehiclesInfo
from gui.shared.system_factory import collectPostbattleSquadFinder as collectPostbattleSquadFinder
from typing import Dict as Dict, Iterator as Iterator, Optional as Optional, Tuple as Tuple
from gui.battle_control import arena_visitor as arena_visitor
from gui.battle_control.arena_info.squad_finder import ISquadFinder as ISquadFinder

class _ReusableInfo(object):
    __slots__: tuple
    itemsCache: Any
    lobbyContext: Any
    __arenaUniqueID: Any
    __clientIndex: Any
    __premiumState: Any
    __premiumPlusState: Any
    __isAddXPBonusApplied: Any
    __common: Any
    __personal: Any
    __players: Any
    __vehicles: Any
    __avatars: Any
    __squadFinder: Any
    __battlePassProgress: Any
    def __init__(self, arenaUniqueID, common, personal, players, vehicles, avatars):
        ...
    @property
    def arenaUniqueID(self):
        ...
    @property
    def clientIndex(self):
        ...
    @clientIndex.setter
    def clientIndex(self, index):
        ...
    @property
    def hasAnyPremiumInPostBattle(self):
        ...
    @property
    def isWotPlusInPostBattle(self):
        ...
    @property
    def premiumState(self):
        ...
    @premiumState.setter
    def premiumState(self, state):
        ...
    @property
    def premiumPlusState(self):
        ...
    @premiumPlusState.setter
    def premiumPlusState(self, state):
        ...
    @property
    def isPremiumBought(self):
        ...
    @property
    def isPremiumPlusBought(self):
        ...
    @property
    def isPostBattlePremium(self):
        ...
    @property
    def isPostBattlePremiumPlus(self):
        ...
    @property
    def isAddXPBonusApplied(self):
        ...
    @isAddXPBonusApplied.setter
    def isAddXPBonusApplied(self, state):
        ...
    @property
    def canUpgradeToPremium(self):
        ...
    @property
    def canUpgradeToPremiumPlus(self):
        ...
    @property
    def canResourceBeFaded(self):
        ...
    @property
    def isSquadSupported(self):
        ...
    @property
    def isStunEnabled(self):
        ...
    @property
    def common(self):
        ...
    @property
    def personal(self):
        ...
    @property
    def players(self):
        ...
    @property
    def vehicles(self):
        ...
    @property
    def avatars(self):
        ...
    @property
    def battlePassProgress(self):
        ...
    @property
    def bonusType(self):
        ...
    def getAvatarInfo(self, dbID=0):
        ...
    def isPersonalTeamWin(self):
        ...
    def getPersonalTeam(self):
        ...
    def getPersonalTeamResult(self):
        ...
    def getPlayerInfo(self, dbID=0):
        ...
    def getPlayerInfoByVehicleID(self, vehicleID):
        ...
    def wasInBattle(self, dbID=0):
        ...
    def getPersonalDetailsIterator(self, result):
        ...
    def getPersonalVehiclesInfo(self, result):
        ...
    def getAllPlayersIterator(self, result, sortKey=...):
        ...
    def getBiDirectionTeamsIterator(self, result, sortKey=...):
        ...
    def getPersonalSquadFlags(self):
        ...
    def updateXPEarnings(self, additionalXPValues):
        ...
    def __findSquads(self):
        ...

def _fetchRecord(results, recordName):
    ...
def _createPostbattleSquadFinder(arenaVisitor):
    ...
def createReusableInfo(results):
    ...
