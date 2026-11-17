# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hub/tabs/basic/daily_section/presenters/daily_missions_block_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
from constants import DAILY_QUESTS_CONFIG as DAILY_QUESTS_CONFIG, PremiumConfigs as PremiumConfigs
from gui import SystemMessages as SystemMessages
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.daily.daily_mission_model import DailyMissionModel as DailyMissionModel
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.daily.daily_missions_block_model import DailyMissionsBlockModel as DailyMissionsBlockModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.missions.missions_helpers import needToUpdateQuestsInModelByIds as needToUpdateQuestsInModelByIds, markQuestProgressAsViewed as markQuestProgressAsViewed, isPremiumPlusAccount as isPremiumPlusAccount
from gui.impl.lobby.user_missions.hub.tabs.basic.daily_section.presenters.base_missions_block_presenter import BaseMissionsBlockPresenter as BaseMissionsBlockPresenter
from gui.impl.lobby.user_missions.tooltips.daily_reroll_tooltip import DailyRerollTooltip as DailyRerollTooltip
from gui.server_events import daily_quests as daily_quests
from gui.server_events.events_helpers import dailyQuestsSortFunc as dailyQuestsSortFunc, isDailyQuestsEnable as isDailyQuestsEnable, isRerollEnabled as isRerollEnabled, EventInfoModel as EventInfoModel, getRerollTimeout as getRerollTimeout, isPremiumQuestsEnable as isPremiumQuestsEnable
from gui.server_events.settings import getNewCommonEvents as getNewCommonEvents, visitEventsGUI as visitEventsGUI
from gui.shared.utils import decorators as decorators
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from typing import List as List, Optional as Optional
from gui.server_events.event_items import DailyQuest as DailyQuest

# base nao representavel no stub: BaseMissionsBlockPresenter[...]
class DailyMissionsBlockPresenter:
    eventsCache: Any
    lobbyContext: Any
    _isRerollEnabled: Any
    _rerollTimerID: Any
    _rerollTimeout: Any
    _hasPremiumMissions: Any
    _isBlockEnabled: Any
    def __init__(self):
        ...
    def update(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _updateHasPremiumMissions(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _finalize(self):
        ...
    def _updateModel(self, model, fullUpdate=False):
        ...
    def _markQuestsAsVisited(self):
        ...
    def _onSyncCompleted(self, *_):
        ...
    def _disableCompletedQuestAnimation(self, vm):
        ...
    def __fillDailyMissions(self, vm, quests):
        ...
    def _updateCountDowns(self, model):
        ...
    def _updateCountdownUntilNextDay(self, model):
        ...
    def _updateCountdownUntilNextReroll(self, model):
        ...
    def _updateRerollEnabled(self, model):
        ...
    def _cancelRerollTimer(self):
        ...
    def __getCountdown(self):
        ...
    def __getCountdownF(self):
        ...
    def _onServerSettingsChanged(self, diff=None):
        ...
    def _onRerollTimerEnd(self):
        ...
    def _arePremiumDailyMissionsCompleted(self):
        ...
    def _onPremiumTypeChanged(self, *_):
        ...
    # decorador original: @decorators.adisp_process(...)
    # decorador original: @args2params(...)
    def __onReRoll(self, questId):
        ...
