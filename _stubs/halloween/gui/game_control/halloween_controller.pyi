# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/game_control/halloween_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import CGF as CGF
import typing as typing
from account_helpers.AccountSettings import CURRENT_VEHICLE as CURRENT_VEHICLE
import Event as Event
import adisp as adisp
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from account_helpers import AccountSettings as AccountSettings
from cgf_components.hangar_camera_manager import HangarCameraSystem as HangarCameraSystem
from constants import EVENT_CLIENT_DATA as EVENT_CLIENT_DATA
from frameworks.wulf import WindowLayer as WindowLayer
from gui import SystemMessages as SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.game_control.season_provider import SeasonProvider as SeasonProvider
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.prb_control import prbEntityProperty as prbEntityProperty
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared import events as events, g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showHangar as showMainHangar
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from gui.shared.system_factory import collectIgnoredModeForAutoSelectVehicle as collectIgnoredModeForAutoSelectVehicle
from gui.shared.utils.scheduled_notifications import Notifiable as Notifiable, SimpleNotifier as SimpleNotifier
from halloween.gui.halloween_gui_constants import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, QUEUE_TYPE_TO_DIFFICULTY_LEVEL as QUEUE_TYPE_TO_DIFFICULTY_LEVEL
from halloween.gui.prb_control.entities.pre_queue.entity import HalloweenEntity as HalloweenEntity
from halloween.gui.prb_control.entities.squad.entity import HalloweenSquadEntity as HalloweenSquadEntity
from halloween.gui.shared.event_dispatcher import closeViewsByID as closeViewsByID, showHangar as showHangar
from halloween.gui.shared.event_dispatcher import showPromoWindowView as showPromoWindowView
from halloween.gui.shared.utils.performance_analyzer import PerformanceAnalyzerMixin as PerformanceAnalyzerMixin
from halloween.skeletons.difficulty_level_controller import IDifficultyLevelController as IDifficultyLevelController
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from halloween.uilogging.loggers import HWMetricsLogger as HWMetricsLogger
from halloween.uilogging.logging_constants import HWLogKeys as HWLogKeys
from halloween_common.configs.halloween_gsw import GSWSchema as GSWSchema
from halloween_common.halloween_constants import HALLOWEEN_GAME_PARAMS_KEY as HALLOWEEN_GAME_PARAMS_KEY
from halloween_common.halloween_constants import HALLOWEEN_QUESTS_PREFFIX as HALLOWEEN_QUESTS_PREFFIX, QUEUE_TYPE as QUEUE_TYPE, PREBATTLE_TYPE as PREBATTLE_TYPE
from helpers import dependency as dependency, time_utils as time_utils
from shared_utils import makeTupleByDict as makeTupleByDict
from skeletons.gui.game_control import IHangarLoadingController as IHangarLoadingController, IHeroTankController as IHeroTankController, IReferralProgramController as IReferralProgramController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from gui.shared.events import GUICommonEvent as GUICommonEvent
from halloween_common.configs.halloween_gsw import GSWModel as GSWModel

# base nao representavel no stub: namedtuple(...)
class _HalloweenConfig:
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

class HalloweenController(IHalloweenController, Notifiable, SeasonProvider, IGlobalListener, PerformanceAnalyzerMixin):
    __lobbyContext: Any
    __eventsCache: Any
    __itemsCache: Any
    __hangarLoadingController: Any
    __heroTankCtrl: Any
    __referralCtrl: Any
    __difficultyLevelCtrl: Any
    __hangarSpace: Any
    __serverSettings: Any
    _prevStates: Any
    _hwQuestsCache: Any
    onEventDisabled: Any
    onSettingsUpdate: Any
    __uiLogger: Any
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
    def onLobbyInited(self, event):
        ...
    def onLobbyStarted(self, ctx):
        ...
    def onPrbEntitySwitched(self):
        ...
    def isEnabled(self):
        ...
    def isBattlesEnabled(self):
        ...
    def isPromoScreenEnabled(self):
        ...
    def isIntroVideoEnabled(self):
        ...
    def isOutroVideoEnabled(self):
        ...
    def isInfoPageEnabled(self):
        ...
    def isInfoMetaEnabled(self):
        ...
    def isAvailable(self):
        ...
    def getConfig(self):
        ...
    @staticmethod
    def getGSWConfig():
        ...
    def getModeSettings(self):
        ...
    def getHWQuestsCache(self):
        ...
    def selectBattle(self, *args, **kwargs):
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
    @property
    def remainingEventSeconds(self):
        ...
    def selectVehicle(self, invID):
        ...
    def hasAccessToVehicle(self, vehTypeCD):
        ...
    def __onServerSettingsChanged(self, serverSettings):
        ...
    def __onHangarLoadedAfterLogin(self):
        ...
    def __updateEventBattlesSettings(self, diff):
        ...
    def __updateStates(self):
        ...
    def __clear(self):
        ...
    def __initHWQuestsCache(self, *args, **kwargs):
        ...
    def __getTimer(self):
        ...
    def __timerUpdate(self):
        ...
    def __closeHalloweenViews(self):
        ...
    def __onSelectVehicleInHangar(self, event):
        ...
    # decorador original: @adisp.adisp_process
    def __selectMode(self, name):
        ...
    @staticmethod
    def __getQueueTypeLocalizedName(queueType):
        ...
