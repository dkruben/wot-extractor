# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/reusable/players.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
from gui.battle_results.components import style as style
from gui.battle_results.reusable import shared as shared
from helpers import dependency as dependency
from shared_utils import findFirst as findFirst
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_ClanInfo: Any

class PlayerInfo(shared.ItemInfo):
    __slots__: tuple
    lobbyContext: Any
    __dbID: Any
    __team: Any
    __fakeName: Any
    __realName: Any
    __prebattleID: Any
    __igrType: Any
    __clanInfo: Any
    __isTeamKiller: Any
    __tags: Any
    squadIndex: Any
    def __init__(self, dbID=0, team=0, name='', realName=..., prebattleID=0, igrType=0, clanAbbrev='', clanDBID=0, wasInBattle=True, **kwargs):
        ...
    @property
    def dbID(self):
        ...
    @property
    def team(self):
        ...
    @property
    def fakeName(self):
        ...
    @property
    def prebattleID(self):
        ...
    @property
    def igrType(self):
        ...
    @property
    def clanInfo(self):
        ...
    @property
    def clanDBID(self):
        ...
    @property
    def clanAbbrev(self):
        ...
    @property
    def realName(self):
        ...
    @property
    def tags(self):
        ...
    def addTag(self, tag):
        ...
    def getFullName(self):
        ...
    def getRegionCode(self):
        ...
    def isAnonymized(self):
        ...

class PlayersInfo(shared.UnpackedInfo):
    __slots__: tuple
    __players: Any
    def __init__(self, players):
        ...
    def getPlayerInfo(self, dbID):
        ...
    @staticmethod
    def makePlayerInfo(dbID=0, realName='', fakeName='', isEnemy=False, wasInBattle=False):
        ...
    def setSquadIndex(self, dbID, index):
        ...
    def getPlayerInfoIterator(self):
        ...
    def getFirstAllyClan(self, team):
        ...
    def getFirstEnemyClan(self, team):
        ...
