# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/items/prb_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from past.builtins import cmp as cmp
from account_helpers import getAccountDatabaseID as getAccountDatabaseID, getPlayerID as getPlayerID
from constants import PREBATTLE_ACCOUNT_STATE as PREBATTLE_ACCOUNT_STATE, PREBATTLE_TEAM_STATE as PREBATTLE_TEAM_STATE, OVERRIDDEN_BADGE as OVERRIDDEN_BADGE
from gui.prb_control.prb_helpers import BadgesHelper as BadgesHelper
from gui.prb_control.settings import PREBATTLE_PLAYERS_SORT_TYPES as PREBATTLE_PLAYERS_SORT_TYPES
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle, getOrderByVehicleClass as getOrderByVehicleClass
from gui.shared.sort_key import SortKey as SortKey
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
PlayersStateStats: Any
_PREBATTLE_PLAYERS_SORT_KEYS: dict

class PlayerPrbInfo(object):
    __slots__: tuple
    lobbyContext: Any
    accID: Any
    name: Any
    dbID: Any
    state: Any
    time: Any
    vehCompDescr: Any
    igrType: Any
    clanDBID: Any
    clanAbbrev: Any
    roster: Any
    badges: Any
    group: Any
    vehEnhancements: Any
    role: Any
    isCreator: Any
    def __init__(self, accID, name='', dbID=0, state=..., time=0.0, vehCompDescr=0, igrType=0, clanDBID=0, clanAbbrev='', roster=0, entity=None, badges=None, group=0, vehEnhancements=None, role=0):
        ...
    def __repr__(self):
        ...
    def getFullName(self, isClan=True, isRegion=True):
        ...
    def isVehicleSpecified(self):
        ...
    def getVehicle(self):
        ...
    def isCurrentPlayer(self):
        ...
    def isReady(self):
        ...
    def inBattle(self):
        ...
    def isOffline(self):
        ...
    def getBadge(self):
        ...
    def getEnhancementVisibility(self):
        ...
    def getEnhancementModules(self):
        ...

class TeamStateInfo(object):
    __slots__: tuple
    state: Any
    def __init__(self, state):
        ...
    def __repr__(self):
        ...
    def isNotReady(self):
        ...
    def isReady(self):
        ...
    def isLocked(self):
        ...
    def isInQueue(self):
        ...

class PrbPropsInfo(object):
    __slots__: tuple
    wins: Any
    battlesCount: Any
    createTime: Any
    teamsPositions: Any
    def __init__(self, wins=None, battlesCount=0, createTime=None, teamsPositions=None, **kwargs):
        ...
    def getBattlesScore(self):
        ...
    def __repr__(self):
        ...

class _PrebattlePlayersSortKey(SortKey):
    __slots__: tuple
    player: Any
    def __init__(self, player):
        ...
    @classmethod
    def _playerNameComparator(cls, player, other):
        ...
    @classmethod
    def _vehicleTypeComparator(cls, player, other):
        ...

class _PrebattlePlayersRegularSortKey(_PrebattlePlayersSortKey):
    def _cmp(self, other):
        ...

class _PrebattlePlayersObserversToBottomSortKey(_PrebattlePlayersSortKey):
    def _cmp(self, other):
        ...

class _PrebattlePlayersByVehicleSortKey(_PrebattlePlayersSortKey):
    def _cmp(self, other):
        ...

class _PrebattlePlayersByNameSortKey(_PrebattlePlayersSortKey):
    def _cmp(self, other):
        ...

class _PrebattlePalyersByStateSortKey(_PrebattlePlayersSortKey):
    def _cmp(self, other):
        ...

def getPlayersSortKey(playerSortKeyType=...):
    ...
