# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/BoostersController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import listvalues as listvalues, viewvalues as viewvalues
from typing import TYPE_CHECKING as TYPE_CHECKING
import Event as Event
from adisp import adisp_process as adisp_process
from BonusCaps import BonusCapsConst as BonusCapsConst
from constants import Configs as Configs
from goodies.goodie_constants import BoosterCategory as BoosterCategory, BOOSTER_CATEGORY_TO_BONUS_CAPS as BOOSTER_CATEGORY_TO_BONUS_CAPS
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.prb_control.prb_getters import isDevTraining as isDevTraining
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from gui.server_events import settings as settings
from gui.shared import events as events, g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA as REQ_CRITERIA
from gui.shared.utils.scheduled_notifications import Notifiable as Notifiable, PeriodicNotifier as PeriodicNotifier
from helpers import dependency as dependency, time_utils as time_utils
from helpers.server_settings import serverSettingsChangeListener as serverSettingsChangeListener
from messenger.m_constants import SCH_CLIENT_MSG_TYPE as SCH_CLIENT_MSG_TYPE
from skeletons.gui.game_control import IBoostersController as IBoostersController, IHangarGuiController as IHangarGuiController
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.system_messages import ISystemMessages as ISystemMessages
from typing import Dict as Dict, TypeVar as TypeVar
from helpers.server_settings import ServerSettings as ServerSettings
from gui.goodies.goodie_items import Booster as Booster
from gui.prb_control.entities.base.entity import BasePrbEntity as BasePrbEntity
from gui.prb_control.entities.base.legacy.entity import LegacyEntity as LegacyEntity
from gui.server_events.settings import _PersonalReservesSettings as _PersonalReservesSettings
PrbEntityType: Any
LegacyEntityType: Any
_logger: Any

class BoostersController(IBoostersController, IGlobalListener):
    itemsCache: Any
    goodiesCache: Any
    lobbyContext: Any
    systemMessages: Any
    __hangarGuiCtrl: Any
    __eventManager: Any
    onPersonalReserveTick: Any
    onClanReserveTick: Any
    onBoostersDataUpdate: Any
    onGameModeStatusChange: Any
    __enabledCategories: Any
    __boostersForUpdate: Any
    __notificatorManager: Any
    __serverSettings: Any
    __supportedQueueTypes: Any
    soonExpireNotificationDisplayed: Any
    def __init__(self):
        ...
    def isGameModeSupported(self, category=None):
        ...
    def fini(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def updateGameModeStatus(self, *_):
        ...
    def shouldShowOnBoardingCardHint(self, boosterID):
        ...
    def setCardHintSeenFor(self, boosterID):
        ...
    # decorador original: @adisp_process
    def selectRandomBattle(self):
        ...
    def getExpirableBoosters(self):
        ...
    def onLobbyInited(self, event):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onDisconnected(self):
        ...
    def _stop(self):
        ...
    def _update(self, *args):
        ...
    def __onServerSettingsChanged(self, serverSettings):
        ...
    # decorador original: @serverSettingsChangeListener(...)
    def __onServerSettingsUpdate(self, _):
        ...
    def __updateSettings(self):
        ...
    def __timeTillNextPersonalReserveTick(self):
        ...
    def __notifyBoosterTime(self):
        ...
    def __timeTillNextClanReserveTick(self):
        ...
    def __processNotifications(self):
        ...
    def __processFirstExpirationsNotification(self, accountSettings):
        ...
    def __processSoonExpirationsNotification(self):
        ...
