# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/HangarSpace.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from queue import Queue as Queue
from functools import wraps as wraps, partial as partial
import BigWorld as BigWorld
import Math as Math
import CGF as CGF
import Event as Event
import Keys as Keys
import ResMgr as ResMgr
import constants as constants
from debug_utils import LOG_DEBUG as LOG_DEBUG
from PlayerEvents import g_playerEvents as g_playerEvents
from gui import g_mouseEventHandlers as g_mouseEventHandlers, InputHandler as InputHandler
from gui.ClientHangarSpace import ClientHangarSpace as ClientHangarSpace
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.game_loading.resources.consts import Milestones as Milestones
from helpers import dependency as dependency, uniprof as uniprof
from helpers.statistics import HANGAR_LOADING_STATE as HANGAR_LOADING_STATE
from MemoryCriticalController import g_critMemHandler as g_critMemHandler
from shared_utils import BoundMethodWeakref as BoundMethodWeakref
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import IGameSessionController as IGameSessionController, IIGRController as IIGRController, IHangarSpaceSwitchController as IHangarSpaceSwitchController
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from skeletons.helpers.statistics import IStatisticsCollector as IStatisticsCollector
from gui import g_keyEventHandlers as g_keyEventHandlers
from gui.shared import g_eventBus as g_eventBus, events as events
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
import AvatarInputHandler as AvatarInputHandler
from AvatarInputHandler.VideoCamera import VideoCamera as VideoCamera
from gui.app_loader import settings as app_settings
from gui import GUI_CTRL_MODE_FLAG as _CTRL_FLAG
from gui.hangar_cameras.hangar_camera_common import CameraMovementStates as CameraMovementStates
from uilogging.performance.hangar.loggers import HangarMetricsLogger as HangarMetricsLogger
from uilogging.performance.battle.loggers import BattleMetricsLogger as BattleMetricsLogger
from cgf_components.hangar_camera_manager import HangarCameraSystem as HangarCameraSystem
_Q_CHECK_DELAY = 0.0
g_execute_after_hangar_space_inited: Any

class _execute_after_hangar_space_inited(object):
    hangarSpace: Any
    __slots__: tuple
    __queue: Any
    def __init__(self):
        ...
    def __call__(self, func):
        ...
    def checkConditionForExit(self):
        ...
    def storeData(self, func, *args, **kwargs):
        ...
    def delayCall(self):
        ...

class HangarVideoCameraController(object):
    hangarSpace: Any
    appLoader: Any
    __eventManager: Any
    __videoCamera: Any
    __enabled: Any
    __lastCameraName: Any
    onEnabledChange: Any
    def __init__(self):
        ...
    @property
    def isEnabled(self):
        ...
    def init(self):
        ...
    def destroy(self):
        ...
    def handleKeyEvent(self, event):
        ...
    def __setEnabled(self, enabled):
        ...
    def __enableVideoCamera(self):
        ...
    def __disableVideoCamera(self):
        ...
    def handleMouseEvent(self, event):
        ...

class HangarSpace(IHangarSpace):
    isPremium: Any
    gameSession: Any
    igrCtrl: Any
    statsCollector: Any
    hangarSwitchController: Any
    __space: Any
    __videoCameraController: Any
    __inited: Any
    __spaceInited: Any
    __isModelLoaded: Any
    __isSpacePremium: Any
    __igrSpaceType: Any
    __environment: Any
    __delayedIsPremium: Any
    __delayedForceRefresh: Any
    __delayedRefreshCallback: Any
    __delayedRecreateCallback: Any
    __spaceDestroyedDuringLoad: Any
    __lastUpdatedVehicle: Any
    __vehicleUpdateRequested: Any
    __logStatisticsPostponed: Any
    __selectableVehicleFlags: Any
    onSpaceRefresh: Any
    onSpaceRefreshCompleted: Any
    onSpaceCreating: Any
    onSpaceCreate: Any
    onSpaceDestroy: Any
    onSpaceChanged: Any
    onMouseEnter: Any
    onMouseExit: Any
    onMouseDown: Any
    onMouseUp: Any
    onHeroTankReady: Any
    onVehicleChanged: Any
    onVehicleChangeStarted: Any
    onSpaceChangedByAction: Any
    onNotifyCursorOver3dScene: Any
    __isCursorOver3DScene: Any
    __isSelectionEnabledCounter: Any
    __selectionLocks: Any
    _performanceMetricsLogger: Any
    _statisticsLogger: Any
    def __init__(self):
        ...
    @property
    def videoCameraController(self):
        ...
    @property
    def space(self):
        ...
    @property
    def spaceID(self):
        ...
    @property
    def inited(self):
        ...
    @property
    def spaceInited(self):
        ...
    @property
    def isCursorOver3DScene(self):
        ...
    @property
    def isSelectionEnabled(self):
        ...
    @property
    def isModelLoaded(self):
        ...
    @property
    def spacePath(self):
        ...
    @property
    def visibilityMask(self):
        ...
    def spaceLoading(self):
        ...
    def getAnchorParams(self, slotId, areaId, regionId):
        ...
    def updateAnchorsParams(self, *args):
        ...
    def setSelectionEnabled(self, enabled):
        ...
    def setEnvironment(self, environment):
        ...
    def __onNotifyCursorOver3dScene(self, event):
        ...
    # decorador original: @uniprof.regionDecorator(...)
    def init(self, isPremium):
        ...
    def refreshSpace(self, isPremium, forceRefresh=False):
        ...
    def destroy(self):
        ...
    # decorador original: @g_execute_after_hangar_space_inited
    # decorador original: @uniprof.regionDecorator(...)
    def updateVehicle(self, vehicle, outfit=None):
        ...
    def startToUpdateVehicle(self, vehicle, outfit=None):
        ...
    def updateVehicleDescriptor(self, descr):
        ...
    def __handleKeyEvent(self, event):
        ...
    # decorador original: @g_execute_after_hangar_space_inited
    def updatePreviewVehicle(self, vehicle, outfit=None, showWaitingBg=True):
        ...
    def getVehicleEntity(self):
        ...
    def getVehicleEntityAppearance(self):
        ...
    def updateVehicleOutfit(self, outfit):
        ...
    def getCentralPointForArea(self, areaID):
        ...
    # decorador original: @g_execute_after_hangar_space_inited
    def removeVehicle(self):
        ...
    def lockVehicleSelectable(self, consumer):
        ...
    def unlockVehicleSelectable(self, consumer):
        ...
    def onPremiumChanged(self, isPremium, attrs, premiumExpiryTime):
        ...
    def resetLastUpdatedVehicle(self):
        ...
    # decorador original: @uniprof.regionDecorator(...)
    def __spaceDone(self):
        ...
    # decorador original: @uniprof.regionDecorator(...)
    def _changeDone(self):
        ...
    def __unlockVehicleOnDel(self, consumer):
        ...
    def __logStatistics(self):
        ...
    def __delayedRefresh(self):
        ...
    def __delayedRecreate(self, descriptor, modelState, outfit):
        ...
