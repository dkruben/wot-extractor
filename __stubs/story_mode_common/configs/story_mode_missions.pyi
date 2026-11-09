# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/common/story_mode_common/configs/story_mode_missions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import datetime as datetime
import typing as typing
from game_params_common.base_manager import GameParamsSchema as GameParamsSchema
from constants import ARENA_BONUS_TYPE_NAMES as ARENA_BONUS_TYPE_NAMES
from dict2model import models as models, schemas as schemas, fields as fields, validate as validate, exceptions as exceptions
from game_params_common.scope import GameParamsScopeFlags as GameParamsScopeFlags
from items import vehicles as vehicles
from story_mode_common.configs.task_conditions import TaskConditionType as TaskConditionType
from story_mode_common.configs.sounds_schema import SoundSchema as SoundSchema
from story_mode_common.helpers import isMissionCompleted as isMissionCompleted
from story_mode_common.story_mode_constants import STORY_MODE_BONUS_TYPES as STORY_MODE_BONUS_TYPES, TaskId as TaskId, MissionId as MissionId, MissionsDifficulty as MissionsDifficulty, MissionType as MissionType, MissionLockCondition as MissionLockCondition
from dict2model.types import ValidatorsType as ValidatorsType, TFilterParams as TFilterParams, TFilter as TFilter
from dict2model.schemas import SchemaModelType as SchemaModelType, TRawData as TRawData
from story_mode_common.configs.sounds_schema import SoundModel as SoundModel
_logger: Any
EVENT_MISSION_MIN_ID = 1000
lockByMissionSchema: Any
battlesCountLockSchema: Any
vehicleSchema: Any
_autoCompleteTaskSchema: Any
_missionTaskSchema: Any
_missionDisabledTimerSchema: Any
missionSoundSchema: Any
missionLockerSchema: Any
_soundsSchema: Any
missionSchema: Any
onboardingSchema: Any
missionsSchema: Any

class VehicleModel(models.Model):
    __slots__: tuple
    name: Any
    styleId: Any
    equipments: Any
    def __init__(self, name, styleId, equipments):
        ...
    def getEquipmentsSetup(self):
        ...

class AutoCompleteTaskModel(models.Model):
    __slots__: tuple
    missionId: Any
    taskId: Any
    giveReward: Any
    def __init__(self, missionId, taskId, giveReward):
        ...

class MissionTaskModel(models.Model):
    __slots__: tuple
    id: Any
    reward: Any
    autoCompleteTasks: Any
    unlockDate: Any
    conditions: Any
    def __init__(self, id, reward, autoCompleteTasks, unlockDate, conditions):
        ...
    def getCondition(self, name):
        ...
    def isLocked(self):
        ...

class MissionDisabledTimerModel(models.Model):
    __slots__: tuple
    showAt: Any
    endAt: Any
    def __init__(self, showAt, endAt):
        ...

class SoundsModel(models.Model):
    __slots__: tuple
    music: Any
    ambience: Any
    battleMusic: Any
    def __init__(self, music, ambience, battleMusic):
        ...

class LockByMissionModel(models.Model):
    __slots__: tuple
    missionId: Any
    def __init__(self, missionId):
        ...
    def getLockReason(self, progress):
        ...

class BattlesCountLockModel(models.Model):
    __slots__: tuple
    battlesCount: Any
    def __init__(self, battlesCount):
        ...
    def getLockReason(self, battlesCount):
        ...

class MissionLockerModel(models.Model):
    __slots__: tuple
    active: Any
    byMission: Any
    battlesCount: Any
    def __init__(self, active, byMission=None, battlesCount=None):
        ...
    def getLockReason(self, progress, battlesCount):
        ...

class MissionModel(models.Model):
    __slots__: tuple
    missionId: Any
    vehicle: Any
    geometry: Any
    bonusType: Any
    displayName: Any
    missionType: Any
    difficulty: Any
    sounds: Any
    tasks: Any
    enabled: Any
    disabledTimer: Any
    reward: Any
    showRewardInBattleResults: Any
    newbieBattlesMin: Any
    newbieBattlesMax: Any
    spawnGroup: Any
    hasOutroVideo: Any
    switchVehicles: Any
    missionLocker: Any
    def __init__(self, missionId, vehicle, geometry, bonusType, displayName, missionType, difficulty, sounds, tasks, enabled, disabledTimer, reward, showRewardInBattleResults, newbieBattlesMin, newbieBattlesMax, spawnGroup, hasOutroVideo, switchVehicles, missionLocker):
        ...
    def getSwitchVehicles(self, withDefaultVehicle=True):
        ...
    def getTask(self, taskId):
        ...
    def getTasksReward(self, tasksIds=None, isBattlePassActive=True):
        ...
    def getMissionReward(self, forBattleResults=False):
        ...
    def getUnlockedTasks(self):
        ...
    @property
    def isEvent(self):
        ...
    def getTaskConditionValues(self):
        ...
    def getLockReason(self, progress, battlesCount):
        ...
    def getBattlesToUnlock(self, battlesCount):
        ...

class OnboardingModel(models.Model):
    __slots__: tuple
    reward: Any
    def __init__(self, reward):
        ...

class MissionsModel(models.Model):
    __slots__: tuple
    missions: Any
    onboarding: Any
    _missionsById: Any
    _regularMissions: Any
    _eventMissions: Any
    _lastMissionId: Any
    def __init__(self, missions, onboarding):
        ...
    @property
    def onboardingLastMissionId(self):
        ...
    def isOnboarding(self, missionId):
        ...
    def isEvent(self, missionId):
        ...
    def getMission(self, missionId):
        ...
    def filter(self, enabled=None, missionType=None):
        ...
    @property
    def isEventEnabled(self):
        ...

class ValidateMissionIds(validate.IterableOfSequential):
    __slots__: tuple
    def __init__(self):
        ...
    def __call__(self, mission, *args, **kwargs):
        ...

class ValidateLockingMission(validate.IterableValidator):
    __slots__: tuple
    def __call__(self, mission, storage, *args, **kwargs):
        ...
    def createStorage(self):
        ...

class ValidateAutoCompleteTasks(validate.IterableValidator):
    __slots__: tuple
    def __call__(self, mission, storage, lastIteration, *args, **kwargs):
        ...
    def createStorage(self):
        ...

class _RewardField(fields.Field):
    def __init__(self, required=True, default=..., filterParams=None, serializedValidators=None, deserializedValidators=None):
        ...
    def _deserialize(self, incoming, **kwargs):
        ...

class ConditionModel(models.Model):
    __slots__: tuple
    name: Any
    value: Any
    type: Any
    def __init__(self, name, value, type):
        ...

class TaskConditionSchema(schemas.Schema):
    def __init__(self):
        ...
    def _deserialize(self, incoming, filter_=None, skipValidation=False, **kwargs):
        ...
    def serialize(self, incoming, filter_=None, silent=False, logError=True, skipValidation=False, **kwargs):
        ...

def validateBonusType(bonusType):
    ...
def _validateShowRewardHasReward(model):
    ...
def _validateMissionDisabledTimer(model):
    ...
def _validateMissionLockers(lockerModel):
    ...
def _getRewardReaders(*args, **kwargs):
    ...
