# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/stats_display_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import math as math
import typing as typing
import BigWorld as BigWorld
import CGF as CGF
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS
from gui.shared.vehicle_stats_helper import getStatTrackersVehicleStats as getStatTrackersVehicleStats
from items.components.c11n_components import adjustToAllowedStatTrackerNumber as adjustToAllowedStatTrackerNumber
from items.components.c11n_constants import StatTrackerStatistic as StatTrackerStatistic
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from PlayerEvents import g_playerEvents as g_playerEvents
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from helpers import dependency as dependency, isPlayerAccount as isPlayerAccount, isPlayerAvatar as isPlayerAvatar, isPlayerExist as isPlayerExist
from GenericComponents import AnimatorComponent as AnimatorComponent, DecalComponent as DecalComponent
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from vehicle_systems.vehicle_composition import findParentVehicle as findParentVehicle
from typing import Optional as Optional
_logger: Any
MAGNITUDE_SYMBOL_LIST: list
OVERFLOW_SYMBOL = '!'

# decorador original: @registerComponent
class StatisticDisplayComponent(object):
    editorTitle = 'Statistic Display'
    domain = CGF.Domain.Client
    delayList: Any
    trackedStatistic: Any
    cachedValue: Any
    def __init__(self):
        ...

class DelayDisplayUpdater(object):
    symbolsList: Any
    time: Any
    updatedIndexes: Any
    def __init__(self, symbolsList):
        ...

class TrackedStatisticComponentSystem(CGF.System):
    StatisticActivated: Any
    StatisticsIterate: Any
    StatisticsUpdateIterate: Any
    AnimatorAccess: Any
    Reactions: Any
    __sessionProvider: Any
    __hangarSpace: Any
    __availableStats: tuple
    def onMappingLoaded(self):
        ...
    def onMappingUnloaded(self):
        ...
    def update(self):
        ...
    @staticmethod
    def updateCounterValue(value, statisticDisplay, decalComponent, animatorCtx=None):
        ...
    def __onAvatarReady(self):
        ...
    def __onDossierResync(self, *_):
        ...
    def __onVehicleStatisticsUpdate(self, vehicleID):
        ...
    def __inBattleUpdate(self, statisticDisplay, vehicle, decalComponent, animatorCtx=None):
        ...
    def __hangarUpdate(self, statisticDisplay, vehicle, decalComponent):
        ...

def vehicleKillsStatsGetter(vehicle, arenaDP):
    ...
def roundDown(value, digitAfterDecimal):
    ...
def numberStatsFormatter(value, digitLimit):
    ...
def displaySymbolsIterator(formattedNum):
    ...
def _isAvatarReady():
    ...
