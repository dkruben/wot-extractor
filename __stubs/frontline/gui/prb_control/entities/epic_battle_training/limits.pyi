# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/prb_control/entities/epic_battle_training/limits.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import PREBATTLE_ACCOUNT_STATE as PREBATTLE_ACCOUNT_STATE, PREBATTLE_TYPE as PREBATTLE_TYPE
from gui.Scaleform.daapi.view.lobby.epicBattle.epic_helpers import isVehLevelUnlockableInBattle as isVehLevelUnlockableInBattle
from gui.prb_control.entities.base.limits import AbstractTeamIsValid as AbstractTeamIsValid, LimitsCollection as LimitsCollection, VehicleIsValid as VehicleIsValid, TeamNoPlayersInBattle as TeamNoPlayersInBattle, TeamIsValid as TeamIsValid
from gui.prb_control.settings import PREBATTLE_RESTRICTION as PREBATTLE_RESTRICTION
from skeletons.gui.shared import IItemsCache as IItemsCache
from helpers import dependency as dependency
from items import vehicles as vehicles

class ObserverInTeamIsValid(AbstractTeamIsValid):
    itemsCache: Any
    def check(self, rosters, team, teamLimits):
        ...
    @classmethod
    def __isAllObservers(cls, accountsInfo):
        ...

class EpicVehicleIsValid(VehicleIsValid):
    def check(self, teamLimits):
        ...

class EpicBattleTrainingLimits(LimitsCollection):
    def __init__(self, entity):
        ...
