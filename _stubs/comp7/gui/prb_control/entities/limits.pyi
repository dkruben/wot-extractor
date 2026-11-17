# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/prb_control/entities/limits.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import PREBATTLE_MAX_OBSERVERS_IN_TEAM as PREBATTLE_MAX_OBSERVERS_IN_TEAM, ROLE_TYPE as ROLE_TYPE, PREBATTLE_TYPE as PREBATTLE_TYPE
from gui.prb_control import prb_getters as prb_getters
from helpers import dependency as dependency
from gui.prb_control.entities.base.limits import ITeamLimit as ITeamLimit, TeamNoPlayersInBattle as TeamNoPlayersInBattle, TeamIsValid as TeamIsValid, TeamAllPlayersReady as TeamAllPlayersReady, LimitsCollection as LimitsCollection
from gui.prb_control.entities.training.legacy.limits import TrainingVehicleIsValid as TrainingVehicleIsValid, ObserverInTeamIsValid as ObserverInTeamIsValid
from gui.prb_control.settings import PREBATTLE_ROSTER as PREBATTLE_ROSTER, PREBATTLE_RESTRICTION as PREBATTLE_RESTRICTION
from items.vehicles import getVehicleType as getVehicleType
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

class MaxPlayersNumber(ITeamLimit):
    def check(self, rosters, team, teamLimits):
        ...
    def __getPlayerRolesNumber(self, teamInfo):
        ...

class Comp7TrainingVehicleLimits(TrainingVehicleIsValid):
    __comp7Controller: Any
    def check(self, teamLimits):
        ...

class Comp7TrainingLimits(LimitsCollection):
    def __init__(self, entity):
        ...
