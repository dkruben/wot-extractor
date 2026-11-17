# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_results/missions_progress/daily_missions_progress.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import EVENT_TYPE as EVENT_TYPE
from gui.battle_results.pbs_helpers.common import getBattleResults as getBattleResults
from gui.battle_results.progress.progress_helpers import getReceivedTokensInfo as getReceivedTokensInfo
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.missions.event_model import EventStatus as EventStatus
from gui.impl.gen.view_models.views.lobby.battle_results.progression.daily_quest_progress_model import DailyQuestProgressModel as DailyQuestProgressModel, DailyQuestTypes as DailyQuestTypes
from gui.impl.gen.view_models.views.lobby.battle_results.progression.daily_quests_progress_model import DailyQuestsProgressModel as DailyQuestsProgressModel
from gui.impl.lobby.battle_results.missions_progress.rewards_helper import packBonusesWithTokensConvertionIfCompleted as packBonusesWithTokensConvertionIfCompleted
from gui.impl.lobby.battle_results.missions_progress.progression_presenter_interface import IProgressionCategoryPresenter as IProgressionCategoryPresenter
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.impl.lobby.user_missions.hub.hub_view import DailyTabs as DailyTabs
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip as AdditionalRewardsTooltip
from gui.server_events import conditions as conditions
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.server_events.events_dispatcher import showDailyQuests as showDailyQuests
from gui.server_events.events_helpers import isDailyQuest as isDailyQuest, isPremium as isPremium
from gui.shared.missions.packers.bonus import getDailyMissionsBonusPacker as getDailyMissionsBonusPacker
from gui.shared.missions.packers.events import getEventUIDataPacker as getEventUIDataPacker
from helpers import dependency as dependency
from skeletons.gui.server_events import IEventsCache as IEventsCache

# base nao representavel no stub: ViewComponent[...]
class DailyMissionsProgressPresenter(IProgressionCategoryPresenter):
    __eventsCache: Any
    __categoryProgressFilter: Any
    __arenaUniqueID: Any
    __allCommonQuests: Any
    __progress: Any
    __tooltipData: Any
    __bonusesModel: Any
    def __init__(self, categoryProgressFilter, arenaUniqueID, allCommonQuests):
        ...
    @classmethod
    def getPathToResource(cls):
        ...
    @classmethod
    def getViewAlias(cls):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _updateProgress(self):
        ...
    def _updateModel(self):
        ...
    def __createModel(self, event, pCur, pPrev, reset, complete, questTokensConvertion, questTokensCount):
        ...
    def __getTooltipData(self, event):
        ...
    def __onNavigate(self):
        ...
