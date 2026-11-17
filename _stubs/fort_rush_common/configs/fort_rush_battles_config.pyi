# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/common/fort_rush_common/configs/fort_rush_battles_config.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL, MIN_VEHICLE_LEVEL as MIN_VEHICLE_LEVEL, VEHICLE_CLASS as VEHICLE_CLASS
from dict2model import models as models, schemas as schemas, fields as fields, validate as validate
from fort_rush_common.fort_rush_constants import EXT_GAME_PARAMS_KEY as EXT_GAME_PARAMS_KEY
from game_params_common.schema import GameParamsSchema as GameParamsSchema
from game_params_common.scope import GameParamsScopeFlags as GameParamsScopeFlags
from typing import List as List
from Arena import Arena as Arena
_VEHICLE_CLASSES: tuple
_DEFAULT_MODE_SELECTOR_COLUMN = 1
_DEFAULT_MODE_SELECTOR_PRIORITY = 40
_stageSchema: Any
_progressionSchema: Any
_dailyMissionsConfigSchema: Any
_awardsByPlaceSchema: Any
_battleEconomySchema: Any
_controllableZonesSchema: Any
_squadTagRestrictionSchema: Any
_squadRestrictionsSchema: Any
_battleSchema: Any
fortRushBattlesConfigGameParamsSchema: Any

class StageModel(models.Model):
    __slots__: tuple
    quest: Any
    level: Any
    def __init__(self, quest, level):
        ...

class ProgressionModel(models.Model):
    __slots__: tuple
    stage: Any
    def __init__(self, stage):
        ...

class DailyMissionsConfigModel(models.Model):
    __slots__: tuple
    dailyMissionQuestPrefix: Any
    hardDailyMissionQuestPrefix: Any
    dailyMissionTokenPrefix: Any
    dailyMissionTokenPostfix: Any
    dailyMissionTokenTtl: Any
    tokenLimit: Any
    dailyGroupsCount: Any
    dailyQuestMaxDays: Any
    def __init__(self, dailyMissionQuestPrefix, hardDailyMissionQuestPrefix, dailyMissionTokenPrefix, dailyMissionTokenPostfix, dailyMissionTokenTtl, tokenLimit, dailyGroupsCount, dailyQuestMaxDays):
        ...

class _AwardsByPlace(models.Model):
    __slots__: tuple
    win: Any
    loss: Any
    draw: Any
    def __init__(self, win, loss, draw):
        ...
    def getAwardForWin(self, place):
        ...
    def getAwardForLoss(self, place):
        ...
    def getAwardForDraw(self, place):
        ...
    @classmethod
    def _getPointsByPlace(cls, place, pointsList):
        ...

class _BattleEconomyModel(models.Model):
    __slots__: tuple
    creditsByPlace: Any
    progressionPointsByPlace: Any
    def __init__(self, creditsByPlace, progressionPointsByPlace):
        ...

class ControllableZonesModel(models.Model):
    __slots__: tuple
    owned2NeutralTime: Any
    neutral2OwnedTime: Any
    progressResetFactor: Any
    maxHealthHealPercentage: Any
    autoSpotDelaySeconds: Any
    def __init__(self, owned2NeutralTime, neutral2OwnedTime, progressResetFactor, maxHealthHealPercentage, autoSpotDelaySeconds):
        ...

class BattleModel(models.Model):
    __slots__: tuple
    controllableZones: Any
    def __init__(self, controllableZones):
        ...

class SquadTagRestrictionModel(models.Model):
    __slots__: tuple
    maxCount: Any
    levels: Any
    def __init__(self, maxCount, levels):
        ...

class SquadRestrictionsModel(models.Model):
    __slots__: tuple
    tags: Any
    def __init__(self, tags):
        ...
    def toPlatoonRestrictionsDict(self):
        ...

class FortRushBattlesConfigModel(models.Model):
    __slots__: tuple
    modeSelectorCardColumn: Any
    modeSelectorCardPriority: Any
    isEnabled: Any
    technicalPause: Any
    startDatetime: Any
    endDatetime: Any
    isInfoPageEnabled: Any
    baseProgressionToken: Any
    completedProgressionToken: Any
    progressionQuestPrefix: Any
    maxRewardsAmountPerStage: Any
    progression: Any
    dailyMissionsConfig: Any
    battleEconomy: Any
    eligibleVehicleTiers: Any
    forbiddenVehClasses: Any
    squadRestrictions: Any
    battle: Any
    def __init__(self, modeSelectorCardColumn, modeSelectorCardPriority, isEnabled, technicalPause, startDatetime, endDatetime, isInfoPageEnabled, baseProgressionToken, completedProgressionToken, progressionQuestPrefix, maxRewardsAmountPerStage, progression, dailyMissionsConfig, battleEconomy, eligibleVehicleTiers, forbiddenVehClasses, squadRestrictions, battle):
        ...

def _createAwardsForPlaceList():
    ...
def getControllableZonesConfig(arena):
    ...
