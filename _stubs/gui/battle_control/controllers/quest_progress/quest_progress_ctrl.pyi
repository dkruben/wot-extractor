# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/quest_progress/quest_progress_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import iteritems as iteritems, itervalues as itervalues, viewvalues as viewvalues
import BigWorld as BigWorld
import personal_missions as personal_missions
from Event import Event as Event, EventManager as EventManager
from gui.impl import backport as backport
from gui.impl.gen import R as R
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import LAST_SELECTED_PM_BRANCH as LAST_SELECTED_PM_BRANCH
from constants import ARENA_PERIOD as ARENA_PERIOD
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.battle_control.arena_info.interfaces import IArenaPeriodController as IArenaPeriodController, IArenaVehiclesController as IArenaVehiclesController
from gui.battle_control.arena_info.settings import ARENA_LISTENER_SCOPE as _SCOPE
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.server_events.personal_progress.formatters import DetailedProgressFormatter as DetailedProgressFormatter
from gui.server_events.personal_progress.storage import BattleProgressStorage as BattleProgressStorage
from helpers import dependency as dependency
from personal_missions import PM_STATE as PM_STATE
from shared_utils import first as first
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any

class QuestProgressController(IArenaPeriodController, IArenaVehiclesController):
    eventsCache: Any
    lobbyContext: Any
    sessionProvider: Any
    _period: Any
    _endTime: Any
    _length: Any
    _callbackID: Any
    __storage: Any
    __selectedQuest: Any
    __eManager: Any
    __battleCtx: Any
    __isInited: Any
    __inProgressQuests: Any
    __needToShowAnimation: Any
    onConditionProgressUpdate: Any
    onHeaderProgressesUpdate: Any
    onFullConditionsUpdate: Any
    onQuestProgressInited: Any
    onShowAnimation: Any
    __lastSelectedQuestID: Any
    def __init__(self):
        ...
    def getInProgressQuests(self):
        ...
    def hasQuestsToPerform(self):
        ...
    def getSelectedQuest(self):
        ...
    def isInited(self):
        ...
    def selectQuest(self, missionID):
        ...
    def invalidateArenaInfo(self):
        ...
    def startControl(self, battleCtx, arenaVisitor):
        ...
    def areQuestsEnabledForArena(self):
        ...
    def stopControl(self):
        ...
    def setPeriodInfo(self, period, endTime, length, additionalInfo):
        ...
    def invalidatePeriodInfo(self, period, endTime, length, additionalInfo):
        ...
    def getQuestFullData(self, vehCmpDescr):
        ...
    def getQuestShortInfoData(self):
        ...
    def getQuestHeaderProgresses(self, vehCmpDescr):
        ...
    def updateQuestProgress(self, questID, info):
        ...
    def getControllerID(self):
        ...
    def getCtrlScope(self):
        ...
    def showQuestProgressAnimation(self):
        ...
    def __updatePeriodInfo(self, period, endTime, length):
        ...
    def __setCallback(self):
        ...
    def __clearCallback(self):
        ...
    def __updateTimerConditions(self, sendDiff=True):
        ...
    def __getFormatter(self, selectedQuest):
        ...

def createQuestProgressController():
    ...
