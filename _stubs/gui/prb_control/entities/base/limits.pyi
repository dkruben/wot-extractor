# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/base/limits.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import weakref as weakref
from collections import defaultdict as defaultdict
from shared_utils import findFirst as findFirst
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import PREBATTLE_ACCOUNT_STATE as PREBATTLE_ACCOUNT_STATE
from gui.prb_control import prb_getters as prb_getters
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.settings import PREBATTLE_ROSTER as PREBATTLE_ROSTER, PREBATTLE_RESTRICTION as PREBATTLE_RESTRICTION
from items.vehicles import VEHICLE_CLASS_TAGS as VEHICLE_CLASS_TAGS, getVehicleType as getVehicleType
from prebattle_shared import isTeamValid as isTeamValid, isVehicleValid as isVehicleValid
from typing import List as List
from gui.prb_control.entities.base.entity import BasePrbEntity as BasePrbEntity

class IVehicleLimit(object):
    def check(self, teamLimits):
        ...

class ITeamLimit(object):
    def check(self, rosters, team, teamLimits):
        ...

class VehicleIsValid(IVehicleLimit):
    def check(self, teamLimits):
        ...

class AbstractTeamIsValid(ITeamLimit):
    def _getAccountsInfo(self, rosters, team):
        ...

class TeamIsValid(AbstractTeamIsValid):
    def check(self, rosters, team, teamLimits):
        ...

class TeamNoPlayersInBattle(ITeamLimit):
    __range: Any
    def __init__(self, prbType):
        ...
    def check(self, rosters, team, teamLimits):
        ...
    def __isPlayerInBattle(self, player):
        ...

class TeamAllPlayersReady(AbstractTeamIsValid):
    def check(self, rosters, team, teamLimits):
        ...
    def __isPlayerNotReady(self, player):
        ...

class MaxCount(ITeamLimit):
    __assigned: Any
    def __init__(self, assigned=True):
        ...
    def check(self, rosters, team, teamLimits):
        ...

class TotalMaxCount(ITeamLimit):
    def check(self, rosters, team, teamLimits):
        ...

class VehiclesLevelLimit(ITeamLimit):
    def check(self, rosters, team, teamLimits):
        ...
    def __calculate(self, rosters):
        ...

class LimitsCollection(object):
    __entity: Any
    __vehicleLimits: Any
    __teamLimits: Any
    def __init__(self, entity, vehicleLimits, teamLimits):
        ...
    def clear(self):
        ...
    def isVehicleValid(self):
        ...
    def isTeamValid(self, team=None):
        ...
    def isTeamsValid(self):
        ...
    def isMaxCountValid(self, team, assigned):
        ...
    def _getEntity(self):
        ...
