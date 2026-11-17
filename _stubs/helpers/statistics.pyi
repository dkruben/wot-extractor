# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/statistics.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import ResMgr as ResMgr
import Settings as Settings
import Sound as Sound
from constants import ARENA_PERIOD as ARENA_PERIOD, INVALID_CLIENT_STATS as INVALID_CLIENT_STATS
from account_helpers.settings_core.settings_constants import GRAPHICS as GRAPHICS, SOUND as SOUND, SoundPhysicsQuality as SoundPhysicsQuality
from gui.shared.utils.graphics import getGraphicsEngineValue as getGraphicsEngineValue
from gui.shared.utils import monitor_settings as monitor_settings
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_NOTE as LOG_NOTE
from helpers import dependency as dependency, isPlayerAvatar as isPlayerAvatar
from math_common import round_py2_style_int as round_py2_style_int
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import IGameSessionController as IGameSessionController
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from skeletons.helpers.statistics import IStatisticsCollector as IStatisticsCollector
from uilogging.helpers import getClientPeripheryID as getClientPeripheryID
STATISTICS_VERSION = '0.0.2'
_OLD_CUSTOM_PRESET_IDX = 6
_NEW_CUSTOM_PRESET_IDX = 5
_HANGAR_LOADING_STATES_PREFIX = 'HANGAR LOADING STATE'
_HANGAR_LOADING_STATES: list
_HANGAR_LOADING_STATES_IDS: list
_IMPORTANT_GRAPHICS_SETTINGS_SET: set
_OTHER_GRAPHICS_SETTINGS_SET: set
_VIDEO_MODE_SIZE_CHANGE_SET: set

class _STATISTICS_STATE(object):
    STARTED = 0
    IN_PROGRESS = 1
    STOPPED = 2

class HARDWARE_SCORE_PARAMS(object):
    PARAM_GPU_MEMORY = 0
    PARAM_GPU_SHARED = 1
    PARAM_GPU_SCORE = 2
    PARAM_CPU_SCORE = 3
    PARAM_CPU_CORES = 4
    PARAM_RAM = 5
    PARAM_VIRTUAL_MEMORY = 6
    MAX_PARAMS = 7

class HANGAR_LOADING_STATE(object):
    LOGIN = 0
    CONNECTED = 1
    SHOW_GUI = 2
    QUESTS_SYNC = 3
    USER_SERVER_SETTINGS_SYNC = 4
    START_LOADING_SPACE = 5
    START_LOADING_VEHICLE = 6
    FINISH_LOADING_VEHICLE = 7
    FINISH_LOADING_SPACE = 8
    HANGAR_UI_READY = 9
    TRAINING_UI_READY = 10
    HANGAR_READY = 11
    START_LOADING_TUTORIAL = 12
    FINISH_LOADING_TUTORIAL = 13
    DISCONNECTED = 14
    COUNT = 15

class StatisticsCollector(IStatisticsCollector):
    update: Any
    sessionProvider: Any
    settingsCore: Any
    connectionMgr: Any
    hangarSpace: Any
    gameSession: Any
    __state: Any
    __hangarLoaded: Any
    __invalidStats: Any
    __dynEvents: Any
    __needCollectSystemData: Any
    __needCollectSessionData: Any
    __hangarWasLoadedOnce: Any
    __sendFullStat: Any
    __loadingStates: Any
    __loadingInitialState: Any
    __hangarLoadingTime: Any
    __lastArenaUniqueID: Any
    __lastArenaTypeID: Any
    __lastArenaTeam: Any
    __randomEvents: Any
    __blArenaPeriod: Any
    __updateFunc: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def reset(self):
        ...
    def needCollectSystemData(self, value):
        ...
    def needCollectSessionData(self, value):
        ...
    def getSessionData(self):
        ...
    def getStatistics(self, andStop=True):
        ...
    def noteLastArenaData(self, arenaTypeID, arenaUniqueID, arenaTeam, randomEvents, blArenaPeriod):
        ...
    def noteHangarLoadingState(self, state, initialState=False, showSummaryNow=False):
        ...
    def __getSessionData(self, statisticsDict):
        ...
    def __getSystemData(self, statisticsDict):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def __onHangarSpaceLoaded(self):
        ...
    def __onClientDisconnected(self):
        ...
    def __onDRRChanged(self):
        ...
    def __updateIdle(self):
        ...
    def __updatePrebattle(self):
        ...
    def __updateBattle(self):
        ...
    def __getPresetIdx(self):
        ...
