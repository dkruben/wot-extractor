# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/training/legacy/limits.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import PREBATTLE_ACCOUNT_STATE as PREBATTLE_ACCOUNT_STATE, PREBATTLE_TYPE as PREBATTLE_TYPE
from gui.prb_control.entities.base.limits import AbstractTeamIsValid as AbstractTeamIsValid, LimitsCollection as LimitsCollection, VehicleIsValid as VehicleIsValid, TeamNoPlayersInBattle as TeamNoPlayersInBattle, TeamIsValid as TeamIsValid, TeamAllPlayersReady as TeamAllPlayersReady
from gui.prb_control.settings import PREBATTLE_RESTRICTION as PREBATTLE_RESTRICTION
from helpers import dependency as dependency
from items import vehicles as vehicles
from skeletons.gui.shared import IItemsCache as IItemsCache

class ObserverInTeamIsValid(AbstractTeamIsValid):
    itemsCache: Any
    def check(self, rosters, team, teamLimits):
        ...
    @classmethod
    def __isAllObservers(cls, accountsInfo):
        ...

class TrainingVehicleIsValid(VehicleIsValid):
    def check(self, teamLimits):
        ...

class TrainingLimits(LimitsCollection):
    def __init__(self, entity):
        ...
