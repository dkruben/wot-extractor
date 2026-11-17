# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/sub_systems/fun_progressions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewitems as viewitems
from fun_random.gui.feature.fun_constants import PROGRESSION_COUNTER_TEMPLATE as PROGRESSION_COUNTER_TEMPLATE, PROGRESSION_TRIGGER_TEMPLATE as PROGRESSION_TRIGGER_TEMPLATE, PROGRESSION_EXECUTOR_TEMPLATE as PROGRESSION_EXECUTOR_TEMPLATE, FEP_PROGRESSION_EXECUTOR_QUEST_ID as FEP_PROGRESSION_EXECUTOR_QUEST_ID, FunTimersShifts as FunTimersShifts, PROGRESSION_UNLIMITED_TRIGGER_TEMPLATE as PROGRESSION_UNLIMITED_TRIGGER_TEMPLATE, PROGRESSION_UNLIMITED_EXECUTOR_TEMPLATE as PROGRESSION_UNLIMITED_EXECUTOR_TEMPLATE, PROGRESSION_UNLIMITED_COUNTER_TEMPLATE as PROGRESSION_UNLIMITED_COUNTER_TEMPLATE
from fun_random.gui.feature.models.progressions import FunProgression as FunProgression
from fun_random.gui.shared.events import FunEventType as FunEventType
from fun_random.helpers.server_settings import FunMetaProgressionConfig as FunMetaProgressionConfig, FunProgressionConfig as FunProgressionConfig
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.shared.event_bus import SharedEvent as SharedEvent
from gui.shared.utils.scheduled_notifications import Notifiable as Notifiable, SimpleNotifier as SimpleNotifier, TimerNotifier as TimerNotifier
from helpers import dependency as dependency, time_utils as time_utils
from shared_utils import first as first
from skeletons.gui.game_control import IFunRandomController as IFunRandomController
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils.requesters import ITokensRequester as ITokensRequester

class FunProgressions(IFunRandomController.IFunProgressions, Notifiable):
    __eventsCache: Any
    __itemsCache: Any
    __activeProgression: Any
    __progressionTimestamp: Any
    __settings: Any
    __subscription: Any
    def __init__(self, subscription):
        ...
    def fini(self):
        ...
    def clear(self):
        ...
    def isProgressionExecutor(self, questID):
        ...
    def getActiveProgression(self):
        ...
    def getProgressionTimer(self):
        ...
    def getSettings(self):
        ...
    def startProgressListening(self):
        ...
    def stopProgressListening(self):
        ...
    def updateSettings(self, progressionSettings):
        ...
    def __onEventsSyncCompleted(self, *_):
        ...
    def __onTokensUpdate(self, diff):
        ...
    def __onProgressionTick(self):
        ...
    def __onProgressionUpdate(self):
        ...
    def __invokeProgressionEvent(self, eventType):
        ...
    def __buildActiveProgression(self, quests):
        ...
    def __buildProgression(self, pConfig, isFirst, isLast, quests, tokens):
        ...
    def __invalidateProgressions(self):
        ...
    def __recalculateProgressionTimer(self, quests, newProgression):
        ...
