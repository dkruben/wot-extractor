# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hub/tabs/basic/weekly_missions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import sys as sys
from datetime import datetime as datetime
import typing as typing
from future.utils import viewvalues as viewvalues
from constants import Configs as Configs
from gui.impl.gen.view_models.views.lobby.tooltips.additional_rewards_tooltip_model import AdditionalRewardsTooltipModel as AdditionalRewardsTooltipModel
from gui.impl.lobby.missions.missions_helpers import markQuestProgressAsViewed as markQuestProgressAsViewed
from gui.server_events.conditions import Cumulativable as Cumulativable
from gui.server_events.settings import visitEventsGUI as visitEventsGUI
from helpers import dependency as dependency, time_utils as time_utils
from gui import SystemMessages as SystemMessages
from gui.impl.gen import R as R
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip as AdditionalRewardsTooltip
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.impl.lobby.user_missions.hangar_widget.utils import addSpecialConditions as addSpecialConditions
from gui.server_events import weekly_quests as weekly_quests
from gui.server_events.events_helpers import getWeeklyRerollTimeout as getWeeklyRerollTimeout
from gui.shared.missions.packers.bonus import getWeeklyMissionsBonusPacker as getWeeklyMissionsBonusPacker, weeklyBonusSortKey as weeklyBonusSortKey
from gui.shared.missions.packers.events import WeeklyQuestUIDataPacker as WeeklyQuestUIDataPacker, findFirstConditionModel as findFirstConditionModel, packQuestBonusModelAndTooltipData as packQuestBonusModelAndTooltipData, packQuestBonusModel as packQuestBonusModel
from gui.shared.utils import decorators as decorators
from gui.shared.utils.scheduled_notifications import AcyclicNotifier as AcyclicNotifier
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, TooltipData as TooltipData
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.weekly_missions_model import WeeklyMissionsModel as WeeklyMissionsModel
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Optional as Optional, Union as Union
from frameworks.wulf.view.view_event import ViewEvent as ViewEvent

# base nao representavel no stub: ViewComponent[...]
class WeeklyMissions:
    LAYOUT_ID: Any
    eventsCache: Any
    lobbyContext: Any
    itemsCache: Any
    _tooltipData: Any
    _rerollTimeout: Any
    __weeklyQuests: Any
    __rerollCountdown: Any
    __acyclicNotifier: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def _firstWeekDay(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *_, **__):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _updateModel(self):
        ...
    def _getTooltipData(self, event):
        ...
    def _markQuestsAsVisited(self):
        ...
    def __fillWeeklyMissions(self, viewModel, questData):
        ...
    def __createWeeklyMissionModel(self, weeklyQuest, questInfo):
        ...
    def __getProgressFromQuest(self, quest, conditionModel):
        ...
    def __getQuestData(self, weeklyQuests):
        ...
    def _setRerollInProgress(self, model, questId):
        ...
    def _updateCountdownsUntilNextReroll(self, model):
        ...
    def __getCountdown(self, id):
        ...
    def __getCountdownF(self, id):
        ...
    def _onRerollTimerEnd(self):
        ...
    def _onServerSettingsChanged(self, diff=None):
        ...
    def __getRerollCountdown(self):
        ...
    def __onSyncCompleted(self, *_):
        ...
    # decorador original: @decorators.adisp_process(...)
    # decorador original: @args2params(...)
    def __onReRoll(self, questId):
        ...
