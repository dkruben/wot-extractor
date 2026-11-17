# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/reusable/common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import defaultdict as defaultdict
import logging as logging
import typing as typing
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as _CAPS
import ArenaType as ArenaType
from battle_modifiers_common import BattleModifiers as BattleModifiers
from gui.battle_results.reusable.players import PlayerInfo as PlayerInfo
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE, FINISH_REASON as FINISH_REASON
from gui.battle_control import arena_visitor as arena_visitor
from gui.battle_results.reusable import shared as shared
from helpers.bots import preprocessBotName as preprocessBotName
_logger: Any

class CommonInfo(shared.UnpackedInfo):
    __slots__: tuple
    __arenaTypeID: Any
    __winnerTeam: Any
    __finishReason: Any
    __bots: Any
    __finishAllPlayersLeft: Any
    __numDefended: Any
    __bonusCapsOverrides: Any
    __battleModifiers: Any
    __arenaVisitor: Any
    def __init__(self, arenaTypeID=0, guiType=..., bonusType=..., winnerTeam=0, finishReason=..., bots=None, finishAllPlayersLeft=False, bonusCapsOverrides=None, battleModifiersDescr=None, **kwargs):
        ...
    @property
    def arenaVisitor(self):
        ...
    @property
    def arenaTypeID(self):
        ...
    @property
    def arenaGuiType(self):
        ...
    @property
    def arenaBonusType(self):
        ...
    @property
    def arenaSubTypeName(self):
        ...
    @property
    def arenaType(self):
        ...
    @property
    def battleModifiers(self):
        ...
    @property
    def winnerTeam(self):
        ...
    @property
    def finishReason(self):
        ...
    @property
    def finishAllPlayersLeft(self):
        ...
    @property
    def numDefended(self):
        ...
    def isSquadSupported(self):
        ...
    def canTakeSquadXP(self):
        ...
    def getArenaIcon(self, subdir=''):
        ...
    def getBotInfo(self, vehicleID):
        ...
    def getBots(self):
        ...
    def checkBonusCaps(self, *bonusCaps):
        ...
