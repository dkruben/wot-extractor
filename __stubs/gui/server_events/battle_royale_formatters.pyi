# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/battle_royale_formatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.Scaleform.locale.BATTLE_ROYALE import BATTLE_ROYALE as BATTLE_ROYALE
from gui.battle_control.arena_info import vos_collections as vos_collections
from gui.battle_control.battle_constants import PERSONAL_EFFICIENCY_TYPE as _ETYPE
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_logger: Any
SOLO_ITEMS_ORDER: list
SQUAD_ITEMS_ORDER: list

class StatsItemType(object):
    PLACE = 'place'
    KILLS_SOLO = 'kills'
    KILLS_SQUAD = 'squadKills'
    DAMAGE_DEAL = 'damageDealt'
    DAMAGE_BLOCK = 'damageBlockedByArmor'

class BRSections(object):
    FINISH_REASON = 'finishReason'
    COMMON = 'common'
    PERSONAL = 'personal'
    STATS = 'stats'
    PROGRESS = 'eventProgression'
    LEADERBOARD = 'leaderboard'
    IN_BATTLE = 'inBattle'
    FINANCE = 'financialBalance'
    FINANCE_PREM = 'financialBalancePrem'
    REWARDS = 'rewards'
    ACHIEVEMENTS = 'achievements'
    BONUSES = 'bonuses'
    BATTLE_PASS = 'battlePass'
    BR_AWARD_TOKENS = 'brAwardTokens'

class IngameBattleRoyaleResultsViewDataFormatter(object):
    __lobbyContext: Any
    __sessionProvider: Any
    __arenaDP: Any
    __playerVehicleID: Any
    __efficiencyCtrl: Any
    def __init__(self, sessionProvider, bonusQuestById):
        ...
    @property
    def isInSquad(self):
        ...
    @property
    def playersCount(self):
        ...
    def getSummaryStats(self):
        ...
    def __getPlace(self):
        ...
    def __maxPlaceValue(self):
        ...
    def __getKilled(self):
        ...
    def __getBlockedDamage(self):
        ...
    def __getDamageDealt(self):
        ...
    @staticmethod
    def __createStatItem(value, descr, imgID):
        ...
