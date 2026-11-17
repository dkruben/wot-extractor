# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/common/BattleRoyaleTournament.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import datetime as datetime
from future.utils import viewitems as viewitems
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
CMD_BATTLE_ROYALE_TRN_JOIN = 20000
CMD_BATTLE_ROYALE_TRN_LEAVE = 20001
CMD_BATTLE_ROYALE_TRN_READY = 20002
CMD_BATTLE_ROYALE_TRN_NOT_READY = 20003
CMD_BATTLE_ROYALE_TRN_START_BATTLE = 20004
CMD_DEV_BATTLE_ROYALE_TRN_ADD_TOKEN = 20005
CMD_DEV_BATTLE_ROYALE_TRN_REM_TOKEN = 20006
RESULT_NAMES: dict
MAX_PLAYERS_IN_SQUAD = 2

class RESULT(object):
    OK = 0
    SOME_ERROR = -1
    ALWAYS_JOINED = 1
    NEVER_JOINED = 2
    INVALID_TOKEN = 3
    WRONG_ROLE = 4
    NO_PLACES = 5
    WRONG_PERIPHERY = 6
    DIFFERENT_ROSTER = 7
    WRONG_VEHICLE = 8
    ACCOUNT_LOCKED = 9

class ROLE(object):
    OBSERVER = 1
    PLAYER = 2
    PLAYER_COMMANDER = 3

class TYPE(object):
    SOLO = 1
    SQUAD = 2
    ANY = 3

class BattleRoyaleTourmanentToken(object):
    isValid: Any
    whatWrong: Any
    data: Any
    startTime: Any
    tournamentID: Any
    peripheryID: Any
    fullTournamentID: Any
    teamID: Any
    type: Any
    role: Any
    def __init__(self, token):
        ...
    @property
    def isObserver(self):
        ...
    @property
    def isSolo(self):
        ...
    @property
    def isCommander(self):
        ...
    @property
    def participantShortDescr(self):
        ...
    def __repr__(self):
        ...

def participantsHash(dbIds):
    ...
