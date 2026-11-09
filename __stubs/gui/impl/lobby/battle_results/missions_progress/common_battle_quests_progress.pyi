# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_results/missions_progress/common_battle_quests_progress.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import constants as constants
from gui.battle_results.pbs_helpers.common import getBattleResults as getBattleResults
from gui.battle_results.progress.progress_helpers import getReceivedTokensInfo as getReceivedTokensInfo
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.missions.event_model import EventStatus as EventStatus
from gui.impl.gen.view_models.views.lobby.battle_results.progression.common_battle_quest_progress_model import CommonBattleQuestProgressModel as CommonBattleQuestProgressModel
from gui.impl.gen.view_models.views.lobby.battle_results.progression.common_battle_quests_progress_model import CommonBattleQuestsProgressModel as CommonBattleQuestsProgressModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.battle_results.missions_progress.progression_presenter_interface import IProgressionCategoryPresenter as IProgressionCategoryPresenter
from gui.impl.lobby.battle_results.missions_progress.rewards_helper import packBonusesWithTokensConvertionIfCompleted as packBonusesWithTokensConvertionIfCompleted
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip as AdditionalRewardsTooltip
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.server_events import conditions as conditions
from gui.server_events.events_dispatcher import showBattleQuest as showBattleQuest
from gui.shared.missions.packers.bonus import getDefaultBonusPacker as getDefaultBonusPacker
from gui.shared.missions.packers.events import TokenUIDataPacker as TokenUIDataPacker, BattleQuestUIDataPacker as BattleQuestUIDataPacker
from helpers import dependency as dependency, time_utils as time_utils
from quest_xml_source import MAX_BONUS_LIMIT as MAX_BONUS_LIMIT
from skeletons.gui.server_events import IEventsCache as IEventsCache

# base nao representavel no stub: ViewComponent[...]
class CommonBattleQuestsProgressPresenter(IProgressionCategoryPresenter):
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
    def __createModel(self, event, pCur, pPrev, isCompleted, questTokensConvertion, questTokensCount):
        ...
    def __setQuestNavigationStatus(self, quest, questModel):
        ...
    def __getTooltipData(self, event):
        ...
    # decorador original: @args2params(...)
    def __onNavigate(self, questId, eventType):
        ...
    def __onEventsUpdate(self, *args):
        ...
