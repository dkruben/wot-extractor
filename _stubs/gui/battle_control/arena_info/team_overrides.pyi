# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/arena_info/team_overrides.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import VOIP as VOIP
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.arena_info.arena_vos import VehicleActions as VehicleActions
from gui.battle_control.arena_info import settings as settings
_DELIVERY_STATUS = settings.INVITATION_DELIVERY_STATUS
_P_STATUS = settings.PLAYER_STATUS

class DefaultTeamOverrides(object):
    __slots__: tuple
    team: Any
    personal: Any
    isReplayPlaying: Any
    def __init__(self, team, personal, isReplayPlaying=False):
        ...
    def isPlayerSelected(self, vo):
        ...
    def isPersonalSquad(self, vo):
        ...
    def isTeamKiller(self, vo):
        ...
    def getAction(self, vo):
        ...
    def getPlayerStatus(self, vo, isTeamKiller=False):
        ...
    def isPostmortemView(self, vo):
        ...
    def getInvitationDeliveryStatus(self, vo):
        ...
    def getColorScheme(self):
        ...
    def clear(self):
        ...

class PlayerTeamOverrides(DefaultTeamOverrides):
    __slots__: tuple
    __isVoipSupported: Any
    def __init__(self, team, personal, isVoipSupported=False, isReplayPlaying=False):
        ...
    def isPlayerSelected(self, vo):
        ...
    def isPersonalSquad(self, vo):
        ...
    def getAction(self, vo):
        ...
    def getPlayerStatus(self, vo, isTeamKiller=False):
        ...
    def getInvitationDeliveryStatus(self, vo):
        ...
    def getColorScheme(self):
        ...

class PersonalInfo(object):
    __slots__: tuple
    vehicleID: Any
    selectedID: Any
    prebattleID: Any
    teamKillSuspected: Any
    def __init__(self):
        ...
    def changeSelected(self, selectedID):
        ...
    def isOtherSelected(self):
        ...

def makeOverrides(isEnemy, team, personal, arenaVisitor, isReplayPlaying=False):
    ...
