# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/game_control/ls_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems
import CGF as CGF
import Event as Event
import WWISE as WWISE
import adisp as adisp
from cgf_components.hangar_camera_manager import HangarCameraSystem as HangarCameraSystem
from skeletons.gui.shared import IItemsCache as IItemsCache
from frameworks.wulf import WindowLayer as WindowLayer
from gui import SystemMessages as SystemMessages
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.game_control.season_provider import SeasonProvider as SeasonProvider
from gui.prb_control import prbEntityProperty as prbEntityProperty
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.shared.utils.scheduled_notifications import Notifiable as Notifiable, SimpleNotifier as SimpleNotifier
from gui.shared import events as events, g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showHangar as showMainHangar
from last_stand.gui.shared.event_dispatcher import closeViewsByID as closeViewsByID, showHangar as showHangar
from last_stand.gui.shared.utils.performance_analyzer import PerformanceAnalyzerMixin as PerformanceAnalyzerMixin
from last_stand.gui.shared.event_dispatcher import showPromoWindowView as showPromoWindowView
from last_stand.gui.sounds.sound_constants import LS_SOUND_REMAPPING as LS_SOUND_REMAPPING
from helpers import dependency as dependency, time_utils as time_utils
from last_stand_common.last_stand_constants import QUEUE_TYPE as QUEUE_TYPE, PREBATTLE_TYPE as PREBATTLE_TYPE, FORBIDDEN_VEHICLE_TAGS as FORBIDDEN_VEHICLE_TAGS
from last_stand.gui.ls_gui_constants import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, QUEUE_TYPE_TO_DIFFICULTY_LEVEL as QUEUE_TYPE_TO_DIFFICULTY_LEVEL
from last_stand.skeletons.ls_controller import ILSController as ILSController
from last_stand_common.last_stand_constants import LAST_STAND_GAME_PARAMS_KEY as LAST_STAND_GAME_PARAMS_KEY
from shared_utils import makeTupleByDict as makeTupleByDict
from skeletons.gui.game_control import IReferralProgramController as IReferralProgramController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.game_control import IHangarLoadingController as IHangarLoadingController
from skeletons.gui.game_control import ILimitedUIController as ILimitedUIController
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from skeletons.gui.game_control import ILootBoxSystemController as ILootBoxSystemController
_VehiclesConfig: Any

# base nao representavel no stub: namedtuple(...)
class _LSConfig:
    __slots__: tuple
    def __new__(cls, **kwargs):
        ...
    def asDict(self):
        ...
    def replace(self, data):
        ...
    @classmethod
    def defaults(cls):
        ...

class LSController(ILSController, Notifiable, SeasonProvider, IGlobalListener, PerformanceAnalyzerMixin):
    __lobbyContext: Any
    __itemsCache: Any
    __hangarLoadingController: Any
    __referralCtrl: Any
    __limitedUIController: Any
    __hangarSpace: Any
    __lootBoxes: Any
    __serverSettings: Any
    _prevStates: Any
    onEventDisabled: Any
    onSettingsUpdate: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def onDisconnected(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onLobbyStarted(self, ctx):
        ...
    def onLobbyInited(self, event):
        ...
    def onPrbEntitySwitched(self):
        ...
    @property
    def lootBoxesEvent(self):
        ...
    def isEnabled(self):
        ...
    def isBattlesEnabled(self):
        ...
    def isPromoScreenEnabled(self):
        ...
    def isIntroVideoEnabled(self):
        ...
    def isInfoPageEnabled(self):
        ...
    def isMetaInfoEnabled(self):
        ...
    def isLootBoxEntryPointEnabled(self):
        ...
    def isHangar3dPointVisible(self):
        ...
    def isHangar3dPointRewardVisible(self):
        ...
    def isParallaxEnabled(self):
        ...
    def isAvailable(self):
        ...
    def getConfig(self):
        ...
    def getModeSettings(self):
        ...
    def selectBattle(self):
        ...
    def openHangar(self):
        ...
    def isEventPrb(self):
        ...
    def selectRandomMode(self):
        ...
    # decorador original: @prbEntityProperty
    def prbEntity(self):
        ...
    def getVehiclesConfig(self):
        ...
    def getSuitableVehicles(self, criteria=None):
        ...
    def getVehiclesCriteria(self):
        ...
    def __onServerSettingsChanged(self, serverSettings):
        ...
    def __onHangarLoadedAfterLogin(self):
        ...
    def __updateLastStandSettings(self, diff):
        ...
    def __updateStates(self):
        ...
    def __clear(self):
        ...
    def __getTimer(self):
        ...
    def __timerUpdate(self):
        ...
    def __closeLSViews(self):
        ...
    def __onSelectVehicleInHangar(self, event):
        ...
    # decorador original: @adisp.adisp_process
    def __selectMode(self, name):
        ...
    @staticmethod
    def __getQueueTypeLocalizedName(queueType):
        ...
