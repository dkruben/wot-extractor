# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/w2gt/w2gt_plugin.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import enum as enum
from collections import defaultdict as defaultdict
from collections import namedtuple as namedtuple
import typing as typing
import BigWorld as BigWorld
import Math as Math
from Event import Event as Event, EventManager as EventManager
from account_helpers.settings_core.settings_constants import GAME as GAME
from chat_commands_consts import MarkerType as MarkerType
from constants import ARENA_PERIOD as ARENA_PERIOD, W2GT_STAGES as W2GT_STAGES
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.controllers.w2gt.w2gt_helper import isPointInsidePolygonByRayTracing as isPointInsidePolygonByRayTracing
from gui.shared.utils.scheduled_notifications import SimpleNotifier as SimpleNotifier
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from typing import Optional as Optional, List as List, Dict as Dict, Callable as Callable
from gui.battle_control.controllers.w2gt.w2gt_data_mgr import W2GTDataMgr as W2GTDataMgr
from helpers.server_settings import _W2GTConfig as _W2GTConfig
_CALL_INTERVAL = 0.5
_W2GT_BATTLE_ZONE_TYPE = 'W2GT_BATTLE_ZONE'
_STAGE_MAP: dict
_SUB_PLUGINS: dict
_ARENA_PERIOD_TO_STAGE: dict

class STAGE(enum.IntEnum):
    WAITING = 0
    ONGOING = 1
    ARRIVAL = 2
    FINISHED = 3
    @classmethod
    def hasValue(cls, value):
        ...

# base nao representavel no stub: namedtuple(...)
class _StageData:
    def __new__(cls, **kwargs):
        ...
    def getCtx(self, name):
        ...
    def passedTime(self):
        ...
    def getNextStageStartTime(self, stageTimeLimit):
        ...

class _SubPlugin(object):
    _STAGE = STAGE.WAITING
    _NEXT_STAGE = STAGE.FINISHED
    __settingsCore: Any
    __eManager: Any
    onStageChanged: Any
    onReadyToDestroy: Any
    _permanentPlugin: Any
    _isReadyToDestroy: Any
    _isDestroyed: Any
    __stage: Any
    __stageData: Any
    __dataMgr: Any
    __durationCallbackID: Any
    __isActive: Any
    def __init__(self, permanentPlugin):
        ...
    @property
    def dataMgr(self):
        ...
    @property
    def stage(self):
        ...
    @property
    def isActive(self):
        ...
    @isActive.setter
    def isActive(self, value):
        ...
    @property
    def isReadyToDestroy(self):
        ...
    @property
    def config(self):
        ...
    def initialize(self, period, dataMgr, stageData):
        ...
    def updateStage(self, period, stage):
        ...
    def update(self):
        ...
    def canDestroy(self):
        ...
    def beforeDestroy(self):
        ...
    def destroy(self):
        ...
    @property
    def _ownVehicle(self):
        ...
    @property
    def _ownPosition(self):
        ...
    @property
    def _isEnabled(self):
        ...
    def _onEnableChanged(self, isEnabled):
        ...
    def _getActionTime(self):
        ...
    def _preInitialize(self, dataMgr, stageData):
        ...
    def _onActivate(self):
        ...
    def _update(self):
        ...
    def _finishStage(self):
        ...
    def _buildExitContext(self, nextStage):
        ...
    def _getNextStage(self):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def __activate(self, period):
        ...
    def __inactivate(self):
        ...
    def __runStageCooldown(self):
        ...
    def __clearDurationCallback(self):
        ...

class _SubPluginOngoing(_SubPlugin):
    _STAGE = STAGE.ONGOING
    _NEXT_STAGE = STAGE.ARRIVAL
    __selectedZoneID: Any
    def __init__(self, permanentPlugin):
        ...
    def _update(self):
        ...
    def _finishStage(self):
        ...
    def _buildExitContext(self, nextStage):
        ...

class _SubPluginArrival(_SubPlugin):
    _STAGE = STAGE.ARRIVAL
    _NEXT_STAGE = STAGE.FINISHED
    __selectedZoneID: Any
    def __init__(self, permanentPlugin):
        ...
    def _preInitialize(self, dataMgr, stageData):
        ...
    def _buildExitContext(self, nextStage):
        ...

class _PermanentPlugin(object):
    __sessionProvider: Any
    __settingsCore: Any
    __dataMgr: Any
    __stage: Any
    __zonesPinsIDs: Any
    __isRandomEventActive: Any
    def __init__(self):
        ...
    @property
    def _isEnabled(self):
        ...
    def initialize(self, dataMgr):
        ...
    def clear(self):
        ...
    def updateStage(self, stage):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def __onRandomEventStarted(self, zoneMarker, matrix):
        ...
    def __onEnableChanged(self):
        ...
    def __updateZones(self):
        ...
    def __initializeGui(self):
        ...
    def __finishGui(self):
        ...
    def __getComponent(self, zoneMarkerID, bcMarkerType):
        ...

class W2GTPlugin(object):
    __period: Any
    __periodStartTime: Any
    __stage: Any
    __subPlugin: Any
    __permanentPlugin: Any
    __dataMgr: Any
    __waitDestroying: Any
    __notifier: Any
    __eManager: Any
    onStagePluginChanged: Any
    def __init__(self):
        ...
    def initialize(self, dataMgr, period, periodStartTime):
        ...
    def updatePeriod(self, period):
        ...
    def setDestroyed(self):
        ...
    def clear(self):
        ...
    def __setupStage(self, period):
        ...
    def __getInitialStage(self, period):
        ...
    def __updateStage(self, stageData):
        ...
    def __changeSubPlugin(self, period, stageData):
        ...
    def __addSubPlugin(self, subPluginCls, period, stageData):
        ...
    def __removeSubPlugin(self, force=False):
        ...
    def __updateSubPlugin(self, period, stageData):
        ...
    def __notify(self):
        ...
    def __destroyWaitedSubPlugins(self):
        ...
    def __onSubPluginStageChanged(self, stage, ctx, startTime=0):
        ...
